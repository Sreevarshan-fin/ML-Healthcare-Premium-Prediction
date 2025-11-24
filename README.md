# **HEALTH INSURANCE PREMIUM MODEL**

## 📙 **Project Summary**

####  **Overview**

- Predicts **annual health insurance premiums** using customer data (age, BMI, income, dependants, smoking status, region, policy type, medical history, etc.).
- Built an **end-to-end machine learning pipeline**: data cleaning, outlier handling, feature engineering, multicollinearity checks, scaling, model training, and evaluation.
- Deployed as an **interactive Streamlit web app** to support underwriters and customers with instant, risk-based premium estimates.

#### **Highlights**

- Designed a **custom health risk score** from medical history and integrated it as a key feature.
- Applied **context-aware outlier treatment** for age and income (IQR + quantile-based capping).
- Performed **correlation analysis and VIF** to handle multicollinearity and refine features.
- Benchmarked models: **Linear Regression, Ridge Regression, XGBoost**.
- Selected a **tuned XGBoost Regressor** as the final model:
  - Test R²: **0.9812**
  - Test RMSE: **1,162.60** (vs ~2,273 for Linear/Ridge)
- Achieved **almost 50% reduction in prediction error** compared to linear baselines, enabling more accurate policy-level pricing.

#### **Tools & Technologies**

- **Programming:** Python  
- **Data & ML:** Pandas, NumPy, Scikit-learn, XGBoost,Regression,Statistics
- **Visualization:** Matplotlib, Seaborn  
- **App Framework:** Streamlit  
- **Environment:** Jupyter Notebook, VS Code  
- **Version Control / Hosting:** Git, GitHub  
- **Deployment:** Streamlit Cloud




