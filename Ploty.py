import plotly.graph_objects as go
import plotly.offline as of
import pandas as pd
import Tree
import json
from prettytable import PrettyTable
import random

random.seed(28)

'''
data = pd.read_csv('Mask.csv')
print(data.head())

# Scatter
line1 = go.Scatter(y=data['NEVER'], x=data['COUNTYFP'], name='Never Mask')
line2 = go.Scatter(y=data['ALWAYS'], x=data['COUNTYFP'], name='Always Mask')
fig = go.Figure([line1, line2])
fig.update_layout(
    title='Mask use',
    xaxis_title='County',
    yaxis_title='Mask'
)
of.plot(fig)
'''


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def state_map():
    df = pd.read_json('states_cases_now.json')
    fig_map = go.Figure(data=go.Choropleth(
        locations=df['state'],
        z=df['cases'].astype(float),
        locationmode='USA-states',
        colorscale='Reds',
        colorbar_title='cases'
    ))

    fig_map.update_layout(
        title_text='Covid cases in USA',
        geo_scope='usa'
    )
    of.plot(fig_map)


def state_cases_deaths():
    with open('states_cases_now.json') as file:
        dict_state = json.load(file)

    bar1 = go.Bar(y=dict_state['cases'], x=dict_state['state'],
                  text=dict_state['cases'], textposition='outside',
                  name='cases')
    bar2 = go.Bar(y=dict_state['deaths'], x=dict_state['state'],
                  text=dict_state['deaths'], textposition='outside',
                  name='deaths')
    fig = go.Figure([bar1, bar2])
    fig.update_layout(
        title='State_cases_deaths',
        xaxis_title='state',
        yaxis_title='data'
    )
    of.plot(fig)


def cases_and_maskuse():
    with open('Mask_use.json') as file:
        list_mask = json.load(file)
    with open('counties_cases_now.json') as file:
        list_counties = json.load(file)

    list_random = random_int_list(0, 3142, 30)
    # SOMETIMES,FREQUENTLY,ALWAYS
    dict_mask_case = {'county': [], 'cases': [], 'mask_use': []}
    for loc in list_random:
        fips = list_counties['fips'][loc]
        county = list_counties['county'][loc]
        cases = list_counties['cases'][loc]
        index = list_mask['fips'].index(fips)
        mask_use = float(list_mask['SOMETIMES'][index]) + float(list_mask['FREQUENTLY'][index]) + float(
            list_mask['ALWAYS'][index])
        dict_mask_case['county'].append(county)
        dict_mask_case['cases'].append((cases - 82) / (61066 - 82))
        dict_mask_case['mask_use'].append((mask_use - 0.53999) / (0.98 - 0.53999))

    max_cases = max(dict_mask_case['cases'])
    min_cases = min(dict_mask_case['cases'])
    max_mask = max(dict_mask_case['mask_use'])
    min_mask = min(dict_mask_case['mask_use'])

    line1 = go.Scatter(y=dict_mask_case['cases'], x=dict_mask_case['county'], name='cases')
    line2 = go.Scatter(y=dict_mask_case['mask_use'], x=dict_mask_case['county'], name='mask_use')
    fig = go.Figure([line1, line2])
    fig.update_layout(
        title='Relation between cases and mask use',
        xaxis_title='county',
        yaxis_title='data'
    )
    of.plot(fig)


def state_cases_vaccinations():
    with open('states_cases_now.json') as file:
        dict_state = json.load(file)
    line1 = go.Scatter(y=dict_state['cases'], x=dict_state['state'], name='cases')
    line2 = go.Scatter(y=dict_state['vaccinationsCompleted'], x=dict_state['state'], name='vaccinationsCompleted')
    fig = go.Figure([line1, line2])
    fig.update_layout(
        title='Relation between cases and vaccinationsCompleted',
        xaxis_title='state',
        yaxis_title='data'
    )
    of.plot(fig)


def county_case_visual():
    with open('counties_cases_his.json') as file:
        dict_county = json.load(file)
    county = input('input county name e.g.Fayette County: ')
    data = dict_county[county]
    dict_county = {'cases': [], 'newCases': [], 'date': []}
    for item in data:
        dict_county['cases'].append(item['cases'])
        dict_county['newCases'].append(item['newCases'])
        dict_county['date'].append(item['date'])
    line1 = go.Scatter(y=dict_county['cases'], x=dict_county['date'], name='cases')
    line2 = go.Scatter(y=dict_county['newCases'], x=dict_county['date'], name='newCases')
    fig = go.Figure([line1, line2])
    fig.update_layout(
        title=county + ' cases',
        xaxis_title='date',
        yaxis_title='data'
    )
    of.plot(fig)


def state_search():
    state = input('input state abbreviation e.g.MI: ')
    with open('list_states_cases_now.json') as file:
        list_states = json.load(file)
    bst = Tree.BST(list_states, 'state')
    result = bst.search(bst.root, bst.root, state, 'state')[1].data
    x = PrettyTable(
        field_names=['state', 'cases', 'deaths', 'riskLevels', 'vaccinationsCompleted', 'population'])
    x.align['state'] = 'l'
    x.add_row([result['state'], result['cases'], result['deaths'], result['riskLevels'],
               result['vaccinationsCompleted'], result['population']])
    print(x)


def county_search():
    county = input('input county name e.g.Fayette County: ')
    with open('list_counties_cases_now.json') as file:
        list_counties = json.load(file)
    bst = Tree.BST(list_counties, 'county')
    result_ = bst.search(bst.root, bst.root, county, 'county')[1].data
    x = PrettyTable(
        field_names=['county', 'state', 'cases', 'deaths', 'riskLevels', 'vaccinationsCompleted', 'population'])
    x.align['state'] = 'l'
    x.add_row([result_['county'], result_['state'], result_['cases'], result_['deaths'], result_['riskLevels'],
               result_['vaccinationsCompleted'], result_['population']])
    print(x)


if __name__ == '__main__':
    while 1:
        mode = input('What is your mode(input search or visualization): ')
        while (mode != 'search' + mode != 'visualization') == 2:
            mode = input('please input search or visualization: ')

        if mode == 'search':
            type_ = input('Search state or county?(input state or county): ')
            while (type_ != 'state' + type_ != 'county') == 2:
                type_ = input('please input state or county: ')
            if type_ == 'state':
                state_search()
            if type_ == 'county':
                county_search()
            control = input('exit or continue? e.g. input exit to exit: ')
            if control == 'exit':
                exit()
            if control == 'continue':
                continue

        if mode == 'visualization':
            type_ = input('state or countie?(input state or county): ')
            while (type_ != 'state' + type_ != 'county') == 2:
                type_ = input('please input state or county: ')
            if type_ == 'state':
                graph = input('Choose a visualization from \'covid map\' or \'bar graph\' '
                              'or \'vaccination relation graph\': ')
                if graph == 'covid map':
                    state_map()
                if graph == 'bar graph':
                    state_cases_deaths()
                if graph == 'vaccination relation graph':
                    state_cases_vaccinations()

            if type_ == 'county':
                graph = input('Choose a visualization from \'cases and mask use relation graph\''
                              ' or \'historical cases\': ')
                if graph == 'cases and mask use relation graph':
                    cases_and_maskuse()
                if graph == 'historical cases':
                    county_case_visual()

            control = input('exit or continue? e.g. input exit to exit: ')
            if control == 'exit':
                exit()
            if control == 'continue':
                continue

