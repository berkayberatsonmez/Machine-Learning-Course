# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 07:19:33 2022

@author: berkayberatsonmez
"""

# KNN Algorithm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%
data = pd.read_csv("data.csv")

# %%
data.drop(["id","Unnamed: 32"],axis=1,inplace=True)
data.tail()
# malignant = M  kotu huylu tumor
# benign = B     iyi huylu tumor

data.shape #(569,31)

data.head() #Data columns name and first 5 value

data.columns #Data columns name

data.info() #Data information

data.isnull().sum() #Any value is null?

data.describe() #Analyzes data

data.corr() #The relationship between the data themselves

# %%
M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]
# scatter plot
plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kotu",alpha= 0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="iyi",alpha= 0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

# %%
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)

# %%
# normalization 
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))


#%%
# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=8)



# %%
# knn model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 3) # n_neighbors = k
knn.fit(x_train,y_train)
prediction = knn.predict(x_test)
print(" {} nn score: {} ".format(3,knn.score(x_test,y_test)))


# %%
# find k value
score_list = []
for each in range(1,15):
    knn2 = KNeighborsClassifier(n_neighbors = each)
    knn2.fit(x_train,y_train)
    score_list.append(knn2.score(x_test,y_test))
    
plt.plot(range(1,15),score_list)
plt.xlabel("k values")
plt.ylabel("accuracy")
plt.show()



y_pred = knn2.predict(x_test)
y_true = y_test
#%% confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true,y_pred)


# %% cm visualization
import seaborn as sns
import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize =(8,5))
sns.heatmap(cm,annot = True,linewidths=0.5,linecolor="red",fmt = ".0f",ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()



#Geri Eleme(Backward Elimination)
import statsmodels.api as sm

X = data.iloc[:,:-1].values
X = np.array(X,dtype=float)
model = sm.OLS(data.iloc[:,-1:],X).fit()
print(model.summary()) #Rapor

data.drop('texture_mean', inplace=True, axis=1)
#data.drop('radius_worst', inplace=True, axis=1)
data.drop('concave points_se', inplace=True, axis=1)
data.drop('texture_worst', inplace=True, axis=1)
data.drop('texture_se', inplace=True, axis=1)
data.drop('perimeter_mean', inplace=True, axis=1)
data.drop('smoothness_se', inplace=True, axis=1)
#data.drop('symmetry_mean', inplace=True, axis=1)


X = data.iloc[:,:-1].values
X = np.array(X,dtype=float)
model = sm.OLS(data.iloc[:,-1:],X).fit()
print(model.summary()) #Rapor



