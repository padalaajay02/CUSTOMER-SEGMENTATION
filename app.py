import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title("🧠 Customer Segmentation Dashboard")

df = pd.read_csv("segmented_customers.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

st.subheader("📌 Customer Type Distribution")
st.bar_chart(df["Customer Type"].value_counts())

st.subheader("📈 Customer Segmentation Visualization")

fig = px.scatter(
    df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    color="Customer Type",
    title="Customer Segmentation"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("💡 Business Insights")

for ctype in df["Customer Type"].unique():
    subset = df[df["Customer Type"] == ctype]
    st.write(f"### {ctype}")
    st.write(f"- Count: {len(subset)}")
    st.write(f"- Avg Income: {subset['Annual Income (k$)'].mean():.2f}")
    st.write(f"- Avg Spending: {subset['Spending Score (1-100)'].mean():.2f}")
