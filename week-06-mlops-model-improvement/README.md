# Week 6: MLOps & Model Improvement

## Overview
Now that you have working models, let's make them better! This week focuses on optimizing models, tracking experiments, and preparing for deployment. MLOps (Machine Learning Operations) is critical in production systems.

## Weekly Objectives
By the end of this week, you should be able to:
- Perform hyperparameter tuning
- Use cross-validation for robust evaluation
- Implement grid search and random search
- Track experiments with MLflow
- Document model versions
- Handle class imbalance
- Optimize for business metrics

## Tasks

### 1. Hyperparameter Tuning (1.5 hours)
- [ ] Understand what hyperparameters are
- [ ] Implement GridSearchCV for systematic search
- [ ] Implement RandomizedSearchCV for efficiency
- [ ] Compare hyperparameter combinations
- [ ] Document best parameters

### 2. Cross-Validation (1 hour)
- [ ] Understand k-fold cross-validation
- [ ] Implement cross_val_score
- [ ] Use StratifiedKFold for imbalanced data
- [ ] Interpret cross-validation results
- [ ] Detect overfitting patterns

### 3. Model Improvement (1.5 hours)
- [ ] Feature engineering for better performance
- [ ] Handle class imbalance (SMOTE, class weights)
- [ ] Remove irrelevant features
- [ ] Try ensemble methods
- [ ] A/B testing concepts

### 4. Experiment Tracking (1 hour)
- [ ] Learn MLflow basics
- [ ] Log parameters and metrics
- [ ] Compare experiment runs
- [ ] Version control for models
- [ ] Document improvements

### 5. Complete Notebooks
- [ ] `model_tuning.ipynb`: Hyperparameter optimization
- [ ] `mlflow_experiments.md`: Experiment tracking documentation
- [ ] Document all improvements with metrics
- [ ] At least 5 commits this week

## Important Libraries

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_val_score
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
from imblearn.over_sampling import SMOTE
import mlflow
import mlflow.sklearn
```

## Resources

### Hyperparameter Tuning
- [Scikit-learn GridSearchCV](https://scikit-learn.org/stable/modules/model_selection.html#grid-search)
- [Bayesian Optimization](https://github.com/fmfn/BayesianOptimization)
- [Optuna](https://optuna.readthedocs.io/)
- [Hyperopt](http://hyperopt.github.io/hyperopt/)

### MLOps & Experiment Tracking
- [MLflow Documentation](https://mlflow.org/)
- [Weights & Biases](https://wandb.ai/)
- [Neptune.ai](https://neptune.ai/)

### Best Practices
- [Google MLOps Best Practices](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [Made With ML - Full Stack](https://madewithml.com/)

## Hyperparameter Tuning Strategies

### Grid Search
```python
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

### Random Search
```python
from sklearn.model_selection import RandomizedSearchCV
param_dist = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10]
}
random_search = RandomizedSearchCV(
    model, param_dist, n_iter=10, cv=5
)
```

## Common Hyperparameters by Algorithm

| Algorithm | Key Hyperparameters | Tuning Tips |
|-----------|-------------------|------------|
| **Decision Tree** | max_depth, min_samples_split | Increase depth → overfitting |
| **Random Forest** | n_estimators, max_depth, min_samples_leaf | More trees = better (but slower) |
| **SVM** | C, kernel, gamma | C = regularization (lower = simpler) |
| **Neural Network** | learning_rate, hidden_layers, batch_size | Start with small networks |
| **Boosting** | learning_rate, n_estimators, max_depth | Lower learning_rate → longer training |

## Class Imbalance Solutions

1. **Resampling**:
   - Oversampling: Duplicate minority class
   - Undersampling: Remove majority class samples
   - SMOTE: Generate synthetic minority samples

2. **Modify Algorithm**:
   - Use `class_weight='balanced'` parameter
   - Adjust threshold for classification

3. **Use Appropriate Metrics**:
   - Use F1, Precision, Recall instead of Accuracy
   - Use ROC-AUC for imbalanced data

## Submission Checklist
- [ ] `model_tuning.ipynb` completes hyperparameter tuning
- [ ] GridSearchCV and cross-validation implemented
- [ ] Best hyperparameters documented
- [ ] Performance improvement shown quantitatively
- [ ] `mlflow_experiments.md` documents all experiments
- [ ] At least 5 commits with clear messages
- [ ] Code follows PEP 8 standards
- [ ] Comparison of baseline vs. tuned model

## Tips for Success
- **Start simple**: Tune 1-2 parameters first
- **Use reasonable ranges**: Don't search impossibly large ranges
- **Cross-validate everything**: Final validation on hold-out test set only
- **Document everything**: Why did you choose these hyperparameters?
- **Consider computational cost**: GridSearch can be very slow
- **Track experiments**: Use MLflow or similar to compare runs
- **Business context matters**: Optimize for business metrics, not just accuracy

## Overfitting vs Underfitting

| Underfitting | Good Fit | Overfitting |
|--------------|----------|------------|
| Train: LOW | Train: GOOD | Train: EXCELLENT |
| Test: LOW | Test: GOOD | Test: POOR |
| Model too simple | Just right | Model memorizing data |
| Solution: Increase complexity | ✓ | Solution: Reduce complexity/get more data |

## Week 6 Challenge
1. Take your best model from Week 5
2. Perform hyperparameter tuning (GridSearchCV)
3. Use 5-fold cross-validation
4. Log experiments with MLflow
5. Document top 3 hyperparameter combinations
6. Show improvement over baseline

---

**Assignment:** Optimize your models from Week 5 and document the improvements.
