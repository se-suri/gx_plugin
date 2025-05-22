from pathlib import Path
import importlib

__all__ = []

for path in Path(__file__).parent.glob("expect_*.py"):
    module_name = path.stem
    if module_name != "__init__":
        module = importlib.import_module(f".{module_name}", package=__name__)
        globals()[module_name] = module
        __all__.append(module_name)