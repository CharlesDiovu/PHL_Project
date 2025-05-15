st.set_page_config(layout="wide")
st.title("📊 Post-Harvest Loss Risk Dashboard")

import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("post-harvest-loss-app/data/merged_crop_climate_data.csv")

df = load_data()

# Filters
st.sidebar.header("Filters")
selected_state = st.sidebar.multiselect(
    "Select State(s)",
    options=df["State"].unique(),
    default=["Lagos", "Kano", "Rivers"]
)

selected_crop = st.sidebar.multiselect(
    "Select Crop(s)",
    options=df["Crop"].unique(),
    default=["Tomatoes", "Bananas", "Cassava, fresh"]
)

risk_level = st.sidebar.multiselect(
    "Risk Level",
    options=df["Risk Score"].unique(),
    default=["Medium", "Low"]
)

# Filter data
filtered_df = df[
    (df["State"].isin(selected_state)) &
    (df["Crop"].isin(selected_crop)) &
    (df["Risk Score"].isin(risk_level))
]

# Main content
tab1, tab2, tab3 = st.tabs(["Geographic View", "Crop Analysis", "Climate Factors"])

with tab1:
    st.header("Geographic Distribution of PHL Risks")
    
    # Create risk map
    state_risk = df.groupby("State")["AVERAGE PHL (%)"].mean().reset_index()
    
    fig = px.choropleth(
        state_risk,
        locations="State",
        locationmode="country names",
        scope="africa",
        color="AVERAGE PHL (%)",
        color_continuous_scale="RdYlGn_r",
        title="Average Post-Harvest Loss by State"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # State-specific data
    if selected_state:
        st.subheader(f"Detailed Data for {', '.join(selected_state)}")
        st.dataframe(filtered_df, use_container_width=True)

with tab2:
    st.header("Crop-Specific Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top crops by PHL
        crop_phl = df.groupby("Crop")["AVERAGE PHL (%)"].mean().nlargest(10).reset_index()
        fig = px.bar(
            crop_phl,
            x="Crop",
            y="AVERAGE PHL (%)",
            title="Top 10 Crops by Average PHL"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Risk distribution by crop
        fig = px.box(
            df,
            x="Risk Score",
            y="AVERAGE PHL (%)",
            color="Risk Score",
            title="PHL Distribution by Risk Level"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Climate Impact on PHL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # PHL vs Rainfall
        fig = px.scatter(
            df,
            x="Avg Rainfall",
            y="AVERAGE PHL (%)",
            color="Risk Score",
            trendline="lowess",
            title="PHL vs Average Rainfall"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # PHL vs Temperature
        fig = px.scatter(
            df,
            x="Avg Temp",
            y="AVERAGE PHL (%)",
            color="Risk Score",
            trendline="lowess",
            title="PHL vs Average Temperature"
        )
        st.plotly_chart(fig, use_container_width=True)
