# phenotyping_data : Data from plant phenotyping platform primarly aimed at desmonstrating/testing opeanalea phenotyping packages


## usage

    from openalea.phenotyping_data.fetch import fetch_data, list_data, fetch_all_data
    list_data()
    path = fetch_data('plant_1/raw/side/0.png')
    datadir = fetch_all_data('plant_1/raw')

## update registry
    
    python -c "import pooch; pooch.make_registry('data', 'src/openalea/phenotyping_data/registry.txt')"