import os

import pandas as pd
import json
import openai
import matplotlib.pyplot as plt
import langchain_experimental
from matplotlib import pyplot as plt
from helper_functions import llm

#from langchain import OpenAI
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

print("go into the customer plot python...")
# Load the Resale file
filename = './data/Resaleflatprices.csv'
#df = pd.read_csv(filepath)

print("after loading the file..")

print ("load the key and create ChatOpenAI object...")
#load API key
#pandasllm = OpenAI(model = 'gpt-4o-mini', OPENAI_API_KEY = llm.OPENAI_KEY)

#Create a OpenAIllm using ChatOpenAi
openAIllm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=llm.OPENAI_KEY,  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)

"""
Create an agent that can access and use a large language model (LLM).
Args: filename: The path to the CSV file that contains the data.
Returns: An agent that can access and use the LLM.
"""
def create_agent(filename: str):
    # Read the CSV file into a Pandas DataFrame.
    df = pd.read_csv(filename)
    #print("top 3 rows of the file ...",df.head(3))

    # Create a Pandas DataFrame agent usng the OpenAIllm with the open AI key
    return create_pandas_dataframe_agent(openAIllm, df, 
        verbose=False,allow_dangerous_code=True)

def query_agent(agent, query):
    #print("user query is .. ", query)
    #print("agent is .. ", agent)
  
    # Run the prompt through the agent.
    #response = agent.run(query)
    response = agent.invoke(query)
    print("response inside query_agent function is ", response)
    # Convert the response to a string.
    #return response.__str__()
    responseStr = str(response)
    return responseStr

def process_user_message(user_input):
    # Create an agent using the CSV file.
    askagent = create_agent(filename)

    print("response inside process_user_message function is ", user_input)
    
    try:
        # Query the agent
        response = query_agent(askagent, user_input)        
        return response
    except:
        err_msg = "An exception has occurred!"
        return err_msg
    