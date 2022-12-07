from aio import ThemeSwitchAIO
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
from crimes_by_states import crimes_states
from map import map
from plot1 import fig1
from plot2 import fig2
from plot3 import fig3
from plot4 import fig4

load_figure_template(["solar", "minty"])
df = pd.read_csv('crimedata.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
crimes = crimes_states()

graphs = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div([dcc.Markdown('''The connection between races and crimes'''),
                        dcc.Graph(figure=fig1())]), lg=6),
                dbc.Col(html.Div([dcc.Markdown('''The connection between lack of education and crime'''),
                        dcc.Graph(figure=fig2())]), lg=6),
            ],
            className="mt-4",
        ),
        dbc.Row(
            [
             html.Div([dcc.Markdown('''Number of crimes per 100000 in different states'''),map()])
            ],
            className="mt-4",
        ),

        dbc.Row(
            [
                dbc.Col(html.Div([dcc.Markdown('''The connection between divorces and crimes'''),
                        dcc.Graph(figure=fig3())]), lg=6),
                dbc.Col(html.Div([dcc.Markdown('''The frequency of crimes in regions 
                with a large percentage of unemployed people'''),
                        dcc.Graph(figure=fig4())]), lg=6),
            ],
            className="mt-4",
        ),
    ]
)
button = html.Div([
       dcc.Markdown('''
            Форма сбора жалоб и предложений
         '''),
       html.Div(dcc.Input(id='input-box', type='text')),
       html.Button('Submit', id='button-example-1'),
       html.Div(id='output-container-button',
                children='Enter a value and press submit')
])
heading = html.H1("Analysis of crimedata.csv")
app.layout = dbc.Container([ThemeSwitchAIO(aio_id="theme",
                            themes=[dbc.themes.SOLAR, dbc.themes.MINTY]),
                            heading, button, graphs],
                            fluid=True)


@app.callback(
    Output('output-container-button', 'children'),
    [Input('button-example-1', 'n_clicks')],
    [State('input-box', 'value')])
def update_output(n_clicks, value):
    return 'Спасибо за ваш отзыв: "{}", будем стараться стать лучше'.format(
        value,
        n_clicks
    )


@app.callback(
    Output("graph", "figure"),
    Input("crime", "value"))
def display_choropleth(crime):
    x = crimes[crime].max()

    fig = px.choropleth(crimes, locations='state',
                        locationmode="USA-states",
                        color=crime,
                        color_continuous_scale="Viridis",
                        range_color=(0, x),
                        scope="usa",
                        )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)  # запускаем сервер
