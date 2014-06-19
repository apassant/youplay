youplay
=======

Extract who's and what's playing - artist(s) and track(s) - from a YouTube music video

Usage
-----

    pip install youplay

This will install the python module and the youplay helper script

    youplay 0UjsXo9l6I8

or

    #!/usr/bin/env python

    import youplay

    (artists, tracks) = youplay.extract('0UjsXo9l6I8')
    print '%s - %s' %(', '.join([artist.name for artist in artists]), tracks[0].name)

    (artists, tracks) = youplay.extract('c-_vFlDBB8A')
    print '%s - %s' %(artists[0].name, tracks[0].name)

Note that your Google API key must be set as an environment variable: `YOUPLAY_GOOGLE_KEY`
If you don't have a key, register at [code.google.com/apis/console/](https://code.google.com/apis/console/)
and register for the YouTube Data API v3 and the Freebase API.

