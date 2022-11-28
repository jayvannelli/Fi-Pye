from fi_pye.readers.serpapi.reader import SerpApiReader


class GTrends(SerpApiReader):
    """ """
    def interest_over_time(self, query: str):
        """ """
        return self.data(
            params={
                "engine": "google_trends",
                "q": query,
                "data_type": "TIMESERIES",
                "api_key": self.apikey,
            },
            key='interest_over_time',
        )
