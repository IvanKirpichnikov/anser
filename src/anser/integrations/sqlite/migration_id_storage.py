from sqlite3 import Connection
from typing import Final

from anser.config import AnserConfig
from anser.entities.migration import MigrationId
from anser.interfaces.migration_id_storage import MigrationIdStorage


CREATE_SQL: Final = '''
    CREATE TABLE __migration_anser__(
        migration_id TEXT NOT NULL
    );
'''
GET_MIGRATION_ID_SQL: Final = '''
    SELECT migration_id
    FROM __migration_anser__;
'''
SET_MIGRATION_ID_SQL: Final = '''
    UPDATE __migration_anser__
    SET migration_id = ?;
'''


class SqliteMigrationIdStorage(MigrationIdStorage):
    def __init__(
        self,
        config: AnserConfig,
        connection: Connection,
    ) -> None:
        self._config = config
        self._connection = connection
    
    def create(self) -> None:
        self._connection.execute(CREATE_SQL)
        self._connection.commit()
    
    def get(self) -> MigrationId | None:
        cursor = self._connection.cursor()
        cursor.execute(GET_MIGRATION_ID_SQL)
        data = cursor.fetchone()
        cursor.close()
        if data is None:
            return None
        return MigrationId(data[0])
    
    def set(
        self,
        migration_id: MigrationId,
    ) -> None:
        self._connection.execute(
            SET_MIGRATION_ID_SQL,
            (migration_id,)
        )
        self._connection.commit()
