import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import numpy as np
from pathlib import Path
import pickle

import streamlit_authenticator as stauth



# ---- USER AUTHENTICATION ----

names  = ["Admin", "User"]
usernames = ["admin1", "user1"]

file_path = Path(__file__).parent / "hashed1.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# Initialize the Authenticate instance with the correct arguments
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "diagnosis", "abcdef", cookie_expiry_days=30)


st.markdown("<h1 style='text-align: center; color: white;'>Typhoid Diagnosis</h1>", unsafe_allow_html=True)
name, authenticatoion_status, username = authenticator.login("Login","main")

if authenticatoion_status == False:
    st.error("Username/Password is incorrect")

if authenticatoion_status == None:
    st.warning("Please enter your username and password")

if authenticatoion_status:

# ---- LOGOUT ----
    authenticator.logout("Logout", "sidebar")

    selected = option_menu (
        menu_title = "Typhoid DIAGNOSTICS ",
        options= ["Home Screen","Do you have typhoid","App Guide","Privacy"],
        icons=["house", "book","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    if selected == "Home Screen":
        st.header("Get quick diagnosis for Typhoid")
        st.write("check on your health status today, your health matters.")

        
    if selected == "Do you have typhoid":
        # Load the trained model
        model  = joblib.load('typhoid.pkl')


        # Define the feature labels
        feature_labels = ['itching', 'skin_rash', 'nodal_skin_eruptions',
        'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
        'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
        'vomiting', 'burning_micturition', 'spotting_ urination',
        'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
        'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
        'patches_in_throat', 'irregular_sugar_level', 'cough',
        'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
        'dehydration', 'indigestion', 'headache', 'yellowish_skin',
        'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
        'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
        'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
        'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
        'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
        'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
        'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
        'fast_heart_rate', 'pain_during_bowel_movements',
        'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
        'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
        'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
        'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
        'excessive_hunger', 'extra_marital_contacts',
        'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
        'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
        'swelling_joints', 'movement_stiffness', 'spinning_movements',
        'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
        'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
        'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
        'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
        'altered_sensorium', 'red_spots_over_body', 'belly_pain',
        'abnormal_menstruation', 'dischromic _patches',
        'watering_from_eyes', 'increased_appetite', 'polyuria',
        'family_history', 'mucoid_sputum', 'rusty_sputum',
        'lack_of_concentration', 'visual_disturbances',
        'receiving_blood_transfusion', 'receiving_unsterile_injections',
        'coma', 'stomach_bleeding', 'distention_of_abdomen',
        'history_of_alcohol_consumption', 'fluid_overload.1',
        'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
        'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
        'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
        'inflammatory_nails', 'blister', 'red_sore_around_nose',
        'yellow_crust_ooze']
        


        # Create a form for user input
        st.title('Typhoid Prediction')

        options = ['itching', 'skin_rash', 'nodal_skin_eruptions',
        'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
        'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
        'vomiting', 'burning_micturition', 'spotting_ urination',
        'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
        'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
        'patches_in_throat', 'irregular_sugar_level', 'cough',
        'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
        'dehydration', 'indigestion', 'headache', 'yellowish_skin',
        'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
        'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
        'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
        'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
        'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
        'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
        'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
        'fast_heart_rate', 'pain_during_bowel_movements',
        'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
        'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
        'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
        'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
        'excessive_hunger', 'extra_marital_contacts',
        'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
        'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
        'swelling_joints', 'movement_stiffness', 'spinning_movements',
        'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
        'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
        'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
        'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
        'altered_sensorium', 'red_spots_over_body', 'belly_pain',
        'abnormal_menstruation', 'dischromic _patches',
        'watering_from_eyes', 'increased_appetite', 'polyuria',
        'family_history', 'mucoid_sputum', 'rusty_sputum',
        'lack_of_concentration', 'visual_disturbances',
        'receiving_blood_transfusion', 'receiving_unsterile_injections',
        'coma', 'stomach_bleeding', 'distention_of_abdomen',
        'history_of_alcohol_consumption', 'fluid_overload.1',
        'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
        'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
        'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
        'inflammatory_nails', 'blister', 'red_sore_around_nose',
        'yellow_crust_ooze']

        
        
        # Convert categorical inputs to numerical values
        # Multiselect widget
        selected_options = st.multiselect('What are your symptoms:', options)
        
        # Create a dictionary to store binary representation
        binary_representation = {option: 1 if option in selected_options else 0 for option in options}
        
        
        # Make a prediction using the machine learning model
        if st.button('Predict'):
            # Prepare the binary representation as input features for the model
            input_features = np.array(list(binary_representation.values())).reshape(1, -1)

            # Make a prediction
            prediction = model.predict(input_features)

            # Display the prediction
            if prediction[0] == 1:
                st.write("Not very Proabable you  have typhoid  but still take good care of yourself regardless")
            else:
                st.write("It is Probable you might have typhoid therfore you should see a doctor")

    if selected == "App Guide":
        st.title(f'Typhoid Dignosis App Guide {selected}')

        '''
        Welcome to the Typhoid Dignosis App guide. This app is designed to help users detect the signs of a typhoid and provide immediate guidance on what to do in such a situation. Please read this guide to familiarize yourself with the app's features and functionality
        1. Installation and Setup:
        - Install the neceesary requirements
        - Launch the app on any broswer of your choice using the code "streamlit run app2.py" on your terminal
        
        2. App Navigation:
        - Use the navigation menu or icons to access different sections of the app.
        
        4. Typhoid Detection:
        - To detect signs of a stroke, select the "Do you have typhoid" feature from the app's main screen.
        - Follow the instructions provided on-screen to begin the detection process.
        - Perform the specified actions, such as imputing the right, as guided by the app.
        - The app will analyze the collected data and provide an assessment of the likelihood of typhoid.
        
        5. Data Privacy and Security:
        - The app may collect personal and health-related data to provide personalized recommendations and improve its services.
        - Ensure that you have reviewed and understand the app's privacy policy before using it.

        
        Conclusion:
        Congratulations! You are now familiar with the Typhoid Detection App. Use the app responsibly to monitor your health and seek professional medical assistance when necessary. Remember, the app is not a substitute for professional medical advice, and it is essential to consult a healthcare professional for a proper diagnosis and treatment. Stay healthy and take care!
        '''

    if selected == "Privacy":
        st.title("App's Privacy Policy")
        '''
        Privacy Policy for Typhoid Diagnosis App

        At Typhoid DIAGNOSTICS, we take your privacy seriously. This Privacy Policy outlines how we collect, use, disclose, and safeguard your personal information when you use our Typhoid Diagnosis App (referred to as the "App").
        
        Please read this Privacy Policy carefully. By accessing or using the App, you acknowledge that you have read, understood, and agree to be bound by the terms and conditions of this Privacy Policy. If you do not agree with this Privacy Policy, please do not use the App.
        
        1. Information We Collect
        
        1.1 Personal Information:
        We do not collect any personally identifiable information (PII) such as your  address, or contact details through the App. We understand the sensitivity of medical information and prioritize the protection of your privacy.
        
        1.2 Non-Personal Information:
        We may collect non-personal information about your use of the App, including but not limited to:
        
        - Device Information: We may collect information about the device you use to access the App, such as the device type, operating system version, and unique device identifiers.
        
        - Log Data: Our servers automatically record certain information when you use the App. This information may include your IP address, browser type, the pages you visit, the time and date of your visit, and other statistics.
        
        2. How We Use Your Information
        
        We only use the information we collect from you to improve and enhance the App's functionality and user experience. The non-personal information we collect is used for analytical purposes, to understand trends, and to troubleshoot technical issues.
        
        3. Information Sharing and Disclosure
        
        We do not sell, trade, or transfer your personal or non-personal information to third parties for marketing or commercial purposes. However, we may disclose your information in the following circumstances:
        
        - Legal Requirements: We may disclose your information if required to do so by law or in response to a valid legal request, such as a court order or government investigation.
        
        - Safety and Security: We may disclose your information to protect the safety and security of the App, our users, or the general public.
        
        4. Data Security
        
        We implement appropriate security measures to protect your information from unauthorized access, alteration, disclosure, or destruction. However, please be aware that no method of transmission over the internet or electronic storage is 100% secure, and we cannot guarantee absolute security.
        
        
        6. Changes to This Privacy Policy
        
        We reserve the right to modify this Privacy Policy at any time. Any changes we make will be effective immediately upon posting the updated Privacy Policy in the App. Your continued use of the App after any modifications to the Privacy Policy constitutes your acceptance of the revised Privacy Policy.
        
        7. Contact Us
        
        If you have any questions, concerns, or suggestions regarding this Privacy Policy or our privacy practices, please contact us at huihul@gmail.com.
        
        Last Updated: 2023
        
            '''