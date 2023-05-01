import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/a-mt/fcc-medical-data-visualizer/master/medical_examination.csv')
data

data['BMI'] = round(data['weight']/(data['height']*0.01)**2,2)
data

data.loc[(data.BMI<=25, 'BMI')] = 0
data.loc[(data.BMI>25, 'BMI')] = 1

data

### Normalizing the data

#The task says that every value greater than one will be replaced by one; every value equal to one will be replaced by 0.

data
chol = data['cholesterol'].value_counts()
print(chol)
gluc = data['gluc'].value_counts()
print(gluc)
smo = data['smoke'].value_counts()
print(smo)
alc = data['alco'].value_counts()
print(alc)
acti = data['active'].value_counts()
print(acti)
card = data['cardio'].value_counts()
print(card)


def normalizer(x,y):
    x = 'cholesterol'
    y = 'gluc'
    z = 'smoke'
    a = 'alco'
    b = 'active'
    c = 'cardio'

    dic = [x,y]

    for i in dic:
        data.loc[(data[i] == 1, i)] = 0
        data.loc[(data[i] > 1, i)] = 1
    data
    return data


x = 'cholesterol'
y = 'gluc'
z = 'smoke'
a = 'alco'
b = 'active'
c = 'cardio'
normalizer(x,y)


chol2 = data['cholesterol'].value_counts()
print(chol2)
gluc2= data['gluc'].value_counts()
print(gluc2)
smo2 = data['smoke'].value_counts()
print(smo2)
alc2 = data['alco'].value_counts()
print(alc2)
acti2 = data['active'].value_counts()
print(acti2)
card2 = data['cardio'].value_counts()
print(card2)


#After normalized the data, is possible to conclude  that the only two variables able to be analyzed are 'cholesterol' and 'gluc'. Let's proceed. Note that the other variables that obly has 0 and 1 were not changed.  

## Catplot.

#Is necessary to create a catplot splited by 'cardio'.

columns = ['cholesterol', 'gluc', 'smoke', 'alco', 'BMI', 'active']

df = pd.melt(data, id_vars=['cardio'], value_vars=columns)
df = df.reset_index().groupby([ 'variable','cardio', 'value']).agg('count').rename(columns = {'index': 'total'}).reset_index()

df

plot = sns.catplot(x="variable", y="total", col="cardio", hue="value", data=df, kind="bar")


#Heatmap

data_heat = data[(data['ap_lo'] <= data['ap_hi']) & (data['height'] >= data['height'].quantile(0.025))  & (data['height'] <= data['height'].quantile(0.975))  & (data['weight'] >= data['weight'].quantile(0.025)) & (data['weight'] <= data['weight'].quantile(0.975)) ]

corr = data_heat.corr()
corr

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True

heat = sns.heatmap(corr, mask = mask)

