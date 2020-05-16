import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Hello Dash"),
    html.Div("Dash: Dashboard with Python"),
    dcc.Graph(id="example",
              figure={
                  "data": [{
                      "x": [1, 2, 3],
                      "y": [4, 1, 3],
                      "type": "bar",
                      "name": "SF"
                  }, {
                      "x": [1, 2, 3],
                      "y": [2, 5, 1],
                      "type": "bar",
                      "name": "SF"
                  }],
                  "layout": {
                      "title": "Bar Plot"
                  }
              })
])

if __name__ == "__main__":
    app.run_server(debug=True)