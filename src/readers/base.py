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
    def data(
            self,
            url_version: str,
            path: str,
            params: dict[str, Union[str, int]],
    ):
        """
        Function to obtain data from the FMP API endpoint, given the FMP
        base url version used by the endpoint, the specific endpoint path,
        and the parameters after the endpoint used in the request.

        :param url_version: Base url used in endpoint ('v3' or 'v4').
        :param path: Endpoint path.
        :param params: Dictionary of parameters used in request.

        ------
        Return : pandas DataFrame
        ------
        """
