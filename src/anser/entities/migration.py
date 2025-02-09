from datetime import datetime, UTC
from hashlib import sha1
from types import ModuleType
from typing import NewType, Self


MigrationId = NewType('MigrationId', str)


def create_migration_id() -> MigrationId:
    migration_id = sha1().hexdigest()[:8]
    return MigrationId(migration_id)


class Migration:
    def __init__(
        self,
        id: MigrationId,
        module: ModuleType,
        name: str,
        created_at: datetime,
        message: str | None = None,
        parent_id: MigrationId | None = None,
    ) -> None:
        self.id = id
        self.module = module
        self.name = name
        self.message = message
        self.parent_id = parent_id
        self.created_at = created_at
    
    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'id={self.id}, '
            f'module={self.module}, '
            f'name={self.name}, '
            f'created_at={self.created_at}, '
            f'message={self.message}, '
            f'parent_id={self.parent_id}'
            ')'
        )
    
    @classmethod
    def create(
        cls,
        name: str,
        module: ModuleType,
        message: str,
    ) -> Self:
        migration_id = create_migration_id()
        created_at = datetime.now(tz=UTC)
        return cls(
            id=migration_id,
            module=module,
            name=name,
            created_at=created_at,
            message=message,
        )
    
    @classmethod
    def from_meta_data(
        cls,
        module: ModuleType,
        meta_data: dict[str, str],
    ) -> Self:
        id = MigrationId(meta_data['current_id'])
        name = meta_data['name']
        created_at = datetime.fromisoformat(meta_data['created_at'])
        message = meta_data['message']
        
        if meta_data.get('parent_id'):
            parent_id = MigrationId(meta_data['parent_id'])
        else:
            parent_id = None
        
        return cls(
            id=id,
            name=name,
            module=module,
            parent_id=parent_id,
            created_at=created_at,
            message=message,
        )
    
    def set_parent_id(self, parent_id: MigrationId) -> None:
        self.parent_id = parent_id


class Migrations:
    def __init__(
        self,
        migrations: list[Migration],
    ) -> None:
        self._list_migrations = migrations
    
    def get_by_offset(
        self,
        current_id: MigrationId,
        offset: int,
    ) -> Migration | None:
        index = 0
        while True:
            migration = self._list_migrations[index]
            if migration.id == current_id:
                break
            
            index += 1
        
        return self._list_migrations[index + offset]
    
    def get_by_id(self, migration_id: MigrationId) -> Migration | None:
        for migration in self._list_migrations:
            if migration.id == migration_id:
                return migration
        return None
    
    def append(self, migration: Migration) -> None:
        self._list_migrations.append(migration)
