from __future__ import unicode_literals
from __future__ import print_function

from copy import deepcopy
import random
from sys import stderr
import unittest

from genetics.base import Gene, Chromosome, Individual
from test_data import *

class TestIndividual(unittest.TestCase):
   
    def setUp(self):
        #random.seed(rand_seed)
        random.seed(8)


    def test_mate(self):
        C2 = deepcopy(C)
        C2.mutate(0.5)
        i0 = Individual(C, len_eval) 
        i1 = Individual(C2, len_eval)
        print('i0:{}'.format(i0), file=stderr)
        print('i1:{}'.format(i1), file=stderr)
        print('', file=stderr)
        
        i2 = i0.mate(i1, 0.5)
        print('i2:{}'.format(i2), file=stderr)
        
