# 🏥 Health Insurance Premium Prediction

## 👋 From Raw Data to Real Impact

I built a machine learning system that predicts **annual health insurance premiums with 98% accuracy** – transforming messy insurance data into a reliable, deployed application that helps both insurers and customers get fair, consistent pricing.

**[![Open in Streamlit](https://img.shields.io/badge/Launch%20App-Streamlit-%23FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge&labelColor=FF4B4B)](https://ml-healthcare-premium-prediction-7qrpw78zqct4zhdm7u8v2d.streamlit.app/)**
 

---

## 🎯 What I Delivered

* **98.1% model accuracy** (R² = 0.981) with **50% lower error** than baseline
* **Processed 50,000+ records** and curated **15,000 high-quality samples** for training
* Engineered a **custom Health Risk Score** to quantify medical complexity
* Built **4 specialized models** (age-based + genetic-risk segmentation)
* Achieved **<10% error** across all segments using advanced feature engineering
* Developed and deployed a **production-ready Streamlit web application**
* Delivered **95%+ predictions within 10% deviation** from actual premiums
* Ensured real-world usability by incorporating **domain expert and user feedback**

---


## 📊 The Results Speak for Themselves

| Model | R² Score | RMSE | Improvement | Training Data |
|-------|----------|------|-------------|---------------|
| Linear Regression | 0.928 | 2,273 | Baseline | 15000 records |
| **XGBoost (My Model)** | **0.981** | **1,163** | **50% error reduction** | **15,000 records** |

---

## 🧠 My Problem-Solving Journey

### 🔍 Phase 1: Data Discovery & Initial Analysis
When I first explored the **50,000-record insurance dataset**, I encountered critical data quality issues that required domain-specific cleaning:

**My Data Foundation Work:**
- **Analyzed 50,000 customer records** to understand data patterns and quality issues
- **Removed biologically impossible values** (ages > 100, impossible medical entries)
- **Preserved legitimate high-income clients** while capping statistical outliers
- **Applied quantile-based capping** to maintain realistic data distributions
- **Selected 15,000 high-quality records** for robust model training

### 🛠️ Phase 2: Intelligent Feature Engineering
The medical history data across all customers was unstructured text that needed transformation into actionable features.

**My Custom Health Risk Score Development:**
- **Researched medical and insurance literature** to understand condition impacts
- **Developed weighted scoring system** based on treatment costs and prevalence data
- **Transformed complex medical text** into a standardized 0-1 numerical scale
- **Iteratively tested weighting approaches** to maximize predictive power
- **Validated scoring methodology** against actual premium patterns in the data

### 🤖 Phase 3: Algorithm Selection & Optimization
I systematically evaluated multiple modeling approaches to find the optimal solution.

**My Modeling Breakthrough:**
- **Tested Linear Regression, Ridge, and XGBoost** on the 15,000-record training set
- **Discovered XGBoost's superiority** in capturing complex insurance pricing relationships
- **Tuned key parameters** (max_depth=5, n_estimators=50, learning_rate=0.1)
- **Selected XGBoost with Random Search CV** for optimal hyperparameter tuning
- **Achieved 50% error reduction** compared to linear baseline models
- **Maintained excellent generalization** across all customer segments

### 🎯 Phase 4: Solving the Business Requirement Gap
My initial success revealed a critical business alignment issue that required deeper analysis.

**The Critical Insight:**
- Despite 98% overall accuracy, **residual errors reached 30%** for specific customer groups
- **Business requirement demanded <10% maximum error** for all predictions
- Error analysis revealed **age-based segmentation patterns** in prediction accuracy

**My Iterative Solution Development:**

**First Attempt: Age-Based Segmentation**
- Built **`01_seg_premium_lt25.ipynb`** for young adults (18-25) with early-life risk focus
- Built **`02_seg_premium_gt25.ipynb`** for mature customers (25+) with established health patterns
- **Result**: Improved accuracy but still above the 10% error threshold

**Breakthrough: Genetic Risk Intelligence**
- **Researched and developed Genetic Risk Score** capturing inherited health predispositions
- Created **`03_seg_genetic_lt25.ipynb`**: Young adults with genetic risk awareness
- Created **`04_seg_genetic_gt25.ipynb`**: Mature customers with genetic context
- **Final Outcome**: **Achieved <10% maximum error** while improving to 99.2% accuracy

### 👥 Phase 5: Real-World Application Development
I transformed the analytical work into a practical business tool through user-centered design.

**My Deployment Strategy:**
- **Built Streamlit web application** for instant premium predictions
- **Conducted feedback sessions** with insurance professionals to refine the interface
- **Ran user testing** with potential customers to ensure intuitive design
- **Incorporated domain expert input** to match industry terminology and workflows
- **Optimized for performance** to deliver sub-second prediction times



## 📈 Model Error Analysis: Honest Assessment

While the model performs exceptionally well overall across **50,000 records**, I conducted deep error analysis to identify improvement areas:

### 📋 Key Findings:
- **95% of predictions** are within 10% of actual premiums across the full dataset
- **Most errors cluster near zero** – indicating strong overall accuracy
- **Higher errors occur primarily** for older age groups (30+)
- **Root cause**: Dataset imbalance with majority of the **50,000 records** aged 18-25

### 💡 My Insight:
This discovery shows the importance of **honest model assessment**. Rather than just celebrating the high R² score, I identified specific limitations in the **50,000-record dataset** and can now address them through techniques like stratified sampling or age-segmented modeling.

---

## 🛠 Technical Implementation

### 📁 Project Structure
```
premium_prediction_project/
│
├── notebooks/
│   ├── 00_premium_full_analysis.ipynb     # Comprehensive initial analysis
│   ├── 01_seg_premium_lt25.ipynb          # Age segmentation attempt 18 < 25
│   ├── 02_seg_premium_lt25.ipynb          # Age segmentation attempt    > 25
│   ├── 03_seg_genetic_lt25.ipynb          # ✅ Final young demographic model
│   └── 04_seg_genetic_gt25.ipynb          # ✅ Final mature demographic model
│
├── app/               # Production Streamlit application
├── models/            # Deployed specialized models
├── data/              # 50,000 analyzed records (15,000 trained)
└── utils/             # Helper functions and utilities
```

### 🔧 Technologies I Used
- **Python** (Pandas, NumPy, Scikit-learn, XGBoost)
- **Visualization** (Matplotlib, Seaborn) 
- **Web Framework** (Streamlit)
- **Deployment** (Streamlit Cloud)
- **Version Control** (Git, GitHub)

### 📊 Dataset Scale
- **50,000 insurance records analyzed** for comprehensive insights

- **15,000 high-quality record**s used for model training

- Comprehensive customer profiles including demographics, medical history, and lifestyle factors

- Real-world insurance premium data spanning multiple age groups and risk categories
  
## 💡 Business Impact

This project delivers real-world value:
- **Helps insurance companies** price policies more accurately and consistently using comprehensive data
- **Benefits customers** with transparent, fair premium estimates backed by 50,000 examples
- **Reduces manual underwriting time** from hours to seconds
- **Demonstrates how AI** can bring efficiency to complex financial decisions at scale

---

## 🚀 Try It Yourself

**[![Open in Streamlit](https://img.shields.io/badge/Launch%20App-Streamlit-%23FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge&labelColor=FF4B4B)](https://ml-healthcare-premium-prediction-7qrpw78zqct4zhdm7u8v2d.streamlit.app/)**
  
Experience how insurance pricing can be both accurate and accessible. The app demonstrates the practical business value of this machine learning solution trained on **50,000 real insurance records**.

---

## 📝 Lessons Learned & Next Steps

### 🔄 What I'd Do Differently:
- Collect more balanced data across age groups within the 50,000 records
- Implement automated data validation pipelines for large datasets
- Add model monitoring for concept drift detection with ongoing data collection

### 🎯 Future Enhancements:
- Age-segmented models for better demographic coverage across all 50,000 records
- Real-time data integration with insurance systems to expand beyond 50,000 records
- Expanded risk factors for even more accurate pricing with larger datasets

---

## 🌟 Why This Project Matters

This project demonstrates my ability to transform complex data into practical business solutions. From messy insurance data to deployed specialized models, I've shown how machine learning can drive real value when aligned with business requirements.

**Built to solve real insurance pricing challenges** - delivering both technical excellence and practical business utility through specialized, requirement-driven machine learning solutions.

⭐ **If this approach to solving complex business problems with data science resonates with your needs, I'd welcome the opportunity to discuss how I can deliver similar results for your organization.**

---


