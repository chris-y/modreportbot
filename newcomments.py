#!/usr/bin/python3

import requests
import json
import sys
import string
import matrix
from pythorhead import Lemmy
from pythorhead.types import SortType,ListingType

def run(lemmy, live, room, muser, mpw, mserver):
  try:
    comments = lemmy.comment.list(sort=SortType.New, type_=ListingType.Subscribed, limit=10)
  except Exception as e:
    print(f'cannot get subscribed comments: {e}\n')

  for c in commentss:
    if c["saved"] is True: # don't want to use thus but you can't get read status, also need to check if we're setting this already elsewhere
      break

    if live:
      # post to matrix
      mtxt = f"New comment: [{c['community']['name']}] {c['post']['name']}\n{c['comment']['content']}"
      matrix.post(mtxt, room, muser, mpw, mserver)

      try:
        lemmy.comment.mark_as_saved(c["comment"]["id"], True)
      except Exception as e:
        print(f'cannot mark as read: {e}\n')

  return
