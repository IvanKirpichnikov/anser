import json
from datetime import datetime

from anser.entities.migration import MigrationId


CONFIG_SCHEMA = '''\
[anser]
url = ''

[anser.main.migrations]
path = '{path_to_migrations}'
'''

TEMPLATE_SCHEMA = '''\
from anser import AnserContext

current_id = {current_id}
parent_id = {parent_id}
message = {message}
created_at = {created_at}

def upgrade(context: AnserContext) -> None:
    pass

def downgrade(context: AnserContext) -> None:
    pass
'''


def create_config_schema(path_to_migrations: str) -> str:
    return CONFIG_SCHEMA.format(path_to_migrations=path_to_migrations)


def create_template_schema(
    current_id: MigrationId,
    created_at: datetime,
    message: str | None = None,
    parent_id: MigrationId | None = None,
) -> str:
    return TEMPLATE_SCHEMA.format(
        meta_data=json.dumps(
            {
                'current_id': current_id,
                'parent_id': parent_id,
                'created_at': created_at,
                'message': message,
            },
            indent=4,
        )
    )
