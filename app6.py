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

st.markdown("<h1 style='text-align: center; color: white;'>Hepatitis Diagnosis</h1>", unsafe_allow_html=True)
name, authenticatoion_status, username = authenticator.login("Login","main")

if authenticatoion_status == False:
    st.error("Username/Password is incorrect")

if authenticatoion_status == None:
    st.warning("Please enter your username and password")

if authenticatoion_status:

# ---- LOGOUT ----
    authenticator.logout("Logout", "sidebar")

    selected = option_menu (
        menu_title = "Malaria DIAGNOSTICS ",
        options= ["Home Screen","Do you have hepatitis","App Guide","Privacy"],
        icons=["house", "book","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    if selected == "Home Screen":
        st.header("Get quick diagnosis for Hepatitis")
        st.write("check on your health status today, your health matters.")

        
    if selected == "Do you have hepatitis":
        # Load the trained model
        model  = joblib.load('hepatitis.pkl')


        # Create a form for user input
        st.title('Hepatitis Prediction')

        
        Age = st.number_input('Age', min_value=1, max_value=100, value=3)
        Sex = st.selectbox('Whats your sex(Male = 1 and Female = 0)' , [1, 0])
        ALB = st.number_input('ALB', min_value=1, max_value=100, value=3)
        ALT = st.number_input('ALT', min_value=1, max_value=400, value=3)
        ALP = st.number_input('ALP', min_value=1, max_value=500, value=3)
        AST = st.number_input('AST', min_value=1, max_value=400, value=3)
        BIL  = st.number_input('BIL', min_value=1, max_value=300, value=3)
        CHE  = st.number_input('CHE', min_value=1, max_value=20, value=3)
        CHOL = st.number_input('CHOL', min_value=1, max_value=15, value=3)
        CREA = st.number_input('CREA', min_value=1, max_value=1200, value=3)
        GGT = st.number_input('GGT', min_value=1, max_value=700, value=3)
        PROT = st.number_input('PROT', min_value=1, max_value=100, value=3)
       
        input_data = [Age, Sex, ALB, ALP, ALT, AST, BIL, CHE, CHOL,
       CREA, GGT, PROT]


        if st.button('Predict'):
            # Convert input data to a 2D NumPy array
            input_data_2d = np.array([list(input_data)])
    
            # Now, you can use input_data_2d for prediction
            prediction = model.predict(input_data_2d)
    
            if prediction[0] == 1:
                st.write("Not very Proabable you will have Hepatitis but still take good care of yourself regardless")
            else:
                st.write("It is Probable you might have Hepatitis soon therfore you should see a doctor")

    if selected == "App Guide":
        st.title(f'Hepatitis Dignosis App Guide {selected}')

        '''
        Welcome to the Hepatitis Dignosis App guide. This app is designed to help users detect the signs of a hepatitis early and provide immediate guidance on what to do in such a situation. Please read this guide to familiarize yourself with the app's features and functionality
        1. Installation and Setup:
        - Install the neceesary requirements
        - Launch the app on any broswer of your choice using the code "streamlit run app6.py" on your terminal
        
        2. App Navigation:
        - Use the navigation menu or icons to access different sections of the app.
        
        4. Hepatitis Detection:
        - To detect signs of a hepatitis, select the "Do you have hepatitis" feature from the app's main screen.
        - Follow the instructions provided on-screen to begin the detection process.
        - Perform the specified actions, such as imputing the right, as guided by the app.
        - The app will analyze the collected data and provide an assessment of the likelihood of a hepatitis.
        
        5. Data Privacy and Security:
        - The app may collect personal and health-related data to provide personalized recommendations and improve its services.
        - Ensure that you have reviewed and understand the app's privacy policy before using it.

        
        Conclusion:
        Congratulations! You are now familiar with the Hepatitis Detection App. Use the app responsibly to monitor your health and seek professional medical assistance when necessary. Remember, the app is not a substitute for professional medical advice, and it is essential to consult a healthcare professional for a proper diagnosis and treatment. Stay healthy and take care!
        '''

    if selected == "Privacy":
        st.title("App's Privacy Policy")
        '''
        Privacy Policy for Hepatitis Diagnosis App

        At P DIAGNOSTICS, we take your privacy seriously. This Privacy Policy outlines how we collect, use, disclose, and safeguard your personal information when you use our Hepatitis Diagnosis App (referred to as the "App").
        
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