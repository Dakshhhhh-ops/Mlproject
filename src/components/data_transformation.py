import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object 



@dataclass # for all input things related to data transformation
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', "preprocessor.pkl")  # path to save preprocessor object



class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()  # create object of config class to access paths

    def get_data_transformer_object(self):   
        '''
        This function is responsible for creating the data transformation pipeline for both numerical and categorical features.
        It defines which columns are numerical and which are categorical, and then creates separate pipelines for each
        ''' 
        try:
            logging.info("Data Transformation initiated")

            # Define which columns are numerical and which are categorical
            numerical_columns = ['writing_score', 'reading_score']
            categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),  # fill missing values with median
                    ('scaler', StandardScaler())  # standardize numerical features
                ]
            )
            cat_pipeline = Pipeline(
                steps=[ 
                    ('imputer', SimpleImputer(strategy='most_frequent')),  # fill missing values with most frequent value
                    ('one_hot_encoder', OneHotEncoder()),  # convert categorical variables to binary vectors
                    ('scaler', StandardScaler(with_mean=False))  # standardize categorical features (after one-hot encoding)
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)]


            )
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)  

    def initiate_data_transformation(self, train_path, test_path):
        try:
            # read train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessor_obj = self.get_data_transformer_object()  # get the preprocessor object

            target_column_name = "math_score"  # define target variable name
            numerical_columns = ['writing_score', 'reading_score']  # define numerical columns

            # separate input features and target variable for train and test data
            # drop target column from input features and convert to numpy array  
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]


            logging.info("Applying preprocessing object on training and testing data")

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)  # fit and transform train data
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)  # transform test data

            # concatenate input features and target variable for train and test data
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)] 

            logging.info("Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)
                          