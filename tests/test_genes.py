from __future__ import unicode_literals
from __future__ import print_function

import unittest
import random
from base import Gene


class TestGenes(unittest.TestCase):
    a = Gene( traits=set(['action', 'inaction', 'protection', 
                            'procrastination']))
    b = Gene( traits=set(['love', 'hate', 'kindness', 'malice', 'wicked']))
    c = Gene( traits=set(['fire', 'water', 'earth', 'wind']))
    d = Gene( traits=set([ 'yin', 'yang' ]))
    e = Gene( traits=set([ 'syntax', 'value', 'dependency', 'linker',
                            'segfault', 'natives', 'internal', 'primitives' ]))
    f = Gene( traits=set([ 'render', 'shader', 'particle', 'buffer', 
                                'stencil', 'vbo', 'vertext', 'mesh', 'screen' ]))
    Genes = [a, b, c, d, e, f] 

    coin = Gene(traits={True, False})
    rand_seed = 5

    def setUp(self):
        random.seed(self.rand_seed)

    def tearDown(self):
        pass

    def test_assert_traits(self):
        self.assertIn('action', self.a)
        self.assertIn('wicked', self.b)
        self.assertIn('wind', self.c)
        self.assertIn('yin', self.d)
        self.assertIn('natives', self.e)
        self.assertIn('vbo', self.f)
        
