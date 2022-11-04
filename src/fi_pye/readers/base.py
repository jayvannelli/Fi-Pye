from abc import ABC, abstractmethod


class BaseReader(ABC):
    """ """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """ """
        ...

    def close(self):
        """Close requests session."""
        ...

    def data(self, *args, **kwargs):
        """ """
        ...
