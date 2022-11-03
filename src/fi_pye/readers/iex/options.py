from .reader import IexReader


class Options(IexReader):
    """ """
    def __init__(self, symbol: str, token: str, session=None):
        """ """
        super(Options, self).__init__(token=token, session=session)

        if not isinstance(symbol, str):
            raise TypeError("symbol must be of type: str. ")

        self.symbol = symbol.upper()

    @property
    def standard_exp_chain(self):
        """ """
        try:
            exp = super().data(
                path=f"stock/{self.symbol}/options",
                params={"token": self.token}
            )

        except AttributeError:
            raise ValueError(f"expiration chain for symbol: {self.symbol} returned None. ")

        return exp

    def chain_by_expiration(self, expiration: str, side: str):
        """ """

        valid_sides = ["both", "call", "put"]
        if side not in valid_sides:
            raise ValueError(f"invalid side: {side}. Valid side values are: {valid_sides}. ")

        if side == "both":
            path = f"stock/{self.symbol}/options/{expiration}"
        else:
            path = f"stock/{self.symbol}/options/{expiration}/{side}"

        return self.data(
            path=path,
            params={"token": self.token},
        )


