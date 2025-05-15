import streamlit as st

st.set_page_config(layout="wide")
st.title("👨‍🌾 Youth Agri-Business Support")

st.header("Resources for Young Agripreneurs")

tab1, tab2, tab3 = st.tabs(["Funding", "Training", "Mentorship"])

with tab1:
    st.header("Funding Opportunities")
    
    st.subheader("Grants for Young Farmers")
    st.markdown("""
    1. Youth Agripreneurs Fund - Up to ₦5,000,000
       - Eligibility: 18-35 years, business plan required
       - Application: www.agricfund.ng/youth
    
    2. Agric SME Grant - Up to ₦2,500,000
       - For businesses <3 years old
       - Application: www.smefund.gov.ng
    
    3. State Agricultural Loans - Varies by state
       - Contact your state agriculture department
    """)
    
    st.subheader("Equipment Financing")
    st.markdown("""
    - Bank of Agriculture: 5% interest rate
    - NIRSAL Microfinance Bank: Collateral-free loans
    - Commercial Banks: Agricultural loan products
    """)

with tab2:
    st.header("Training Programs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Online Courses")
        st.markdown("""
        - Post-Harvest Management (FAO)
        - Agribusiness Fundamentals (Coursera)
        - Agricultural Value Chains (Udemy)
        """)
        st.button("View Online Courses")
    
    with col2:
        st.subheader("Practical Training")
        st.markdown("""
        - Songhai Farms Training (6 months)
        - IITA Youth Program (3 months)
        - State Agricultural Training Centers
        """)
        st.button("Find Local Training")

with tab3:
    st.header("Mentorship Network")
    
    st.subheader("Connect with Experienced Agripreneurs")
    st.markdown("""
    Our mentorship program matches you with successful farmers and agribusiness owners:
    - 1-on-1 mentoring sessions
    - Business plan review
    - Market access guidance
    - Technical advice
    """)
    
    st.subheader("Sign Up for Mentorship")
    with st.form("mentor_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=18, max_value=40)
        location = st.text_input("Location")
        crop = st.text_input("Main Crop/Activity")
        experience = st.selectbox("Years of Experience", ["<1", "1-3", "3-5", "5+"])
        submit = st.form_submit_button("Apply for Mentorship")
        
        if submit:
            st.success("Application submitted! We'll match you with a mentor within 7 days.")
