from networksecurity.components.data_ingesion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
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
        logging.info("data ingestion completed")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingesionartifact,data_validation_config)
        logging.info("initiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)