# Week 7: Deployment & Capstone Project

## Overview
This is where your data science work meets the real world! You'll package your best model as a production-ready service, create an API for predictions, and begin your capstone project.

## Weekly Objectives
By the end of this week, you should be able to:
- Package models for deployment
- Create an interactive web application for predictions
- Containerize with Docker
- Document model for production use
- Build a complete end-to-end data science project
- Present results in a professional manner

## Tasks

### 1. Model Packaging (1 hour)
- [ ] Save trained model to disk (pickle or joblib)
- [ ] Create model loader utility
- [ ] Document model metadata (version, features, hyperparameters)
- [ ] Create requirements.txt for dependencies
- [ ] Version control the model

### 2. Web Application Development (1.5 hours)
- [ ] Set up Streamlit application
- [ ] Create interactive input forms
- [ ] Implement single prediction page
- [ ] Add batch prediction with CSV upload
- [ ] Display results with visualizations
- [ ] Test application locally

### 3. Containerization (1 hour)
- [ ] Create Dockerfile for Streamlit
- [ ] Build Docker image
- [ ] Test containerized application
- [ ] Document deployment instructions
- [ ] (Optional) Deploy to cloud (Streamlit Cloud, AWS, Heroku)

### 4. Capstone Project Setup (1.5 hours)
- [ ] Define your project problem
- [ ] Collect/prepare dataset
- [ ] Create project documentation
- [ ] Set up notebook/code structure
- [ ] Plan deliverables

### 5. Complete Deliverables
- [ ] `app.py`: Streamlit application with multiple pages
- [ ] `requirements.txt`: All dependencies including Streamlit
- [ ] `Dockerfile`: Containerization config
- [ ] README: Clear deployment instructions
- [ ] Working application with single and batch prediction pages

## Important Libraries & Tools

```python
# Web Framework
import streamlit as st
import pandas as pd
import numpy as np

# Model Serialization
import pickle
import joblib

# Run Streamlit app
streamlit run app.py

# Containerization
docker build -t my-model-app .
docker run -p 8501:8501 my-model-app
```

## Resources

### Streamlit Development
- [Streamlit Official Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### Deployment Platforms
- [Streamlit Cloud](https://streamlit.io/cloud) - Free hosting for Streamlit apps
- [Docker for Data Science](https://docker-curriculum.com/)
- [AWS SageMaker](https://aws.amazon.com/sagemaker/)
- [Google Cloud AI](https://cloud.google.com/products/ai)
- [Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/)
- [Heroku (for learning)](https://www.heroku.com/)

### Project Examples
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [ML Portfolio Projects](https://www.insideaiml.com/machine-learning-projects/)

## Sample Streamlit Application Structure

```python
import streamlit as st
import pickle
import numpy as np

# Configure page
st.set_page_config(page_title="Model Prediction", layout="wide")

# Load model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# Title and description
st.title("🤖 ML Model Prediction")
st.write("Enter features to get a prediction")

# Sidebar for navigation
page = st.sidebar.radio("Select page:", ["Single Prediction", "Batch Prediction"])

if page == "Single Prediction":
    # Input form
    feature1 = st.number_input("Feature 1", value=0.0)
    feature2 = st.number_input("Feature 2", value=0.0)
    
    if st.button("Make Prediction"):
        features = np.array([[feature1, feature2]])
        prediction = model.predict(features)
        st.success(f"Prediction: {prediction[0]}")
```

## Capstone Project Structure

```
capstone-project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_cleaning.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── preprocess.py
│   ├── model.py
│   └── utils.py
├── models/
│   ├── trained_model.pkl
│   └── preprocessor.pkl
├── tests/
│   └── test_model.py
├── app.py
├── requirements.txt
└── README.md
```

## Capstone Project Ideas

### Beginner:
- House Price Prediction
- Iris Flower Classification
- Email Spam Detection
- Movie Recommendation
- Weather Forecasting

### Intermediate:
- Customer Churn Prediction
- Sentiment Analysis on Reviews
- Stock Price Prediction
- Credit Risk Assessment
- Sales Forecasting

### Advanced:
- Fraud Detection System
- Natural Language Processing
- Computer Vision Application
- Time Series Forecasting
- Custom NLP Model

## Submission Checklist
- [ ] Model successfully saved and loaded
- [ ] `app.py` implements working API endpoint
- [ ] `requirements.txt` lists all dependencies
- [ ] Dockerfile successfully builds and runs
- [ ] API accepts JSON input and returns JSON output
- [ ] Input validation implemented
- [ ] Clear error handling
- [ ] README includes deployment instructions
- [ ] Test predictions work correctly
- [ ] Code is documented and follows PEP 8
- [ ] At least 5 commits this week

## Production Readiness Checklist
- [ ] Model versioning implemented
- [ ] Input/output validation complete
- [ ] Error handling for edge cases
- [ ] Logging for debugging
- [ ] Documentation complete
- [ ] Unit tests pass
- [ ] Performance acceptable
- [ ] Security considerations (sanitize inputs, rate limiting)
- [ ] Monitoring plan established

## Tips for Success
- **Start simple**: Create app.py with basic input form first
- **Use caching**: Use @st.cache_resource for models to improve performance
- **Organize pages**: Use sidebar radio buttons for multi-page apps
- **Test locally first**: Run `streamlit run app.py` before dockerizing
- **Document everything**: Future you will appreciate it
- **Version your model**: Track which model is in production
- **Use Streamlit Cloud**: Free and easy deployment option
- **Monitor performance**: Check if model degrades over time
- **Plan for updates**: How will you retrain and redeploy?

## Common Deployment Issues

| Issue | Solution |
|-------|----------|
| Model not loading in container | Copy model file into Docker image and use correct path |
| Streamlit port conflict | Use `streamlit run app.py --server.port 8501` |
| Pages not updating | Use @st.cache_resource for models, not @st.cache_data |
| Memory issues with batch processing | Implement pagination or limit batch size |
| Different versions of libraries | Lock versions in requirements.txt |
| Model performance degradation | Retrain regularly with new data |

---

**Assignment:** Deploy your model as a Streamlit web application and plan/start your capstone project.
