import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import dill
from src.exception import CustomException

from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)  # create directory if it doesn't exist    
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_model(X_train, y_train, X_test, y_test, models): 
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]  # get model object
            model.fit(X_train, y_train)  # fit model on train data
            y_train_pred = model.predict(X_train)  # predict on train data
            y_test_pred = model.predict(X_test)  # predict on test data
            train_model_score = r2_score(y_train, y_train_pred)  # calculate r2 score for train data
            test_model_score = r2_score(y_test, y_test_pred)  # calculate r2 score
            report[list(models.keys())[i]] = test_model_score  # add model name and score to report
        return report
    except Exception as e:
        raise CustomException(e, sys)   