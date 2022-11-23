from .reader import NasdaqReader
from .utils import _validate_limit


class Blockchain(NasdaqReader):
    """
    Query Nasdaq Data Link API endpoints related to the
    Blockchain dataset published by Quandl.
    """

    def difficulty(self, limit: int = 25):
        """Query Nasdaq / BCHAIN/DIFF / API.

        A relative measure of how difficult it is to find a new block.
        The difficulty is adjusted periodically as a function of how
        much hashing power has been deployed by the network of miners.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="BCHAIN/DIFF",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def avg_block_size(self, limit: int = 25):
        """Query Nasdaq / BCHAIN/AVBLS / API.

        The average block size in MB.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="BCHAIN/AVBLS",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def network_deficit(self, limit: int = 25):
        """Query Nasdaq / BCHAIN/NETDF / API.

        Data showing difference between transaction fees and cost of bitcoin mining.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="BCHAIN/NETDF",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def hash_rate(self, limit: int = 25):
        """Query Nasdaq / BCHAIN/HRATE / API.

        The estimated number of tera hashes per second (trillions of hashes per second)
        the Bitcoin network is performing.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="BCHAIN/HRATE",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def miner_operating_margin(self, limit: int = 25):
        """Query Nasdaq / BCHAIN/MIOPM / API.

        Data showing miners revenue minus estimated electricity and bandwidth costs.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="BCHAIN/MIOPM",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def miner_revenue(self, limit: int = 25):
        """Query Nasdaq / BCHAIN/MIREV / API.

        Total value of coinbase block rewards and transaction fees paid to miners.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="BCHAIN/MIREV",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def est_transaction_volume(self, limit: int = 25, as_usd: bool = False):
        """Query Nasdaq / BCHAIN/ETRVU | BCHAIN/ETRAV / API.

        The total estimated value of transactions on the Bitcoin
        blockchain (does not include coins returned to sender as change).
        *Can return value in BTC or USD

        Parameters
        ----------
        as_usd : default = False
            Query Nasdaq / BCHAIN/ETRVU / (ie. Bitcoin Estimated transaction Volume USD).
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if as_usd:
            path = "BCHAIN/ETRVU"
        else:
            path = "BCHAIN/ETRAV"

        return self.data(
            base="datasets",
            path=path,
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )





