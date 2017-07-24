"""
    Azure Functions HTTP Helper for Python
    
    Created by Anthony Eden
    http://MediaRealm.com.au/
"""

import os
import urlparse


class HTTPHelper(object):
    
    def __init__(self):
        self._headers = {}
        self._query = {}
        self._env = {}
        
        for x in os.environ:
            if x[:12] == "REQ_HEADERS_":
                self._headers[x[12:].lower()] = os.environ[x]
            
            elif x[:10] == "REQ_QUERY_":
                self._query[x[10:].lower()] = os.environ[x]
            
            else:
                self._env[x.lower()] = str(os.environ[x])
    
    @property
    def headers(self):
        return self._headers
    
    @property
    def get(self):
        return self._query
    
    @property
    def env(self):
        return self._env
    
    @property
    def post(self):
        postData = open(os.environ['req'], "r").read()
        postDataParsed = urlparse.parse_qs(postData)
        return postDataParsed