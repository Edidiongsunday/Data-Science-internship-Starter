# Datasets Directory

This folder contains datasets used throughout the Virtual Data Science Internship.

## How to Use

1. **Download Datasets**: Follow instructions in each week's README to download datasets
2. **Place Files Here**: Save downloaded CSV, Excel, or other data files in this directory
3. **Reference in Code**: Load datasets using relative paths like:
   ```python
   import pandas as pd
   df = pd.read_csv('datasets/my_dataset.csv')
   ```

## Available Datasets

### Week 3: Data Cleaning & EDA
- **Titanic Dataset**: Passenger survival prediction
  - Source: [Kaggle](https://www.kaggle.com/c/titanic)
  - Size: ~900 rows × 12 columns
  - Use: Data cleaning and EDA practice

- **Iris Dataset**: Flower classification
  - Source: [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/iris)
  - Size: 150 rows × 5 columns
  - Use: Simple EDA and basic ML

### Week 4: SQL & Statistics
- **Sample Employee Database**: HR data
  - Use: SQL query practice
  - Tables: employees, sales, departments

### Week 5-6: Machine Learning
- **Sample Employee Data**: Salary prediction
  - Size: 100-200 samples
  - Use: Regression and classification

## Recommended Public Datasets

For your Capstone Project, consider these sources:

### Beginner-Friendly
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UC Irvine ML Repository](https://archive.ics.uci.edu/ml/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Seaborn Sample Datasets](https://github.com/mwaskom/seaborn-data)

### Real-World Data
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [Data.gov](https://www.data.gov/) - US Government data
- [World Bank Data](https://data.worldbank.org/)
- [COVID-19 Data](https://github.com/covid-19-open-data/covid-19-open-data)

### Domain-Specific
- **Finance**: Yahoo Finance, Quandl
- **Real Estate**: Zillow, Real Estate APIs
- **Health**: UCI ML, Kaggle competitions
- **Social**: Twitter API, Reddit
- **Sports**: ESPN, sports-reference.com

## Data Privacy

⚠️ **Important**:
- Never commit sensitive data (PII, passwords, API keys) to GitHub
- Use `.gitignore` to exclude large files and sensitive data
- Anonymize/pseudonymize personally identifiable information
- Follow GDPR, CCPA, and other privacy regulations

Example `.gitignore`:
```
# Data files
*.csv
*.xlsx
*.json
data/raw/*

# Sensitive files
*.key
*.pem
.env

# Large files
*.tar.gz
*.zip
```

## Loading Data in Python

### CSV Files
```python
import pandas as pd
df = pd.read_csv('datasets/filename.csv')
```

### Excel Files
```python
df = pd.read_excel('datasets/filename.xlsx')
```

### JSON Files
```python
df = pd.read_json('datasets/filename.json')
```

### From URL
```python
url = 'https://example.com/data.csv'
df = pd.read_csv(url)
```

## Tips

1. **Always explore first**: Use `df.head()`, `df.info()`, `df.describe()`
2. **Check for missing values**: `df.isnull().sum()`
3. **Understand data types**: `df.dtypes`
4. **Document your source**: Add comment with data location/date
5. **Keep raw data**: Never modify original files, save cleaned versions separately

## Questions?

Refer to the week-specific README files for more details on using datasets for each topic.
