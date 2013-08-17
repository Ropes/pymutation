from genetics.base import Gene, Chromosome

rand_seed = 5
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
