import pandas as pd


def crimes_states():
    df = pd.read_csv('crimedata.csv')
    states = df['state'].unique()
    lst = ['murders',
    'rapes',
    'robberies',
    'assaults',
    'burglaries', 'larcenies', 'autoTheft', 'arsons']
    murders = dict()
    rapes = dict()
    robberies = dict()
    assaults = dict()
    burglaries = dict()
    larcenies = dict()
    autoTheft = dict()
    arsons = dict()

    crimes = [murders, rapes, robberies, assaults, burglaries, larcenies,
    autoTheft,
    arsons]
    i = 0
    while i < 8:
        dct = crimes[i]
        key = lst[i]
        for state in states:
            result = df.loc[df['state'] == state, key].sum()
            population = df.loc[df['state'] == state, 'population'].sum()
            dct[state] = (result/population) * 100000
        i += 1
    d = {'state': states, 'murders' : murders.values(),
         'rapes' : rapes.values(), 'robberies' : robberies.values(),
         'assaults' : assaults.values(), 'burglaries' : burglaries.values(),
         'larcenies' : larcenies.values(), 'autoTheft' : autoTheft.values(),
         'arsons' : arsons.values()}
    df_crimes_states = pd.DataFrame(data=d)

    return df_crimes_states
    //Moore

