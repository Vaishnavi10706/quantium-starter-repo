import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")

df['Date'] = pd.to_datetime(df['Date'])

daily_sales = (
  df.groupby('Date', as_index=False)['Sales']
  .sum()
  .sort_values('Date')
)

fig = px.line(
  daily_sales,
  x='Date',
  y='Sales',
  title='Pink Morsel Sales Over Time'
)
fig.update_layout(
  xaxis_title='Date',
  yaxis_title="Sales"
)
app = Dash(__name__)

app.layout = html.Div([
  html.H1("Pink Morsel Sales Visualizer"),
  dcc.Graph(
    figure=fig
  )
])

if __name__ == '__main__':
  app.run(debug=True)
