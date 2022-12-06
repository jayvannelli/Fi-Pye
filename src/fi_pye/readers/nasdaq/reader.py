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
    __slots__ = "apikey", "session", "headers"

    def __init__(self, apikey: str, session: requests.Session | None = None):
        """Create instantiation of reader used to obtain data from Nasdaq API.

        Parameters
        ----------
        apikey :
            Nasdaq API token.
        session : default = None
            requests Session.
        """
        if not apikey or not isinstance(apikey, str):
            raise ValueError("Nasdaq api key needed.")

        self.apikey = apikey
        self.session = _init_session(session)  # Initialize session.
        self.headers = None

    def close(self):
        """Close requests session."""
        self.session.close()

    def data(self, base: str, path: str, params: dict[str, Union[str, int]]):
        """Function to obtain data from the Nasdaq API endpoints.

        Parameters
        ----------
        base :
            Nasdaq url 'base' (either 'datatables' or 'datasets')
        path :
            Endpoint path (after base url but before parameters)
        params :
            Dictionary of parameters used for request.

        Return
        -------
        object : pandas.DataFrame | None
            pandas.Dataframe
        """
        valid_bases = ["datatables", "datasets"]
        if base not in valid_bases:
            raise ValueError(f"Invalid base: {base}. Valid bases include: {valid_bases}. ")

        try:
            return self._get_data(url=f"https://data.nasdaq.com/api/v3/{base}/{path}", params=params)
        finally:
            self.close()

    def _get_data(self, url, params):
        """ """
        out_json = self._get_response(url=url, params=params).json()["dataset"]

        try:
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
