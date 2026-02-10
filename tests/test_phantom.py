import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from nullsec_phantom_id.core import DeviceProfiler

class TestProfiler(unittest.TestCase):
    def test_profile(self):
        p=DeviceProfiler()
        r=p.get_profile("windows10")
        self.assertEqual(r["ttl"],128)
    def test_detect(self):
        p=DeviceProfiler()
        self.assertEqual(p.detect_os(128,65535),"Windows")
        self.assertEqual(p.detect_os(64,29200),"Linux")
    def test_phantom(self):
        p=DeviceProfiler()
        r=p.generate_phantom("iphone")
        self.assertTrue(r["phantom"])
        self.assertEqual(r["os"],"iOS")

if __name__=="__main__": unittest.main()
