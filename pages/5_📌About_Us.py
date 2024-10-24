import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Resale HDB Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Type C Project")

st.write("This is a Streamlit App that use the OpenAI API to generate text completions.")

with st.expander("2 Use cases"):
    st.write("Use Case 1 - Query on HDB Resale price by location, floor area etc")
    st.write("Use Case 2 - Check how to apply resale flat using CPF.")
    st.write("The app will generate a text completion after users enter their question.")
