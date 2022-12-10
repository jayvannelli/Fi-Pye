from abc import ABC, abstractmethod


class BaseReader(ABC):
    """Base 'Reader' to establish child class interface and instantiation."""

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
