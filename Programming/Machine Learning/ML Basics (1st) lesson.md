**Codewords:** Machine-learning definition, Types of Machine Learning

## Definition of Machine Learning 

Machine Learning (ML) is about enabling computers to learn from data—discovering patterns and making decisions with minimal human intervention. Instead of following explicit instructions, ML systems improve through experience.

More formally, it's often reffered as ""




---

### **Core Concepts**  
**Machine Learning (ML)**:  
- Goal: Extract patterns from data to make predictions/decisions without explicit programming.  
- **Data** is the foundation:  
  - **Features** (input variables, e.g., "age," "income").  
  - **Labels** (target variable, e.g., "loan approved: yes/no").  

**Data Preparation**:  
- **Critical issues**:  
  1. **Missing values**: Gaps in data (e.g., NaN entries).  
     - Fix: Impute (mean/median), drop rows/columns, or model-based prediction.  
  2. **Noise/outliers**: Erroneous data points (e.g., typos in age: 150 years).  
     - Fix: Filtering, transformations (log), or robust models.  
  3. **Imbalanced classes**: One category dominates (e.g., 99% "not spam" emails).  
     - Fix: Resampling (oversample minority, undersample majority), synthetic data (SMOTE).  
  4. **Data leakage**: Test data info "leaks" into training (e.g., scaling before split).  
     - Fix: Strict train-test split, time-based splitting.  
  5. **Feature engineering**: Creating meaningful features (e.g., extracting "day of week" from a timestamp).  

---

### **Types of ML**  
1. **Supervised Learning**:  
   - **Regression** (predict numbers): Linear regression, decision trees.  
   - **Classification** (predict categories): SVM, logistic regression.  
   - *Example task*: Predict house prices (regression) or tumor type (classification).  

2. **Unsupervised Learning**:  
   - **Clustering**: Group similar data (k-means, DBSCAN).  
   - **Dimensionality reduction**: PCA, t-SNE.  
   - *Example task*: Customer segmentation (clustering).  

3. **Reinforcement Learning**:  
   - Agent learns via rewards (e.g., AlphaGo).  

---

### **Model Training**  
- **Loss function**: Measures prediction error (e.g., MSE for regression).  
- **Overfitting**: Model memorizes noise in training data (high variance).  
  - **Solutions**: Regularization (L1/L2), dropout (neural nets), early stopping.  
- **Underfitting**: Model too simple (high bias).  
  - **Solutions**: Add features, reduce regularization, use complex models.  

**Validation**:  
- **Cross-validation**: Split data into folds to assess generalization (e.g., 5-fold CV).  

---

### **Evaluation Metrics**  
- **Classification**:  
  - Accuracy: (Correct predictions) / (Total predictions).  
  - Precision/Recall: Tradeoff between false positives vs. false negatives.  
  - F1-score: Harmonic mean of precision and recall.  
- **Regression**:  
  - MAE (Mean Absolute Error), RMSE (Root Mean Squared Error).  

---

### **Key Questions from the Article**  
**Data & Preprocessing**:  
- *Why is data splitting (train/val/test) crucial?*  
  Prevents overfitting and ensures unbiased performance estimation.  
- *How does missing data harm models?*  
  Models may learn incorrect patterns or fail to generalize.  
- *What is the "curse of dimensionality"?*  
  High-dimensional data requires exponentially more samples to generalize.  

**Modeling**:  
- *Why can’t we use accuracy for imbalanced datasets?*  
  A model predicting the majority class always will have high accuracy but poor utility.  
- *What is the difference between parametric and non-parametric models?*  
  Parametric (e.g., linear regression) assumes fixed input-output structure; non-parametric (e.g., k-NN) adapts complexity to data.  

**Deployment**:  
- *What is model drift?*  
  Performance degrades over time as data distributions change (e.g., user preferences shift).  

---

### **Code Example (Handling Missing Data)**  
```python  
from sklearn.impute import SimpleImputer  
import pandas as pd  

# Load data with missing values  
data = pd.read_csv("data.csv")  

# Impute missing values with column median  
imputer = SimpleImputer(strategy="median")  
data_imputed = imputer.fit_transform(data)  
```  

---

### **Practical Tasks**  
4. **Data Cleaning**:  
   - Load a dataset with missing values (e.g., Titanic dataset).  
   - Apply imputation and compare model performance (e.g., logistic regression before/after).  

5. **Bias-Variance Tradeoff**:  
   - Train polynomial regression models of varying degrees on noisy data.  
   - Plot training vs. validation error to visualize overfitting/underfitting.  

---

### **Flashcards**  
#🃏/ml-basics  
- **Q: How to detect data leakage?**  
  A: Check if preprocessing steps (e.g., scaling) were applied before train-test split.  

- **Q: Why use cross-validation instead of a single train-test split?**  
  A: Reduces variance in performance estimation by averaging across multiple splits.  

- **Q: What is SMOTE?**  
  A: Synthetic Minority Oversampling Technique: Generates synthetic samples for imbalanced classes.  

--- 

This conspect preserves all critical details from the article, including **data pitfalls**, **key questions**, and **practical nuances**, structured for clarity and spaced repetition. Let me know if you need even deeper dives!
- **Model:** A mathematical function that maps inputs to outputs.
- **Training:** The process of tuning a model's parameters using data.
- **Loss Function & Optimization:** Tools to measure errors and adjust the model to minimize them.
- **Overfitting/Underfitting:** Balancing model complexity so it generalizes well without being too rigid or too simplistic.

**Types of Machine Learning:**

- **Supervised Learning:** Learning from labeled data (e.g., classification, regression).
- **Unsupervised Learning:** Discovering hidden patterns in unlabeled data (e.g., clustering, dimensionality reduction).
- **Reinforcement Learning:** Learning through trial and error, receiving feedback from an environment.

**Applications:**  
ML powers everything from image and speech recognition to recommendation systems and fraud detection—transforming raw data into actionable insights.

**Key Questions (for flashcards):**

6. **What is Machine Learning?**  
    It’s a method for computers to learn from data and improve their performance without being explicitly programmed.
    
7. **How do supervised and unsupervised learning differ?**  
    Supervised learning uses labeled data to guide predictions, while unsupervised learning finds patterns in data without predefined labels.
    
8. **What is overfitting?**  
    Overfitting occurs when a model learns noise in the training data, resulting in poor performance on new, unseen data.
    
9. **Why are loss functions important?**  
    They quantify prediction errors and drive the optimization process to fine-tune the model.