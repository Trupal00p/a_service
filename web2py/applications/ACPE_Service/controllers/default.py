import json
import urllib2

def report_credit():
    """ redirect ACPE request """

    try:
        data = json.loads(request.body.read())
    except:
        data = None

    if data:
        url = data.get('url')
        auth_token = data.get('auth_token')
    else:
        url = None
        auth_token = None

    if url and auth_token=="LqbOhYAFpz3TAz5S9%i2ZP%raVa^W%qSHGXH7#NpS4k5E%d$Dq":

        response = urllib2.urlopen(url)

        json_string = response.read()

    else:

        json_string = json.dumps(
            {
                "action":"I",
                "status":"Rejected",
                "error_message":" * Missing Data For ACPE Request.",
                "errors":[
                    {
                    "error_number":987,
                    "error_source":"LecturePanda",
                    "error_description":"Missing Data For ACPE Request."
                    }
                ]
            }
        )

    return json_string
