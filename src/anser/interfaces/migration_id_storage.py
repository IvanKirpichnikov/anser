from abc import abstractmethod
from typing import Protocol

from anser.entities.migration import MigrationId


class MigrationIdStorage(Protocol):
    @abstractmethod
    def get(self) -> MigrationId | None:
        raise NotImplementedError
    
    @abstractmethod
    def set(
        self,
        migration_id: MigrationId,
    ) -> None:
        raise NotImplementedError
