from src.resources.domain.models import Resource
from src.resources.domain.repositories import ResourcesRepository


class PostgreSQLResourcesRepository (ResourcesRepository):
    def get(self) -> Resource:
        pass