from omegaconf import OmegaConf
from pydantic import BaseModel, field_validator
import os


class BaseDataLoaderConfig(BaseModel):
    
    data_source: str

    @field_validator('data_source')
    def check_data_source(cls, value):
        if not isinstance(value, str):
            raise ValueError("Data source must be a string path to a JSON file")
        # make sure the path exists
        if not os.path.exists(value):
            raise FileNotFoundError(f"File not found: {value}")
        
        extension = value.split('.')[-1]
        if extension not in {'json', 'csv', 'xml', 'yaml'}:
            raise ValueError(f"Only JSON, CSV, XML, and YAML files are supported for the data loader. Got: {extension}")

        return value
    


class Config(BaseModel):
    data_loader: BaseDataLoaderConfig



def load_config(config_path: str) -> Config:
    config = OmegaConf.load(config_path)

    config_dict = OmegaConf.to_container(config, resolve=True)

    return Config.model_validate(config_dict)



