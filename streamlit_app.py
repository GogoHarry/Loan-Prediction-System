import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load the preprocessing pipeline and the trained model
model_pipeline = joblib.load('best_rf_model.pkl')

# Define the function for making predictions
def predict_loan_status(data):
    # Make predictions using the model pipeline
    predictions = model_pipeline.predict(data)
    return predictions

def run_data():
    st.set_page_config(page_title='Loan Prediction Web App')
    st.sidebar.header('Loan Prediction App')
    loan_image = Image.open(r'C:\Users\Harrison\Documents\loan_prediction_system\images\loan.jpg')
    st.sidebar.info('This app is created to predict whether an applicant is eligible for a loan or not.')
    st.sidebar.image(loan_image, use_column_width=True)
    st.title('Please fill this form..')

    gender = st.selectbox('Gender', ['Male', 'Female'])
    married = st.selectbox('Married', ['Yes', 'No'])
    dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
    education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    self_emp = st.selectbox('Self Employed', ['Yes', 'No'])
    total_income = st.number_input('Total Income', min_value=1000, max_value=81000, value=1000)
    loan_amount = st.number_input('Loan Amount', min_value=100, max_value=10000, value=100)
    loan_amount_term = st.selectbox('Loan Amount Term', [1010, 2000, 3500])
    credit_history = st.selectbox('Credit History', [0, 1])
    property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

    output = ""

    input_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_emp],
        'TotalIncome': [total_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    # Button for making predictions
    if st.button('Predict'):
        prediction = predict_loan_status(input_data)
        if prediction == 1:
            st.success('The applicant is eligible for loan')
        else:
            st.error('The applicant is not eligible for loan')

if __name__ == '__main__':
    run_data()

# Custom footer with social media links
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    </style>
    <div class="footer">
        Developed by Gogo Harrison - ©2024
        <br>
        <a href="https://x.com/G_Harrison27" target="_blank">Twitter</a>
        <a href="https://www.linkedin.com/in/gogo-harrison/" target="_blank">LinkedIn</a>
        <a href="https://github.com/GogoHarry" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)
