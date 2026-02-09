# Week 5: Machine Learning Fundamentals

## Overview
This is where data science comes to life! You'll learn the core concepts of machine learning, train your first models, and understand how computers learn from data.

## Weekly Objectives
By the end of this week, you should be able to:
- Understand supervised vs. unsupervised learning
- Prepare data for machine learning
- Train regression and classification models
- Evaluate model performance with appropriate metrics
- Understand overfitting and underfitting
- Choose appropriate algorithms for problems
- Make predictions on new data

## Tasks

### 1. ML Fundamentals (1.5 hours)
- [ ] Understand the ML workflow: data → features → model → prediction
- [ ] Learn supervised learning (regression, classification)
- [ ] Learn unsupervised learning (clustering)
- [ ] Understand training vs. test data
- [ ] Know when to use which algorithm

### 2. Regression Models (1.5 hours)
- [ ] Understand linear regression (y = mx + b)
- [ ] Implement Linear Regression
- [ ] Implement Polynomial Regression
- [ ] Calculate R² and RMSE metrics
- [ ] Interpret coefficients

### 3. Classification Models (1.5 hours)
- [ ] Understand logistic regression
- [ ] Implement Decision Trees
- [ ] Try Random Forests
- [ ] Calculate Accuracy, Precision, Recall, F1-Score
- [ ] Create confusion matrices

### 4. Model Evaluation (1 hour)
- [ ] Train-test split methodology
- [ ] Cross-validation
- [ ] Overfitting vs underfitting
- [ ] Hyperparameter tuning basics
- [ ] Evaluation metrics selection

### 5. Complete model_training.ipynb
- [ ] Build at least 2 regression models
- [ ] Build at least 2 classification models
- [ ] Evaluate all models with appropriate metrics
- [ ] Compare model performances
- [ ] Make predictions on new data

## Important Libraries

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix
```

## Resources

### ML Fundamentals
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Andrew Ng's ML Course](https://www.coursera.org/learn/machine-learning)
- [Fast.ai Practical Deep Learning](https://course.fast.ai/)

### Practical Examples
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- [Scikit-learn Examples](https://scikit-learn.org/stable/auto_examples/index.html)

## Machine Learning Workflow

```
┌────────────────────┐
│  Problem Definition │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│   Data Collection  │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│  Data Preparation  │ ◄─── CLEANING & FEATURE ENGINEERING
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ Exploratory Analysis│ ◄─── UNDERSTAND PATTERNS & RELATIONSHIPS
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ Feature Engineering │ ◄─── CREATE MEANINGFUL FEATURES
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│  Model Selection   │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│  Model Training    │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│  Model Evaluation  │ ◄─── METRICS: ACCURACY, PRECISION, RECALL, F1
└──────────┬─────────┘
           │
       ◄───┴─ ITERATE: TRY DIFFERENT FEATURES/ALGORITHMS
       │
       ▼
┌────────────────────┐
│ Hyperparameter Tune│
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ Final Evaluation   │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│  Deploy Model      │
└────────────────────┘
```

## Common Algorithms

| Algorithm | Type | Use Case | Pros | Cons |
|-----------|------|----------|------|------|
| **Linear Regression** | Regression | Predict continuous values | Simple, interpretable | Limited to linear relationships |
| **Logistic Regression** | Classification | Binary classification | Fast, interpretable | Assumes linear decision boundary |
| **Decision Tree** | Both | Any problem | Interpretable, handles non-linearity | Prone to overfitting |
| **Random Forest** | Both | General purpose | Robust, less overfitting | Black box, slower |
| **SVM** | Both | Complex boundaries | Works well in high dimensions | Slower on large datasets |
| **Neural Networks** | Both | Complex patterns | Very flexible | Needs lots of data, slow |

## Evaluation Metrics

### For Regression:
- **MSE (Mean Squared Error)**: Lower is better
- **RMSE (Root Mean Squared Error)**: Square root of MSE, same units as y
- **MAE (Mean Absolute Error)**: Average absolute error
- **R² Score**: Percentage of variance explained (0-1, higher is better)

### For Classification:
- **Accuracy**: % correct predictions
- **Precision**: Of positive predictions, how many were correct?
- **Recall**: Of actual positives, how many did we catch?
- **F1-Score**: Harmonic mean of precision and recall

## Submission Checklist
- [ ] `model_training.ipynb` runs without errors
- [ ] At least 2 regression models implemented and evaluated
- [ ] At least 2 classification models implemented and evaluated
- [ ] All evaluation metrics calculated and interpreted
- [ ] Train-test split used (80-20 or 70-30)
- [ ] Clear explanations in markdown cells
- [ ] At least 5 commits this week
- [ ] No data leakage (test data not used during training)

## Tips for Success
- **Start simple**: Linear regression before neural networks
- **Always split data**: Training set, validation set, test set
- **Understand metrics**: Choose metrics matching your business goal
- **Iterate**: Most of ML is trying different approaches
- **Document assumptions**: Why did you choose this model?
- **Check for data leakage**: Data from test set shouldn't touch training

## Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Not splitting train/test | Always use separate train & test sets |
| Using wrong metrics | Classification ≠ Regression metrics |
| Not scaling features | Normalize/standardize numerical features |
| Overfitting the test data | Use validation set for tuning |
| Ignoring class imbalance | Handle imbalanced classes appropriately |
| Not baseline testing | Compare against simple baseline first |

---

**Assignment:** Build at least 2 models in `model_training.ipynb` with proper evaluation and interpretation.
