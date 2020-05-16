import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    "This is the div tag",
    html.Div(["This is a Inner div"], style={"color": "red"})
],
                      style={
                          "color": "green",
                          "border": "1px solid green",
                          "padding": "5px"
                      })

if __name__ == "__main__":
    app.run_server(debug=True)