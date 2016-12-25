import unittest
import cv2
from src.hero_detector import HeroDetector

class HeroDetectorTest(unittest.TestCase):
  def test_constructor(self):
    original = cv2.imread('sample-screenshots/full-teams.jpg')
    detector = HeroDetector(original)
    self.assertEqual(2560, detector.original_w)
    self.assertEqual(1440, detector.original_h)
    self.assertEqual(720, detector.mid_height)

  def test_is_red_team(self):
    original = cv2.imread('sample-screenshots/full-teams.jpg')
    detector = HeroDetector(original)
    self.assertTrue(detector.is_red_team(400))
    self.assertFalse(detector.is_red_team(900))
