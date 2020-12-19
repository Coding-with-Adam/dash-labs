import dash
import dash_express as dx
import plotly.express as px
tips = px.data.tips()
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)
# template = dx.templates.DbcSidebar(title="Dash Express App")
template = dx.templates.DdkSidebar(title="Dash Express App", sidebar_width="400px", show_editor=True)
# template = dx.templates.DccCard(title="Dash Express App")


def filter(max_total_bill, tip_range, sex):
    # Let parameterize infer output component
    filtered = tips

    if max_total_bill is not None:
        filtered = filtered.query(f"total_bill < {max_total_bill}")

    if tip_range is not None:
        filtered = filtered.query(f"tip >= {tip_range[0]} & tip <= {tip_range[1]}")

    if sex is not None:
        filtered = filtered.query(f"sex == '{sex}'")

    return [
        "### Filtered tips plot",
        px.scatter(filtered, x="total_bill", y="tip"),
        html.Hr(),
        "### Filtered tips table",
        filtered,
    ]


layout = dx.parameterize(
    app,
    filter,
    params=dict(
        max_total_bill=(0, 50.0, 0.25),
        tip_range=dcc.RangeSlider(min=0, max=20, value=(5, 10)),
        sex=["Male", "Female"],
    ),
    template=template,
    labels={
        "max_total_bill": "Max total bill ($): {value:.2f}",
        "tip_range": lambda v: "Tip range ($): " + (f"{v[0]:.2f} - {v[1]:.2f}" if v else "None"),
        "sex": "Patron Gender",
    },
    optional=["max_total_bill", "max_tip", "sex", "tip_range"]
)

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True, port=9037)
