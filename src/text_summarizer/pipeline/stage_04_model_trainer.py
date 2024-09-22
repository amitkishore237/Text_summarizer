from src.text_summarizer.components import data_transformation
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_transformation import DataTransformation
from src.text_summarizer.logging import logger
from src.text_summarizer.components.model_trainer import ModelTrainer

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()