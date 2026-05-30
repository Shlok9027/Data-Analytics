# import streamlit as st
# import pandas as pd

# import joblib
 

# model = joblib.load(r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\KNN_heart_disease_predictor_model.pkl')

# scaler = joblib.load(r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\scaler.pkl')

# expected_columns = joblib.load(r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\columns.pkl')

# st.title("Heart Disease Prediction App by Shlok💖")

# st.markdown('Provide the following details to predict the likelihood of heart disease:')


# age = st.slider('Age', 18,100,40)
# sex = st.selectbox('Gender',['M', 'F'])

# chest_pain_type = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'TA', 'ASY'])

# resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 90,200,120)

# cholesterol = st.number_input('Cholesterol (mg/dl)', 100,600,200)


# fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])


# resting_ecg = st.selectbox('Resting ECG' , ['Normal', 'ST', 'LVH'])


# max_hr = st.slider('Max Heart Rate', 60,220,150)


# exercise_angina = st.selectbox('Exercise Induced Angina', ['Y', 'N'])

# oldpeak = st.number_input('Oldpeak (ST depression)', 0.0,6.0,1.0)

 
# st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])




# if st.button('Predict'):
#     raw_data = {
#         'age': age,
#         'RestingBP': resting_bp,
#         'Cholesterol': cholesterol,
#         'FastingBS': fasting_bs,
#         'MaxHR': max_hr,
#         'Oldpeak': oldpeak,
#         'Sex_' +sex :1,
#         'ChestPainType_' + chest_pain_type :1,
#         'RestingECG_' + resting_ecg :1,
#         'ExerciseAngina_' + exercise_angina :1,
#         'ST_Slope_' + st_slope :1

#     }


#     input_data = pd.DataFrame([raw_data])

#     for col in expected_columns:
#         if col not in input_data.columns:
#             input_data[col] = 0


#     input_data = input_data[expected_columns]


#     scaled_data = scaler.transform(input_data)

#     prediction = model.predict(scaled_data)[0]



#     if prediction == 1:
#         st.error('⚠️ High Rish of Heart Diease... Please consult a doctor immediately!')
#     else:
#         st.success('✅ Low Risk of Heart Disease. Keep up the healthy lifestyle!')




import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="💖",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #111827, #1e293b);
    color: white;
}

/* Title Styling */
.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: 700;
    background: linear-gradient(to right, #ff4b91, #ff7eb3, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 10px;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #d1d5db;
    margin-bottom: 40px;
}

/* Glassmorphism Card */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 25px;
    padding: 35px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.15);
}

/* Input Labels */
label {
    color: white !important;
    font-weight: 500 !important;
}

/* Buttons */
.stButton>button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(90deg, #ff4b91, #7c3aed);
    color: white;
    font-size: 22px;
    font-weight: bold;
    transition: 0.3s ease;
    box-shadow: 0 0 20px rgba(255,75,145,0.5);
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #7c3aed, #ff4b91);
    box-shadow: 0 0 30px rgba(124,58,237,0.8);
}

/* Success Message */
.stSuccess {
    border-radius: 15px;
    padding: 20px;
    font-size: 20px;
}

/* Error Message */
.stError {
    border-radius: 15px;
    padding: 20px;
    font-size: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #1e293b);
}

/* Animated Glow */
.glow {
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from {
        text-shadow: 0 0 10px #ff4b91;
    }
    to {
        text-shadow: 0 0 25px #7c3aed;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #
model = joblib.load(
    r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\KNN_heart_disease_predictor_model.pkl'
)

scaler = joblib.load(
    r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\scaler.pkl'
)

expected_columns = joblib.load(
    r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\columns.pkl'
)

# ---------------- HEADER ---------------- #
st.markdown(
    '<h1 class="main-title glow">💖 Heart Disease Prediction App 💖</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">AI Powered Heart Risk Analysis System by Shlok</p>',
    unsafe_allow_html=True
)

# ---------------- MAIN CARD ---------------- #
with st.container():

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider('Age', 18, 100, 40)

        sex = st.selectbox('Gender', ['M', 'F'])

        chest_pain_type = st.selectbox(
            'Chest Pain Type',
            ['ATA', 'NAP', 'TA', 'ASY']
        )

        resting_bp = st.number_input(
            'Resting Blood Pressure (mm Hg)',
            90, 200, 120
        )

        cholesterol = st.number_input(
            'Cholesterol (mg/dl)',
            100, 600, 200
        )

        fasting_bs = st.selectbox(
            'Fasting Blood Sugar > 120 mg/dl',
            [0, 1]
        )

    with col2:

        resting_ecg = st.selectbox(
            'Resting ECG',
            ['Normal', 'ST', 'LVH']
        )

        max_hr = st.slider(
            'Max Heart Rate',
            60, 220, 150
        )

        exercise_angina = st.selectbox(
            'Exercise Induced Angina',
            ['Y', 'N']
        )

        oldpeak = st.number_input(
            'Oldpeak (ST depression)',
            0.0, 6.0, 1.0
        )

        st_slope = st.selectbox(
            'ST Slope',
            ['Up', 'Flat', 'Down']
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- PREDICT BUTTON ---------------- #
    if st.button('🔍 Predict Heart Risk'):

        raw_data = {
            'age': age,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'MaxHR': max_hr,
            'Oldpeak': oldpeak,
            'Sex_' + sex: 1,
            'ChestPainType_' + chest_pain_type: 1,
            'RestingECG_' + resting_ecg: 1,
            'ExerciseAngina_' + exercise_angina: 1,
            'ST_Slope_' + st_slope: 1
        }

        input_data = pd.DataFrame([raw_data])

        for col in expected_columns:
            if col not in input_data.columns:
                input_data[col] = 0

        input_data = input_data[expected_columns]

        scaled_data = scaler.transform(input_data)

        prediction = model.predict(scaled_data)[0]

        st.markdown("<br>", unsafe_allow_html=True)

        if prediction == 1:
            st.error(
                '⚠️ High Risk of Heart Disease Detected!\n\nPlease consult a doctor immediately.'
            )
        else:
            st.success(
                '✅ Low Risk of Heart Disease.\n\nKeep maintaining a healthy lifestyle!'
            )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #
st.markdown("""
<div style='text-align:center; margin-top:30px; color:gray;'>
Made with ❤️ using Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)