from .client import AbstractOrder, AbstractOrderLine, Client
VERSION = (0, 3, 2)


def get_version():
    return '.'.join(map(str, VERSION))

__version__ = get_version()

