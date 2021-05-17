import unittest
from app.parsing import get_img


def is_img_nice(img):
    return True


class ImgTest(unittest.TestCase):
    def test_img(self):
        self.assertTrue(is_img_nice(get_img()))
