import requests
import logging
import pandas as pd
from typing import Union

from fi_pye.readers.fmp.utils import (
    CONNECTION_TIMEOUT,
    READ_TIMEOUT,
    _init_session,
)
from fi_pye.readers.base import BaseReader


class SerpApiReader(BaseReader):
    __slots__ = "apikey", "session", "headers"

    def __init__(self, apikey: str, session: requests.Session | None = None):
        """
        Create instantiation of reader, which is used to obtain data
        from Nasdaq without needing to input an API key with each request.

        Parameters
        ----------
        apikey :
            Nasdaq API token.
        session : default = None
            requests Session.
        """
        if not apikey or not isinstance(apikey, str):
            raise ValueError("SerpApi api key needed.")

        self.apikey = apikey
        self.session = _init_session(session)  # Initialize session.
        self.headers = None

    def close(self):
        """Close requests session."""
        self.session.close()

    def data(self, params: dict[str, Union[str, int]], key: str):
        """
        Function to obtain data from the FMP API endpoint, given the FMP
        base url version used by the endpoint, the specific endpoint path,
        and the parameters after the endpoint used in the request.

        Parameters
        ----------
        params :
            Dictionary of parameters used for request.

        Return
        -------
        object : pandas.DataFrame | None
            pandas.Dataframe
        """
        try:
            r = self._get_data(url="https://serpapi.com/search.json", params=params).json()
            d = r[key]
        except KeyError as key_error:
            logging.error(f"Key error: {key_error}. ")
        else:
            return pd.DataFrame(d)
        finally:
            self.close()

    def _get_data(self, url, params=None, headers=None):
        """ """
        headers = headers or self.headers
        response = self.session.get(
            url=url, params=params, headers=headers, timeout=(CONNECTION_TIMEOUT, READ_TIMEOUT)
        )

        if response.status_code == requests.codes.ok:
            return response

        else:
            logging.error(f"Response: {response} with status code: {response.status_code} isn't an okay code. ")
