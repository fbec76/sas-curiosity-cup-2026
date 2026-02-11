# sas-curiosity-cup-2026
# NBA Hit/Miss Classification Project Workflow (SAS)  

- Shots Dataset: https://github.com/DomSamangy/NBA_Shots_04_25/tree/main
- Schedule Metrics Dataset: https://github.com/josedv82/public_sport_science_datasets/tree/main/NBA%20Schedule%20Metrics
- Physical and Anthropometric Dataset: https://github.com/josedv82/public_sport_science_datasets/tree/main/NBA%20Combine

## 1. Overview

**Goal:** Compare different classification models (Logistic Regression, Decision Tree, Random Forest, possibly BMM) for predicting NBA shot success (hit/miss) using player, team, game, and location data in SAS.

---

## 2. Workflow Outline

### Week 1: Project Setup & Data Understanding

- **Literature review:** Short summary of similar works (1 day)
- **Dataset acquisition:** Download + briefly inspect all 3 datasets (1 day)
- **Variable identification:** List/describe relevant features (player, team, coords, etc.) from all datasets (1 day)
- **Project plan & division of labor:** (if group) (1 day)

---

### Week 2: Data Preparation and Preprocessing

- **Data merging:** Join datasets on appropriate keys (e.g., player ID, game ID) (1 day)
- **Cleaning:**  
  - Handle missing values, outliers  
  - Data type corrections, transformations as needed (2 days)
- **Feature engineering:**  
  - Create/transform features (distance to basket, shot angle, clock, etc.) (1 day)
- **Exploratory data analysis:**  
  - Summarize, visualize distributions, check class balance (1 day)

---

### Week 3: Modeling, Evaluation, and Reporting

- **Modeling in SAS:**  
  - Logistic Regression (`PROC LOGISTIC`)
  - Decision Trees & Random Forests (`PROC TREE`, `PROC HPFOREST`)
  - (Optional) BMM if feasible in SAS (1.5 days)
- **Evaluation:**  
  - Use cross-validation, ROC curves, confusion matrices, other metrics (accuracy, AUC, sensitivity, specificity) (1 day)
- **Visualization:**  
  - Save significant output graphs (feature importances, ROC, distributions) (0.5 days)
- **Write report:**  
  - Introduction, problem statement, data/methods, results, conclusions, suggestions for future (1 day)
- **Peer review/editing, finalize appendix (visualizations):** (0.5 days)

---

## 3. Report Outline

1. **Introduction:** Context, importance, predictive problem
2. **Data:** Datasets used, sources, summary tables
3. **Problem:** Clearly state prediction target, scope, constraints
4. **Data Cleaning/Validation:** Steps for quality control
5. **Analysis:**  
   - Model selection criteria/methods  
   - SAS procedures used (with product names)
   - Quantitative and visual comparison of model results  
6. **Visualization (Appendix):** Model comparison graphs, EDAs
7. **Suggestions for Future Studies:** Improvements/extensions
8. **Conclusion:** Main findings, implications

---

## 4. Summary Timeline Table

| Week  | Key Activities                            |
|-------|-------------------------------------------|
| 1     | Literature review, data download, plan    |
| 2     | Data merging, cleaning, EDA, features     |
| 3     | Modeling, evaluation, visualizing, report |

---

**Tip:** Document all key SAS code steps for reproducibility and consider adding a workflow diagram for clarity.  
Are there specific models or SAS products you want more focus on? Or do you want example code stubs for any step?
