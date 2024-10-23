import streamlit as st
from logics.customer_query_cpf import ask_cpf_chatbot
#from logics.customer_query_cpf import scrape_cpf_website
from helper_functions.utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Project Type C"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Ask CPF query")

# Check if the password is correct.  
if not check_password():  
    st.stop()

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")
    st.divider()

    #response, result = process_user_message(user_prompt)
    response = ask_cpf_chatbot(user_prompt)
    
    st.divider()
    st.write(response)