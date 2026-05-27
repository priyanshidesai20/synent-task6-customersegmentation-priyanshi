import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("AI Customer Segmentation Dashboard")

# Load clustered data
df = pd.read_csv("data/clustered_customers.csv")

# Show data
st.subheader("Customer Data")
st.dataframe(df)

# Scatter plot
fig = px.scatter(
    df,
    x='Quantity',
    y='TotalAmount',
    color='Cluster',
    hover_data=['CustomerID']
)

st.plotly_chart(fig)

# Cluster count chart
st.subheader("Cluster Distribution")

cluster_count = df['Cluster'].value_counts()

st.bar_chart(cluster_count)

# Recommendations
st.subheader("Marketing Recommendations")

cluster = st.selectbox(
    "Select Cluster",
    sorted(df['Cluster'].unique())
)

recommendation = df[df['Cluster'] == cluster]['Recommendation'].iloc[0]

st.success(recommendation)

# Download button
csv = df.to_csv(index=False)

st.download_button(
    label="Download Clustered Data",
    data=csv,
    file_name='clustered_customers.csv',
    mime='text/csv'
)