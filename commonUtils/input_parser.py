from pprint import pprint
import re
import json

def create_config():
     file_path='D:\\pythonProject3\\pythonProject1\\db_project\\input\\tnsnames.txt'
     f = open(file_path)
     data = f.read()
     f.close()
     records = data.split("\n\n")
     dict_db_mapper = {}
     for record in records:
          db_name = record.split("=")[0].strip()
          con_details = re.findall(r'\(\w+ = \w+\.?\w+\.?\w+\)', record)
          d = {}
          for details in con_details:
               k, v = details.split("=")
               k = k[1:]
               v = v[:-1]
               d[k] = v
          dict_db_mapper[db_name] = d
     # Creating Input JSON File
     json_data = json.dumps(dict_db_mapper, indent=4)
     with open("input_config.json", "w") as outfile:
          outfile.write(json_data)
     return dict_db_mapper

def read_config():
     file_path='D:\\pythonProject3\\pythonProject1\\db_project\\libUtlis\\input_config.json'
     f=open(file_path)
     data = json.load(f)
     return data

if __name__ == "__main__":
     pass

