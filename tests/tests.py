import youplay
import unittest

class YouPlayTest(unittest.TestCase):

    def test_no_artist_no_track(self):
        # https://www.youtube.com/watch?v=q_NspcNZjLM
        # Nirvana - Smells Like Teen Spirit
        (artists, tracks) = youplay.extract('q_NspcNZjLM')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/0b1zz')
        self.assertEqual(tracks[0].mid, '/m/0dt1wtv')
        return

    def test_no_artist_one_track(self):
        # Need more data
        return

    def test_no_artist_multiple_tracks(self):
        # Need more data
        return

    def test_one_artist_no_track(self):
        # https://www.youtube.com/watch?v=lidFipyLG8k
        # Jerry Lee Lewis - Great Balls of Fire
        (artists, tracks) = youplay.extract('lidFipyLG8k')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/0p7h7')
        self.assertEqual(tracks[0].mid, '/m/0ldg06')
        # https://www.youtube.com/watch?v=3y6oWTigBu0
        # Agnostic Front - Victim in Pain
        (artists, tracks) = youplay.extract('3y6oWTigBu0')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/022tqm')
        self.assertEqual(tracks[0].mid, '/m/0wwyj5')
        return
  
    def test_one_artist_one_track(self):
        # https://www.youtube.com/watch?v=c-_vFlDBB8A
        # Dropkick Murphys - Worker's Song
        (artists, tracks) = youplay.extract('c-_vFlDBB8A')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/02t3ln')
        self.assertEqual(tracks[0].mid, '/m/0qgggv')
        # https://www.youtube.com/watch?v=pAOQkSFTKMw
        # The Rolling Stones - Let's Spend the Night Together
        (artists, tracks) = youplay.extract('pAOQkSFTKMw')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/07mvp')
        self.assertEqual(tracks[0].mid, '/m/0rmqd9')
        return
      
    def test_one_artist_multiple_tracks(self):
        # Need more data
        return
      
    def test_multiple_artists_no_track(self):
        # https://www.youtube.com/watch?v=3fIqq5XVFKQ
        # Nirvana - Lithium
        (artists, tracks) = youplay.extract('3fIqq5XVFKQ')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/0b1zz')
        self.assertEqual(tracks[0].mid, '/m/0vwkfq')
        # https://www.youtube.com/watch?v=6W_joHLBr5k
        # Blondie - Atomic
        (artists, tracks) = youplay.extract('6W_joHLBr5k')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/017lb_')
        self.assertEqual(tracks[0].mid, '/m/0_k5sk')
        return

    def test_multiple_artists_one_track(self):
        # https://www.youtube.com/watch?v=zYxkezUr8MQ
        # Nirvana - Smells Like Teen Spirit
        (artists, tracks) = youplay.extract('zYxkezUr8MQ')
        self.assertEqual(len(artists), 1)
        self.assertEqual(len(tracks), 1)
        self.assertEqual(artists[0].mid, '/m/0b1zz')
        self.assertEqual(tracks[0].mid, '/m/0nft9n')
        # https://www.youtube.com/watch?v=0UjsXo9l6I8
        # Jay-Z and Alicia Keys - Empire State of Mind
        (artists, tracks) = youplay.extract('0UjsXo9l6I8')
        self.assertEqual(len(artists), 2)
        self.assertEqual(len(tracks), 1)
        self.assertTrue('/m/01vw20h' in [a.mid for a in artists])
        self.assertTrue('/m/0g824' in [a.mid for a in artists])
        self.assertEqual(tracks[0].mid, '/m/0fvh4xz')
        # https://www.youtube.com/watch?v=sp7PBrYXD6c
        # RHCP and Snoop Dogg - Scar Tissue
        (artists, tracks) = youplay.extract('sp7PBrYXD6c')
        self.assertEqual(len(artists), 2)
        self.assertEqual(len(tracks), 1)
        self.assertTrue('/m/06mj4' in [a.mid for a in artists])
        self.assertTrue('/m/01vw8mh' in [a.mid for a in artists])
        self.assertEqual(tracks[0].mid, '/m/0tw82f')
        return

    def test_multiple_artists_multiple_tracks(self):
        # Need more data
        return

if __name__ == '__main__':
    unittest.main()