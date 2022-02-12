from datetime import datetime, timedelta


class Config(object):

    # Bucket configuration
    BUCKET = 's3://era5-atlantic-northeast/netcdf/single-levels-hq-ensemble/day'
    CLIENT_KWARGS = {'endpoint_url': 'https://s3.us-east-2.wasabisys.com',
                     'region_name': 'us-east-2'}
    CONFIG_KWARGS = {'max_pool_connections': 30}
    PROFILE = 'default'

    STORAGE_OPTIONS = {'profile': PROFILE,
                       'client_kwargs': CLIENT_KWARGS,
                       'config_kwargs': CONFIG_KWARGS
                       }

    # Dataset
    START_DATE = "1979-01-01"
    END_DATE = (datetime.utcnow() - timedelta(days=5)).strftime('%Y-%m-%d')

    VARIABLES = {
                 'precipitation_type':'ptype',
                 'snow_depth': 'sd',
                 'snowfall': 'sf',
                 '2m_temperature': 't2m',
                 'total_precipitation': 'tp'}

    TIMES = ['00:00', '03:00', '06:00',
            '09:00', '12:00', '15:00',
            '18:00', '21:00']