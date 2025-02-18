from omegaconf import OmegaConf
from pydantic import BaseModel, field_validator
import os


"""
Config module for the data-filter application.
"""


class BaseDataLoaderConfig(BaseModel):

    loader_name: str

    @field_validator("loader_name")
    def check_loader_name(cls, value):
        if not isinstance(value, str):
            raise ValueError("loader_name must be a string")

        if value not in {"json", "csv", "xml", "yaml"}:
            raise ValueError(
                f"Only JSON, CSV, XML, and YAML files are supported for the data loader. Got: {value}"
            )

        return value


class Config(BaseModel):
    data_loader: BaseDataLoaderConfig


def load_config(config_path: str) -> Config:
    config = OmegaConf.load(config_path)

    config_dict = OmegaConf.to_container(config, resolve=True)

    return Config.model_validate(config_dict)
