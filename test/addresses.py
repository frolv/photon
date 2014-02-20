import unittest

from test.base import PhotonImplementationTest, BERLIN


class Addresses(PhotonImplementationTest):
    def test_berlin_1(self):
        self.assertMatch("dircksenstr 51", {'osm_id': 1552576044})

    def test_berlin_2(self):
        self.assertMatch("Rosa-Luxemburg-Straße 22", {'osm_id': 736787797}, center=BERLIN)

    def test_au(self):
        self.assertMatch("Jaghausen 4", {'osm_id': 135405796})

    def test_paris(self):
        self.assertMatch("Boulevard Jourdan 95", {'osm_id': 1773529891})

    def test_stockholm(self):
        self.assertMatch("Källargränd 3", {'osm_id': 1815123244})

    def test_birmingham(self):
        self.assertMatch("9 Ivor Road Birmingham", {'osm_id': 144738133})


if __name__ == '__main__':
    unittest.main(verbosity=2)
