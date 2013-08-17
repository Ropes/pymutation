from __future__ import unicode_literals
from __future__ import print_function

import random
import sys
import unittest

from genetics.base import Gene, Chromosome

class TestChromosomes(unittest.TestCase):
    rand_seed = 5


    def setUp(self):
        random.seed(self.rand_seed)

    def tearDown(self):
        pass

    