#### **Click Here to Launch the App**
**[![Open in Streamlit](https://img.shields.io/badge/Launch%20App-Streamlit-%23FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge&labelColor=FF4B4B)](https://ml-healthcare-premium-prediction-7qrpw78zqct4zhdm7u8v2d.streamlit.app/)**
  
---------------------------------------------------------------------------------------------------------------------------------------------
## 📝 **Detailed Project Documentation**

This project builds an end-to-end machine learning solution to predict annual health insurance premiums using customer demographics, lifestyle factors, and medical history. The workflow covers data cleaning, outlier treatment, EDA, feature engineering (including a custom health risk score), multicollinearity checks (VIF), and feature scaling. Multiple models were evaluated, and a tuned XGBoost regressor was selected, almost halving prediction error compared to linear baselines. The final model is integrated into a Streamlit web application to provide underwriters and customers with fast, consistent, risk-based premium estimates.

**Content**

- [1) Project Overview](#1-project-overview)
- [2) Scope of Work (SOW)](#2-scope-of-work-sow)
- [3) Problem Understanding](#3-problem-understanding)
- [4) Data Collection](#4-data-collection)
- [5) Data Preprocessing](#5-data-preprocessing)
- [6) Data Visualization](#6-data-visualization)
- [7) Feature Engineering](#7-feature-engineering)
- [Correlation & Multicollinearity Analysis](#correlation--multicollinearity-analysis)
- [Feature Scaling](#feature-scaling)
- [8) Model Evaluation](#8-model-evaluation)




----------------------------------------------------------------------------------------------------------------------------------------------

## 📘 **1) Project Overview**

This project focuses on developing a **predictive model** that estimates **health insurance premiums** based on user characteristics such as **age**, **BMI**, **smoking habits**, and **medical history**.  

The aim is to help **insurance underwriters** and **customers** quickly estimate premium amounts using an **AI-powered web application**.

####  **Project Phases**

- **Phase 1 (MVP):** Build and deploy a predictive model with a **Streamlit web app**.  
- **Phase 2 (Future Scope):** Develop infrastructure for **Straight-Through Processing (STP)** of insurance quotes.

  -------
  

## 📝 **2) Scope of Work (SOW)**

#### 🎯 **Objectives**

- **Build** a high-accuracy model (**>97%**) for premium prediction.  
- **Ensure** the prediction error remains within **10%** for at least **95%** of cases.  
- **Deploy** the trained model on the **cloud** for remote and scalable access.  
- **Develop** an interactive **Streamlit interface** for real-time premium predictions.


---------


## **Project Scope**

#### **1. Data Collection and Preprocessing**
- Gather and clean labeled datasets relevant to insurance premiums.  
- Handle missing values, outliers, and feature encoding.  
- Perform **Exploratory Data Analysis (EDA)** to identify patterns and trends.

#### **2. Model Development**
- Train multiple algorithms (**Linear Regression**, **Random Forest**, **XGBoost**).  
- Compare and optimize the **best-performing model** using evaluation metrics.

#### **3. Model Deployment**
- Deploy the final model using **Streamlit Cloud** or **AWS**.  
- Ensure secure, scalable, and reliable access to predictions.

#### **4. Streamlit App Development**
- Build an **interactive web app** for user data input.  
- Display **premium predictions** and **visual insights** through charts and metrics.

#### **5. Testing and Validation**
- Validate model performance using **real-world** or **simulated test data**.  
- Conduct **user testing** for accuracy, usability, and performance.

#### **6. Documentation and Training**
- Prepare comprehensive **technical documentation** and a **user guide** for underwriters.  

---

### **Deliverables**

- ✅ Trained and validated **predictive model**.  
- ✅ **Cloud-deployed** model endpoint.  
- ✅ **Streamlit web application** for interactive predictions.  
- ✅ Complete **project documentation** and **training materials**.

---

### **Timeline**

| **Task** | **Duration** |
|-----------|--------------|
| Data Collection & Pre-processing | 2 weeks |
| Model Development & Evaluation | 4 weeks |
| Deployment & App Development | 3 weeks |
| Testing & Documentation | 2 weeks |

----------

##  🧠 **3) Problem Understanding**

The **rising complexity of medical expenses** has made it increasingly difficult for insurance companies to determine **fair and accurate premium pricing**.  
To address this challenge, this project aims to develop a **predictive machine learning model** capable of estimating **health insurance premiums** based on individual **health and lifestyle factors** such as **age**, **BMI**, **smoking habits**, and **medical history**.

The core objectives of the model include:
- Achieving a **prediction accuracy greater than 97%**.  
- Maintaining a **prediction error margin within 10%** for at least **95% of test cases**.  
- Ensuring the model is **interpretable**, **scalable**, and **deployable** for **real-world use** by underwriters through an **AI-powered web interface**.

This initiative not only supports **data-driven underwriting decisions** but also enhances transparency and efficiency in premium estimation.

---

## 📂 **4) Data Collection**

A **labeled insurance dataset** was sourced from a **trusted third-party data vendor** specializing in anonymized customer and insurance data for **research and analytics** purposes.  

The dataset comprises the following key features:

| **Feature** | **Description** |
|--------------|-----------------|
| **Age** | Age of the individual |
| **BMI** | Body Mass Index — an indicator of body fat based on height and weight |
| **Children** | Number of dependents covered under the insurance plan |
| **Smoker** | Smoking status of the individual (`Yes` / `No`) |
| **Region** | Geographical location of the policyholder |
| **Charges** | Actual medical insurance cost (**target variable**) |

The dataset was provided in **CSV format**, fully compliant with **privacy and data protection regulations** — ensuring that **no personally identifiable information (PII)** was included.  

Before modeling, comprehensive **data validation and cleaning** were conducted:
- Checked for **missing or inconsistent values**.  
- Detected and addressed **outliers**.  
- Conducted **Exploratory Data Analysis (EDA)** to understand feature distributions, correlations, and relationships impacting premium charges.

This data foundation ensured a **robust, reliable, and ethical** starting point for predictive modeling.

---

##  🧹 **5) Data Preprocessing**

Data preprocessing is a critical step in any machine learning workflow — ensuring that the dataset used for model training is accurate, consistent, and free from noise that can mislead predictions.

For this health insurance premium prediction project:

- **No missing values** were found.  
- **Duplicates** were identified and removed.  
- **Outliers** were detected and treated to maintain realistic data distribution.

---

##   ✂️ Outlier Detection and Treatment in Health Insurance Data

When preparing data for machine learning, **outlier detection and treatment** play a vital role in ensuring that the model learns from realistic patterns rather than extreme or erroneous values.

Outliers can **heavily influence model behavior** — especially in regression problems like **insurance premium prediction**, where extreme cases can distort the model’s understanding of how different features affect charges.

---

### What Are Outliers?

Outliers are data points that differ significantly from the majority of the dataset.  
They can occur due to:

- Data entry or measurement errors  
- Rare but valid real-world scenarios  

Outliers can:
- Skew averages and statistical summaries  
- Mislead visualizations  
- Cause **overfitting**, where the model focuses on anomalies instead of genuine trends  

In this project, contextual understanding was used to distinguish between **invalid data points** and **rare but possible values**.

---

### Example — Real Cases from the Dataset

- Most policyholders are aged between **18 and 60**, so a record with **age = 150** clearly indicates an invalid entry.  
- Similarly, if typical **income values** range between **5 and 50 lakhs**, a record showing **900 lakhs** represents an extreme case that can distort the model’s income–premium relationship.

---

### 🔎 Outlier Detection and Treatment

#### 1️⃣ Age — Removing Unrealistic Values

When visualizing the **Age** feature with a box plot, most policyholders were between **20 and 50 years old** — but a few records stood out with values like **124**, **136**, **203**, **224**, and even **356**.

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/64d3e418-7878-4ddb-a5c4-816269761c6a" />


Clearly, no one lives that long. Since the oldest verified human age is **122 years**, anything above **100** is considered unrealistic and likely due to a data entry error.  
Keeping such values would heavily skew averages and confuse the model.

<img width="400" height="350" alt="image" src="https://github.com/user-attachments/assets/ccb05988-7d8b-456b-bca3-4cb666e77faa" />

##### **After Treatment of Outliers**

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/64b519df-bd23-440e-be8a-b67340ab164b" />

#### 2️⃣ Income — Handling Extreme but Valid Values

The **income_lakhs** feature displayed a noticeable **right-skewed distribution**, indicating that a small portion of individuals earned significantly higher than the majority.

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/78ade7ce-ab63-4113-973e-f0e4b55fb2c5" />

While high-income values are valid in some cases, extreme entries — such as **900 lakhs** — introduced distortions in the model’s ability to understand the relationship between **income** and **insurance premiums**.

#### **IQR method**
<img width="920" height="463" alt="image" src="https://github.com/user-attachments/assets/e7d4996b-8a02-486f-82f7-554856e0c530" />

Initially, the **Interquartile Range (IQR) method** was applied, but it proved too restrictive — flagging several legitimate high-income records as outliers. 
To balance accuracy and fairness, a **quantile-based capping** approach was implemented instead.

#### **Quantile-Based**
<img width="791" height="363" alt="image" src="https://github.com/user-attachments/assets/fd3bc79d-bd01-46a0-9fdd-cc89889e2a4e" />

#### **After Treatment of Outliers**
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/073e65ab-652f-40dd-a594-3f099ffe4bcd" />

### Understanding Outliers After Data Cleaning

Outlier detection is essential for identifying unusual data points that can affect a model’s accuracy and stability.  
However, not every outlier represents an error — some reflect genuine real-world variations.

In this project, domain knowledge played a key role in distinguishing **invalid data** from **meaningful exceptions**.

- Unrealistic entries such as **ages above 224 years** were removed, as they clearly indicate data entry errors.  
- High but realistic incomes between **70–100 lakhs** were **retained**, since affluent individuals often purchase **premium insurance plans**.  
- **Extreme income values** exceeding **100 lakhs** were **capped** using quantile-based thresholds to maintain distributional balance without losing essential business insights.  

Even after cleaning, **box plots** displayed a few points beyond the whiskers — these represent valid **high-income policyholders**, not data anomalies.

By integrating **statistical techniques** with **domain understanding**, the outlier handling process became more intelligent and context-driven — ensuring the model learns from real insurance behaviors, not random noise.

----------------------

##  📊 **6) Data Visualization**

### 📈 **Univariate Analysis of Key Variables**


<img width="1000" height="800" alt="image" src="https://github.com/user-attachments/assets/ca735eba-c0cc-4bea-8959-e43158104a2d" />



- **Age Distribution:** The policyholder base is predominantly young, with the highest frequency of customers around 20 years of age.
- **Number of Dependants Distribution:** The most frequent category is $0$ dependants, although $1$ through $4$ dependants are also very common household structures.
- **Income (in Lakhs) Distribution:** The income distribution is heavily right-skewed, with a vast majority of policyholders reporting an income under 20 lakhs.
- **Annual Premium Amount Distribution:** The premiums are centered around 10,000, with the majority of policies having an annual premium between 5,000 and 25,000.


### 📈 **Bivariate Analysis of Key Variables**

<img width="1800" height="1000" alt="scatter_plot" src="https://github.com/user-attachments/assets/1ab55f9b-4e10-44bb-a27c-e68c407765f0" />


###  **Key Findings & Domain Insights from Relationship Plots**

The scatter plots provided valuable insights into how various customer attributes influence **annual health insurance premiums**.  
Each relationship was analyzed to understand the underlying patterns from both a **data** and **domain** perspective.



#### 🧓 Age vs. Annual Premium  
A clear **upward trend** was observed — older customers tend to pay **higher minimum premiums**.  
This aligns perfectly with insurance logic: as **age increases**, **health risks** typically rise, leading to **higher premium amounts**.



#### 💰 Income (in Lakhs) vs. Annual Premium  
Premium values were **scattered across all income levels**, showing **no strong direct correlation** between income and premium amount.  
In health insurance, pricing is **risk-based**, not wealth-based — meaning both high-income and middle-income individuals with similar risk profiles pay **comparable premiums**.



#### 👨‍👩‍👧 Number of Dependents vs. Annual Premium  
The number of dependents had **minimal impact** on premium amounts.  
Premiums remained largely **consistent across different family sizes**, indicating that **individual health risk**, rather than family count, is the primary pricing factor.



### 💡 Domain Insight

These visual relationships confirm that insurance pricing models are designed around **risk and health factors**, not demographic or financial attributes.  
Such data-driven insights ensure **fairness, consistency, and transparency** in how premiums are calculated — aligning with the core principles of responsible underwriting.


----------------


## 🧩 **7) Feature Engineering**

Feature engineering transformed raw insurance data into meaningful, machine-readable formats, improving model learning and prediction accuracy.

---

### 🔢 **Encoded Text Features**

To make categorical text data understandable to the model, two encoding methods were applied:

- **One-Hot Encoding:**  
Used for ordered categories such as policy type and income group.  

**policy type :**  


 <img width="1092" height="85" alt="image" src="https://github.com/user-attachments/assets/3bc0b586-d861-4d32-aa4d-ed8e9398348b" />
 
 
- Bronze → 1  
- Silver → 2  
- Gold → 3
  
----

**Income Level:**  

<img width="953" height="175" alt="image" src="https://github.com/user-attachments/assets/5f20a446-e42e-4d90-a5a4-041310b4201c" />
 
- `<10L` → 1  
- `10L–25L` → 2  
- `25L–40L` → 3  
- `>40L` → 4  


This allowed the model to recognize the ranking between plan levels or income brackets.


----


-  **Label Encoding:**  
Applied to non-ordinal features such as:  

<img width="1105" height="312" alt="image" src="https://github.com/user-attachments/assets/aa89c116-3ec3-43aa-bd0f-2bf09f497ca4" />

**`gender`, `region`, `marital_status`, `bmi_category`, `smoking_status`, and `employment_status`.** 

Each unique label was assigned a numerical value without implying hierarchy.


---


### 🩺  Health Risk Scoring in Insurance Data

A custom **health risk scoring system** was developed to represent the impact of medical history numerically.  
Each disease (such as diabetes, heart disease, or thyroid) was given a severity-based score.  
When multiple conditions were present, their scores were summed and then normalized between **0 and 1**.

This standardized score provided a consistent measure of health risk, helping the model make fair and accurate premium predictions.

<img width="1141" height="606" alt="image" src="https://github.com/user-attachments/assets/9d71667d-9125-48de-b6d2-98a1ba4c1f7a" />


--------


#### 📝  **Data Sets Information After Encoded Text and Risk Score** 

<img width="678" height="701" alt="image" src="https://github.com/user-attachments/assets/668cbeb1-e065-4109-a22c-058c520e2198" />


---

### 🧠 Feature Selection

After risk scoring, redundant or intermediate variables — such as the raw medical history text and temporary disease columns — were removed.  
This step streamlined the dataset, retaining only the most relevant and high-impact features for model training, ensuring better performance and interpretability.


<img width="901" height="83" alt="image" src="https://github.com/user-attachments/assets/902fdb7a-401e-474a-a3f9-cbde85e02eaa" />


---

#### 🖼️ **Feature Engineering Workflow Overview**

   <img width="1000" height="350" alt="Feature Engineering" src="https://github.com/user-attachments/assets/19333410-86c8-4a14-9e10-2d81a6a24896" />

***************


## 📊 **Correlation & Multicollinearity Analysis**

Before training the model, it was important to check how features relate to each other. Highly correlated variables can distort model learning and reduce interpretability. To ensure reliable results, two diagnostic techniques were applied — Correlation Heatmap and Variance Inflation Factor (VIF).

### 🧮 Understanding Multicollinearity

Multicollinearity occurs when independent variables convey overlapping information. In regression or tree-based models, this can make predictions unstable and coefficients unreliable. Identifying and handling it ensures a robust, interpretable model.

### 🧩 Correlation Heatmap

A correlation heatmap was generated to visualize relationships between numerical features.
Values close to +1 or –1 indicate strong correlation, suggesting potential redundancy.

<img width="1000" height="745" alt="Project 1 Correlation" src="https://github.com/user-attachments/assets/22ffdfb8-82da-4a2b-871c-ae4ed99b0abc" />


**Figure:** Correlation Heatmap highlighting relationships between features.

The analysis showed moderate correlations across a few features, but none severe enough to impact the model’s integrity.


### 🧠 **Variance Inflation Factor (VIF)**

VIF was calculated to quantify multicollinearity. It measures how much a variable’s variance is inflated due to correlation with others.

| VIF Range | Meaning                  | Action           |
| --------- | ------------------------ | ---------------- |
| **1–5**   | Moderate correlation     | Acceptable       |
| **>5**    | High correlation         | Review feature   |
| **>10**   | Severe multicollinearity | Consider removal |


<img width="938" height="158" alt="image" src="https://github.com/user-attachments/assets/7cb5337b-5303-435e-9650-5baa900ed4d0" />



<img width="441" height="720" alt="image" src="https://github.com/user-attachments/assets/69935d33-ac49-4dca-835a-bb4f94110818" />


**The VIF results show that most features have low multicollinearity, except for income_level (12.45) and income_lakhs (11.18), which are highly correlated and may need review or removal.**


#### **After Removal of High VIF:**

<img width="452" height="693" alt="image" src="https://github.com/user-attachments/assets/dbe99a94-264b-485b-96fd-7b53716a01fc" />

-----------------------

## 📏 **Feature Scaling**

In healthcare insurance premium prediction, features like age, income_lakhs, and number_of_dependants have very different ranges. To make sure all features contribute fairly, we applied Min-Max Scaling, which rescales values to a 0–1 range.

**This helps the model:**

Learn faster and more stably.

Treat all features equally, so no single feature dominates.

Keep coefficients interpretable, showing relative importance.

Work well with regularized models like Ridge or Lasso.

💡 **Key Insight:**
   Scaling ensures the model can make accurate, consistent, and meaningful predictions for insurance premiums.

   <img width="1027" height="246" alt="image" src="https://github.com/user-attachments/assets/32083434-855f-4554-981a-64c58e8b45eb" />
   
----------------------



## 📊 **8) Model Evaluation**

To identify the best algorithm for premium prediction, multiple regression models were trained and evaluated on the same train–test split.

### 🔹 Linear Regression

- **Train R²:** 0.9282  
- **Test R²:** 0.9281  
- **Test MSE:** 5,165,611.91  
- **Test RMSE:** 2,272.80  

**Observation:**  
Linear Regression provides a strong baseline (R² ≈ 0.93), but the error level (RMSE ≈ 2,273) shows that a purely linear relationship cannot fully capture the complexity of health insurance premiums.

---

### 🔹 Ridge Regression (α = 1.0)

- **Train R²:** 0.9282  
- **Test R²:** 0.9281  
- **Test MSE:** 5,165,652.02  
- **Test RMSE:** 2,272.81  

**Observation:**  
Ridge Regression delivers **almost identical** performance to Linear Regression.  
This indicates that L2 regularization adds little value in this setting because:

- Features were already cleaned and reviewed for multicollinearity (via VIF).  
- The design matrix is stable enough that regularization has minimal effect.

---

### 🔹 XGBoost Regressor (Initial Trial: n_estimators = 20, max_depth = 3)

- **Train R²:** 0.9252  
- **Test R²:** 0.9261  
- **Test MSE:** 5,302,478.00  
- **Test RMSE:** 2,302.71  

**Observation:**  
The initial XGBoost setup actually **underperformed** the linear baselines.  
With shallow trees and a low number of estimators, the model was slightly **underfit** and did not yet exploit the strength of gradient boosting.

---

### 🔹 XGBoost Regressor (After Hyperparameter Tuning)

- **Best Parameters (Random Search + CV):**  
  - `n_estimators = 50`  
  - `max_depth = 5`  
  - `learning_rate = 0.1`  

- **Cross-Validation Best R²:** 0.9809  

**Test Set Metrics (Best Model):**

- **Train R²:** 0.9813  
- **Test R²:** 0.9812  
- **Test MSE:** 1,351,649.63  
- **Test RMSE:** 1,162.60  

**Observation:**  
After tuning, XGBoost:

- Boosted performance from R² ≈ 0.93 to **R² ≈ 0.98**.  
- Cut RMSE from ~**2,273** (Linear/Ridge) to ~**1,163**, almost halving typical error.  
- Showed excellent generalization, with very similar Train and Test R² scores.

---

### 🏁 Final Model Selection & Business Justification

- **Linear & Ridge Regression**
  - Useful as interpretable baselines with R² ≈ 0.93.
  - However, higher residual error (RMSE ≈ 2,273) limits their use for accurate premium pricing at the policy level.

- **XGBoost (Tuned)**
  - Delivers the **highest accuracy (R² ≈ 0.98)** and **lowest error (RMSE ≈ 1,163)**.
  - Captures **non-linear interactions** between age, BMI, income, smoking status, dependants, and health risk.
  - Provides stable performance across training, validation, and test sets.

✅ **Final Recommendation**  
The **tuned XGBoost Regressor** is selected as the **production model** because it:

- Provides substantially **higher accuracy** than linear baselines.  
- Reduces average prediction error, improving both **pricing fairness** and **portfolio profitability**.  
- Better reflects real-world health insurance dynamics by modeling complex, non-linear patterns.

-----------------------

## 📄 **Model Error Analysis**

#### 📊 **1. Residual Distribution (Diff %)**

This plot shows how much the model’s predictions differ from the actual values (in percentage).

**What the distribution shows**

Most residuals are tightly centered around 0%, indicating that the model is accurate for a large portion of customers.

**The distribution is not symmetric:**

A noticeable right tail represents large positive errors.

The left tail is much smaller.

**Interpretation**

The model tends to overpredict more than it underpredicts.

A small subset of customers shows very high errors (40–90%), which indicates:

They behave differently from the majority.

The current feature set does not fully capture their patterns.

#### 📈 **2. Extreme Error Thresholds (10% vs 40%)**

**At a 10% threshold**

Customers with |prediction error| ≥ 10%: 4,478 rows

This is about one-third of the dataset.

These represent moderate-to-high error cases.

**At a 40% threshold**

Only the most extreme cases remain.

Expected count reduces to 300–900 customers.

**Why this happens**

Only a small portion of observations fall into the far-right tail, representing the largest prediction failures.

#### 👥 **3. Age Distribution & Its Influence on Errors**

**The age histogram shows:**

Majority of customers are aged 18–25.

Very few are above 30.

Ages 40–60 are nearly absent.

**Impact on the model**

The model is mostly trained on young customers, making predictions reliable for this group.

**Older customers have very limited representation:**

The model cannot learn their behavior effectively.

This results in higher error rates.

Many of the extreme errors in the residual plot come from these underrepresented age groups.

#### 🧠 **4. Overall Insight**

✔ The model performs strongly for the dominant demographic (18–25 years).

✔ Errors increase significantly for underrepresented groups (30+ years).

✔ The majority of extreme errors come from customers the model has rarely seen during training.

----------------------------------------------------------------------------------------------------------------------------------------------
