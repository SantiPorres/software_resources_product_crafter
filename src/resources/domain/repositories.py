from abc import abstractmethod, ABC

from src.resources.domain.models import Resource


class ResourcesRepository(ABC):
    @abstractmethod
    def get(self) -> Resource: ...