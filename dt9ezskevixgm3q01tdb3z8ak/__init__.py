from importlib.metadata import version, PackageNotFoundError
from .dt9ezskevixgm3q01tdb3z8ak import dt9ezskevixgm3q01tdb3z8ak as _

try:
    __version__ = version("your_package_distribution_name")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
