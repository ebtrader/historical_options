import pandas as pd

# https://towardsdatascience.com/finding-and-removing-duplicate-rows-in-pandas-dataframe-c6117668631f#:~:text=We%20can%20use%20Pandas%20built,()%20to%20drop%20duplicate%20rows.

df = pd.read_csv('train.csv')
# print(df)

# dupes = df.loc[df.duplicated(), :]
# print(dupes)

# dupe_cabin = df.Sex.duplicated().sum()
#
# print(dupe_cabin)

# dupe = df.Cabin.duplicated()
# print(dupe)

# multi = df.duplicated(subset=['Survived', 'Pclass', 'Sex'])
# multi.to_csv('multi.csv')

extract = df.loc[df.duplicated(subset=['Survived', 'Pclass', 'Sex', 'Name']), :]
extract.to_csv('extract.csv')

drop_dupes = df.drop_duplicates(subset=['Survived', 'Pclass', 'Sex', 'Name'])
drop_dupes.to_csv('dropped.csv')
