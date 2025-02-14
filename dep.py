import streamlit as st
import pandas as pd
import pickle
import numpy as np
from scipy.spatial.distance import cdist
import os

# Function to load the model
def load_model(pkl_path):
    if os.path.exists(pkl_path):
        with open(pkl_path, "rb") as file:
            return pickle.load(file)
    else:
        st.error(f"Error: {pkl_path} not found!")
        return None

# Load models
model = load_model("hierarchical_model.pkl")
pca = load_model("pca_model.pkl")

# Streamlit UI
st.title("🌍 World Development Clustering")

# Sidebar inputs
st.sidebar.header("Feature Inputs")
st.sidebar.write("Enter values for each feature below:")

# Feature inputs
features = {
    "Birth Rate": (0.005, 0.15, 0.025),
    "Business Tax Rate": (1.0, 1500.0, 50.0),
    "CO2 Emissions": (1.0, 30000000.0, 5000.0),
    "Days to Start Business": (1.0, 2000.0, 30.0),
    "Energy Usage": (5.0, 20000000.0, 10000.0),
    "GDP": (50000.0, 100000000000000.0, 1e9),
    "Health Exp % GDP": (0.005, 0.60, 0.05),
    "Health Exp/Capita": (1.0, 100000.0, 500.0),
    "Hours to do Tax": (10.0, 15000.0, 200.0),
    "Infant Mortality Rate": (0.001, 0.60, 0.05),
    "Internet Usage": (0.0, 200.0, 50.0),
    "Life Expectancy Female": (35.0, 130.0, 75.0),
    "Life Expectancy Male": (35.0, 130.0, 70.0),
    "Mobile Phone Usage": (0.0, 15.0, 1.5),
    "Population 0-14": (0.1, 1.0, 0.3),
    "Population 15-64": (0.4, 1.2, 0.6),
    "Population 65+": (0.002, 0.6, 0.1),
    "Population Total": (10000.0, 10000000000.0, 1e7),
    "Population Urban": (0.08, 3.0, 0.5),
    "Tourism Inbound": (500000.0, 2000000000000.0, 1e6),
    "Tourism Outbound": (100000.0, 1000000000000.0, 1e6)
}

user_input = np.array([
    st.sidebar.number_input(name, min_value=min_v, max_value=max_v, value=default_v)
    for name, (min_v, max_v, default_v) in features.items()
]).reshape(1, -1)

# Predict cluster
if st.sidebar.button("Predict Cluster"):
    if model and pca:
        transformed_input = pca.transform(user_input)
        cluster = model.fit_predict(transformed_input)
        st.success(f"The data belongs to Cluster {cluster[0]}")

        # Cluster descriptions
        cluster_descriptions = {
            0: "Developed nations with strong economies and infrastructure.",
            1: "Emerging markets with growing industrialization.",
            2: "Developing countries with high dependency on agriculture.",
            3: "Underdeveloped regions facing economic and health challenges."
        }
        st.write(f"📝 **Cluster Description:** {cluster_descriptions.get(cluster[0], 'Unknown Cluster')}")
    else:
        st.error("Model or PCA transformation is missing!")

# Footer
st.markdown("---")
st.markdown(
    """
    <h3>📌 Model Overview</h3>
    <p style='font-size:18px; text-align:justify;'>
        This model applies hierarchical clustering to analyze a diverse set of world development indicators, 
        including economic, health, and infrastructure metrics. By identifying underlying patterns, it classifies 
        countries into distinct development clusters, offering valuable insights into global trends, disparities, and 
        policy implications.
    </p>
    <p style='font-size:18px; text-align:justify;'>
        Policymakers, researchers, and analysts can leverage these clusters to compare economic growth, 
        healthcare accessibility, energy usage, and urbanization trends across nations. This enables better 
        decision-making, resource allocation, and strategic planning to drive sustainable development worldwide. 🌍📊
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("👨‍💻 Deployed by Nagaraju Gorantla with ❤️ Using Streamlit Cloud Community ☁")
