import os

import requests

from freebase import Entity, Recording, Artist
from __init__ import YouPlay, YOUPLAY_GOOGLE_KEY, ENVIRON

YOUTUBE_VIDEOS = 'https://www.googleapis.com/youtube/v3/videos'
YOUTUBE_SEARCH = 'https://www.googleapis.com/youtube/v3/search'

class Video(YouPlay):

    def __init__(self, yid, recurse=True):
        """The Video object. Built from a YouTube video ID"""
        self.yid = yid
        self.video = None
        self.title = None
        self.description = None
        self.artists = []
        self.tracks = []
        self._recurse = recurse
        self.set_api_key()
        
    def _add_entity(self, entity):
        """Add an entity in the list of tracks of artists, depending on its type"""
        if entity.has_type('/music/recording'):
            entity.__class__ = Recording
            self.tracks.append(entity)
        elif entity.has_type('/music/artist'):
            entity.__class__ = Artist
            self.artists.append(entity)

    def _related(self):
        """Find related videos"""
        # Do nothing if we're already into a loop
        if not self._recurse:
            return []
        request = requests.get(YOUTUBE_SEARCH, params={
            'relatedToVideoId': self.yid,
            'part':"id",
            'type': 'video',
            'maxResults' : 20,
            'key': self.api_key,
        })
        if request.status_code == 200:
            data = request.json()
            if data.get('items'):
                return [Video(video['id']['videoId'], False) for video in data['items']]
        return []
    
    def _lookup(self):
        """Lookup information about the video from the YouTube API"""
        request = requests.get(YOUTUBE_VIDEOS, params={
            'id': self.yid,
            'part':"id,snippet,topicDetails",
            'key': self.api_key
        })
        if request.status_code == 200: 
            data = request.json()
            if data.get('items'):
                # Assign video and title
                self.video = data['items'][0]
                if self.video.get('snippet'):
                    self.title = self.video['snippet'].get('title', '').lower().strip()
                    self.description = self.video['snippet'].get('description', '').lower()
                # Assign Freebase-related music topics
                if self.video.get('topicDetails'):
                    for mid in self.video['topicDetails'].get('topicIds', []):
                        self._add_entity(Entity(mid))
        return
        
    def _no_artist_no_track(self):
        # Don't try to extract anything from a non-music video, unless explicitely asked for
        if int(self.video['snippet'].get('categoryId', 0)) != 10:
            return
        related = {}
        for video in self._related():
            (artist, track) = video.get_music_data()
            if artist:
                key = artist.mid
                related.setdefault(key, {
                    'artist': artist,
                    'count': 0
                })
                related[key]['count'] += 1
        if not related:
            return
        sorted_ = sorted(related.values(), key=lambda x: x['count'], reverse=True)
        self.artists = sorted_[0:1]['artist']
        return self._one_artist_no_track()
        
    def _no_artist_one_track(self):
        self.tracks = self.tracks[0:1]
        self.artists = self.track.get_artists()
        return self._x_artists_one_track()
        
    def _no_artist_x_tracks(self):
        self.tracks = self.tracks[0:1]
        return
        
    def _one_artist_no_track(self):
        self.artists = self.artists[0:1]
        title = self.title.replace(self.artists[0].name.lower(), '')
        tracks = [t for t in self.artists[0].get_tracks() if t.name and t.name.lower() in title]
        if len(tracks) == 0:
            return
        elif len(tracks) == 1:
            self.tracks = _tracks[0:1]
        else:
            for type_ in ['/music/single', '/media_common/cataloged_instance']:
                _tracks = [t for t in tracks if type_ in t.types]
                if _tracks:
                    self.tracks = _tracks[0:1]
        return
        
    def _one_artist_one_track(self):
        self.artists = self.artists[0:1]
        self.tracks = self.tracks[0:1]
        return
        
    def _one_artist_x_tracks(self):
        self.artists = self.artists[0:1]
        return

    def _x_artists_no_track(self):
        artists = [a for a in self.artists if a.name and a.name.lower() in self.title]
        if len(artists) == 0:
            return
        if len(artists) == 1:
            self.artists = artists[0:1]
            return self._one_artist_no_track()
        return
        
    def _x_artists_one_track(self):
        self.tracks = self.tracks[0:1]
        artists = [a for a in self.tracks[0].get_artists() if a in self.artists]
        if len(artists) == 0:
            return self._no_artist_one_track()
        elif len(artists) == 1:
            self.artists = artists[0:1]
            return self._one_artist_one_track()
        return
        
    def _x_artists_x_tracks(self):
        return
        
    def _apply_heuristics(self):
        """Apply a set of heuristics to identify the correct (artist, track) combo"""
        num_artists, num_tracks = (len(self.artists), len(self.tracks))
        print (num_artists, num_tracks)
        if num_artists == 0:
            h = (num_tracks == 0 and self._no_artist_no_track) \
                      or (num_tracks == 1 and self._no_artist_one_track) \
                      or self._no_artst_x_tracks
        elif num_artists == 1:
            h = (num_tracks == 0 and self._one_artist_no_track) \
                      or (num_tracks == 1 and self._one_artist_one_track) \
                      or self._one_artst_x_tracks
        else:
            h = (num_tracks == 0 and self._x_artists_no_track) \
                      or (num_tracks == 1 and self._x_artists_one_track) \
                      or self._x_artists_x_tracks
        h()
        return
      
    def get_music_data(self):
        """Get artist and track for the video"""
        self._lookup()
        if self.video:
            self._apply_heuristics()
        return (self.artists, self.tracks)


