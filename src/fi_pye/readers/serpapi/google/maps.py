from fi_pye.readers.serpapi.reader import SerpApiReader


class GMaps(SerpApiReader):
    """ """
    def local_results(
            self,
            query: str,
            lat: float,
            lon: float,
            zoom: int = 14,
    ):
        """

        zoom :
            Map zoom value. This can be any value between 3 (fully zoomed out) and 21 (fully zoomed in).
        """
        return self.data(
            params={
                "engine": "google_maps",
                "q": query,
                "ll": f"@{lat},{lon},{zoom}z",
                "type": "search",
                "api_key": self.apikey,
            },
            key='local_results',
        )

    def photos(self, data_id: str,):
        """

        """
        return self.data(
            params={
                "engine": "google_maps_photos",
                "data_id": data_id,
                "api_key": self.apikey,
            },
            key='photos',
        )

    def reviews(self, data_id: str,):
        """

        """
        return self.data(
            params={
                "engine": "google_maps_reviews",
                "data_id": data_id,
                "api_key": self.apikey,
            },
            key='reviews',
        )

