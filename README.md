# **Health Insurance Premium Prediction Model**

---

## 📙 **Project Summary**

### 🔍 **Overview**

* Built a machine learning system that predicts **annual health insurance premiums** using key customer attributes such as age, BMI, income, smoking status, dependants, region, policy type, and medical history.
* Completed a full **end-to-end ML pipeline**: data cleaning, outlier handling, EDA, feature engineering, multicollinearity checks, feature scaling, modelling, evaluation, and deployment.
* Developed an easy-to-use **Streamlit web application** that allows underwriters and customers to get instant, risk-based premium estimates.

### ✨ **Highlights**

* Created a **custom Health Risk Score** (0–1) from medical history to improve premium prediction.
* Applied **context-driven outlier treatment** (Using IQR and quantile capping) , age and income.
* Reduced multicollinearity using **Correlation Heatmap + VIF** analysis.
* Compared multiple models — **Linear Regression**, **Ridge Regression**, **XGBoost**.
* Selected a **tuned XGBoost model** delivering:

  * **R² = 0.9812**
  * **RMSE = 1,162.60** (vs ~2,273 with linear models)
* Achieved ~**50% lower error**, improving pricing fairness and accuracy.
* Model deployed into a **Streamlit web app** for real-time usage.

### 🛠 **Tools & Technologies**

* **Python**, Pandas, NumPy, Scikit-learn, XGBoost
* **Visualization:** Matplotlib, Seaborn
* **Framework:** Streamlit
* **IDE:** VS Code, Jupyter Notebook
* **Version Control:** Git & GitHub
* **Deployment:** Streamlit Cloud

---

## 📁 **Project Workflow Structure**

```
premium_prediction_project/
│
├── notebooks/                                  All project notebooks: full analysis, segmentation, and experiments
│   ├── 00_premium_full_analysis.ipynb   --->   Complete EDA, preprocessing, modelling, tuning, and final evaluation
│   ├── 01_seg_premium_lt25.ipynb        --->   Segmentation analysis for customers with premium < 25
│   ├── 02_seg_premium_gt25.ipynb        --->   Segmentation analysis for customers with premium > 25
│   ├── 03_seg_genetic_lt25.ipynb        --->   Segmentation using genetic risk score for premium_gr < 25
│   └── 04_seg_genetic_gt25.ipynb        --->   Segmentation using genetic risk score for premium_gr > 25
│
├── README.md                         Main project documentation and explanation
└── other project files…              Streamlit app, model files, data, utilities, and supporting scripts

```

Each notebook focuses on a **different experiment**, making it extremely easy to reviewers and follow your workflow.

---

## 🔗 **Launch the App**

