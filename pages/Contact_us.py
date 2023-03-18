import streamlit as st
import pandas as pd
from send_email import send_email

# load the topics from a csv file
topics_df = pd.read_csv("topics.csv")
topics_list = topics_df["topic"].tolist()

# create the form
with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    st.selectbox("What Topic do you want to discuss?", topics_list)
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    send_email(message)
    st.info("Your email was sent successfully")