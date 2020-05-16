import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("data/OldFaithful.csv")

app = dash.Dash(__name__)

# figure = {
#     "data": [go.Scatter(x=df["X"], y=df["Y"], mode="markers")],
#     "layout": go.Layout(title="OldFaithful")
# }

app.layout = html.Div([
    dcc.Graph(
        id="graph",
        figure=go.Figure(
            data=[go.Scatter(x=df["X"], y=df["Y"], mode="markers")],
            layout=go.Layout(
                title="OldFaithful",
                xaxis={"title": "Duration of the current eruption in minutes"},
                yaxis={
                    "title": "Waiting time until the next eruption in minutes"
                }),
        ),
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
