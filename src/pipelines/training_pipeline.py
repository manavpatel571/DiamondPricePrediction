import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
<<<<<<< HEAD
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
=======
>>>>>>> 0e35abaf4e6a6fabd7ecff6f5d7c326693235ced


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
<<<<<<< HEAD
    data_transformation =  DataTransformation()
    train_arr,test_arr,obj_path=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)
=======
>>>>>>> 0e35abaf4e6a6fabd7ecff6f5d7c326693235ced
    