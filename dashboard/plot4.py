import plotly.express as px
from diff_crimes import number_of_crimes


def fig4():
    return px.pie(number_of_crimes(), values='number', names='crimes')
