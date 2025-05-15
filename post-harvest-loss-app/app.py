import streamlit as st

st.set_page_config(
    page_title="Nigeria Post-Harvest Loss Dashboard",
    page_icon="🌾",
    layout="wide"
)

st.title("Nigeria Post-Harvest Loss Dashboard")
st.sidebar.success("Select a page above.")

st.markdown("""
 Welcome to the Post-Harvest Loss Reduction Platform
This interactive dashboard helps young agripreneurs and farmers:
- Identify high-risk areas for crop losses
- Predict potential post-harvest losses
- Access smart solutions to minimize losses
- Connect with resources for youth-led agri-businesses

Select a page from the sidebar to get started.
""")
