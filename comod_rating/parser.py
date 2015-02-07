"""
Must define three methods:

* answer_pattern(pattern, args)
* render_answer_html(answer_data)
* render_answer_json(answer_data)
"""
from .patterns import PATTERNS

import json
import requests
from django.template import loader, Context
from random import Random

#####
#API key
def get_api_key():
    key = "38ea9c3c78f3407189201e33ab2be446"
    return key


def vote_search(topic):
    url = 'https://congress.api.sunlightfoundation.com/votes?apikey=%s&query=%s' % (get_api_key(), topic)
    resp = requests.get(url)
    return resp.json()

############################################################
# Pattern-dependent behavior
def answer_pattern(pattern, args):
    """
    Returns a `dict` representing the answer to the given
    pattern & pattern args.

    'plaintxt' should always be a returned field

    """
    if pattern not in PATTERNS:
      return None
    
    if pattern in PATTERNS:
      topic = args[0]
      return {
        'type': 'vote',
        'data': vote_search(topic)
      }

############################################################
# Applicable module-wide
#def render_answer_html(answer_data):
#    template = loader.get_template('comod_rating/example.html')
#    return template.render(Context(answer_data))

def render_answer_html(answer_data):
   # This receives what we got in `answer_pattern` and returns HTML.
    if answer_data and answer_data.get('type', None) == "vote":
        data = answer_data['data']
        template = loader.get_template('comod_rating/results.html')
        return template.render(Context(data))
    else:
    # TODO: render a template for "we don't know how to handle this search
        raise Exception

def render_answer_json(answer_data):
    return json.dumps(answer_data)
