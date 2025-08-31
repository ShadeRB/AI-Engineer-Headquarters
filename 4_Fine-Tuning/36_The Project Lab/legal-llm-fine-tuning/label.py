from label_studio_sdk import Client

ls = Client(url="http://localhost:8080", api_key="your_api_key")

project = ls.get_project(1)
project.import_tasks([{'text': 'Sample Clause for labeling.'}])