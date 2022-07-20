def build_url(url, params):
    if params:
        url += "?" + "&".join([f"{k}={v}" for k, v in params.items()])
    return url