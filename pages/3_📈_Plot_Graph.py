import streamlit as st
from logics.customer_plot_graph import process_user_message
from helper_functions.utility import check_password
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Project Type C"
)
# endregion <--------- Streamlit App Configuration --------->
#Title of the page
st.title("Plot Graph - Resale Flat")
st.markdown("""<style>.small-font {font-size:15px;}
    </style><div class='small-font'>Sample query 1 - Create a bar chart on the top 5 town by resale prices
</div>""", unsafe_allow_html=True)
st.markdown("""<style>.small-font {font-size:15px;}
    </style><div class='small-font'>Sample query 2 - Do a table with 5 towns have the highest remaining lease and their resale price columns
</div>""", unsafe_allow_html=True)
st.markdown("""<style>.small-font {font-size:15px;}
    </style><div class='small-font'>Sample query 2 - Do a bar chart with top 3 towns have the highest remaining lease
</div>""", unsafe_allow_html=True)
st.markdown("\n\n")

# Check if the password is correct.  
if not check_password():  
    st.stop()

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    # User has clicked the submit button
    st.toast(f"User Input Submitted - {user_prompt}")
    st.divider()
    
    #st.write("Going into the graph program..")
    response = process_user_message(user_prompt)
    st.divider()
    #write_response(response)

    fig = plt.gcf()
    if fig.get_axes():
        st.pyplot(fig, use_container_width=False)
    else:
        st.write(response)

