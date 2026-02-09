## Week 6: MLflow Experiment Tracking

This document tracks all experiments, hyperparameter combinations, and results for model improvement.

---

## Experiment Tracking Template

For each experiment, fill in the following:

### Experiment 1: Baseline Model
**Date:** [Date]
**Model:** Random Forest
**Objective:** Establish baseline performance

**Hyperparameters:**
```python
{
    'n_estimators': 100,
    'max_depth': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1
}
```

**Results:**
- Accuracy: 0.XX
- Precision: 0.XX
- Recall: 0.XX
- F1-Score: 0.XX
- Cross-Val Score (5-fold): 0.XX ± 0.XX

**Notes:** Baseline to compare improvements against.

---

### Experiment 2: Hyperparameter Tuning - Depth
**Date:** [Date]
**Model:** Random Forest
**Objective:** Find optimal max_depth parameter

**Hyperparameters Tested:**
- max_depth: [3, 5, 7, 10, 15, None]

**Best Parameters:**
```python
{
    'max_depth': 7,
    'n_estimators': 100
}
```

**Results:**
- Accuracy: 0.XX
- F1-Score: 0.XX
- Improvement vs Baseline: +X.XX%

**Notes:** Max depth of 7 shows good balance between performance and complexity.

---

### Experiment 3: Grid Search - Full Tuning
**Date:** [Date]
**Model:** Random Forest
**Objective:** Find optimal combination of hyperparameters

**Parameters Grid:**
```python
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
```

**Best Parameters Found:**
```python
{
    'n_estimators': 150,
    'max_depth': 7,
    'min_samples_split': 5,
    'min_samples_leaf': 2
}
```

**Results:**
- Accuracy: 0.XX
- Precision: 0.XX
- Recall: 0.XX
- F1-Score: 0.XX
- Best CV Score: 0.XX

**Top 5 Parameter Combinations:**
1. Accuracy: 0.XX, F1: 0.XX
2. Accuracy: 0.XX, F1: 0.XX
3. Accuracy: 0.XX, F1: 0.XX
4. Accuracy: 0.XX, F1: 0.XX
5. Accuracy: 0.XX, F1: 0.XX

**Notes:** Grid search found optimal balance with moderate depth and larger min_samples values.

---

### Experiment 4: Cross-Validation Analysis
**Date:** [Date]
**Objective:** Evaluate model stability across folds

**Model:** Random Forest (Best parameters from Exp 3)

**5-Fold Cross-Validation Results:**
- Fold 1 Accuracy: 0.XX
- Fold 2 Accuracy: 0.XX
- Fold 3 Accuracy: 0.XX
- Fold 4 Accuracy: 0.XX
- Fold 5 Accuracy: 0.XX
- **Mean: 0.XX**
- **Std Dev: 0.XX**

**Interpretation:** Low std dev indicates consistent performance across folds (good generalization).

**Fold Comparison Chart:**
```
Fold Scores: [0.XX, 0.XX, 0.XX, 0.XX, 0.XX]
            ├────────────────────────────────
            │    Consistent performance!
```

---

### Experiment 5: Class Imbalance Handling
**Date:** [Date]
**Objective:** Improve minority class detection

**Approach 1: Class Weights**
```python
RandomForestClassifier(class_weight='balanced')
```
- Accuracy: 0.XX
- Recall (Minority): 0.XX
- F1-Score: 0.XX

**Approach 2: SMOTE (Synthetic Minority Oversampling)**
```python
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
```
- Accuracy: 0.XX
- Recall (Minority): 0.XX
- F1-Score: 0.XX

**Best Approach:** SMOTE shows better recall for minority class.

---

## Summary of Improvements

| Metric | Baseline | Final Model | Improvement |
|--------|----------|------------|------------|
| Accuracy | 0.XX | 0.XX | +XX% |
| Precision | 0.XX | 0.XX | +XX% |
| Recall | 0.XX | 0.XX | +XX% |
| F1-Score | 0.XX | 0.XX | +XX% |

---

## Learning Outcomes

1. ✅ Hyperparameter tuning significantly improves model performance
2. ✅ Cross-validation ensures robust evaluation
3. ✅ Different algorithms require different optimization strategies
4. ✅ Class imbalance handling is critical for fair evaluation
5. ✅ Systematic experiment tracking enables reproducibility

---

## MLflow Quick Reference

### Log Experiment
```python
import mlflow
import mlflow.sklearn

with mlflow.start_run():
    mlflow.log_params({'param1': value1, 'param2': value2})
    mlflow.log_metrics({'metric1': value1, 'accuracy': 0.95})
    mlflow.sklearn.log_model(model, 'model')
```

### View Results
```bash
mlflow ui
# Navigate to http://localhost:5000
```

### Compare Runs
- Use MLflow UI to compare metrics across experiments
- Track which hyperparameters led to best results
- Visualize performance progression

---

## Next Steps for Week 7
- Deploy best model as a web service
- Create prediction API with Flask or FastAPI
- Package model for production
- Begin capstone project
