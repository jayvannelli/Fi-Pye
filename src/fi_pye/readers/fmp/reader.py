import logging
import pandas as pd
import requests

from fi_pye.readers.fmp.utils import (
    CONNECTION_TIMEOUT,
    READ_TIMEOUT,
    _construct_url,
    _init_session,
)
from typing import Union

from fi_pye.readers.base import BaseReader


class FmpReader(BaseReader):
    __slots__ = "apikey", "session", "headers"

    def __init__(self, apikey: str, session: requests.Session | None = None):
        """
        Create instantiation of reader, which is used to obtain data
        from FMP without needing to input an API key with each request.

        Parameters
        ----------
        apikey :
            FMP API token.
        session : default = None
            requests Session.
        """
        if not apikey or not isinstance(apikey, str):
            raise ValueError("FMP api key needed.")

        self.apikey = apikey
        self.session = _init_session(session)  # Initialize session.
        self.headers = None

    def close(self):
        """Close requests session."""
        self.session.close()

    def data(self, url_version: str, path: str, params: dict[str, Union[str, int]] | None):
        """
        Function to obtain data from the FMP API endpoint, given the FMP
        base url version used by the endpoint, the specific endpoint path,
        and the parameters after the endpoint used in the request.

        Parameters
        ----------
        url_version :
            Base url used in endpoint, either 'v3' or 'v4'
        path :
            Endpoint path (after base url but before parameters)
        params :
            Dictionary of parameters used for request.

        Return
        -------
        object : pandas.DataFrame | None
            pandas.Dataframe
        """
        if params is None:
            params = {"apikey": self.apikey}
        else:
            params.update({"apikey": self.apikey})

        try:
            return self._get_data(url=_construct_url(url_version, path), params=params)
        finally:
            self.close()

    def _get_data(self, url, params):
        """ """
        with self.session as s:
            r = s.get(url=url, params=params, timeout=(CONNECTION_TIMEOUT, READ_TIMEOUT))

            if r.status_code == requests.codes.ok:
                out = r.json()

            elif r.status_code == 403:
                raise ValueError(f"The url: {url} is not available to free api keys.")

            else:
                logging.error(f"Response error: {r} occurred during http request. ")

            if len(out) == 0:
                service = self.__class__.__name__
                raise IOError(
                    f"Request from: {service} returned no data; check if URL is invalid. "
                    f"Request url: {url} ."
                )

        return pd.DataFrame(out)
