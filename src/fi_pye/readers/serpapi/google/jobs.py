from fi_pye.readers.serpapi.reader import SerpApiReader


class GJobs(SerpApiReader):
    """ """
    def job_listings(self, query: str):
        """ """
        return self.data(
            params={
                "engine": "google_jobs",
                "q": query,
                "data_type": "TIMESERIES",
                "api_key": self.apikey,
            },
            key='jobs_results',
        )
