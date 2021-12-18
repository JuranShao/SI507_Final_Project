import requests
import json
import pandas as pd


CACHE_FILENAME = "cache.json"


def open_cache():
    ''' opens the cache file if it exists and loads the JSON into
    a dictionary, which it then returns.
    if the cache file doesn't exist, creates a new cache dictionary
    Parameters
    ----------
    None
    Returns
    -------
    The opened cache
    '''
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict


def save_cache(cache_dict):
    ''' saves the current state of the cache to disk
    Parameters
    ----------
    cache_dict: dict
        The dictionary to save
    Returns
    -------
    None
    '''
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME, "w")
    fw.write(dumped_json_cache)
    fw.close()


def extract_url_content(url):
    dicta = requests.get(url).json()
    return dicta


def fetch_json(url):
    cache = open_cache()
    if url not in cache:
        content = extract_url_content(url)
        cache[url] = content
        save_cache(cache)
    return cache[url]




# Web API you haven’t used before that requires no authorization 3 point
url_2021_US = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us.csv'
# req = requests.get(url_2021_US)
# dict_ = req.text.split('\n')

# Multiple related CSV or JSON files with at least one file containing > 1000 records 4 point
# csv_data = pd.read_csv('county_income.csv')
# csv_data = pd.read_csv('Mask.csv')

# Web API you haven’t used before that requires API key or HTTP Basic authorization 4 point
# data definitions https://apidocs.covidactnow.org/data-definitions
url_states_historical = 'https://api.covidactnow.org/v2/states.timeseries.json?' \
             'apiKey=0994c69ead924e1b95a6572f4920a8ca'
# fetch_json(url_states)

url_counties_historical = 'https://api.covidactnow.org/v2/counties.timeseries.json?' \
               'apiKey=0994c69ead924e1b95a6572f4920a8ca'
# fetch_json(url_counties_historical)


# 2021-12-07
url_states_cur = 'https://api.covidactnow.org/v2/states.json?' \
                 'apiKey=0994c69ead924e1b95a6572f4920a8ca'
# fetch_json(url_states_cur)

url_counties_cur = 'https://api.covidactnow.org/v2/counties.json?' \
                 'apiKey=0994c69ead924e1b95a6572f4920a8ca'
# fetch_json(url_counties_cur)

url_US_cur = 'https://api.covidactnow.org/v2/country/US.json?' \
             'apiKey=0994c69ead924e1b95a6572f4920a8ca'
# fetch_json(url_US_cur)

# print(open_cache()[url_states_cur][0])
# key stored: 'fips', 'state', 'population', 'riskLevels'['overall'],
# 'actuals'['cases', 'deaths'], 'hospitalBeds'['capacity']
# 'newCases', 'vaccinationsCompleted',

# print(open_cache()[url_counties_cur][0])
# key stored: 'fips', 'state', 'county', 'population', 'riskLevels'['overall']
# 'actuals'['cases', 'deaths'], 'newCases', ', 'vaccinationsCompleted'

# print(open_cache()[url_US_cur])
# key stored: 'population', 'riskLevels'['overall']
# 'actuals'['cases', 'deaths'], 'hospitalBeds'['capacity']
# 'newCases', 'vaccinationsCompleted',


# Github Oauth token
# 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

# data clean

'''
list_counties = fetch_json(url_counties_cur)
dict_counties = {'fips': [], 'state': [], 'county': [], 'cases': [],
                 'deaths': [], 'newCases': [], 'population': [], 'riskLevels': [],
                 'vaccinationsCompleted': []}
for item in list_counties:
    dict_counties['fips'].append(item['fips'])
    dict_counties['state'].append(item['state'])
    dict_counties['county'].append(item['county'])
    dict_counties['cases'].append(item['actuals']['cases'])
    dict_counties['population'].append(item['population'])
    dict_counties['deaths'].append(item['actuals']['deaths'])
    dict_counties['newCases'].append(item['actuals']['newCases'])
    dict_counties['riskLevels'].append(item['riskLevels']['overall'])
    dict_counties['vaccinationsCompleted'].append(item['actuals']['vaccinationsCompleted'])

with open('counties_cases_now.json', 'w') as outfile:
    json.dump(dict_counties, outfile)

dict_mask = {'fips': [], 'NEVER': [], 'RARELY': [], 'SOMETIMES': [], 'FREQUENTLY': [], 'ALWAYS': []}
with open('Mask.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    for row in csv_reader:
        dict_mask['fips'].append(row[0])
        dict_mask['NEVER'].append(row[1])
        dict_mask['RARELY'].append(row[2])
        dict_mask['SOMETIMES'].append(row[3])
        dict_mask['FREQUENTLY'].append(row[4])
        dict_mask['ALWAYS'].append(row[5])

with open('Mask_use.json', 'w') as outfile:
    json.dump(dict_mask, outfile)

list_states = fetch_json(url_states_cur)
dict_states = {'fips': [], 'state': [], 'cases': [],
                 'deaths': [], 'newCases': [], 'population': [], 'riskLevels': [],
                 'vaccinationsCompleted': []}
for item in list_states:
    dict_states['fips'].append(item['fips'])
    dict_states['state'].append(item['state'])
    dict_states['cases'].append(item['actuals']['cases'])
    dict_states['deaths'].append(item['actuals']['deaths'])
    dict_states['newCases'].append(item['actuals']['newCases'])
    dict_states['population'].append(item['population'])
    dict_states['riskLevels'].append(item['riskLevels']['overall'])
    dict_states['vaccinationsCompleted'].append(item['actuals']['vaccinationsCompleted'])

with open('states_cases_now.json', 'w') as outfile:
    json.dump(dict_states, outfile)
'''

'''
list_counties_or = fetch_json(url_counties_cur)
list_counties = []
for item in list_counties_or:
    dict_counties = {}
    dict_counties['fips'] = item['fips']
    dict_counties['state'] = item['state']
    dict_counties['cases'] = item['actuals']['cases']
    dict_counties['deaths'] = item['actuals']['deaths']
    dict_counties['county'] = item['county']
    dict_counties['newCases'] = item['actuals']['newCases']
    dict_counties['population'] = item['population']
    dict_counties['riskLevels'] = item['riskLevels']['overall']
    dict_counties['vaccinationsCompleted'] = item['actuals']['vaccinationsCompleted']
    list_counties.append(dict_counties)

with open('list_counties_cases_now.json', 'w') as outfile:
    json.dump(list_counties, outfile)
'''

'''
list_states_or = fetch_json(url_states_cur)
list_states = []
for item in list_states_or:
    dict_states = {}
    dict_states['fips'] = item['fips']
    dict_states['state'] = item['state']
    dict_states['cases'] = item['actuals']['cases']
    dict_states['deaths'] = item['actuals']['deaths']
    dict_states['newCases'] = item['actuals']['newCases']
    dict_states['population'] = item['population']
    dict_states['riskLevels'] = item['riskLevels']['overall']
    dict_states['vaccinationsCompleted'] = item['actuals']['vaccinationsCompleted']
    list_states.append(dict_states)
with open('list_states_cases_now.json', 'w') as outfile:
    json.dump(list_states, outfile)
'''

list_county_his = fetch_json(url_counties_historical)
dict_counties = {}
for item in list_county_his:
    dict_counties[item['county']] = item['actualsTimeseries'][-30:]  # value is 30 dicts 'cases' and 'date' are needed
    with open('counties_cases_his.json', 'w') as outfile:
        json.dump(dict_counties, outfile)
