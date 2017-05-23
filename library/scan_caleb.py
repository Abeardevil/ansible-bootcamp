#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

def main():
    module = AnsibleModule(
        argument_spec = dict(
            latitude = dict(required=True),
            longitude = dict(required=True),
    ))

    api_key = '7f7bbf445ea4401fe20e962cec3c1cd1'

    apiURL  = 'https://api.darksky.net/forecast/' + api_key + '/' + module.params['latitude'] + ',' + module.params['longitude']

    response = open_url(apiURL, method='GET', http_agent = 'this_sucks')

    body = json.loads(response.read())

    results = dict(ansible_facts=body['daily'])
    module.exit_json(**results)

main()
