import streamlit as st
import pickle
import numpy as np

# Load model
@st.cache_resource
def load_model():
    with open("pipe.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Streamlit UI
st.title("🏃‍♂️ Athletic Performance Predictor")
# Markdown for description
st.markdown("**Note:** The model is trained on a dataset of basketball players. Working on other sports data is in progress.")
st.markdown("**Disclaimer:** This is a demo application and the predictions are not guaranteed to be accurate. But i will try to make it as accurate as possible.")
st.markdown("Enter the athlete's data below:")
posture=['PF', 'SG', 'C', 'SF', 'PG', 'F', 'G', 'C-PF', 'SF-SG', 'PG-SG', 'PF-C', 'SG-PG', 'SG-SF', 'PF-SF', 'SF-PF', 'G-F', 'F-C', 'F-G', 'C-F', 'SG-PF', 'C-SF', 'SF-PG', 'PG-SF']
# Example inputs (customize these as per your model)
posture = st.selectbox("Position", posture)
age = st.number_input("Age", min_value=16, max_value=45, value=26)
mp = st.number_input("Minutes Played", min_value=0, max_value=4000, value=90)#MP
sm = st.number_input("Successful Makes", min_value=0, max_value=1800,value=200)#FG
ta = st.number_input("Total Attempts",min_value=0,max_value=3500,value=400)#FGA
asr = st.number_input("Accuracy Success Rate", min_value=0.0, max_value=1.0, value=0.5)#FG%
tps = st.number_input("Total Player Score", min_value=0, max_value=4000,value=400)#PTS
height = st.number_input("Height (cm)", min_value=100, max_value=235, value=180)
weight = st.number_input("Weight (Kg)", min_value=45, max_value=250, value=75)

if st.button("Predict Performance"):
    # Preprocess input data
    input_data = [posture, age, mp, sm, ta, asr, tps, height, weight,sm/(ta+0.000001),weight/((height/100)**2),tps/(sm+0.000001),tps/(ta+0.000001),height/weight]
    
    # Predict
    prediction = model.predict(np.array(input_data).reshape(1, -1))
    # Convert prediction to a more interpretable format if necessary
    prediction= int(np.round(prediction[0], 2))  # Example: round to 2 decimal places
    prediction= ((prediction+90)/219)*100
    # Output
    st.success(f"🏅 Predicted Performance(Percentage): {round(prediction,2)}")
