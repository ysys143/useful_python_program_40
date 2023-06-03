import seaborn as sns

df = sns.load_dataset('titanic')
print(df, "\n")
print(df.info())

df1 = df.drop(['class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'], axis=1)
print(df1, "\n")
print(df1.info())

df2 = df1.dropna(subset=['age'], how='any', axis=0)
print(df2, "\n")
print(df2.info())

freq_value = df2['embarked'].value_counts(dropna=True).idxmax()
print(freq_value)

df3 = df2.copy()
df3['embarked'].fillna(freq_value, inplace=True)
print(df3, "\n")
print(df3.info())

df3.loc[df3['sex'] == 'male', 'sex'] = 1
df3.loc[df3['sex'] == 'female', 'sex'] = 0

for idx, item in enumerate(df3['embarked'].unique()):
    df3.loc[df3['embarked'] == item, 'embarked'] = idx

df3 = df3.astype({'sex':'int', 'embarked':'int'})
print(df3, "\n")
print(df3.info())