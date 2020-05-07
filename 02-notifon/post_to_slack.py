# -*- coding: utf-8 -*-

import requests

url = '' # REPLACE WITH SLACK WEBHOOK

data = {'text': 'Hello, World'}
requests.post(url, json=data)
