from typing import Union
from pydantic import BaseModel


# Contents of JWT token
class TokenPayload(BaseModel):
    sub: Union[int, None] = None