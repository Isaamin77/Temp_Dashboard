import streamlit as st
import pandas as pd
import plotly.express as px

# loading the datasets
contribution_data = pd.read_csv('Contribution_Temp_Increase_Gas.csv')
temperature_data = pd.read_csv('Temp_Increase.csv')
population_data = pd.read_csv('world_population_data.csv')

# Giving the dashboard a title 
st.title('Temperature Change Key Insights')

# Creating the sidebar widget for selecting the region
region = st.sidebar.selectbox('Select Region:', contribution_data['Region'].unique())

# Filtering contribution data by region
subset_contribution_data = contribution_data[contribution_data['Region'] == region]

# Filtering temperature data by region
subset_temperature_data = temperature_data[temperature_data['Region'] == region]

# Filtering population data by region
subset_population_data = population_data[population_data['Region'] == region]

# Making the line plot for greenhouse gas contributions
st.subheader('Greenhouse Gas Contributions')
fig_gas = px.line(subset_contribution_data, x='Year', y=['Change caused by CO2', 'Change caused by Methane', 'Change caused by nitrous oxide'])
fig_gas.update_traces(mode='lines+markers', hoverinfo='text+name')
fig_gas.update_layout(hoverlabel=dict(bgcolor="white", font_size=12))
st.plotly_chart(fig_gas)

# Making the bar chart for temperature increase
st.subheader('Temperature Increase')
fig_temp = px.bar(subset_temperature_data, x='Year', y='Temperature Increase', labels={'Temperature Increase': 'Temperature Increase (°C)'})
fig_temp.update_layout(xaxis_title='Year', yaxis_title='Temperature Increase (°C)', title='Temperature Increase Over Time')
st.plotly_chart(fig_temp)

# reshaping population data for line graph
subset_population_data_melted = pd.melt(subset_population_data, id_vars=['Region'], var_name='Year', value_name='Population')

# Making line graph for population over time
st.subheader('Population Over Time')
fig_population_line = px.line(subset_population_data_melted, x='Year', y='Population', color='Region', labels={'Population': 'Population', 'Year': 'Year'})
fig_population_line.update_layout(xaxis_title='Year', yaxis_title='Population', title='Population Over Time')
st.plotly_chart(fig_population_line)
