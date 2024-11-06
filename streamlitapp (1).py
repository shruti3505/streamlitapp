# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

# --- App Title ---
st.set_page_config(page_title="Interactive Visualizations", layout="wide")
st.title("Interactive Visualizations with Plotly and Streamlit")
st.markdown("### An engaging workshop for visualization skills with Plotly and Streamlit")

# --- Sidebar for User Input ---
st.sidebar.header("Workshop Details")
name = st.sidebar.text_input("Name:", "SHRUTI ROY")
usn = st.sidebar.text_input("USN:", "45")
instructor_name = st.sidebar.text_input("Instructor:", "SOCSE")

# --- Load and Display Dataset ---
tips = sns.load_dataset('tips')
st.write("### Dataset Overview", tips.head())

# --- Interactive Bar Chart ---
st.subheader("Bar Chart - Average Tip by Day")
fig = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig, use_container_width=True)
