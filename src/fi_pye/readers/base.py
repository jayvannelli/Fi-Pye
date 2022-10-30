from typing import Union
from abc import ABC, abstractmethod


class BaseReader(ABC):

    @abstractmethod
    def __init__(*args, **kwargs):
        """Must be overriden by child class. """

    @abstractmethod
    def close(self):
        """Close requests.session. Must be overriden by child class. """

    @abstractmethod
    def data(self, url_version: str, path: str, params: dict[str, Union[str, int]]):
        """Obtain data from FMP as DataFrame (must be overriden). """
