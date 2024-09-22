from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

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

