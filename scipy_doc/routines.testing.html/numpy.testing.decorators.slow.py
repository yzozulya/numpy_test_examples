from unittest import TestCase
import numpy


class Test(TestCase):
    pass

numpy.testing.decorators.slow(Test)