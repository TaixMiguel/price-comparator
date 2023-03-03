APP_NAME = 'Comparador de precios'
APP_VERSION = "0.1.0_alpha"  # Mantener comillas dobles para el CI


class Config:
    class Application:
        ROOT: str = 'app'
        ALLOWED_HOSTS: str = 'allowedHosts'
        CORS_ALLOWED_ORIGINS: str = 'corsAllowedOrigins'
        DEBUG_MODE: str = 'debugMode'
        SECRET_KEY: str = 'secretKey'

    class BBDD:
        ROOT: str = 'bbdd'
        ENGINE: str = 'engine'
        NAME: str = 'name'
