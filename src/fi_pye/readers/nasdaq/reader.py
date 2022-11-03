import logging
import pandas as pd
import requests

from fi_pye.readers.fmp.utils import (
    CONNECTION_TIMEOUT,
    READ_TIMEOUT,
    _init_session,
)
from typing import Union
from fi_pye.readers.base import BaseReader


class NasdaqReader(BaseReader):
    __slots__ = "api_key", "limit", "session", "headers"

    def __init__(self, api_key: str, default_limit: int = 25, session: requests.Session | None = None):
        """
        Create instantiation of reader, which is used to obtain data
        from FMP without needing to input an API key with each request.

        Parameters
        ----------
        api_key :
            Nasdaq API token.
        session : default = None
            requests Session.
        """
        if not api_key or not isinstance(api_key, str):
            raise ValueError("IEX api key needed.")

        if not isinstance(default_limit, int):
            raise TypeError("limit must be of type: int. ")

        self.api_key = api_key
        self.limit = default_limit
        self.session = _init_session(session)  # Initialize session.
        self.headers = None

    def close(self):
        """Close requests session."""
        self.session.close()

    def data(self, path: str, params: dict[str, Union[str, int]]):
        """
        Function to obtain data from the IEX API endpoint, given the
        specific endpoint path and parameters used in request.

        Parameters
        ----------
        path :
            Endpoint path (after base url but before parameters)
        params :
            Dictionary of parameters used for request.

        Return
        -------
        object : pandas.DataFrame | None
            pandas.Dataframe
        """
        try:
            return self._get_data(url=f"https://data.nasdaq.com/api/v3/datasets/{path}", params=params)
        finally:
            self.close()

    def _get_data(self, url, params):
        """ """
        out_json = self._get_response(url=url, params=params).json()["dataset"]

        try:
            #out = pd.DataFrame(out_json)
            out = pd.DataFrame(
                data=out_json["data"],
                columns=out_json["column_names"]
            )

        except Exception as e:
            logging.error(f"JSON conversion exception: {e}")

        else:
            if len(out) == 0:
                service = self.__class__.__name__
                raise IOError(
                    f"Request from: {service} returned no data; check if URL is invalid. "
                    f"Request url: {url} ."
                )

            return out

    def _get_response(self, url, params=None, headers=None):
        """ """
        headers = headers or self.headers
        response = self.session.get(
            url=url, params=params, headers=headers, timeout=(CONNECTION_TIMEOUT, READ_TIMEOUT)
        )
        if response.status_code == requests.codes.ok:
            return response
