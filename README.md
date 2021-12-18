# SI507_Final_Project
Project code
Link to Github:
https://github.com/JuranShao/SI507_Final_Project

README:
API keys are provided in the Data_Get.py file
Users could interact with the program using command line prompts

Required Python packages
plotly.graph_objects, plotly.offline, pandas as pd, import Tree, json, prettytable, random

Data Sources
1. The historical covid data of counties
URL: 'https://api.covidactnow.org/v2/counties.timeseries.json?apiKey=0994c69ead924e1b95a6572f4920a8ca'
Format: JSON
Description: Access this by web API using API key; Caching was used. 
Summary of data: 
# Records available: 3222 counties covid-data from 2020/4 to 2021/12
# Record retrieved: all records available are obtained. But due to PC computing ability, only save latest 1 month data to local JSON file. And, only below data of attributes were saved to JSON.
Description of records: 
Attributes: fips, county name, cases, newCases, date

2. The current covid data of counties
URL:
'https://api.covidactnow.org/v2/counties.json? apiKey=0994c69ead924e1b95a6572f4920a8ca'
Format: JSON
Description: Access this by web API using API key; Caching was used. 
Summary of data: 
# Records available: current 3222 counties covid-data 
# Record retrieved: all records available are obtained. But due to PC computing ability, only data of below attributes were saved to JSON file. 
Description of records: 
Attributes: fips, state, county, cases, deaths, riskLevels, population, vaccinationsCompleted 

3. The current covid data of states
URL:
'https://api.covidactnow.org/v2/states.json?apiKey=0994c69ead924e1b95a6572f4920a8ca'
Format: JSON
Description: Access this by web API using API key; Caching was used. 
Summary of data: 
# Records available: current 53 states covid-data 
# Record retrieved: all records available are obtained. But due to PC computing ability, only data of below attributes were saved to JSON file. 
Description of records: 
Attributes: fips, state, county, cases, deaths, riskLevels, population, vaccinationsCompleted

4. The data of mask using for counties
URL:
https://github.com/nytimes/covid-19-data/tree/master/mask-use
Format: CSV
Description: download from the URL 
Summary of data: 
# Records available: current 3222 counties mask use data 
# Record retrieved: all records available are obtained. 
Description of records: 
Attributes: fips, NEVER, RARELY, SOMETIMES, FREQUENTLY, ALWAYS 

5. The data of income for counties
URL:
https://github.com/tomhbyrne/county_income_inequality/tree/master/data
Format: CSV
Description: download from the URL
Summary of data: 
# Records available: current 3222 counties gini(income) data 
# Record retrieved: all records available are obtained. 
Description of records: 
Attributes: year, fips, gini


 
Data Structure
README (Tree)
I created Binary Search Trees using the data in ascending order of counties/states name. To be specific, I stored covid data and corresponding county/state data in tree notes. By storing data in the BST, I can use BST to search and get data with a given county/state name efficiently. 

Tree.py constructs the trees

Tree_county.json and Tree_state.json stored the trees

Read_tree.py reads the json of my trees 

Screenshot: 
 

 
Interaction and Presentation Options
Description: 
First, users would be asked to choose the mode of search or visualization.

If they choose the search mode, users could search a specific state covid data or county covid data. The result would be showed in table view using prettytable module.

If they choose the visualization mode, they could choose the visualization of state or county. If they choose the state, they have three state visualization presentations to get: covid map, bar graph, vaccination relation graph. Otherwise, they have two county visualization presentations to get: cases and mask use relation graph, historical cases line chart. 

Interactive and presentation technologies used:
Plotly, prettytable, command line prompts


Instruction:
Users could use the command line prompts to interact with my program.
![image](https://user-images.githubusercontent.com/59003395/146629266-fe2d6a58-b93e-43cf-9578-b568eb32b385.png)