#### **Click Here to Launch the App**
**[![Open in Streamlit](https://img.shields.io/badge/Launch%20App-Streamlit-%23FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge&labelColor=FF4B4B)](https://ml-healthcare-premium-prediction-7qrpw78zqct4zhdm7u8v2d.streamlit.app/)**
  
---

# 📝 **Detailed Documentation**

### **Content**


---

# 📘 **1) Project Overview**

This project builds a **premium prediction model** that estimates insurance charges based on customer attributes such as age, BMI, smoking status, income, and medical risk.

The model powers a **Streamlit web application** used for real-time premium estimation.

### 🔄 **Project Phases**

* **Phase 1:** Build high-accuracy ML model + deploy Streamlit MVP
* **Phase 2:** Extend to **Straight-Through Processing (STP)** in underwriting workflows

---

# 📝 **2) Scope of Work (SOW)**

### 🎯 **Objectives**

* Achieve **R² > 0.97**
* Keep prediction error within **±10%**
* Deploy the model on the cloud
* Build an intuitive **Streamlit UI**

### 📌 **Deliverables**

* Trained ML model
* Streamlit web app
* Cloud-deployed system
* Full project documentation

### 🗂 **Timeline**

| Task                    | Duration |
| ----------------------- | -------- |
| Data Preparation        | 2 weeks  |
| Modelling & Tuning      | 4 weeks  |
| Deployment              | 3 weeks  |
| Testing & Documentation | 2 weeks  |

---

# 🧠 **3) Problem Understanding**

Health insurance pricing is complex because it depends heavily on individual health, lifestyle, and demographic factors.

This project solves that by building a **consistent, data-driven, and explainable premium prediction model**.

Target outcomes:

* High accuracy (R² > 0.97)
* Low error (≤10% deviation)
* Stable and explainable predictions
* Usable via a deployed interactive app

---

# 📂 **4) Data Collection**

A clean, anonymized dataset was sourced containing:

| Feature  | Description          |
| -------- | -------------------- |
| Age      | Customer age         |
| BMI      | Body mass index      |
| Children | Number of dependants |
| Smoker   | Yes/No               |
| Region   | Location             |
| Charges  | Target premium       |

Checks performed:

* Missing values → none
* Duplicates → removed
* Outliers → detected and fixed
* EDA → completed

---

# 🧹 **5) Data Preprocessing**

Performed:

* Duplicate removal
* Outlier handling
* Feature encoding
* Data cleaning
* EDA and feature preparation

### ✂️ **Outlier Treatment**

* **Age:** removed unrealistic values (e.g., above 100 years)
* **Income:** right-skewed → handled using **quantile capping**

This ensured pattern integrity without losing valid high-income behavior.

---

# 📊 **6) Data Visualization**

### 📈 Key Findings

* **Age:** Most policyholders are young adults (18–25).
* **Income:** Strong right skew.
* **Premiums:** Mostly between 5,000–25,000.
* **Dependants:** Little impact on pricing.
* **Age vs Premium:** Clear upward trend.

These patterns match **real insurance underwriting logic**.

---

# 🧩 **7) Feature Engineering**

### 🔢 Encodings

* **Ordinal:** policy type, income level
* **Label:** region, gender, BMI category, smoker, marital status

### 🩺 **Health Risk Score**

* Built a custom **0–1 normalized score** from medical history
* Improved model understanding of health-related premium differences

### 🧠 **Feature Selection**

* Dropped redundant intermediate variables
* Reduced multicollinearity

---

# 📊 **Correlation & Multicollinearity**

Used:

* **Correlation Heatmap**
* **Variance Inflation Factor (VIF)**

High-VIF income variables were managed to reduce redundancy.

---

# 📏 **Feature Scaling**

Applied **Min-Max Scaling** to numerical features to:

* Improve model stability
* Balance feature influence
* Support regularized models

---

# 🤖 **8) Model Evaluation**

### **Model Comparison**

| Model               | Test R²    | RMSE        | Notes                         |
| ------------------- | ---------- | ----------- | ----------------------------- |
| Linear Regression   | ~0.93      | ~2273       | Good baseline, but high error |
| Ridge Regression    | ~0.93      | ~2273       | Same as linear                |
| XGBoost (Initial)   | ~0.926     | ~2302       | Underfit                      |
| **XGBoost (Tuned)** | **0.9812** | **1162.60** | ⭐ **Best Model**              |

### ⭐ **Why XGBoost Is the Best Model**

* Captures **non-linear health risk patterns**
* Delivers **highest accuracy** and **lowest error**
* Stable across train/test (no overfitting)
* Nearly **50% error reduction** vs linear models
* Best suited for **insurance pricing**

---

# 📄 **9) Model Error Analysis**

### 📊 Residual Insights

* Most predictions fall near **0% error**
* Distribution is **right-skewed**, meaning slight overprediction is more common
* High-error cases (40–90%) are **very rare**

### 👥 Age Influence

* Dataset is dominated by ages **18–25**
* Older customers (30+) are underrepresented → higher error
* Extreme residuals occur mainly in **underrepresented age groups**

### 🎯 Insight

The model performs extremely well for majority segments.
To improve performance for older customers, **more balanced data** is required.

---


---



---





