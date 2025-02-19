from pydantic_settings import BaseSettings


# This Settings class automatically retrieves environment variables and stores them
# in these class variables. Environment variable names are expected to be in all caps.
# Type validation is done automatically.
class Settings(BaseSettings):
    public_base_url: str = "http://localhost:8008"
    host_address: str = "0.0.0.0"
    port: int = 8008
    db_host: str = "localhost"
    db_port: int = 5432
    db_username: str = "root"
    db_password: str = "root"
    db_database: str = "ecommerce"

    def get_db_url(self):
        return "postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}".format(
            username=self.db_username,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_database,
        )