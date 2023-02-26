import json
import logging
import os
from threading import Lock

log = logging.getLogger(__name__)


class ConfigAppMeta(type):

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigApp(metaclass=ConfigAppMeta):

    __configData: dict = {}

    def __init__(self) -> None:
        from pathlib import Path
        path_file: str
        try:
            path_file = os.environ['CONFIG_FILE_PRICE_COMPARATOR']
            if not Path(path_file).is_file():
                log.error(f'No se encuentra el fichero de configuración "{path_file}"')
                path_file = f'{Path(__file__).resolve().parent.parent}/config/configDefault.json'
        except KeyError:
            log.error('No se ha definido la variable de entorno CONFIG_FILE_PRICE_COMPARATOR')
            path_file = f'{Path(__file__).resolve().parent.parent}/config/configDefault.json'
        finally:
            with open(path_file, 'r') as config_file:
                self.__configData = json.load(config_file)

    def __get_value(self, first_element: str, second_element: str, default):
        try:
            return self.__configData[first_element][second_element]
        except KeyError:
            log.info(f'No se encuentra el elemento de configuración "{first_element}=>{second_element}"')
            return default

    def get_value(self, first_element: str, second_element: str, default='') -> str:
        return self.__get_value(first_element=first_element, second_element=second_element, default=default)

    def get_value_array(self, first_element: str, second_element: str, default=[]) -> list:
        return self.__get_value(first_element=first_element, second_element=second_element, default=default)

    def get_value_integer(self, first_element: str, second_element: str, default=0) -> int:
        return self.__get_value(first_element=first_element, second_element=second_element, default=default)

    def get_value_boolean(self, first_element: str, second_element: str, default=False) -> bool:
        return self.__get_value(first_element=first_element, second_element=second_element, default=default)
