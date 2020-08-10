import pandas as pd
from src.preprocess import load_fromweb


def test_load_fromweb_URL_iscorrect(monkeypatch):
    datestring = '2019-05-27'
    url = (
        "https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv"
        + "?query=select * where `requested_datetime` >= '2019-05-27' "
        + "AND `service_name` = 'Street and Sidewalk Cleaning'"
        + "&accessType=DOWNLOAD"
    )

    def mock_read_csv(*args, **kwargs):
        # first argument should be the URL
        return args[0]
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)
    mock_url = load_fromweb(datestring)
    assert mock_url == url
