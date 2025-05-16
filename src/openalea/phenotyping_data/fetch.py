from pathlib import Path
from importlib.resources import files, as_file
import pooch

REGISTRY = files('openalea.phenotyping_data') / 'registry.txt'
BASE_URL = "https://raw.githubusercontent.com/openalea/phenotyping_data/main/data/"
POOCH = pooch.create(
    path=pooch.os_cache("phenotyping_data"),
    base_url=BASE_URL,
    version_dev="main",
    # We'll load it from a file later
    registry=None,
)
with as_file(REGISTRY) as registry_path:
    POOCH.load_registry(registry_path)


def fetch_data(filename):
    return POOCH.fetch(filename)


def list_data(prefix=""):
    return [name for name in POOCH.registry if name.startswith(prefix)]

    
def fetch_all_data(prefix=""):
    for filename in list_data(prefix):
        fetch_data(filename)
        
    data_dir = Path(str(POOCH.abspath)) / prefix
    
    return data_dir

