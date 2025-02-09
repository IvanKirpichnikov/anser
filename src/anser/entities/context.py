from typing import Generic, TypeVar

from anser.entities.migration import Migration


ConnectionType = TypeVar('ConnectionType')


class AnserContext(Generic[ConnectionType]):
    def __init__(
        self,
        migration: Migration,
        connection: ConnectionType,
    ) -> None:
        self._migration = migration
        self._connection = connection
    
    @property
    def migration(self) -> Migration:
        return self._migration
    
    @property
    def connection(self) -> ConnectionType:
        return self._connection
