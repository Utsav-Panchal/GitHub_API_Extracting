from github_lib.grab_github_context import AllContextData
import json
basic_url = 'https://api.github.com/search/repositories?q=is:public+language:python'
scrap = AllContextData(basic_url)

class ParseFilter:
    def __init__(self, context):
        self.context = context["items"]

    @property
    def filter_data(self):
        self.into_json = json.dumps(self.context)
        self.into_python = json.loads(self.into_json)
        return [data for data in self.into_python if data['language'] == 'Python' and data['forks'] >= 200 and data['stargazers_count'] >= 2000 and data['forks'] >= 200]
