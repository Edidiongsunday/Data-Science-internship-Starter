"""
Streamlit Application for Model Predictions
Week 7: Deployment

Interactive Streamlit application for making predictions from a trained ML model.
Run with: streamlit run app.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import logging
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit page config
st.set_page_config(
    page_title="ML Model Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .title { font-size: 2.5rem; font-weight: bold; color: #0066cc; }
    .subtitle { font-size: 1.2rem; color: #666; margin-top: -1rem; }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    """Load trained model from disk (cached for performance)."""
    try:
        # TODO: Replace with your actual model path
        # model = pickle.load(open('models/trained_model.pkl', 'rb'))
        # scaler = pickle.load(open('models/scaler.pkl', 'rb'))
        
        # For demo, we'll use a simple mock model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        scaler = StandardScaler()
        
        # Train on dummy data for demo
        X_dummy = np.random.randn(50, 5)
        y_dummy = np.random.randint(0, 2, 50)
        model.fit(X_dummy, y_dummy)
        scaler.fit(X_dummy)
        
        logger.info("Model loaded successfully")
        return model, scaler
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        st.error(f"Failed to load model: {e}")
        return None, None


def main():
    """Main Streamlit application."""
    
    # Load model
    model, scaler = load_model()
    if model is None:
        st.error("Model failed to load. Please check the model file.")
        return
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a page:",
        ["🏠 Home", "🔮 Single Prediction", "📊 Batch Prediction", "ℹ️ Model Info"]
    )
    
    # Page content
    if page == "🏠 Home":
        show_home(model)
    elif page == "🔮 Single Prediction":
        show_single_prediction(model, scaler)
    elif page == "📊 Batch Prediction":
        show_batch_prediction(model, scaler)
    elif page == "ℹ️ Model Info":
        show_model_info(model)


def show_home(model):
    """Home page."""
    st.markdown('<p class="title">🤖 ML Model Prediction System</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Interactive Application for Model Predictions</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Welcome!** This application allows you to:
        
        - 🔮 Make single predictions
        - 📊 Process batch predictions
        - ℹ️ View model information
        """)
    
    with col2:
        st.success(f"""
        **Status:** Online ✓
        
        **Model Version:** 1.0.0
        
        **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """)
    
    st.divider()
    
    st.subheader("Getting Started")
    st.markdown("""
    1. **Single Prediction**: Go to the "Single Prediction" page to make predictions on individual samples
    2. **Batch Prediction**: Use "Batch Prediction" to process multiple samples at once
    3. **Model Info**: Check "Model Info" to see details about the current model
    """)


