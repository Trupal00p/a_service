def report_credit():
    """ redirect ACPE request """
    import json
    import urllib2

    data = json.loads(request.body.read())

    url = data.get('url')
    auth_token = data.get('auth_token')

    if url and auth_token=="SUPERDUPERLONGAUTHTOKEN":

        response = urllib2.urlopen(url)

        json_string = response.read()

    else:

        json_string = json.dumps({'errors':'Missing Data For ACPE Request.'})


    return json_string
