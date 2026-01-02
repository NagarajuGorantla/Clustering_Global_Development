import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="🌍 Global Development Clustering",
    layout="wide"
)

st.title("🌍 Global Development Clustering Explorer")
st.caption("Interactive ML dashboard for clustering countries based on development indicators")

# ---------------- PATHS ----------------
DATA_PATH = os.path.join("data", "Cleaned_World_Development_Measurements.xlsx")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_excel(DATA_PATH)

df = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔧 Clustering Controls")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

selected_features = st.sidebar.multiselect(
    "Select features for clustering",
    numeric_cols,
    default=numeric_cols[:3]
)

n_clusters = st.sidebar.slider(
    "Number of clusters",
    min_value=2,
    max_value=6,
    value=3
)

country_filter = st.sidebar.multiselect(
    "Filter countries (optional)",
    df["Country"].unique()
)

# ---------------- DATA FILTER ----------------
filtered_df = df.copy()
if country_filter:
    filtered_df = filtered_df[filtered_df["Country"].isin(country_filter)]

# ---------------- CLUSTERING ----------------
if len(selected_features) >= 2:
    X = filtered_df[selected_features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = AgglomerativeClustering(n_clusters=n_clusters)
    filtered_df["Cluster"] = model.fit_predict(X_scaled)

    # ---------------- VISUALIZATION ----------------
    st.subheader("📊 Cluster Visualization")

    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox("X-axis", selected_features, index=0)
    with col2:
        y_axis = st.selectbox("Y-axis", selected_features, index=1)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=filtered_df,
        x=x_axis,
        y=y_axis,
        hue="Cluster",
        palette="tab10",
        s=80,
        ax=ax
    )
    ax.set_title("Country Clusters")
    st.pyplot(fig)

    # ---------------- CLUSTER SUMMARY ----------------
    st.subheader("📈 Cluster Summary")

    summary = (
        filtered_df
        .groupby("Cluster")[selected_features]
        .mean()
        .round(2)
    )

    st.dataframe(summary, use_container_width=True)

    # ---------------- COUNTRY VIEW ----------------
    st.subheader("🌐 Country-Level View")

    selected_country = st.selectbox(
        "Select a country",
        filtered_df["Country"].unique()
    )

    country_row = filtered_df[filtered_df["Country"] == selected_country]
    st.dataframe(country_row, use_container_width=True)

else:
    st.warning("⚠️ Please select at least two features for clustering.")
