import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/Cursos/Data analysis FCC/Cencus_project/data.csv", sep = ';')

df.head()
df.tail()
df.info()
df.describe()

df.isnull()
df.isnull().sum()


df_clean = df.drop(32561)
print(df_clean.tail())
print(df_clean.isnull().sum())
print(df_clean.value_counts())
df_clean = df

racesSerie = df_clean['race']
print(racesSerie)

countRaces = racesSerie.value_counts()

print(countRaces)

round(df_clean[['sex', 'age']].groupby('sex').mean(),0)

df_clean['education'] == ' Bachelors'

bach = df_clean[df_clean['education'] == ' Bachelors']
bach

bach_perc = round((bach['education'].count()/df_clean['education'].count())*100,0)
print('The percentage of people who have a Bachelors degree is',bach_perc, '%')

master = df_clean[df_clean['education'] == ' Masters']
doc = df_clean[df_clean['education'] == ' Doctorate']

Advanced_studies = pd.concat([bach, master, doc])
Advanced_studies

more_50_advanced = Advanced_studies[Advanced_studies['Salary'] == ' >50K']
more_50_advanced

more_50_perc = round((more_50_advanced['Salary'].count()/Advanced_studies['Salary'].count())*100,0)
print('The amount of people with advanced studies earning more than 50K is',more_50_perc, '%')


no_advanced = df.drop(df.index[df.education == ' Bachelors'] | df.index[df.education == ' Masters'] | df.index[df.education == ' Doctorate'], axis = 0)
no_advanced

no_advanced_more_50 = no_advanced[no_advanced['Salary'] == ' >50K']
no_advanced_more_50

no_advanced_more_50_perc = round((no_advanced_more_50['education'].count()/no_advanced['education'].count())*100,0)
print('The percentage of people without advanced studies who earn more than 50K is',no_advanced_more_50_perc, '%')


min_hours = df_clean['hours_per_week'].min()
print('the minimum value of hours is',min_hours, 'hour')


minimum = df_clean[df_clean['hours_per_week'] == min_hours]
minimum

minimum_more_50 = minimum[minimum['Salary'] == ' >50K']
minimum_more_50

minimum_more_50_perc = round((minimum_more_50['Salary'].count()/minimum['Salary'].count())*100,0)
print('The percentage of people with the minimum of hours per week who earn more than 50K is',minimum_more_50_perc, '%')


more_50_general = df_clean[df_clean['Salary'] == ' >50K']
more_50_general


more_50_general['native_country'].value_counts()


print('From this DataSerie was determinated that the country with the maximum amount of people who earn more than 50K is United States. The percentage is')


united_states = more_50_general[more_50_general['native_country'] == ' United-States']
united_states

perc_countries = round((united_states['native_country'].count()/more_50_general['native_country'].count())*100,0)
print('The country with more poeple who earn more tha 50K is the United States, representing the',perc_countries, '%')


more_50_general_india = more_50_general[more_50_general['native_country'] == ' India']
more_50_general_india


more_50_general_india['occupation'].describe()
print('The conclution was that the most popular occupaion in india with a salary >50K is Prof_specialty')

