from openalea.phenotyping_data.fetch import fetch_data, list_data


def test_list_data():
    l = list_data()
    assert len(l) > 0
    l = list_data('plant_6')
    assert len(l) == 43


def test_fetch():
    path = fetch_data('plant_1/raw/side/0.png')
    assert path.exists()
    assert path.stat().st_size > 0
