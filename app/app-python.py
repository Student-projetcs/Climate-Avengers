#Librairies importation
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc

#Dataset importation 1
url1="https://raw.githubusercontent.com/Student-projetcs/Climate-Avengers/main/datasets/Methane_emissions_cleaned.csv"
df= pd.read_csv(url1)
#Dataset importation 2

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

#figure 3


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("CLIMATE CHANGE ANALYTICS", className="Dasboard-title"),
    html.Div([
        html.H1("IEA estimates for methane emissions (kilotonnes) by country in 2022"),
        dcc.Graph(figure=fig1)
        ],className="section1"),
    html.Div([
        html.H1("Figure 3"),
        dcc.Graph(),
        ], className="section2"),
     html.Div([
        html.H1("Figure 4"),
        dcc.Graph()
        ], className="section4"),
     html.Div([
        html.H1("Figure 5"),
        dcc.Graph()
        ], className="section5"),
    ], className="mainSection")


# Run the app
if __name__ == '__main__':
    app.run(port= 8000, debug=True)
