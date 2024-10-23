#import streamlit as st
#from bs4 import BeautifulSoup
#import openai
import requests
from requests import get
from helper_functions import llm
from openai import OpenAI
import feedparser
#from langchain_community.llms import OpenAI
#from langchain_openai import OpenAI

# OpenAI API key (get the API key from llm)
client = OpenAI(api_key=llm.OPENAI_KEY)
#client = OpenAI(api_key=llm.OPENAI_KEY)

#Get the CPF URL from the Ask_CPF.py
def scrape_cpf_website():
    print("inside scrape function..")
    url = 'https://www.cpf.gov.sg/member/infohub/educational-resources/guide-for-first-time-resale-flat-buyers'
    #url = 'https://api.python.langchain.com/en/latest/llms/langchain_community.llms.openai.OpenAI.html'
    
    rss_feed = get(url).text
    feed = feedparser.parse(rss_feed)
    text = ''
    for post in feed['entries']:
        text = f'{text} {post["title"]} - {post["description"]}'
    
    return text

#Then ask the LLM
def ask_cpf_chatbot(query):
    print("inside ask cpf chatbot.. query.. ", query)
    text = scrape_cpf_website()
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"provide answer from this document {text}"},
        {"role": "user", "content": query}
    ]
    )
    response = completion.choices[0].message.content
    return response
    


 