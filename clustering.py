import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load Excel dataset
df = pd.read_excel("data/Mall_Customers.xlsx")

# Remove rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Create TotalAmount column
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Group data by customer
customer_data = df.groupby('CustomerID').agg({
    'Quantity': 'sum',
    'TotalAmount': 'sum'
}).reset_index()

# Features for clustering
X = customer_data[['Quantity', 'TotalAmount']]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans
kmeans = KMeans(n_clusters=5, random_state=42)

# Create clusters
customer_data['Cluster'] = kmeans.fit_predict(X_scaled)

# Recommendation function
def recommendation(cluster):

    strategies = {
        0: "Premium customer - Offer luxury products",
        1: "Discount customer - Give coupons",
        2: "Frequent buyer - Reward loyalty points",
        3: "Low activity customer - Send re-engagement emails",
        4: "High spender - Target with exclusive offers"
    }

    return strategies.get(cluster)

# Add recommendations
customer_data['Recommendation'] = customer_data['Cluster'].apply(recommendation)

# Save clustered data
customer_data.to_csv("data/clustered_customers.csv", index=False)

print("Clustering Completed Successfully!")
print(customer_data.head())