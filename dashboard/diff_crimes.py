import pandas as pd


def number_of_crimes():
    df = pd.read_csv('crimedata.csv')
    states = df['state'].unique()
    lst = ['murders',
           'rapes',
            'robberies',
            'assaults',
            'burglaries',
            'larcenies', 'autoTheft', 'arsons']
    dct = dict()
    i = 0
    while i < 8:
        key = lst[i]
        result = df.loc[df['PctUnemployed'] > 10, key].sum()
        dct[key] = int(result)
        i += 1

    d = {'crimes': lst, 'number' : dct.values()}
    df_crimes_states = pd.DataFrame(data=d)

    return df_crimes_states


