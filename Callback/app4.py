import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(id="range",
                    min=-5,
                    max=5,
                    step=1,
                    value=[-2, 2],
                    marks={i: str(i)
                           for i in range(-5, 6)}),
    html.Div(id="ans")
])


@app.callback(Output("ans", "children"), [Input("range", "value")])
def callback_range_slider(value):
    ans = value[0] * value[1]
    return "Multiplication is {}".format(ans)


if __name__ == "__main__":
    app.run_server(debug=True)
