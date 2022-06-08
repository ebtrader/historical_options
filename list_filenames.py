# https://www.geeksforgeeks.org/python-list-files-in-a-directory/
# https://www.geeksforgeeks.org/how-to-move-all-files-from-one-directory-to-another-using-python/
# https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python

import os
import shutil

# move one file

# source_root = 'C:/Users/jsidd/PycharmProjects/historical_options'
# filename = '3320220610.csv'
# source = source_root + "/" + filename
# destination_root = 'C:/Users/jsidd/PycharmProjects/historical_options/staging_area'
# destination = destination_root + "/" + filename
#
# os.rename(source, destination)

# move all files

# source_root = 'C:/Users/jsidd/PycharmProjects/historical_options'
# filename = '3120220610.csv'
# source = source_root + "/" + filename
# # print(source)
#
# destination = 'C:/Users/jsidd/PycharmProjects/historical_options/staging_area'
#
# allfiles = os.listdir(source)
#
# for f in allfiles:
#     shutil.move(source + f, destination + f)
#
# list of all files in a directory

# Get the list of all files and directories
# path = "C://Users//Vanshi//Desktop//gfg"
path = 'C:/Users/jsidd/PycharmProjects/historical_options/staging_area'
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)
