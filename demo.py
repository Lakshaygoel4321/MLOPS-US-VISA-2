from src.logger import logging
from src.exception import USvisaException
from src.components.data_ingestion import DataIngestion,DataIngestionConfig
import sys
import os


if __name__ == '__main__':
    logging.info('There is error occured')

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise USvisaException(e,sys)
    
    