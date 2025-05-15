import streamlit as st

st.set_page_config(layout="wide")
st.title("💡 Smart Solutions Hub")

st.header("Innovative Solutions to Reduce Post-Harvest Losses")

tab1, tab2, tab3, tab4 = st.tabs(["Storage", "Transportation", "Processing", "Market Linkages"])

with tab1:
    st.header("Smart Storage Solutions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Cold Storage Units")
        st.markdown("""
        - Mobile cold rooms: ₦500,000 - ₦2,000,000
        - Solar-powered cold storage: ₦1,500,000 - ₦5,000,000
        - Evaporative cooling: ₦50,000 - ₦200,000
        """)
        st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", width=300)
    
    with col2:
        st.subheader("Traditional Improved Storage")
        st.markdown("""
        - Hermetic bags: ₦1,500 - ₦3,000 per bag
        - Metal silos: ₦50,000 - ₦200,000
        - Improved cribs: ₦20,000 - ₦100,000
        """)
        st.image("https://images.unsplash.com/photo-1586773860418-d37222d8fce3", width=300)

with tab2:
    st.header("Transportation Solutions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Cold Chain Logistics")
        st.markdown("""
        - Refrigerated trucks: ₦5,000 - ₦15,000 per trip
        - Cooling vans: ₦3,000 - ₦10,000 per trip
        - Insulated containers: ₦500 - ₦2,000 per use
        """)
    
    with col2:
        st.subheader("Logistics Partners")
        st.markdown("""
        - ColdHubs Logistics: 0803-XXX-XXXX
        - FarmConnect: 0805-XXX-XXXX
        - AgroMovers: 0807-XXX-XXXX
        """)
        st.button("Request Transportation")

with tab3:
    st.header("Processing Solutions")
    
    st.subheader("Small-Scale Processing Equipment")
    st.markdown("""
    | Equipment | Price Range | Capacity |
    |-----------|------------|----------|
    | Solar dryer | ₦150,000 - ₦500,000 | 50-200kg/day |
    | Milling machine | ₦200,000 - ₦1,000,000 | 100-500kg/hr |
    | Juice extractor | ₦300,000 - ₦1,200,000 | 200-1000kg/day |
    """)
    
    st.subheader("Processing Service Providers")
    st.markdown("""
    - AgroProcess Nigeria: 0802-XXX-XXXX
    - FarmPro Services: 0804-XXX-XXXX
    - NaijaProcess: 0806-XXX-XXXX
    """)

with tab4:
    st.header("Market Linkage Solutions")
    
    st.subheader("Digital Marketplaces")
    st.markdown("""
    - Farmcrowdy: www.farmcrowdy.com
    - ThriveAgric: www.thriveagric.com
    - AgroMall: www.agromall.com
    """)
    
    st.subheader("Direct Buyer Connections")
    st.text_input("Enter your crop and quantity to find buyers")
    st.button("Search Buyers")
