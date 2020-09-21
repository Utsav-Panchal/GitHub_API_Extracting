from get_me_csv.store_filtered_data_into_csv import CSV_FILTERED
from github_lib.grab_github_context import AllContextData
from parse_github.specific_filter import ParseFilter


URL = 'https://api.github.com/search/repositories?q=is:public+language:python'

context = AllContextData(URL).grab_context_by_request # import req and get dict

# context in python format and return filter list data to get_me_csv
filtered_data = ParseFilter(context).filter_data

# convert into csv
csv_success = CSV_FILTERED(filtered_data).get_csv

print("Your csv file has been created. Please open csv file on semicolon seprator.")