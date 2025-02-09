from pathlib import Path


def exists_file(path: Path) -> None:
    if path.exists():
        raise FileExistsError(path)


class InitAnser:
    def __init__(self, current_path: Path) -> None:
        self._current_path = current_path
    
    def _create_file(self, path: Path) -> None:
        exists_file(path)
        path.open('x').close()
    
    def _build_anser_directory_path(self) -> Path:
        path = self._current_path / 'anser'
        return path
    
    def _create_anser_directory(self) -> None:
        path = self._build_anser_directory_path()
        self._create_file(path)
    
    def _create_config_file(self) -> None:
        path = self._current_path / 'anser.toml'
        self._create_file(path)
    
    def _create_migrations_directory(self) -> None:
        path = self._build_anser_directory_path()
        
        migrations_directory_path = path / 'migrations'
        self._create_file(migrations_directory_path)
        
        init_file_path = migrations_directory_path / '__init__.py'
        self._create_file(migrations_directory_path)
    
    def _create_template_file(self) -> None:
        path = self._build_anser_directory_path()
        template_file_path = path / 'template.py.j2'
        self._create_file(template_file_path)
    
    def execute(self) -> None:
        self._create_config_file()
        self._create_anser_directory()
        self._create_migrations_directory()
        self._create_template_file()
