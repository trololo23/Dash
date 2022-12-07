import pandas as pd
import plotly.graph_objects as go

sliders = [
{'steps':[
{'method': 'update'
,
'label': 'assaults'
,
'args': [{'visible': [True, False, False]}]},
{'method': 'update'
,
'label': 'robberies'
,
'args': [{'visible': [False, True, False]}]},
{'method': 'update'
,
'label': 'murders'
,
'args': [{'visible': [False, False, True]}]}
]}
]

def fig2():

    df = pd.read_csv('crimedata.csv')
    lst = ["assaults", "robberies", "murders"]
    fig = go.Figure()

    for column in lst:
        fig.add_trace(
            go.Scatter(
                x=df['PctLess9thGrade'],
                y=df[column],
                name=column
            )
        )

    fig.update_layout(
        {'sliders': sliders}, title='X-axis - the percentage of people'
                                    'who graduated from less than 9 classes,'
                                    )
    fig.update_layout(
        title='X-axis -- the percentage of people who graduated from less than 9 classes',
        updatemenus=[go.layout.Updatemenu(
            active=0,

            buttons=list(
                [dict(label='All',
                      method='update',
                      args=[{'visible': [True, True, True]},
                            {'title': 'All',
                             'showlegend': True}]),

                 ])
        )
        ])
    return fig
