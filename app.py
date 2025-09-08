import streamlit as st
import requests

st.title("📊 Instagram Channel Analyzer")

backend_url = "http://127.0.0.1:8000"

if st.button("Health Check"):
    r = requests.get(f"{backend_url}/health")
    st.write(r.json())

if st.button("View Metrics"):
    r = requests.get(f"{backend_url}/metrics")
    st.json(r.json())

if st.button("Summarize Channel"):
    r = requests.get(f"{backend_url}/summarize")
    st.json(r.json())

if st.button("Get Recommendation"):
    r = requests.get(f"{backend_url}/recommend")
    st.json(r.json())
