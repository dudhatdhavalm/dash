import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="number-in", value=1, style={"fontSize": 24}),
    html.Button(id="btn", type="submit", n_clicks=0, children="Submit"),
    html.H1(id="number-out")
])


@app.callback(Output("number-out", "children"), [Input("btn", "n_clicks")],
              [State("number-in", "value")])
def callback(n_clicks, number):
    print(n_clicks)
    return number


if __name__ == "__main__":
    app.run_server(debug=True)
