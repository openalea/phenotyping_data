import pooch

BASE_URL = "https://raw.githubusercontent.com/openalea/phenotyping_data/main/data/"

def get_data_file(filename):
    return pooch.retrieve(
        url=BASE_URL + filename,
        known_hash=None,  # Optionally add SHA256 hash
        fname=filename,
        path=pooch.os_cache("phenomenal-data"),
    )
