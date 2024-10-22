import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

pdf_file = './data/Project_Info.pdf'
#pdf_viewer('./data/Project_info.pdf')
pdf_viewer(pdf_file)
