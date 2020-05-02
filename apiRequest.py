import requests
import json
import csv

url = "http://127.0.0.1:8119/inference"
int_path = "chata-caas-npx/bluelink/1"
row = []
array = []
dict_out = {}

with open("query_file.csv", "r") as query_file:
    csv_file = csv.reader(query_file, delimiter=',')
    for row in csv_file:
        print(row[0])

        reqJson = {"q": row[0], "path": int_path}
        response = requests.post(url, json=reqJson)
        data_dict = response.json()
        query_string = [data_dict["confidence_probabilities_np"][0], str(data_dict["parsed_queries_np"][0][0])]
        # print('response code is ', response.status_code)

        dict_out['eng_query'] = row[0]
        dict_out['response'] = query_string

        array.append(dict_out)

print(array)


# print('response headers are ', response.headers)

# with open("output_sql.csv", "wb") as wr:
#     fieldnames = ['eng_query', 'response']
#     writer = csv.DictWriter(wr, fieldnames=fieldnames)
#     # writer.writeheader()
#     writer.writerow(array)

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})





