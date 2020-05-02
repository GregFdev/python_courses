import csv


file_name = "columns_display_english.csv"
list_titles = []

with open(file_name, "r") as display_file:
    csv_file = csv.reader(display_file, delimiter=',')
    for row in csv_file:
        # print(row[1].title())
        list_titles.append(row[1].title())
# joined = " ".join(list_titles)

print(list_titles)

result_file = open("output_titles.csv", "w")
wr = csv.writer(result_file, dialect='excel')
    # print('item is {}'.format(item))
wr.writerow(list_titles)