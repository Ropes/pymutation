#!/usr/bin/python

from base import *
from copy import deepcopy
from random import choice


class Population(object):
    def __init__(self):
        self.entities = []

    def crossover(self):
        prob = 5.0
        pass

    def mutation(self):
        prob = 5.0
        pass

    def selection(self):
        #Pick the best, mate them
        #Pick top 60%
        pass

if __name__ == '__main__':
    a = Gene('x', traits=set(['action', 'inaction', 'protection', 
                                'procrastination']))
    b = Gene('y', traits=set(['love', 'hate', 'kindness', 'malice', 'wicked']))
    c = Gene('z', traits=set(['fire', 'water', 'earth', 'wind']))
    d = Gene('j', traits=set([ 'yin', 'yang' ]))
    e = Gene('k', traits=set([ 'syntax', 'value', 'dependency', 'linker',
                                'segfault', 'natives', 'internal' ]))
    f = Gene('l', traits=set([ 'render', 'shader', 'particle', 'buffer', 
                                'stencil', 'vbo', 'vertext', 'mesh', 'screen' ]))

    def get_genes():
        x = deepcopy(a) 
        y = deepcopy(b) 
        z = deepcopy(c)
        j = deepcopy(d)
        k = deepcopy(e)
        l = deepcopy(f)
        j.trait = choice(list(j.possible_traits))
        k.trait = choice(list(k.possible_traits))
        l.trait = choice(list(l.possible_traits))
        x.trait = choice(list(x.possible_traits))
        y.trait = choice(list(y.possible_traits))
        z.trait = choice(list(z.possible_traits))
        return {'x': x, 'y': y, 'z': z, 'j': j, 'k': k, 'l': l}

    '''
    x = deepcopy(a) 
    y = deepcopy(b) 
    z = deepcopy(c)
    j = deepcopy(d)
    k = deepcopy(e)
    l = deepcopy(f)
    j.trait = 'yin'
    k.trait = 'segfault'
    l.trait = 'vbo'
    x.trait = 'action'
    y.trait = 'love'
    z.trait = 'fire'
    
    X = deepcopy(a) 
    Y = deepcopy(b) 
    Z = deepcopy(c)
    J = deepcopy(d)
    K = deepcopy(e)
    L = deepcopy(f)
    J.trait = 'yang'
    K.trait = 'syntax'
    L.trait = 'shader'
    X.trait = 'inaction'
    Y.trait = 'hate'
    Z.trait = 'earth'

    genes = {'x': x, 'y': y, 'z': z, 'j': j, 'k': k, 'l': l}
    gy = {'x': X, 'y': Y, 'z': Z, 'j': J, 'k': K, 'l': L}

    c = Chromosome(genes)
    d = Chromosome(gy)

    def len_eval(genes):
        i = 0
        for k,v in genes.items():
            print v.trait
            i += len(v.trait)
        return i

    ia = Individual(len_eval, c)
    ib = Individual(len_eval, d)

    i = 0
    print ia
    print ib

    print '============================================================'
    ic = Individual( ia.mate(ib), len_eval )
    print
    print 'ic'
    print ic
    ''' 

    for x in range(0, 10):
        genes = get_genes()
        print genes
        for k,v in genes.items():
            print k,v
