from pydantic import BaseModel, field_validator
import pandas as pd


class CSVDataContainer(BaseModel):
    

    @staticmethod
    def _as_pandas_data_frame(data_source: str) -> pd.DataFrame:
        return pd.read_csv(data_source)
    
    

    
    
    
    
    