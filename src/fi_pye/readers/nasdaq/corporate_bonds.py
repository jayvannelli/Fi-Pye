from .reader import NasdaqReader
from .utils import _validate_limit

VALID_BOND_GRADING = ["AAA", "AA", "A", "BBB", "BB", "B", "CCC"]


class CorporateBonds(NasdaqReader):
    """
    Query Nasdaq Data Link API endpoints related to the
    Corporate Bond Yield Rates dataset published by Quandl.
    """
    def bond_index_yield(self, grading: str, limit: int = 25):
        """ """
        if grading.upper() not in VALID_BOND_GRADING:
            raise ValueError(f"Invalid bond grading: {grading}. Valid 'grading' values include: {VALID_BOND_GRADING}.")

        # If grading is AA, BB or CCC, path ends in a single 'Y' and not 'EY'.
        if len(grading) == 2 or grading.upper() == "CCC":
            path = f"ML/{grading.upper()}Y"
        else:
            path = f"ML/{grading.upper()}EY"

        return self.data(
            base="datasets",
            path=path,
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def total_return_index(self, grading: str, limit: int = 25):
        """ """
        if grading.upper() not in VALID_BOND_GRADING:
            raise ValueError(f"Invalid bond grading: {grading}. Valid 'grading' values include: {VALID_BOND_GRADING}.")

        return self.data(
            base="datasets",
            path=f"ML/{grading.upper()}TRI",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def emerging_markets_index_oas(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/EMCBI",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def emerging_markets_tri(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/EMCTRI",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def emerging_markets_high_grade(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/EMHGY",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def emerging_markets_high_yield(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/EMHYY",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def euro_emerging_markets_index(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/EEMCBI",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def us_high_yield_index_oas(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/HYOAS",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def us_high_yield_tri(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/USTRI",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def us_total_return_index(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/TRI",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def us_bond_index(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/USEY",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def emea_total_return_index(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/EMHG",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def ig_emerging_markets_tri(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/IGEM",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def aa_rated_index_oas(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/AAOAS",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def b_rated_index_oas(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="ML/BOAS",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )
