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
    html.Div([
        html.H1("Figure 1")
        ])
])


# Run the app
if __name__ == '__main__':
    app.run(port= 8000, debug=True)