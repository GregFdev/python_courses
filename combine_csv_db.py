# script to combine csv's in a directory in a format for importing to database.
# also parses current complexity column into where_count and group_count


import os
import glob
import pandas as pd
import re

os.chdir("./csv_files")
all_filenames = glob.glob('*.csv')
file_array = []
mult_name = re.compile(r'\w+')

# loop through files to get names array
for filename in all_filenames:
    mult_group = mult_name.search(filename)

    file_df = pd.read_csv(filename)

     # add multiplier group column
    file_df["multiplier_group"] = mult_group.group(0)
    print('file_df is ',file_df)

    #append current DF to list
    file_array.append(file_df)

# combine all files in the list
combined2_csv = pd.concat(file_array)


# print("final file is : ", combined2_csv)

# export to csv
combined2_csv.to_csv( "combined2_csv.csv", index=False, encoding='utf-8-sig')