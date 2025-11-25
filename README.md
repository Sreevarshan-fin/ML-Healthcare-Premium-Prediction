# 🩺 **Health Insurance Premium Prediction Model**

A machine learning system designed to predict **annual health insurance premiums** using demographic, lifestyle, and medical history data. This project demonstrates a full end-to-end ML workflow — from data preparation to model deployment — and is integrated into an interactive **Streamlit web application** for real-time premium estimation.

---

## 🚀 **Live Demo**

**[▶ Launch Streamlit App](https://ml-healthcare-premium-prediction-7qrpw78zqct4zhdm7u8v2d.streamlit.app/)**

---
## 📝 **2) Project Goals & Approach**

### 🎯 **Objectives**

* Build a **high-accuracy premium prediction model** (R² > 0.97)
* Maintain prediction error within **±10% for at least 95%** of users
* Deploy the trained model on the cloud for **scalable access**
* Develop an interactive **Streamlit app** for real-time premium estimation

### 📌 **Project Scope**

1. **Data Collection & Preprocessing**

   * Clean and validate insurance premium datasets
   * Handle missing values, outliers, and categorical encodings
   * Perform detailed EDA to understand trends and patterns

2. **Model Development**

   * Train multiple algorithms (Linear Regression, Ridge, XGBoost)
   * Compare models based on R², RMSE, and residual behavior
   * Tune the best-performing model

3. **Model Deployment**

   * Deploy using **Streamlit Cloud**
   * Enable secure, scalable access to predictions

4. **Streamlit App Development**

   * Build an interactive UI for user data input
   * Display predictions and relevant visual insights

5. **Testing & Validation**

   * Validate model performance on real-world and test datasets
   * Conduct usability testing for speed and accuracy

6. **Documentation**

   * Prepare full technical documentation
   * Provide user instructions for underwriters
---

## 📌 **Project Highlights**

* Developed a **custom Health Risk Score** (0–1) to quantify medical risk and improve prediction accuracy.
* Applied **context-driven outlier treatment** (IQR + quantile capping) for age and income.
* Reduced multicollinearity using **Correlation Heatmap + VIF** analysis.
* Built and compared multiple regression models:
  **Linear Regression**, **Ridge Regression**, **XGBoost**.
* Selected a **tuned XGBoost Regressor** delivering:

  * **R² = 0.9812**
  * **RMSE = 1,162.60** (vs ~2,273 with linear models)
* Achieved **~50% lower prediction error**, improving pricing fairness and business reliability.
* Deployed as a **Streamlit application** for instant premium predictions.

---

## 🛠 **Tools & Technologies**

* **Python**, Pandas, NumPy, Scikit-learn, XGBoost
* **Visualization:** Matplotlib, Seaborn
* **App:** Streamlit
* **Environment:** Jupyter Notebook, VS Code
* **Version Control:** Git & GitHub
* **Deployment:** Streamlit Cloud

---

## 📁 **Project Structure**

```
premium_prediction_project/
│
├── notebooks/
│   ├── 00_premium_full_analysis.ipynb     # Complete workflow (EDA → Modelling → Evaluation)
│   ├── 01_seg_premium_lt25.ipynb          # Premium < 25 analysis
│   ├── 02_seg_premium_gt25.ipynb          # Premium > 25 analysis
│   ├── 03_seg_genetic_lt25.ipynb          # Genetic score analysis (<25)
│   └── 04_seg_genetic_gt25.ipynb          # Genetic score analysis (>25)
│
├── app/                                   # Streamlit application
├── models/                                # Saved ML models
├── data/                                  # Input dataset(s)
├── utils/                                 # Helper functions & scripts
└── README.md                              # Recruiter-facing summary
```

---

## 📘 **1) Problem Overview**

Insurance pricing varies significantly based on individual risk factors such as age, lifestyle, and medical history. Manually estimating premiums can be inconsistent and time-consuming.

This project builds a **data-driven premium prediction model** that:

* Provides consistent and accurate premium estimates
* Handles complex non-linear relationships
* Is deployable and easy to use via a web interface

---

## 🧹 **2) Data Preparation**

Key preprocessing steps:

* Removed duplicates and irrelevant records
* Treated unrealistic values (e.g., age > 100)
* Applied quantile capping for high but valid incomes
* Ensured all variables were clean, consistent, and usable for modeling

---

## 🧩 **3) Feature Engineering**

* **Ordinal Encoding:** Policy type, income buckets
* **Label Encoding:** Region, gender, BMI category, smoker status
* **Custom Health Risk Score:** Summarized medical conditions into a standardized 0–1 scale
* **Feature Selection:** Removed redundant and high-VIF features
* **Scaling:** Min–Max scaling for stable learning

---

## 🤖 **4) Modelling & Evaluation**

### Models Tested

* Linear Regression
* Ridge Regression
* XGBoost (baseline + tuned)

### Final Model: **Tuned XGBoost Regressor**

| Metric          | Value        |
| --------------- | ------------ |
| **R² (Test)**   | **0.9812**   |
| **RMSE (Test)** | **1,162.60** |

Why XGBoost was selected:

* Handles non-linear risk patterns
* Robust to skewed distributions
* Excellent generalization (train ≈ test performance)


---



# 📄 **Model Error Analysis**


* Most predictions are very close to the real premium values, with errors centered around 0%.

* The model slightly tends to overpredict more often than it underpredicts.

* Only a small group of customers shows large errors (40–90%).

* These big errors usually happen because their patterns are rare or not well represented in the data.

* Most of the dataset consists of customers aged 18–25, creating a strong age imbalance.

* Customers aged 30+ appear much less often, so the model learns their patterns poorly.

* As a result, most high-error cases come from these older, underrepresented age groups.

* Getting more age-balanced data or using age-based models can improve performance.



---



