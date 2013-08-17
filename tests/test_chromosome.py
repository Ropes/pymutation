from __future__ import unicode_literals
from __future__ import print_function

import random
from sys import stderr
import unittest

from genetics.base import Gene, Chromosome
from test_data import *

class TestChromosomes(unittest.TestCase):

    def setUp(self):
        #random.seed(rand_seed)
        random.seed(8)

    def tearDown(self):
        pass


    def test_mutate(self):
        #print(C.genes[1], file=stderr)
        #print('pre mutation {}'.format(C), file=stderr)
        self.assertEqual(C.genes[1].trait, 'malice')
        self.assertEqual(C.genes[3].trait, 'yang')
        C.mutate(0.5)
        #print('mutated: {}'.format(C), file=stderr)

        self.assertEqual(C.genes[1].trait, 'hate')
        self.assertEqual(C.genes[3].trait, 'yang')
    
