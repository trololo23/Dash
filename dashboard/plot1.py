
import pandas as pd
import plotly.graph_objects as go


def fig1():

    df = pd.read_csv('crimedata.csv')
    lst = ["racepctblack", "racePctWhite", "racePctAsian", "racePctHisp"]
    fig = go.Figure()

    for column in lst:
        fig.add_trace(
            go.Scatter(
                x=df[column],
                y=df["ViolentCrimesPerPop"],
                mode='markers',
                name=column
            )
        )

    fig.update_layout(
        title='Connection between races and crimes',
        updatemenus=[go.layout.Updatemenu(
            active=0,

            buttons=list(
                [dict(label='All',
                      method='update',
                      args=[{'visible': [True, True, True, True]},
                            {'title': 'All',
                             'showlegend': True}]),
                 dict(label='racepctblack',
                      method='update',
                      args=[{'visible': [True, False, False, False]},
                            {'title': 'racepctblack',
                             'showlegend': True}]),
                 dict(label='racePctWhite',
                      method='update',
                      args=[{'visible': [False, True, False, False]},
                            {'title': 'racePctWhite',
                             'showlegend': True}]),
                 dict(label='racePctAsian',
                      method='update',
                      args=[{'visible': [False, False, True, False]},
                            {'title': 'racePctAsian',
                             'showlegend': True}]),
                 dict(label='racePctHisp',
                      method='update',
                      args=[{'visible': [False, False, False, True]},
                            {'title': 'racePctHisp',
                             'showlegend': True}]),
                 ])
        )
        ])
    return fig
