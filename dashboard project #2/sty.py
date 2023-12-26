import streamlit as st
import pickle

model_file = 'final_svm_model.pkl'

def predict(symptoms):
    with open('final_svm_model.pkl', 'rb') as file:
        clf = pickle.load(file)
        # Convert symptoms to numerical features before prediction
        # symptoms_numerical = [symptoms.index(symptom) for symptom in symptoms]
        # symptoms_numerical = [symptoms_numerical]  # Model expects a 2D array

        symptoms_numerical = [symptoms.index(symptom) + 1 for symptom in symptoms]
        symptoms_numerical = [symptoms_numerical + [0] * (132 - len(symptoms_numerical))]  # Pad with zeros if needed


        result = clf.predict(symptoms_numerical)
        return result

#print(f"Model '{model_file}' loaded successfully!")
#     else:
#         print(f"Error: File '{model_file}' not found.")
# except Except try:
#     if os.path.exists(model_file):
#         final_svm_model = joblib.load(model_file)
#         ion as e:
#     print(f"Error loading model: {str(e)}")

# with open('final_svm-model.pkl','rb')as file:
#  clf=pickle.load(file)

symptoms=["itching","skin_rash","nodal_skin_eruptions","continuous_sneezing","shivering","chills",
 "joint_pain","stomach_pain","acidity","ulcers_on_tongue","muscle_wasting","vomiting",
 "burning_micturition","spotting_","urination","fatigue","weight_gain","anxiety",
 "cold_hands_and_feets","mood_swings","weight_loss","restlessness","lethargy","patches_in_throat",
 "irregular_sugar_level","cough","high_fever","sunken_eyes","breathlessness","sweating",
 "dehydration","indigestion","headache","yellowish_skin","dark_urine","nausea","loss_of_appetite",
 "pain_behind_the_eyes","back_pain","constipation","abdominal_pain","diarrhoea","mild_fever",
 "yellow_urine","yellowing_of_eyes","acute_liver_failure","fluid_overload""swelling_of_stomach",
 "swelled_lymph_nodes","malaise","blurred_and_distorted_vision","phlegm","throat_irritation",
 "redness_of_eyes","sinus_pressure","runny_nose","congestion","chest_pain","weakness_in_limbs",
 "fast_heart_rate","pain_during_bowel_movements","pain_in_anal_region","bloody_stool",
 "irritation_in_anus","neck_pain","dizziness","cramps","bruising","obesity","swollen_legs",
 "swollen_blood_vessels","puffy_face_and_eyes","enlarged_thyroid","brittle_nails",
 "swollen_extremeties","excessive_hunger","extra_marital_contacts","drying_and_tingling_lips",
 "slurred_speech","knee_pain","hip_joint_pain","muscle_weakness","stiff_neck","swelling_joints",
 "movement_stiffness","spinning_movements","loss_of_balance","unsteadiness",
 "weakness_of_one_body_side","loss_of_smell","bladder_discomfort","foul_smell_of",
 "urine","continuous_feel_of_urine","passage_of_gases","internal_itching",
 "toxic_look_(typhos)","depression","irritability","muscle_pain","altered_sensorium",
 "red_spots_over_body","belly_pain","abnormal_menstruation","dischromic","patches",
 "watering_from_eyes","increased_appetite","polyuria","family_history","mucoid_sputum",
 "rusty_sputum","lack_of_concentration","visual_disturbances"",""receiving_blood_transfusion",
 "receiving_unsterile_injections","coma","stomach_bleeding","distention_of_abdomen",
 "history_of_alcohol_consumption","fluid_overload","blood_in_sputum","prominent_veins_on_calf",
 "palpitations","painful_walking","pus_filled_pimples","blackheads","scurring","skin_peeling",
 "silver_like_dusting","small_dents_in_nails","inflammatory_nails","blister","red_sore_around_nose",
 "yellow_crust_ooze"]

st.title('Disease Prediction System')
selected_symptoms = st.multiselect('Please Select the Symptoms', options=symptoms)

st.write('You selected:', selected_symptoms)

if st.button('Predict'):
    # prediction_result = predict(selected_symptoms)
    st.write('Prediction Result:', selected_symptoms.type)