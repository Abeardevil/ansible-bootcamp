#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

def main():

  module = AnsibleModule(
    argument_spec = dict(
      question = dict(required=True),
    )
  )

  question = module.params['question']

  apiURL   = 'https://8ball.delegator.com/magic/JSON/'
  apiURL   = apiURL + question

  response = open_url(apiURL, method='GET', http_agent = "this_sucks")

  body = json.loads(response.read())

  magic_answer = body['magic']['answer']
  magic_type   = body['magic']['type']

  if (magic_type == 'Contrary'):
    failed = True
  else:
    failed = False

  module.exit_json(failed = failed, changed=False, question=question, answer=magic_answer, type=magic_type)

if __name__ == '__main__':
  main()
