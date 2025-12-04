🌍 Global Development Clustering — Interactive Streamlit App




An interactive Hierarchical Clustering web app built on Streamlit, designed to explore global development indicators across countries.
Users can visualize dendrograms, select features, adjust cluster count, and view clustered outputs in real time.

🚀 Live Demo
👉 Launch Streamlit App

➡️ https://your-streamlit-app-url

(Replace with your real deployed link when ready.)

📌 About the Project

This project analyzes key global socio-economic indicators and groups countries into meaningful clusters using Agglomerative Clustering (Ward Method).
The goal is to uncover patterns in global development and offer an intuitive, interactive dashboard for exploration.

The app includes:

Real-time clustering visualization

Dynamic dendrogram generation

Interactive feature selection

Auto-scaling & preprocessing

Model saving for reuse

Built with clarity, modularity, and real-world ML workflows in mind.

🖼️ Screenshots

(Add your own screenshots later — these are placeholders.)

📊 Dendrogram Visualization
[ Insert image here ]

🌍 Interactive Clustering Output
[ Insert image here ]

🧠 Key Features
🔹 1. Interactive Feature Selection

Pick any combination of development metrics for clustering.

🔹 2. Auto-Scaling with StandardScaler

Ensures consistent distance metrics across variables.

🔹 3. Hierarchical Dendrogram

Powered by SciPy’s linkage and plotted using Matplotlib.

🔹 4. Agglomerative Clustering

Modern sklearn implementation:

AgglomerativeClustering(n_clusters, linkage="ward")

🔹 5. Model Persistence

Model is saved automatically to:

data/hierarchical_model.pkl

🔹 6. Streamlit UI

Fast, clean, minimal, and interactive.

📂 Project Structure
Clustering_Global_Development/
│── deployment.py
│── Clustering_Global_Development.ipynb
│── Cleaned_World_Development_Measurements.xlsx
│── Project_clustering.docx
│── data/
│     └── hierarchical_model.pkl
│── README.md
│── requirements.txt

🧪 How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/your-username/Global-Development-Clustering.git
cd Global-Development-Clustering

2️⃣ Create & Activate Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
streamlit run deployment.py

📦 Dependencies

requirements.txt:

streamlit
pandas
numpy
scikit-learn
scipy
matplotlib
openpyxl

🧭 Architecture Overview
Data Loading

Reads cleaned global development dataset

Cached with Streamlit for efficiency

Preprocessing

Drop missing values

Standardize selected features

Modeling

Hierarchical clustering using Ward linkage

Clusters assigned back to dataset

Visualization

SciPy dendrogram

Cluster labels shown in tabular form

Persistence

Model saved via pickle for reproducibility

🌟 Future Enhancements

Add K-Means and DBSCAN clustering

Integrate PCA to visualize clusters in 2D

Add silhouette score comparison

Provide CSV download of clustered results

Deploy a V2 UI with sidebar navigation

Host second version on HuggingFace Spaces

🤝 Contributing

Contributions are welcome!
Feel free to:

Open issues

Submit pull requests

Suggest features

Improve UI/UX

📬 Contact : nagarajugorantla972@gmail.com
