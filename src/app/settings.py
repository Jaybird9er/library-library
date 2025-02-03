from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host_address: str = "0.0.0.0"
    port: int = 8000
