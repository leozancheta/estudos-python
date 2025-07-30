async def request_adapter(request, user):
    """Adapt Flask request to a generic HTTP request format.
    This function extracts relevant data from a Flask request object
    and returns it in a standardized format.
    """
    body = None
    try:
        body = request.json
    except Exception as e:
        body = {}

    headers = dict(request.headers)
    query_params = request.args
    path_params = {'user': user
                   }
    return {
        "header": headers,
        "body": body,
        "query_params": query_params,
        "path_params": path_params
    }