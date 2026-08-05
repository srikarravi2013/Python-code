import importlib
import pkgutil
import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Type, Any


class BaseHandler(ABC):
    """Abstract Base Class that all file handlers must inherit from."""

    # Define the target extensions in child classes (e.g., [".jpg", ".jpeg"])
    supported_extensions: list[str] = []

    @abstractmethod
    def analyze(self, path: Path) -> Dict[str, Any]:
        """Extract and return metadata specific to this format."""
        pass


class HandlerRegistry:
    """Central registry for mapping file extensions to analysis handlers."""

    def __init__(self):
        self._registry: Dict[str, Type[BaseHandler]] = {}

    def register(self, handler_cls: Type[BaseHandler]) -> None:
        """Register a handler for its supported extensions."""
        for ext in handler_cls.supported_extensions:
            ext_clean = ext.lower()
            if not ext_clean.startswith("."):
                ext_clean = f".{ext_clean}"
            self._registry[ext_clean] = handler_cls

    def get_handler(self, extension: str) -> BaseHandler:
        """Retrieve an initialized handler for the given extension, if present."""
        handler_cls = self._registry.get(extension.lower())
        return handler_cls() if handler_cls else None

    def load_builtins(self, package_path: str, package_name: str) -> None:
        """Auto-discover and register handlers inside internal modules."""
        for _, module_name, _ in pkgutil.iter_modules([package_path]):
            full_module_name = f"{package_name}.{module_name}"
            module = importlib.import_module(full_module_name)
            self._register_from_module(module)

    def load_external_plugins(self, plugin_dir: Path) -> None:
        """Dynamically load drop-in python plugins from an external directory."""
        if not plugin_dir.exists() or not plugin_dir.is_dir():
            return

        sys.path.insert(0, str(plugin_dir.resolve()))
        for file in plugin_dir.glob("*.py"):
            if file.name.startswith("__"):
                continue
            module_name = file.stem
            module = importlib.import_module(module_name)
            self._register_from_module(module)

    def _register_from_module(self, module) -> None:
        """Inspect a module for subclasses of BaseHandler and register them."""
        for obj in module.__dict__.values():
            if (
                isinstance(obj, type)
                and issubclass(obj, BaseHandler)
                and obj is not BaseHandler
            ):
                self.register(obj)


# Global registry instance
registry = HandlerRegistry()