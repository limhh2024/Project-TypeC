# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_resale import process_user_message
from helper_functions.utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Project Type C"
)
# endregion <--------- Streamlit App Configuration --------->

#Title of the page
st.title("HDB resale flat price query")
st.markdown("""<style>.small-font {font-size:15px;}
    </style><div class='small-font'>Sample query 1 - What is the largest area flat in pasir ris
</div>""", unsafe_allow_html=True)
st.markdown("""<style>.small-font {font-size:15px;}
    </style><div class='small-font'>Sample query 2 - Which flat type has the highest resale price in simei st 1
</div>""", unsafe_allow_html=True)
st.markdown("""<style>.small-font {font-size:15px;}
    </style><div class='small-font'>Sample query 3 - How much is the cheapest Executive flat type in Geylang
</div>""", unsafe_allow_html=True)
st.markdown("\n\n")

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
    response = process_user_message(user_prompt)
    #st.write(response)

    st.divider()

    st.write(response)
    #print(result)
    #df = pd.DataFrame(course_details)
    #df 
