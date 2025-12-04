import streamlit as st
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import pickle
import os

# Load dataset
@st.cache_data
def load_data():
    file_path = "Cleaned_World_Development_Measurements.xlsx"
    df = pd.read_excel(file_path)
    return df

data = load_data()

st.title("Hierarchical Clustering on Global Development Data")

# Show dataset preview
if st.checkbox("Show raw data"):
    st.write(data.head())

# Select features for clustering
selected_features = st.multiselect(
    "Select features for clustering",
    data.columns,
    default=list(data.columns[:5])
)

if selected_features:

    # Create /data folder if missing
    os.makedirs("data", exist_ok=True)

    # Data preprocessing
    X = data[selected_features].dropna()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Show dendrogram
    st.subheader("Dendrogram")
    fig, ax = plt.subplots(figsize=(10, 5))
    sch.dendrogram(sch.linkage(X_scaled, method='ward'), ax=ax)
    st.pyplot(fig)

    # Perform clustering
    num_clusters = st.slider("Select number of clusters", 2, 10, 3)

    # FIXED: Removed deprecated 'affinity' argument
    model = AgglomerativeClustering(
        n_clusters=num_clusters,
        linkage="ward",  # metric is automatically 'euclidean'
    )

    clusters = model.fit_predict(X_scaled)

    # Assign clusters to data
    data['Cluster'] = clusters
    st.subheader("Clustered Data")
    st.write(data.head())

    # Save model
    model_path = "data/hierarchical_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    st.success("Model saved successfully!")
