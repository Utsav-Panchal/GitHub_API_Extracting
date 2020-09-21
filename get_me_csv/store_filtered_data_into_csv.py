from parse_github.specific_filter import ParseFilter

class CSV_FILTERED:

    def __init__(self, filtered_data):
        self.filtered_data = filtered_data

    @property
    def get_csv(self):
        file = open('test.csv', 'w')
        file.write('name; description; html_url; watchers_count; stargazers_count; forks_count \n')

        for data in self.filtered_data:
            csv_string = f"{data['name']};{data['description']};{data['html_url']};{data['stargazers_count']};{data['forks_count']};{data['watchers_count']} \n"
            file.write(csv_string)
        file.close()