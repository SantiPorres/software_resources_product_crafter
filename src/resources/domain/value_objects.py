from dataclasses import dataclass
import validators

from resources.domain.exceptions import UrlIsNotValid


@dataclass(frozen=True)
class ResourceUrl:
    value: str

    def __post_init__(self) -> None:
        if not validators.url(self.value):
            raise UrlIsNotValid