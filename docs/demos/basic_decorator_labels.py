import dash
import dash_express as dx
import numpy as np
import dash_core_components as dcc
import plotly.express as px

app = dash.Dash(__name__, plugins=[dx.Plugin()])

@app.callback(
    args=dict(
        fun=dx.Input(["sin", "cos", "exp"], label="Function"),
        figure_title=dx.Input(dcc.Input(value="Initial Title"), label="Figure Title"),
        phase=dx.Input((1, 10), label="Phase"),
        amplitude=dx.Input((1, 10), label="Amplitude"),
    ),
)
def greet(fun, figure_title, phase, amplitude):
    xs = np.linspace(-10, 10, 100)
    return dcc.Graph(figure=px.line(
        x=xs, y=getattr(np, fun)(xs + phase) * amplitude
    ).update_layout(title_text=figure_title))

app.layout = greet.layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)
