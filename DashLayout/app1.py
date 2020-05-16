import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {"background": "#111111", "text": "#7FDBFF"}

app.layout = html.Div(children=[
    html.H1("Hello Dash",
            style={
                "textAlign": "center",
                "color": colors["text"]
            }),
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
                      "title": "Bar Plot",
                      "plot_bgcolor": colors["background"],
                      "paper_bgcolor": colors["background"],
                      "font": {
                          "color": colors["text"],
                      },
                  }
              },
              style={"backgroundColor": colors["background"]})
])

if __name__ == "__main__":
    app.run_server(debug=True)