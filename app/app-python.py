#Librairies importation
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc

#Dataset importation 1

#Dataset importation 2

#Dataset importation 3
df=pd.read_csv("OneColumnTempChange.csv")
#Figure1

#figure 2

#figure 3


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div([
        html.H1("Figure 1"),
        dcc.Graph()
        ]),
    html.Div([
        
        html.H1('Temperature Changes Over Time'),
        dcc.Graph(id="graph"),
        dcc.Checklist(
            id="checklist",
            options=["Asia", "Europe", "Africa","Americas","Oceania",'Global Avg'],
            value=[ "Global Avg"],
            inline=True
        ),
    
])

@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"))
    
def update_line_chart(continents):

    mask = df.Continent.isin(continents)
    fig = px.line(df[mask], x=df[mask]['Year'], y=df[mask]['Temp Change'], color=df[mask]['Continent'])


    fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Temperature Change",
    legend_title="",
   )

    return fig

        
        ]),
     html.Div([
        html.H1("Figure 4"),
        dcc.Graph()
        ]),
     html.Div([
        html.H1("Figure 5"),
        dcc.Graph()
        ])
])


# Run the app
if __name__ == '__main__':
    app.run(port= 8000, debug=True)
