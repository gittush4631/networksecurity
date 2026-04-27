from networksecurity.components.data_ingesion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


if __name__=='__main__':
    try:
        logging.info("Enter try block")
        
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingesionconfig=DataIngestionConfig(trainingpipelineconfig)
        dataingesion=DataIngestion(dataingesionconfig)
        logging.info("Running data ingestion")
        dataingesionartifact=dataingesion.init_data_ingestion()
        print(dataingesionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)