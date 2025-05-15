from abc import abstractmethod, ABC

from resources.domain.models import Resource


class ResourcesRepository(ABC):
    @abstractmethod
    def all(self) -> list[Resource]: ...

    @abstractmethod
    def save(self, resource: Resource) -> None: ...