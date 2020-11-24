from dataclasses import dataclass


@dataclass
class Token:
    access_token: str
    token_type: str
    expire_in: int
