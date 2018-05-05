def is_good_response(resp):
    """
    Return true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)
