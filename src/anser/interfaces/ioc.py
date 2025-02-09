from abc import abstractmethod
from typing import ContextManager, Protocol

from anser.interfaces.migration_id_storage import MigrationIdStorage


class IoC(Protocol):
    @abstractmethod
    def migration_id_storage(self) -> ContextManager[MigrationIdStorage]:
        raise NotImplementedError
