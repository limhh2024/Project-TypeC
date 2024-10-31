import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

#To note - filename is case sensitive for pdf_viewer
pdf_file = './data/Project_Info.pdf'
pdf_viewer(pdf_file)
