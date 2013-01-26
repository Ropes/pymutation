#!/usr/bin/python

from base import *
from copy import deepcopy


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

    x = deepcopy(a) 
    y = deepcopy(b) 
    z = deepcopy(c)
    j = deepcopy(d)
    k = deepcopy(e)
    l = deepcopy(f)
    x.trait = 'action'
    y.trait = 'love'
    z.trait = 'fire'
    j.trait = 'yin'
    k.trait = 'segfault'
    l.trait = 'vbo'
    
    X = deepcopy(a) 
    Y = deepcopy(b) 
    Z = deepcopy(c)
    J = deepcopy(d)
    K = deepcopy(e)
    L = deepcopy(f)
    X.trait = 'inaction'
    Y.trait = 'hate'
    Z.trait = 'earth'
    J.trait = 'yang'
    K.trait = 'syntax'
    L.trait = 'shader'

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
    while i < 10:
        i += 1
        print '============================================================'
        ic = ia.mate(ib)
        print
        print 'ic'
        print ic
     
