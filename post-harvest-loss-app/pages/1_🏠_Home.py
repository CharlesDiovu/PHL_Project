import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🌾 Post-Harvest Losses in Nigeria")

col1, col2 = st.columns(2)

with col1:
    st.header("The Problem")
    st.markdown("""
    - Nigeria loses 30-50% of perishable agricultural produce annually
    - Annual economic loss: \$9 billion
    - Major causes:
        - Poor storage facilities
        - Inadequate transportation
        - Limited processing infrastructure
        - Weak market linkages
    """)
    
    st.image("https://images.unsplash.com/photo-1605000797499-95a51c5269ae", width=350)

with col2:
    st.header("Our Solution")
    st.markdown("""
    This platform provides data-driven tools to:
    - Predict post-harvest loss risks
    - Visualize high-risk areas and crops
    - Recommend appropriate interventions
    - Connect farmers with solutions providers
    
    Designed specifically to support:
    - Young agripreneurs
    - Smallholder farmers
    - Agricultural cooperatives
    """)
    
    st.image("https://images.unsplash.com/photo-1586771107445-d3ca888129ce", width=350)

st.markdown("---")
st.header("Key Statistics")
stats = pd.DataFrame({
    "Metric": ["Annual PHL Value", "Average PHL Rate", "Most Vulnerable Crops", "Highest Risk States"],
    "Value": ["\$9 billion", "30-50%", "Tomatoes, Bananas, Leafy Vegetables", "Lagos, Rivers, Kano"]
})
st.dataframe(stats, hide_index=True, use_container_width=True)
