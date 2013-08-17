from __future__ import unicode_literals
from __future__ import print_function

from genetics.base import Gene, Chromosome
import random

rand_seed = 5
random.seed(rand_seed)

a = Gene( traits=set(['action', 'inaction', 'protection', 
                        'procrastination']))
b = Gene( traits=set(['love', 'hate', 'kindness', 'malice', 'wicked']))
c = Gene( traits=set(['fire', 'water', 'earth', 'wind']))
d = Gene( traits=set([ 'yin', 'yang' ]))
e = Gene( traits=set([ 'syntax', 'value', 'dependency', 'linker',
                        'segfault', 'natives', 'internal', 'primitives' ]))
f = Gene( traits=set([ 'render', 'shader', 'particle', 'buffer', 
                            'stencil', 'vbo', 'vertext', 'mesh', 'screen' ]))
genes = [a, b, c, d, e, f] 

coin = Gene(traits={True, False})

C = Chromosome(genes)

