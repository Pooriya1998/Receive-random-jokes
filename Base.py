from abc import ABC, abstractmethod
import requests


class JokeApiBase(ABC):
    def __init__(self, apikey, apihost, **kwargs):
        pass

    @abstractmethod
    def get_random_joke(self):
        pass
