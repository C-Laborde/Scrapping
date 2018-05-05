from requests import get
# from contextlib import closing
from requests.exceptions import RequestException

from aux_func.is_good_response import is_good_response
from aux_func.log_error import log_error


def simple_get(url):
    """
    Attempts to get the content at url by making an HTTP GET request. If the
    content-type of response is some kind of HTML/XML, return the text content,
    otherwise return None
    """

    try:
        # with closing(get(url, stream=True)) as resp:
        resp = get(url)
        if is_good_response(resp):
            print("Page status code: %s Download correct" % resp.status_code)
            return resp.content
        else:
            return None

    except RequestException as e:
        log_error("Error during requests to {0} : {1}".format(url, str(e)))
        return None
