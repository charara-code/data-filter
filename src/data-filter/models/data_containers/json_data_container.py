from pydantic import BaseModel
from typing import List, Dict, Union
"""
JSON schemas accepted 

{
    "data": [

        {
            "item": {
                "field1": "value1",
                "field2": 2,
                "field3": 3.0,
                "field4": true,
                "field5": [1, 2, 3], # or any list that containes values of the types mentioned above (LIST OF LISTS OR LIST OF DICTS/OBJs NOT SUPPORTED)
            }
        },
        {
            "item": {
                "field1": "value2",
                "field2": 3,
                "field3": 4.0,
                "field4": false,
                "field5": [4, 5, 6],
            }
        },
    ]
    
}

"""

class JsonDataItem(BaseModel):

    item: Dict[str, Union[  str, int, float, bool, List[ Union[str, int, float, bool] ]  ] ]


class JsonDataContainer(BaseModel):

    data: List[JsonDataItem]