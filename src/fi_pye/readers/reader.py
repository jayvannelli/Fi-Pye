import requests
from typing import Union

from .utils import (
    _construct_url,
    _init_session,
    _get_df,
)

from .base import BaseReader


class Reader(BaseReader):
    __slots__ = "apikey", "session"

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

    def close(self):
        """Close requests session."""
        self.session = self.session.close()

    def data(self, url_version: str, path: str, params: dict[str, Union[str, int]]):
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
        return _get_df(_construct_url(url_version, path), params, self.session)
