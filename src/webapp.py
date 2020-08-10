# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from flask import Flask
from dash.dependencies import Input, Output

import pandas as pd

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

markdown_text = '''
# SF City Prediction

Prediction model for dataset. Click button to run.
'''

app.layout = html.Div(children=[

    dcc.Markdown(markdown_text),

    html.Div([
        html.Button('Run Model', id='btn-run')
    ]),

    html.Div(id='container-table'),

    html.Div(id='container-graph'),

])


def gen_html_table(df):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(cell) for cell in row
            ]) for _, row in df.iterrows()
        ])
    ])


@app.callback(
    [Output('container-table', 'children'),
     Output('container-graph', 'children')],
    [Input('btn-run', 'n_clicks')])
def do_figures(n_clicks):
    if not n_clicks:
        return None, None
    df = pd.DataFrame({
        "Request ID": ["1", "2", "3", "4", "5", "6"],
        "Prediction": [5, 4, 3, 1, 4, 2],
    })
    fig = px.bar(
        df, x="Request ID", y="Prediction", barmode="group", title='EXAMPLE')
    table = [html.Strong('EXAMPLE RESULT'), gen_html_table(df)]
    return table, dcc.Graph(id='Chart', figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True)
