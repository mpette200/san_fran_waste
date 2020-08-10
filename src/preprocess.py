import pandas as pd


def load_fromweb(datestring):
    '''Loads data from web api. Fetching data after specified date.

    Parameters
    -----------
    datestring : str
        Date in format YYYY-MM-DD

    Returns
    --------
    pandas.DataFrame
    '''
    url_template = (
        "https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv"
        + "?query=select * where `requested_datetime` >= '{date_str}' "
        + "AND `service_name` = 'Street and Sidewalk Cleaning'"
        + "&accessType=DOWNLOAD"
    )
    url = url_template.format(date_str=datestring)
    return pd.read_csv(url)
