import subprocess
import importlib
import sys


def install_if_not(lib_name: str):
    try:
        importlib.import_module(lib_name)
    except ImportError:
        subprocess.run(f'{sys.executable} -m pip install --user {lib_name}')
