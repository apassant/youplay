"""YouPlay - Extract who's and what's playing - artist(s) and track(s) - from a YouTube music video."""

# Author: Alexandre Passant - apassant.net
# (c) 2014 MDG Web Ltd. - mdg.io / seevl.fm
# Licensed: MIT - see LICENSE.txt

YOUPLAY_GOOGLE_KEY = 'YOUPLAY_GOOGLE_KEY'
ENVIRON = "You need to set-up your Google API key as %s environment variable" %(YOUPLAY_GOOGLE_KEY)

def extract(yid):
    from youtube import Video
    return Video(yid).get_music_data()


class YouPlay(object):
      
    def set_api_key(self):
        import os
        self.api_key = os.environ.get(YOUPLAY_GOOGLE_KEY)
        assert self.api_key, ENVIRON
