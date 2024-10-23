import streamlit as st
import pandas as pd

# Load the JSON file
filepath = './data/Resaleflatprices.csv'
df = pd.read_csv(filepath)
# Display the content of the DataFrame in streamlit
# Display the dataframe in Streamlit
st.dataframe(df)  
# Alternatively, you can use st.table(df) to display a static table

