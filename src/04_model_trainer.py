import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import BaggingClassifier,RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, StackingClassifier
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


path = os.path.join('data', 'treatments_2017-2020_train')

df = pd.read_parquet( path + '.parquet')
print(df.shape)


batch = 100000
df = df.sample(batch).reset_index(drop=True)

X = df.drop("NOPRIOR", axis=1)
y = df["NOPRIOR"]



columns_one_hot = ['GENDER', 'RACE', 'ETHNIC', 'MARSTAT', 'EMPLOY', 'VET' ,	'LIVARAG',	'PRIMINC',
                   'DIVISION',	'SERVICES' ,  'PSOURCE' , 	'SUB1' , 	'FREQ1', 
                   'PSYPROB' ,	'FREQ_ATND_SELF_HELP']


X = pd.get_dummies(X, columns=columns_one_hot, drop_first=True)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)



xgb_model = XGBClassifier()

# parameters to choose from
parameters = {
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                }

# Type of scoring used to compare parameter combinations
scorer = metrics.make_scorer(metrics.f1_score)

#  grid search
grid_obj = RandomizedSearchCV(xgb_model, parameters,scoring=scorer,cv=3)
grid_obj = grid_obj.fit(X_train, y_train)

# Set the clf to the best combination of parameters
xgb = grid_obj.best_estimator_

# Fit the best algorithm to the data.
xgb.fit(X_train, y_train)



def metrics_report(model,features,target):
    predictions = model.predict(features)
    acc = accuracy_score(target, predictions)  # to compute Accuracy
    recall = recall_score(target, predictions)  # to compute Recall
    precision = precision_score(target, predictions)  # to compute Precision
    f1 = f1_score(target, predictions)  # to compute F1-score

        # creating a dataframe of metrics
    df_metrics = pd.DataFrame({
            "Accuracy": acc,
            "Recall": recall,
            "Precision": precision,
            "F1 Score": f1,
            },index=[0],)

    return df_metrics




metrics_train = metrics_report(xgb,X_train,y_train)
metrics_test = metrics_report(xgb,X_test,y_test)


metrics_dataframe = pd.concat([metrics_train, metrics_test]).reset_index()

metrics_dataframe['index'] = ['train','test']
metrics_dataframe.set_index('index',inplace=True)


print(metrics_dataframe)