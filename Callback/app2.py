import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df = pd.read_csv("data/mpg.csv")

app = dash.Dash()

features = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id="xaxis",
                     options=[{
                         "label": i,
                         "value": i
                     } for i in features],
                     value="displacement")
    ],
             style={
                 "width": "48%",
                 "display": "inline-block"
             }),
    html.Div([
        dcc.Dropdown(id="yaxis",
                     options=[{
                         "label": i,
                         "value": i
                     } for i in features],
                     value="mpg")
    ],
             style={
                 "width": "48%",
                 "display": "inline-block"
             }),
    dcc.Graph(id="graph")
],
                      style={"padding": 10})


@app.callback(
    Output("graph", "figure"),
    [Input("xaxis", "value"), Input("yaxis", "value")])
def update_graph(xaxis, yaxis):
    trace = go.Scatter(x=df[xaxis],
                       y=df[yaxis],
                       text=df["name"],
                       mode="markers",
                       marker={
                           "size": 15,
                           "opacity": 0.5,
                           "line": {
                               "width": 0.5,
                               "color": "white"
                           }
                       })

    return {
        "data": [trace],
        "layout":
        go.Layout(title="My Dashboard For MPG",
                  xaxis={"title": xaxis},
                  yaxis={"title": yaxis},
                  hovermode="closest")
    }


if __name__ == "__main__":
    app.run_server(debug=True)