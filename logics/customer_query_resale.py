import openai
import pandas as pd
from helper_functions import llm
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent

# Load the Resale file
filepath = './data/Resaleflatprices.csv'
df = pd.read_csv(filepath)


def process_user_message(user_input):
    agent = create_csv_agent(llm.llmLangChain, filepath, verbose=True,allow_dangerous_code=True)
    response = agent.run(user_input)

    return response