#!/usr/bin/env python3

import sys
import requests

def request_status(srv):
    try:
        response =requests.get(srv)
    except Exception as e:
        return(str(e))
    else:
        return(response.status_code)

resp_code=request_status(sys.argv[1])

if resp_code==200:
    print('Success! {}'.format(resp_code))
else:
    print('Faild. {}'.format(resp_code))
    sys.exit(1)
