# Week 3: Data Cleaning & Exploratory Data Analysis (EDA)

## Overview
This is where real data science begins! You'll learn how to work with real-world messy data, clean it, and explore it to uncover insights. In practice, data scientists spend 70-80% of their time on data cleaning and EDA!

## Weekly Objectives
By the end of this week, you should be able to:
- Load and inspect data using pandas
- Identify and handle missing values
- Deal with outliers and duplicates
- Perform data type conversions
- Create meaningful visualizations
- Generate descriptive statistics
- Tell a story with your data

## Tasks

### 1. Pandas Fundamentals (2 hours)
- [ ] Create DataFrames from lists, dictionaries, and CSV files
- [ ] Understand rows and columns
- [ ] Use `.head()`, `.tail()`, `.info()`, `.describe()`
- [ ] Filter data using boolean indexing
- [ ] Select specific columns
- [ ] Handle column naming conventions

### 2. Data Cleaning (2 hours)
- [ ] Identify missing values with `.isnull()` and `.isna()`
- [ ] Handle missing data: drop, fill forward/backward, interpolate
- [ ] Remove duplicates with `.drop_duplicates()`
- [ ] Detect and handle outliers
- [ ] Fix data type issues
- [ ] Standardize values (to lowercase, remove whitespace, etc.)

### 3. Exploratory Data Analysis (2 hours)
- [ ] Calculate descriptive statistics (mean, median, std, etc.)
- [ ] Understand distributions
- [ ] Identify correlations between variables
- [ ] Explore categorical variables
- [ ] Document findings in markdown cells

### 4. Data Visualization (1.5 hours)
- [ ] Create histograms and bar charts
- [ ] Draw scatter plots for relationships
- [ ] Make box plots to visualize distributions
- [ ] Add titles, labels, and legends
- [ ] Use matplotlib and seaborn effectively

### 5. Complete the Notebooks
- [ ] `data_cleaning.ipynb`: Load, clean, and prepare a dataset
- [ ] `eda.ipynb`: Analyze the cleaned data and find insights
- [ ] At least 5 commits this week with clear messages

## Important Libraries

```python
import pandas as pd           # Data cleaning & manipulation
import numpy as np            # Numerical operations
import matplotlib.pyplot as plt  # Plotting
import seaborn as sns         # Advanced plotting
```

## Resources

### Pandas & Data Cleaning
- [Pandas Documentation](https://pandas.pydata.org/)
- [Real Python Pandas Tutorial](https://realpython.com/learning-paths/data-science-python/)
- [Kaggle Data Cleaning Guide](https://www.kaggle.com/learn/data-cleaning)

### Visualization
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Data Visualization Best Practices](https://www.tableau.com/about/blog/2016/7/what-makes-effective-visualization)

### Datasets to Practice With
- [Titanic Dataset](https://www.kaggle.com/c/titanic)
- [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
- [Mushroom Dataset](https://www.kaggle.com/datasets/uciml/mushroom-classification)

## Key Concepts

| Concept | What to Know |
|---------|-------------|
| **Missing Values** | Different types of missing data required different strategies |
| **Data Types** | Ensure variables are correct type (int vs string vs datetime) |
| **Outliers** | Not always errors - sometimes they're interesting insights! |
| **Distributions** | Understanding data distribution guides analysis choices |
| **Correlation** | Correlation ≠ Causation (important!) |
| **Visualization** | A good chart tells a story better than statistics |

## Submission Checklist
- [ ] `data_cleaning.ipynb` runs without errors
- [ ] All missing values handled with comments explaining choices
- [ ] Duplicates identified and resolved
- [ ] Data types are correct
- [ ] `eda.ipynb` contains at least 5 visualizations
- [ ] Clear markdown explanations throughout
- [ ] At least 5 commits this week
- [ ] No sensitive data (remove PII if working with real data)

## Data Cleaning Workflow
```
1. Load Data
   ↓
2. Inspect Structure & Quality
   ↓
3. Handle Missing Values
   ↓
4. Remove Duplicates
   ↓
5. Fix Data Types
   ↓
6. Handle Outliers
   ↓
7. Feature Standardization
   ↓
8. Document & Export
```

## Tips for Success
- **Explore before cleaning**: Understand your data first
- **Know your data**: Ask: "Where does it come from? Who collected it?"
- **Be thoughtful about handling missing data**: Deletion vs. imputation has consequences
- **Visualize often**: Create plots to verify your changes
- **Document decisions**: Write markdown explaining why you made each choice
- **Compare before & after**: Show how many rows changed, missing values, etc.

## Common Data Quality Issues

| Issue | Solution | Code Example |
|-------|----------|-------------|
| Missing values | Drop or fill | `df.drop (na()` or `df.fillna()` |
| Duplicates | Remove | `df.drop_duplicates()` |
| Wrong data type | Convert | `df['col'].astype(int)` |
| Extra whitespace | Strip | `df['col'].str.strip()` |
| Inconsistent cases | Standardize | `df['col'].str.lower()` |
| Wrong date format | Parse | `pd.to_datetime(df['col'])` |

---

**Assignment:** Complete both notebooks using a real dataset (Kaggle, Titanic, Iris, or your own choice).
