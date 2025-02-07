from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    @abstractmethod
    def exists(self, login):
        """Check if a login exists in dataset. Must be implemented by subclasses."""
        pass