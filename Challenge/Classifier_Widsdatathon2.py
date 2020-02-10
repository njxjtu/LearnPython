# Importing Required Libraries
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

data = pd.read_csv("widsdatathon2020/training_v2.csv")
unlabeled = pd.read_csv("widsdatathon2020/unlabeled.csv")
unlabeled0 = unlabeled
print(data)
train,test=train_test_split(data,test_size=0.1,random_state=0,stratify=data['hospital_death'])
print(train.head())
# Dropping Features
train = train.drop(['encounter_id'], axis=1)
test = test.drop(['encounter_id'], axis=1)
unlabeled = unlabeled.drop(['encounter_id'], axis=1)

train = train.drop(['patient_id'], axis=1)
test = test.drop(['patient_id'], axis=1)
unlabeled = unlabeled.drop(['patient_id'], axis=1)

train = train.drop(['hospital_admit_source'], axis=1)
test = test.drop(['hospital_admit_source'], axis=1)
unlabeled = unlabeled.drop(['hospital_admit_source'], axis=1)

# Convert categorical variables into dummy/indicator variables
train_processed = pd.get_dummies(train)
test_processed = pd.get_dummies(test)
unlabeled_processed = pd.get_dummies(unlabeled)
# Filling Null Values
train_processed = train_processed.fillna(train_processed.mean())
test_processed = test_processed.fillna(test_processed.mean())
unlabeled_processed = unlabeled_processed.fillna(unlabeled_processed.mean())
# Create X_train,Y_train,X_test
X_train = train_processed.drop(['hospital_death'], axis=1)
Y_train = train_processed['hospital_death']

X_test  = test_processed.drop(['hospital_death'], axis=1)
Y_test  = test_processed['hospital_death']

X_unlabeled  = unlabeled_processed.drop(['hospital_death'], axis=1)
# Display
print("Processed DataFrame for Training : hospital_death is the Target, other columns are features.")
print(train_processed.head())

# Random Forest
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
random_forest_preds = random_forest.predict(X_test)
print('Prediction for X_test in 0 or 1: ')
print(random_forest_preds)
print('The accuracy of the Random Forests model is :\t',metrics.accuracy_score(random_forest_preds,Y_test))
random_forest_preds = random_forest.predict_proba(X_unlabeled)
print('Prediction for X_unlabeled in probabilities: ')
df = pd.DataFrame(random_forest_preds[:,1],columns=['hospital_death'])
df['encounter_id'] = unlabeled0['encounter_id']
print(random_forest_preds[:,1])
export_csv = df.to_csv(r'export_dataframe.csv', index = None, header=True) 