def show_single_prediction(model, scaler):
    """Single prediction page."""
    st.title("🔮 Single Prediction")
    
    st.markdown("Enter feature values to get a prediction from the model.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        feature1 = st.number_input("Feature 1", value=0.0, step=0.1, format="%.2f")
    with col2:
        feature2 = st.number_input("Feature 2", value=0.0, step=0.1, format="%.2f")
    with col3:
        feature3 = st.number_input("Feature 3", value=0.0, step=0.1, format="%.2f")
    
    col4, col5 = st.columns(2)
    
    with col4:
        feature4 = st.number_input("Feature 4", value=0.0, step=0.1, format="%.2f")
    with col5:
        feature5 = st.number_input("Feature 5", value=0.0, step=0.1, format="%.2f")
    
    if st.button("🎯 Make Prediction", use_container_width=True):
        try:
            # Prepare features
            features = np.array([[feature1, feature2, feature3, feature4, feature5]])
            
            # Scale features
            if scaler is not None:
                features_scaled = scaler.transform(features)
            else:
                features_scaled = features
            
            # Make prediction
            prediction = model.predict(features_scaled)[0]
            
            # Get probability if available
            try:
                probabilities = model.predict_proba(features_scaled)[0]
                confidence = float(np.max(probabilities))
                class_0_prob = probabilities[0]
                class_1_prob = probabilities[1]
            except:
                confidence = None
                class_0_prob = None
                class_1_prob = None
            
            # Display results
            st.divider()
            st.success("✓ Prediction Completed!")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Prediction", int(prediction))
            
            if confidence is not None:
                with col2:
                    st.metric("Confidence", f"{confidence:.2%}")
                
                with col3:
                    st.metric("Timestamp", datetime.now().strftime('%H:%M:%S'))
            
            # Show probabilities
            if class_0_prob is not None and class_1_prob is not None:
                st.subheader("Prediction Probabilities")
                prob_data = pd.DataFrame({
                    'Class': ['Class 0', 'Class 1'],
                    'Probability': [class_0_prob, class_1_prob]
                })
                st.bar_chart(prob_data.set_index('Class'))
            
            # Show input features
            st.subheader("Input Features")
            input_df = pd.DataFrame({
                'Feature': ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5'],
                'Value': [feature1, feature2, feature3, feature4, feature5]
            })
            st.table(input_df)
            
            logger.info(f"Single prediction made: {prediction}")
        
        except Exception as e:
            st.error(f"❌ Prediction failed: {str(e)}")
            logger.error(f"Prediction error: {e}")


def show_batch_prediction(model, scaler):
    """Batch prediction page."""
    st.title("📊 Batch Prediction")
    
    st.markdown("Upload a CSV file with multiple samples for batch predictions.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # Read CSV
            df = pd.read_csv(uploaded_file)
            
            st.subheader("📁 Uploaded Data")
            st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
            st.dataframe(df.head(10))
            
            # Check if file has enough columns
            if df.shape[1] < 5:
                st.warning(f"⚠️ Expected at least 5 features, found {df.shape[1]}")
                return
            
            # Use first 5 columns
            X = df.iloc[:, :5].values
            
            # Make predictions
            if st.button("🎯 Predict All", use_container_width=True):
                try:
                    # Scale features
                    if scaler is not None:
                        X_scaled = scaler.transform(X)
                    else:
                        X_scaled = X
                    
                    # Get predictions
                    predictions = model.predict(X_scaled)
                    
                    # Get probabilities
                    try:
                        probabilities = model.predict_proba(X_scaled)
                        confidence = np.max(probabilities, axis=1)
                    except:
                        confidence = np.ones(len(predictions))
                    
                    # Create results dataframe
                    results_df = pd.DataFrame({
                        'Prediction': predictions,
                        'Confidence': confidence,
                        'Timestamp': datetime.now().strftime('%H:%M:%S')
                    })
                    
                    st.divider()
                    st.success(f"✓ Predictions completed for {len(predictions)} samples!")
                    
                    # Display results
                    st.subheader("📈 Results")
                    st.dataframe(results_df, use_container_width=True)
                    
                    # Summary statistics
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Total Predictions", len(predictions))
                    with col2:
                        st.metric("Avg Confidence", f"{confidence.mean():.2%}")
                    with col3:
                        st.metric("Class 1 Count", int(predictions.sum()))
                    
                    # Download results
                    csv = results_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results as CSV",
                        data=csv,
                        file_name=f"predictions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
                    
                    logger.info(f"Batch predictions made for {len(predictions)} samples")
                
                except Exception as e:
                    st.error(f"❌ Batch prediction failed: {str(e)}")
                    logger.error(f"Batch prediction error: {e}")
        
        except Exception as e:
            st.error(f"❌ Failed to read CSV file: {str(e)}")
            logger.error(f"CSV reading error: {e}")
    
    else:
        st.info("👆 Please upload a CSV file to get started")


def show_model_info(model):
    """Model information page."""
    st.title("ℹ️ Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Model Details")
        st.write(f"**Model Type:** {type(model).__name__}")
        st.write(f"**Version:** 1.0.0")
        st.write(f"**Last Updated:** 2026-02-09")
        st.write(f"**Number of Features:** 5")
    
    with col2:
        st.subheader("Status")
        st.metric("Status", "Online ✓")
        st.metric("Model Ready", "Yes")
    
    st.divider()
    
    st.subheader("Model Parameters")
    if hasattr(model, 'get_params'):
        params = model.get_params()
        params_df = pd.DataFrame(list(params.items()), columns=['Parameter', 'Value'])
        st.dataframe(params_df, use_container_width=True)
    else:
        st.write("No parameters available")
    
    st.divider()
    
    st.subheader("💡 Usage Tips")
    st.markdown("""
    - **Single Prediction**: Best for testing individual predictions
    - **Batch Prediction**: Use CSV files with 5+ columns for multiple predictions
    - **Model Info**: Check model type and parameters
    - **Data Format**: Ensure all features are numeric values
    """)


if __name__ == "__main__":
    main()
