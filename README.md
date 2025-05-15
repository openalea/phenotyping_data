# phenotyping_data : Data from plant phenotyping platform primarly aimed at desmonstrating/testing opeanalea phenotyping packages


## usage

    from openalea.phenotyping_data.fetch import get_data, list_data
    list_data()
    path = get_data('plant_1/raw/side/0.png')

## update registry
    
    python -c "import pooch; pooch.make_registry('data', 'src/openalea/phenotyping_data/registry.txt')"