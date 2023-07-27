#Librairies importation
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc

#Dataset importation 1

#Dataset importation 2

#Dataset importation 3

#Figure1

#figure 2

#figure 3


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Dashboard title", className="Dasboard-title"),
    html.Div([
        html.H1("Figure 1"),
        dcc.Graph()
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
