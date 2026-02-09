# Week 4: SQL & Statistics

## Overview
This week you'll learn SQL for data extraction and statistical testing for hypothesis validation. SQL is essential for working with databases, and statistics helps you draw meaningful conclusions from data.

## Weekly Objectives
By the end of this week, you should be able to:
- Write SELECT, WHERE, GROUP BY, and JOIN queries
- Aggregate data using SUM, AVG, COUNT, etc.
- Understand probability distributions
- Perform hypothesis testing (t-tests, chi-square)
- Interpret statistical results
- Use SQL to answer business questions

## Tasks

### 1. SQL Fundamentals (2 hours)
- [ ] Understand relational databases and tables
- [ ] Write SELECT statements with WHERE filters
- [ ] Use GROUP BY and HAVING clauses
- [ ] Master JOIN operations (INNER, LEFT, RIGHT)
- [ ] Practice ORDER BY and LIMIT
- [ ] Use aggregate functions (SUM, AVG, COUNT, MIN, MAX)

### 2. SQL Practice (1.5 hours)
- [ ] Create sample tables and insert data
- [ ] Write 10+ queries answering specific questions
- [ ] Practice joining multiple tables
- [ ] Use subqueries and CTEs
- [ ] Complete all exercises in `sql_queries.sql`

### 3. Statistical Foundations (1.5 hours)
- [ ] Understand population vs. sample
- [ ] Learn probability distributions (normal, binomial, Poisson)
- [ ] Calculate confidence intervals
- [ ] Understand standard deviation and variance
- [ ] Learn about p-values and significance levels

### 4. Statistical Testing (1.5 hours)
- [ ] T-tests (one-sample, two-sample, paired)
- [ ] Chi-square tests for categorical data
- [ ] ANOVA for multiple groups
- [ ] Effect size calculations
- [ ] Interpret test results correctly

### 5. Complete notebooks and queries
- [ ] All SQL queries execute without errors
- [ ] `statistics.ipynb` contains examples and exercises
- [ ] Clear comments explaining each test
- [ ] At least 4 commits this week

## Resources

### SQL Learning
- [SQLZoo - Interactive SQL Tutorial](https://sqlzoo.net/)
- [LeetCode Database Problems](https://leetcode.com/problemset/all/?topicSlugs=database)
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

### Statistics Resources
- [Khan Academy Statistics](https://www.khanacademy.org/math/statistics-probability)
- [Real Python Statistics](https://realpython.com/python-statistics/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [StatQuest with Josh Starmer](https://www.youtube.com/c/joshstarmer)

## Key SQL Concepts

| Concept | Purpose | Example |
|---------|---------|---------|
| SELECT | Choose columns | `SELECT name, age FROM users` |
| WHERE | Filter rows | `WHERE age > 21` |
| GROUP BY | Aggregate by category | `GROUP BY department` |
| HAVING | Filter groups | `HAVING COUNT(*) > 5` |
| JOIN | Combine tables | `INNER JOIN orders ON users.id = orders.user_id` |
| ORDER BY | Sort results | `ORDER BY salary DESC` |
| LIMIT | Limit rows | `LIMIT 10` |

## Key Statistical Tests

| Test | Use When | Null Hypothesis |
|------|----------|-----------------|
| **t-test** | Comparing 2 group means | μ₁ = μ₂ |
| **ANOVA** | Comparing 3+ group means | μ₁ = μ₂ = μ₃ |
| **Chi-square** | Testing categorical association | Variables are independent |
| **Correlation** | Testing relationship strength | ρ = 0 (no correlation) |

## Submission Checklist
- [ ] All SQL queries in `sql_queries.sql` execute successfully
- [ ] Queries include comments explaining what they do
- [ ] `statistics.ipynb` contains at least 5 different statistical tests
- [ ] Results are interpreted with business context
- [ ] Code follows PEP 8 style guidelines
- [ ] At least 4 commits this week
- [ ] No hardcoded values in SQL (use variables/parameters)

## Practice Datasets

### For SQL:
- Create your own employee database
- Use Kaggle datasets with multiple tables
- Practice with public databases (SQLZoo, LeetCode)

### For Statistics:
- Sample data from Week 3 (employee data)
- Kaggle datasets for case studies
- Simulated data for controlled testing

## Common SQL Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting GROUP BY with aggregates | Always use GROUP BY when aggregating |
| Wrong JOIN type | Test with small datasets to verify |
| NULL values in calculations | Use COALESCE or ISNULL |
| Not indexing columns | Index frequently filtered/joined columns |

## Tips for Success
- **Practice SQL daily**: Even 30 minutes makes a difference
- **Test your queries**: Always verify results make sense
- **Learn statistical intuition**: Understand concepts, not just formulas
- **Interpret results in context**: What does the p-value mean for your business?
- **Combine SQL + Statistics**: Extract data, then analyze statistically

## Week 4 Challenge
Build a mini project:
1. Create a database with 3+ related tables
2. Write 5 complex queries answering business questions
3. Conduct 3 statistical tests on the extracted data
4. Summarize findings in markdown

---

**Assignment:** Complete all SQL queries and run statistical tests with detailed interpretations.
