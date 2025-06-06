import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("📊 Marketing Campaign Dashboard")

# Load data
df = pd.read_csv("marketing_campaign.csv")
df['ctr'] = df['clicks'] / df['impressions']

# Sidebar
channel = st.sidebar.selectbox("Choose Channel", df['channel_name'].unique())

# Filtered data
filtered_df = df[df['channel_name'] == channel]

# Display basic stats
st.subheader(f"Selected Channel: {channel}")
st.metric("Avg CTR", round(filtered_df['ctr'].mean(), 4))
st.metric("Total Clicks", int(filtered_df['clicks'].sum()))
st.metric("Total Impressions", int(filtered_df['impressions'].sum()))

# CTR barplot
st.subheader("CTR by Channel")
ctr_by_channel = df.groupby('channel_name')['ctr'].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=ctr_by_channel, x='channel_name', y='ctr', palette='viridis', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
