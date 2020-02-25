import os
import glob
import pandas as pd
import re

os.chdir("./csv_files")
all_filenames = glob.glob('*.csv')
file_array = []
complex_name = re.compile(r'[w]\d[_][g]\d')

# loop through files
for filename in all_filenames:
    complexity = complex_name.search(filename)

    file_df = pd.read_csv(filename)
    # add column complexity
    file_df["complexity"] = complexity.group()

    #append current DF to list
    file_array.append(file_df)

# combine all files in the list
combined_csv = pd.concat(file_array)


print("final file is : ", combined_csv)

# export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')