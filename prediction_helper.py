import pandas as pd
import joblib

# Load pre-trained models and scalers
model_young = joblib.load("artifacts/model_young.joblib")
model_rest = joblib.load("artifacts/model_rest.joblib")
scaler_young = joblib.load("artifacts/scaler_young.joblib")
scaler_rest = joblib.load("artifacts/scaler_rest.joblib")


def calculate_normalized_risk(medical_history: str) -> float:
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    diseases = medical_history.lower().split(" & ")
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)

    max_score = 14  # heart disease + diabetes/high BP
    return total_risk_score / max_score


def preprocess_input(input_dict: dict) -> pd.DataFrame:
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Map categorical inputs
    if input_dict.get('Gender') == 'Male':
        df['gender_Male'] = 1
    if input_dict.get('Region') in ['Northwest', 'Southeast', 'Southwest']:
        df[f"region_{input_dict['Region']}"] = 1
    if input_dict.get('Marital Status') == 'Unmarried':
        df['marital_status_Unmarried'] = 1
    if input_dict.get('BMI Category') in ['Obesity', 'Overweight', 'Underweight']:
        df[f"bmi_category_{input_dict['BMI Category']}"] = 1
    if input_dict.get('Smoking Status') in ['Occasional', 'Regular']:
        df[f"smoking_status_{input_dict['Smoking Status']}"] = 1
    if input_dict.get('Employment Status') in ['Salaried', 'Self-Employed']:
        df[f"employment_status_{input_dict['Employment Status']}"] = 1

    df['insurance_plan'] = insurance_plan_encoding.get(input_dict.get('Insurance Plan'), 1)
    df['age'] = input_dict.get('Age', 0)
    df['number_of_dependants'] = input_dict.get('Number of Dependants', 0)
    df['income_lakhs'] = input_dict.get('Income in Lakhs', 0)
    df['genetical_risk'] = input_dict.get('Genetical Risk', 0)
    df['normalized_risk_score'] = calculate_normalized_risk(input_dict.get('Medical History', 'none'))

    return handle_scaling(df['age'].values[0], df)


def handle_scaling(age: int, df: pd.DataFrame) -> pd.DataFrame:
    scaler_object = scaler_young if age <= 25 else scaler_rest
    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    # Workaround for scaler column dependency
    df['income_level'] = 0
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis=1, inplace=True)

    return df


def predict(input_dict: dict) -> int:
    input_df = preprocess_input(input_dict)
    model = model_young if input_dict['Age'] <= 25 else model_rest
    prediction = model.predict(input_df)
    return int(prediction[0])
