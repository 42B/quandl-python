try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from quandl.api_config import ApiConfig


class RequestType(object):
    MAX_URL_LENGTH_FOR_GET = 8000  # Most webservers have a maximum get request url length of 8000 characters
    USE_GET_REQUEST = True  # This is used to simplify testing code

    @classmethod
    def get_request_type(cls, url, **params):
        query_string = urlencode(params['params'])
        request_url = '%s/%s/%s' % (ApiConfig.api_base, url, query_string)
        if RequestType.USE_GET_REQUEST and (len(request_url) < cls.MAX_URL_LENGTH_FOR_GET):
            return 'get'
        else:
            return 'post'
