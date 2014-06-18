import json
import os

import requests

from __init__ import YouPlay, YOUPLAY_GOOGLE_KEY, ENVIRON

FREEBASE_MQL = 'https://www.googleapis.com/freebase/v1/mqlread'
COVER_MID = 'm/014_42'

class Entity(YouPlay):
    
    def __init__(self, mid, name=None, types=[], lookup=True):
        self.mid = mid
        self.name = name
        self.types = types
        self.set_api_key()
        if lookup:
            self._lookup()
    
    def __eq__(self, other):
        return isinstance(other, Entity) and self.mid == other.mid

    def __str__(self):
        return "%s [%s]" %(self.name, self.mid)
    __repr__ = __str__

    def jsonify(self):
        return {
            'mid' : self.mid,
            'name' : self.name
        }

    def _get_data(self, properties=None, relations=None):
        """Get entity data from Freebase, either values or relations."""
        assert properties or relations
        properties = properties or []
        relations = relations or []
        # Base queries
        query = {
            "mid": self.mid
        }
        # Values to retrieve
        for property_ in properties:
            query.update({
                property_ : []
            })
        # FIXME - Add cursor
        for relation in relations:
           query.update({
                relation : [{
                    "mid": None,
                    "name": None,
                    "optional": "optional",
                    "type": [],
                    "limit": 1000
                }]
            })
        request = requests.get(FREEBASE_MQL, params={
            'query': json.dumps(query), 
            'key': self.api_key
        })
        if request.status_code == 200: 
            return request.json()['result']
        return {}

    def get_properties(self, properties):
        return self._get_data(properties=properties)

    def get_relations(self, relations, properties=None):
        data = self._get_data(relations=[relations])
        if data:
            return [Entity(d.get('mid'), d.get('name'), d.get('type'), False) for d in data[relations]]

    def _lookup(self):
        """Assign type and name of the entity via Freebase."""
        data = self.get_properties(['type', 'name'])
        self.name = data.get('name', [None])[0]
        self.types = data.get('type')
 
    def has_type(self, path):
        """Check if an entity has any of this topic in the given path."""
        for types in self.types:
            if path in types:
                return True
        return False

class Artist(Entity):
    def get_tracks(self):
        return self.get_relations('/music/artist/track', ['/music/recording/artist'])

class Recording(Entity):
    def get_artists(self):
        return self.get_relations('/music/recording/artist')
