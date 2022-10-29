import logging
import requests

import pandas as pd

CONNECTION_TIMEOUT = 5
READ_TIMEOUT = 30


def _init_session(session=None):
    if session is None:
        session = requests.Session()
    else:
        if not isinstance(session, requests.Session):
            raise TypeError("session must be a requests.Session")

    return session


def _construct_url(url_version, path):
    """ """
    valid_values = ["v3", "v4"]
    if url_version not in valid_values:
        raise ValueError(
            f"Invalid url version: {url_version}. "
            "The only available url versions are 'v3' and 'v4'. "
        )

    else:
        return f"https://financialmodelingprep.com/api/{url_version}/{path}"


def _format_multiple_symbols(symbols: list[str]) -> str:
    """ """
    if not isinstance(symbols, list):
        raise TypeError(
            f"Invalid symbols type passed: {symbols} is of type {type(symbols)}. "
            "symbols must be of type list. "
        )

    for symbol in symbols:
        if not isinstance(symbol, str):
            raise TypeError(
                f"Invalid symbol passed within list of symbols: {symbols}. "
                f"Invalid symbol type passed: {symbol} is of type {type(symbol)}. "
                "symbol must be of type string (str). "
            )

    return ",".join([symbol.upper() for symbol in symbols])


def _get_df(url, params, session):
    """ """
    if session is None:
        raise Exception("requests.Session cannot be None.")

    with session as s:
        response = s.get(
            url=url,
            params=params,
            timeout=(CONNECTION_TIMEOUT, READ_TIMEOUT),
        )

    if len(response.json()) == 1 and "Error Message" in response.json():
        raise ValueError("Invalid API token response received.")

    try:
        df = pd.DataFrame(response.json())

    except Exception as e:
        logging.error(f"DataFrame conversion exception: {e}")

    else:
        if len(df) == 0:
            logging.error(
                "DataFrame appears to be empty. "
                f"Request ( url / params): {url} / {params}. "
                "Returning None."
            )
            return None

        return df
