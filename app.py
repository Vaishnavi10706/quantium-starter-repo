import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

def create_chart(selected_region):
    filtered_df = df
    if selected_region != "all":
        filtered_df = df[df["Region"] == selected_region]
    sales_data = (
        filtered_df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )
    fig = px.line(
        sales_data,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time"
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )
    return fig

app.layout = html.Div(
    className="container",
    children=[
        html.H1(
            "Pink Morsel Sales Visualizer",
            className="title"
        ),
        html.Div(
            [
                html.Label(
                    "Select Region:",
                    className="label"
                ),
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"}
                    ],
                    value="all",
                    inline=True
                )
            ],
            className="controls"
        ),
        dcc.Graph(
            id="sales-chart",
            figure=create_chart("all")
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(region):
    return create_chart(region)

if __name__ == "__main__":
    app.run(debug=True)