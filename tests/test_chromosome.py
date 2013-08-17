from __future__ import unicode_literals
from __future__ import print_function

import random
from sys import stderr
import unittest

from genetics.base import Gene, Chromosome
from test_data import *

class TestChromosomes(unittest.TestCase):

    def setUp(self):
        random.seed(rand_seed)

    def tearDown(self):
        pass


    def test_mutate(self):
        print(C, file=stderr)
        C.mutate(0.5)
        print('mutated: {}'.format(C), file=stderr)
    
