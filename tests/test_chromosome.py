from __future__ import unicode_literals
from __future__ import print_function

from copy import deepcopy
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
    
    def test_cross(self):
        #print('{}'.format(C), file=stderr)
        C2 = deepcopy(C)
        C2.mutate(0.5)
        #print('MutatedC2:{}'.format(C2), file=stderr)
        #print('C:{}'.format(C), file=stderr)

        #Chromosomes set for crossover test
        C3 = C2.crossover(C, 0.4)

        #print('C3:{}'.format(C), file=stderr)
        self.assertEqual(C3.genes[0].trait, 'inaction')
        self.assertEqual(C3.genes[1].trait, 'love')
        self.assertEqual(C3.genes[2].trait, 'fire')

        self.assertEqual(C3.genes[3].trait, 'yang')
        self.assertEqual(C3.genes[4].trait, 'internal')
        self.assertEqual(C3.genes[5].trait, 'mesh')

