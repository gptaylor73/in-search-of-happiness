import streamlit as st
import pandas as pd
import plotly.express as px

# Read CSV
df = pd.read_csv('happy.csv')

# Create options for select boxes
choices = ['Happiness', 'GDP', 'Social Support', 'Life Expectancy',
           'Freedom To Make Life Choices', 'Generosity', 'Corruption']

# Add a title widget
st.title('In Search of Happiness')

# Create select box widgets and match the choice to dateframe columns to
# allow for selection in the chart
x_choice = st.selectbox("Select the X axis: ", choices)
match x_choice:
    case 'Happiness':
        x = 'happiness'
    case 'GDP':
        x = 'gdp'
    case 'Social Support':
        x = 'social_support'
    case 'Life Expectancy':
        x = 'life_expectancy'
    case 'Freedom To Make Life Choices':
        x = 'freedom_to_make_life_choices'
    case 'Generosity':
        x = 'generosity'
    case 'Corruption':
        x = 'corruption'
y_choice = st.selectbox("Select the Y axis: ", choices)
match y_choice:
    case 'Happiness':
        y = 'happiness'
    case 'GDP':
        y = 'gdp'
    case 'Social Support':
        y = 'social_support'
    case 'Life Expectancy':
        y = 'life_expectancy'
    case 'Freedom To Make Life Choices':
        y = 'freedom_to_make_life_choices'
    case 'Generosity':
        y = 'generosity'
    case 'Corruption':
        y = 'corruption'

# Subheader widget for chart
st.subheader(f"{x_choice} and {y_choice}")

# Create figure for plotly chart and add country field to the hover text
figure = px.scatter(data_frame=df, x=df[x], y=df[y],
                    labels={'x': x_choice,
                            'y': y_choice},
                    hover_data=['country'])

# Add the chart widget
st.plotly_chart(figure)

