import os  # operating system related tasks like creating folders
import sys  # system information, used for custom exception handling

from src.exception import CustomException  # custom error handling class
from src.logger import logging  # logging setup

import pandas as pd  # dataframe handling
from sklearn.model_selection import train_test_split  # train-test split

from dataclasses import dataclass  # used to create config class

from src.components.data_transformation import DataTransformation  # to call data transformation component after ingestion
from src.components.data_transformation import DataTransformationConfig  # to access preprocessor object path

@dataclass # a box that store paths
class DataIngestionConfig:  # stores paths required by data ingestion component

    train_data_path: str = os.path.join('artifacts', "train.csv")  # path for train data

    test_data_path: str = os.path.join('artifacts', "test.csv")  # path for test data

    raw_data_path: str = os.path.join('artifacts', "data.csv")  # path for raw/original data


class DataIngestion:

    def __init__(self):
        # create object of config class and store paths
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        # log that ingestion process has started
        logging.info("Entered the data ingestion method or component")

        try:
            # read csv file into dataframe
            df = pd.read_csv('notebook\data\stud.csv')

            # log successful reading
            logging.info("Read the dataset as dataframe")

            # create artifacts folder if it doesn't exist
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            # save raw/original dataset
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            # log before splitting
            logging.info("Train test split initiated")

            # split dataset into train and test
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # save train dataset
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            # save test dataset
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            # log successful completion
            logging.info("Ingestion of the data is completed")

            # return paths for next pipeline component
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            # if any error occurs, raise custom exception
            raise CustomException(e, sys)




if __name__ == "__main__":

    # create object of DataIngestion class
    obj = DataIngestion()

    # start data ingestion process
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation = DataTransformation()  # create object of data transformation class
    data_transformation.initiate_data_transformation(train_data, test_data)  # start data transformation process