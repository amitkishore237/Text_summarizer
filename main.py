from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline

from src.text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME="Data Ingestion Pipeline stage_01"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data validation Pipeline stage_02"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Pipeline stage_03"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training Pipeline stage_04"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_validation = ModelTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model evaluation Pipeline stage_05"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_validation = ModelEvaluationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e