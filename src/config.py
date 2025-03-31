from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    DB_HOST : str
    DB_PORT : int
    DB_USER : str
    DB_PASSWORD : str
    DB_NAME : str

    @property
    def DATABASE_URL_psycopg(self):
        #postgres://user:pass@localhost:5432/dbname  postgresql://username:password@localhost/dbname
        return f'postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    #model_config = SettingsConfigDict(env_file = '.env')
    #model_config = SettingsConfigDict(env_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env')))


settings = Settings()