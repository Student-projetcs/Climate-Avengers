#Librairies importation
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FixedLocator, FixedFormatter
import plotly.graph_objects as go
from dash.dependencies import Input, Output

#Dataset importation 1
url1="https://raw.githubusercontent.com/Student-projetcs/Climate-Avengers/main/datasets/Methane_emissions_cleaned.csv"
df= pd.read_csv(url1)

#Dataset importation 2
SMALL_SIZE = 14
MEDIUM_SIZE = 16
BIGGER_SIZE = 18
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.style.use('fast')

url2="https://raw.githubusercontent.com/Student-projetcs/Climate-Avengers/main/datasets/Global%20Mean%20Sea%20Level%20Data%201993-2023%20Cleaned%20and%20simplifyed.csv"
df2 = pd.read_csv(url2)

#Dataset importation 3

#Figure1

country_names = df["country"]
values = df["emissions"]
segments=df['segment']

data = {
    "Country": country_names,
    "Emissions": values,
    "Segment":segments
}

custom_color_scale = [
    (0.0, 'green'),   # For the minimum value (0.0), use green color
    (0.2, 'yellow'),   # For the minimum value (0.2), use yellow color
    (0.5, 'orange'),  # For the middle value (0.5), use orange color
    (1.0, 'red')     # For the maximum value (1.0), use red color
]

# Create the choropleth map using Plotly Express

fig1 = px.choropleth(data_frame=data,
                    locations="Country",
                    locationmode="country names",
                    color="Emissions",
                    color_continuous_scale=custom_color_scale,
                    projection="natural earth")


#figure 2

"""A function to convert the fractional years to timestamps:"""

def _frac_year_to_dt(x):
    year = int(x)
    base = datetime(year, 1, 1)
    remainder = x - year
    result = base + timedelta(seconds=(base.replace(year=base.year + 1) - base).total_seconds() * remainder)
    return result

(
    _frac_year_to_dt(df2.year.min()).strftime("%Y-%m-%d %H:%M:%S"),
    _frac_year_to_dt(df2.year.max()).strftime("%Y-%m-%d %H:%M:%S")
)

"""Apply the new function _frac_year_to_dt to the year column of the data frame, which should return realistic dates (between 1993 and 2023)."""

dates = df2['year'].apply(_frac_year_to_dt)

"""Rename the series to time so it doesn't conflict with the existing year column:"""

dates.name = "time"

"""This next step is key for convenient data transformations and plotting.

Now set the datetimes as the new index for the data frame using the pandas.DataFrame.set_index method, which replaces the existing integer indices:
"""

df2 = df2.set_index(dates)

# Get the upper and lower bounds of the error region
error_upper = df2.gmsl_variation_with_gia + df2.gmsl_variation_with_gia_std
error_lower = df2.gmsl_variation_with_gia - df2.gmsl_variation_with_gia_std

# Create the line plot for GMSL variation with GIA
fig = go.Figure()
fig.add_trace(go.Scatter(x=df2.index, y=df2.gmsl_variation_with_gia, name="GMSL Variation with GIA", mode="lines"))

# Customize the layout
fig.update_layout(
    title=dict(
        text="",
        x=0.5,  # Center the title horizontally
        y=0.95,  # Set the y-coordinate to adjust the title vertical position
        xanchor='center',  # Anchor point for the x-coordinate (center)
        yanchor='top',  # Anchor point for the y-coordinate (top)
        font=dict(size=24)  # Set the font size of the title
    ),
    xaxis_title="Year",
    yaxis_title="Sea Height Variation (mm)",
    xaxis=dict(range=[df2.index[0], df2.index[-1]]),
    yaxis=dict(range=[-60, 75]),
    legend=dict(x=1, y=0.1),
    margin=dict(l=100, r=100, t=100, b=100),
    hovermode='x'
)


#figure 3




#Figure 4

meta_tags=[
    {"name": "Climate change dashboard"},
    {"name":"viewport", "content":"width=device-width, initial-scale=1.0"}
]

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div([
    #section1
        html.H1("CLIMATE CHANGE ANALYTICS", className="Dasboard-title"),
        html.Div([
            html.H1("IEA estimates for methane emissions (kilotonnes) by country in 2022", className="title"),
            dcc.Graph(figure=fig1)
            ],className="section2"),
        #section2
        html.Div([
                html.H1("Global Sea Level variations 1993-2023 in three decades",className="title"),
                dcc.Graph(id='sea-level-variation', figure=fig),
                dcc.Dropdown(
                id='decade-dropdown',
                options=[
                    {'label': '1993-2003', 'value': '1993-2003'},
                    {'label': '2003-2013', 'value': '2003-2013'},
                    {'label': '2013-2023', 'value': '2013-2023'}
                        ],
                value='1993-2003',
                ),
            ], className="section1"),
        #section3
        html.Div([
            html.H1("Figure 3"),
            dcc.Graph()
            ], className="section4"),
        #section4
        html.Div([
            html.H1("Figure 5"),
            dcc.Graph()
            ], className="section5"),
    ], className="inner-div"),
 ], className="mainSection")


# Define the callback function
@app.callback(
    Output('sea-level-variation', 'figure'),
    [Input('decade-dropdown', 'value')]
)
def update_sea_level_figure(selected_decade):
    # Extract the data for the selected decade from the DataFrame
    selected_data = df2[(df2['year'] >= int(selected_decade[:4])) & (df2['year'] <= int(selected_decade[-4:]))]

    # Update the x and y data of the figure
    fig.update_traces(x=selected_data.index, y=selected_data['gmsl_variation_with_gia'])

    # Update the x-axis range
    fig.update_xaxes(range=[selected_data.index.min(), selected_data.index.max()])

    return fig

# Run the app
if __name__ == '__main__':
    app.run(port= 8000, debug=True)
