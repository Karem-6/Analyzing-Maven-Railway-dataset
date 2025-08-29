import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load Data
df = pd.read_csv("train_data_clean.csv")
df.columns = df.columns.str.strip() 


# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/National_Rail_logo.png")
st.sidebar.header("Filters")

st.sidebar.header("Filters")

# Filter Route
select_all_routes = st.sidebar.checkbox("Select All Routes", value=True)

if select_all_routes:
    routes = df['Route'].unique()
else:
    routes = st.sidebar.multiselect(
        "Select Routes",
        options=df['Route'].unique(),
        default=df['Route'].unique()
    )

df = df[df['Route'].isin(routes)]


# Filter Day
days = st.sidebar.multiselect("Select Days", options=df['DayOfWeek'].unique(), default=df['DayOfWeek'].unique())
df = df[df['DayOfWeek'].isin(days)]

# KPIs Section
st.title("🚄 Railway Performance Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Journeys", df.shape[0])

with col2:
    st.metric("Delayed Journeys", df[df['Journey Status'] == "Delayed"].shape[0])

with col3:
    st.metric("Cancelled Journeys", df[df['Journey Status'] == "Cancelled"].shape[0])

with col4:
    st.metric("Avg Delay (min)", round(df['DelayMinutes'].mean(), 2))


# Popular Route
st.subheader("Top 10 Most Popular Routes")
top_routes = df['Route'].value_counts().head(10).reset_index()
top_routes.columns = ['Route', 'Journeys']
fig_routes = px.bar(top_routes, x='Journeys', y='Route', orientation='h', color='Journeys', color_continuous_scale="Blues")
st.plotly_chart(fig_routes, use_container_width=True)

# On-time vs Delayed vs Cancelled
st.subheader("On-time Performance")
status_counts = df['Journey Status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']
fig_status = px.pie(status_counts, values='Count', names='Status', hole=0.4, color='Status')
st.plotly_chart(fig_status, use_container_width=True)


# Peak Travel Times
st.subheader("Journeys by Hour and Day")
heatmap_data = df.groupby(["DayOfWeek", "HourBin"]).size().reset_index(name="Count")
fig_heatmap = px.density_heatmap(
    heatmap_data, x="HourBin", y="DayOfWeek", z="Count", color_continuous_scale="YlGnBu"
)
st.plotly_chart(fig_heatmap, use_container_width=True)


# Revenue by Ticket Type & Class
st.subheader("Revenue by Ticket Type and Class")
revenue_data = df.groupby(["Ticket Type", "Ticket Class"])['Price'].sum().reset_index()
fig_revenue = px.bar(
    revenue_data,
    x="Ticket Type", y="Price", color="Ticket Class",
    barmode="stack", text_auto=True
)
st.plotly_chart(fig_revenue, use_container_width=True)


# Reasons for Delay & Cancellation
st.subheader("Reasons for Delay vs Cancellation")
reason_data = df.groupby(["Journey Status", "Reason for Delay"]).size().reset_index(name="Count")
fig_reasons = px.bar(
    reason_data, x="Reason for Delay", y="Count", color="Journey Status",
    barmode="group"
)
st.plotly_chart(fig_reasons, use_container_width=True)


