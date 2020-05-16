import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

graph1 = dcc.Graph(
    id="scatterplot1",
    figure={
        "data": [
            go.Scatter(x=random_x,
                       y=random_y,
                       mode="markers",
                       marker={
                           "size": 18,
                           "color": "rgb(51,204,155)",
                           "symbol": "pentagon",
                           "line": {
                               "width": 2
                           }
                       }),
        ],
        "layout":
        go.Layout(title="My Scatter Plot", xaxis={"title": "Some x title"}),
    },
)

graph2 = dcc.Graph(
    id="scatterplot2",
    figure={
        "data": [
            go.Scatter(x=random_x,
                       y=random_y,
                       mode="markers",
                       marker={
                           "size": 18,
                           "color": "rgb(200,204,155)",
                           "symbol": "pentagon",
                           "line": {
                               "width": 2
                           }
                       }),
        ],
        "layout":
        go.Layout(title="My Scatter Plot", xaxis={"title": "Some x title"}),
    },
)

app.layout = html.Div([graph1, graph2])

if __name__ == "__main__":
    app.run_server(debug=True)