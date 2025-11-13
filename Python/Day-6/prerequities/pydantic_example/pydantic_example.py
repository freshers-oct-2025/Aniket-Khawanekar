from pydantic import BaseModel,Field
from typing import Optional
from enum import Enum
from datetime import datetime
import time

class Language(str,Enum):
    PY="python",
    JAVA="java",
    GO="got"

class Blog(BaseModel):
    title:str
    description:Optional[str]=None
    is_active:bool
    language:Language=Language.PY
    created_at:datetime=Field(default_factory=datetime.now)
    
first_blog=Blog(title="GW",is_active=True)
print(first_blog)
time.sleep(5)
second_blog=Blog(title="GW",is_active=True)
print(second_blog)