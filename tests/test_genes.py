from __future__ import unicode_literals
from __future__ import print_function

import random
import sys
import unittest

from genetics.base import Gene
from test_data import *


class TestGenes(unittest.TestCase):

    def setUp(self):
        random.seed(rand_seed)

    def tearDown(self):
        pass

    def test_assert_traits(self):
        self.assertIn('action', a.alleles)
        self.assertIn('wicked', b.alleles)
        self.assertIn('wind', c.alleles)
        self.assertIn('yin', d.alleles)
        self.assertIn('natives', e.alleles)
        self.assertIn('vbo', f.alleles)
        self.assertIn(True, coin.alleles)

    def test_mutate(self):
        a.mutate()
        b.mutate()
        '''
        print('\n', file=sys.stderr)
        print(a, file=sys.stderr) 
        print(b, file=sys.stderr) 
        '''
        self.assertEqual('protection', a.trait)
        self.assertEqual('malice', b.trait)
        
