"""
Problem:
Fetch GitHub repository data using following API
https://api.github.com/search/repositories?q=is:public
● Use following filters which are defined in dictionary to fetch only limited relevant
repositories
{
"language": "Python",
"forks": ">=200"
}
● Store fetched repositories data into following columns in CSV file
name, description, html_url, watchers_count, stargazers_count, forks_count
● Store only those repositories which have more than 2000 “stargazers_count”
"""
import json
import requests

basic_url = 'https://api.github.com/search/repositories?q=is:public+language:python'

respose = requests.get(basic_url).json()["items"]
json_conv = json.dumps(respose)  #Coverting dictionary output into   json format
python_conv = json.loads(json_conv)
# print(len(python_conv))

file = open('test.csv', 'w')
file.write('name, description, html_url, watchers_count, stargazers_count, forks_count \n')
for data in python_conv:
    if data['language'] == 'Python' and data['forks'] >= 200 and data['stargazers_count'] >= 2000:
        # print('stargazers_count', data['stargazers_count'])
        # print('forks', data['forks'])
        # print('language', data['language'])
        # print(data['forks'])
        # print("Inserting data into csv file")
        # csv_string = f"{data['name']},{data['description']},{data['html_url']},{data['stargazers_count']},{data['forks_count']},{data['watchers_count']} \n"
        # file.write(csv_string)
        # print("added")
        pass
file.close()