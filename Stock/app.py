import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output, State
from datetime import datetime
import pandas_datareader.data as web
import os

os.environ["IEX_API_KEY"] = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

app = dash.Dash()

app.layout = html.Div([
    html.H1("Stock Data"),
    html.H3("Enter a stock symbol"),
    dcc.Input(id="stock_picker", value="TSLA"),
    dcc.DatePickerRange(id="date-range"),
    html.Button(id="submit", n_clicks=0, children="Submit"),
    dcc.Graph(id="graph",
              figure={
                  "data": [{
                      "x": [1, 2],
                      "y": [3, 1]
                  }],
                  "layout": go.Layout(title="Stock Data")
              })
])


@app.callback(Output("graph", "figure"), [Input("submit", "n_clicks")], [
    State("stock_picker", "value"),
    State("date-range", "start_date"),
    State("date-range", "end_date")
])
def callback_stock(n_clicks, stock_value, start_date, end_date):
    start_date = datetime(2019, 1, 1)
    end_date = datetime(2019, 12, 31)
    df = web.DataReader(stock_value, "iex", start_date, end_date)
    fig = {
        "data": [{
            "x": df.index,
            "y": df["close"]
        }],
        "layout": go.Layout(title="Stock Data" + stock_value)
    }
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
