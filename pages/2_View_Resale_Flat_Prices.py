import streamlit as st
import pandas as pd

# Load the JSON file
filepath = './data/Resaleflatprices.csv'
df = pd.read_csv(filepath)
# Display the content of the DataFrame in streamlit
# Display the dataframe in Streamlit
st.dataframe(df)  
# Alternatively, you can use st.table(df) to display a static table

#with open(filepath, 'r') as file:
#    json_string = file.read()
#    dict_of_courses = json.loads(json_string)
#    print(dict_of_courses)

# Extract the value of the `dict_of_courses` dictionary
# If you are not sure what the dictionary looks like, you can print it out
#list_of_dict = []
#for course_name, details_dict in dict_of_courses.items():
#    list_of_dict.append(details_dict)

# display the `dict_of_course` as a Pandas DataFrame
#df = pd.DataFrame(list_of_dict)
#df