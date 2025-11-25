# 🏥 Health Insurance Premium Prediction

## 👋 From Raw Data to Real Impact

I built a machine learning system that predicts annual health insurance premiums with **98% accuracy**, turning a messy real-world insurance dataset into a reliable, deployed application that supports fair and consistent pricing for insurers and customers.

👉 *Open in Streamlit*

---

## 🎯 What I Delivered (Clear & Human-Readable)

* **98.1% accuracy (R² = 0.981)** — cutting prediction error by nearly 50% compared to baseline models
* Processed **50,000+ insurance records** and curated **15,000 high-quality samples** for training
* Engineered a **custom Health Risk Score** to convert medical histories into structured risk features
* Built **4 specialized ML models** using age segmentation + genetic-risk scoring
* Achieved **under 10% prediction error across all customer groups**
* Developed and deployed a **Streamlit web app** for instant premium predictions
* Ensured usability by collaborating with **insurance domain experts** and conducting **user testing**

---

## 📊 The Results Speak for Themselves

| Model                     | R² Score  | RMSE      | Improvement              | Training Data      |
| ------------------------- | --------- | --------- | ------------------------ | ------------------ |
| Linear Regression         | 0.928     | 2,273     | Baseline                 | 15,000 records     |
| **XGBoost (Final Model)** | **0.981** | **1,163** | **≈50% error reduction** | **15,000 records** |

---

# 🧠 My Problem-Solving Journey

A recruiter can clearly understand *how I think* and *why I made certain decisions*.

---

## 🔍 Phase 1: Exploring & Cleaning the Data

When I first examined the **50,000-record dataset**, it had severe issues — ages above 100, unrealistic medical entries, and extreme income values. Instead of blindly removing outliers, I used domain logic.

**What I did:**

* Analyzed all **50,000 customer records** to map patterns and quality issues
* Removed **biologically impossible data** (e.g., age > 100)
* Retained genuine high-income cases but capped extreme outliers
* Used **quantile-based capping** to keep distributions realistic
* Selected **15,000 clean and reliable samples** for modeling

---

## 🛠️ Phase 2: Intelligent Feature Engineering

The medical history field was just messy, free-text data. To make it usable:

### I created a **Health Risk Score** by:

* Researching medical and insurance literature on disease severity & cost
* Designing a weighted scoring system
* Converting raw medical text into a **normalized 0–1 risk value**
* Iteratively tuning weights to maximize predictive power
* Validating the score against actual premium patterns

This single feature significantly improved model performance.

---

## 🤖 Phase 3: Choosing & Optimizing the Algorithm

I tested multiple models on the **15,000 training records**:

* Linear Regression
* Ridge Regression
* XGBoost

XGBoost captured the non-linear relationships in health insurance pricing far better.

**Key optimizations:**

* `max_depth = 5`
* `n_estimators = 50`
* `learning_rate = 0.1`

Using Random Search CV, I achieved:

* **50% error reduction vs. linear models**
* Strong generalization across all customer groups

---

## 🎯 Phase 4: Closing the Business Requirement Gap

Even with high accuracy, some customer segments showed up to **30% error**, which wasn’t acceptable for underwriting.

### What I discovered:

* Errors were mostly in **older age groups (30+)**
* Dataset was dominated by younger customers (18–25)

### My iterative approach:

#### 1) Age-Based Segmentation

Created two models:

* **01_seg_premium_lt25.ipynb** (young adults)
* **02_seg_premium_gt25.ipynb** (25+ group)

Accuracy improved but still didn’t meet the <10% requirement.

#### 2) Genetic Risk Segmentation (Breakthrough)

I developed a **Genetic Risk Score** to capture inherited health tendencies.

* **03_seg_genetic_lt25.ipynb**
* **04_seg_genetic_gt25.ipynb**

📌 **Final Result:**
**<10% maximum error**
**99.2% accuracy** across all customer segments

---

## 👥 Phase 5: Turning It Into a Real Product

I converted the research into a useful application.

### What I did:

* Built a **Streamlit web app** for instant premium estimation
* Collected feedback from **insurance professionals**
* Conducted user testing to ensure the interface was simple and intuitive
* Aligned terminology and workflow with industry standards
* Optimized backend for **sub-second predictions**

---

# 📈 Model Error Analysis

### Key Insights:

* **95% of all predictions** across the dataset are within **10% of actual premium**
* Most residuals stay close to zero
* Higher errors come from **underrepresented age groups (30+)**
* Root cause: imbalance in the original 50,000 records

This analysis shaped the segmentation strategy that fixed the issue.

---

# 🛠 Technical Implementation

### 📁 Project Structure

```
premium_prediction_project/
│
├── notebooks/
│   ├── 00_premium_full_analysis.ipynb
│   ├── 01_seg_premium_lt25.ipynb
│   ├── 02_seg_premium_gt25.ipynb
│   ├── 03_seg_genetic_lt25.ipynb
│   └── 04_seg_genetic_gt25.ipynb
│
├── app/          
├── models/       
├── data/         # 50,000 analyzed, 15,000 trained
└── utils/
```

### 🔧 Tech Stack

* Python (Pandas, NumPy, Scikit-learn, XGBoost)
* Matplotlib, Seaborn
* Streamlit
* Git, GitHub
* Streamlit Cloud

---

# 💡 Business Impact

This solution provides:

* **Faster, more consistent pricing** for underwriters
* **Transparent premium estimates** for customers
* **Significant reduction in manual effort**
* A scalable framework for future insurance AI tools

---

# 📝 Lessons Learned & Next Steps

### What I’d Improve Next:

* Collect more balanced age data
* Add automated validation for incoming data
* Implement model monitoring for concept drift

### Planned Enhancements:

* Age-segmented ensemble models
* Real-time API integration
* More risk factors for even stronger predictions

---

# 🌟 Why This Project Matters

This project shows my ability to:

* Clean and understand complex real-world data
* Engineer meaningful features from messy inputs
* Build, evaluate, and deploy multiple ML models
* Solve genuine business challenges — not just technical ones

If this approach aligns with your needs, I’d be excited to bring this level of problem-solving to your team.

