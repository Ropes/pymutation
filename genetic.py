#!/usr/bin/python

from base import *
from copy import deepcopy
from random import choice


class Population(object):
    def __init__(self, size=5):
        self.size = size
        self.individuals = []

    def crossover(self):
        prob = 5.0
        pass

    def mutation(self):
        prob = 0.08
        for i in self.individuals:
            i.chromosome.mutate(prob)

    def selection(self):
        #Pick the best, mate them
        #Pick top 60%
        pass

if __name__ == '__main__':
    a = Gene( traits=set(['action', 'inaction', 'protection', 
                            'procrastination']))
    b = Gene( traits=set(['love', 'hate', 'kindness', 'malice', 'wicked']))
    c = Gene( traits=set(['fire', 'water', 'earth', 'wind']))
    d = Gene( traits=set([ 'yin', 'yang' ]))
    e = Gene( traits=set([ 'syntax', 'value', 'dependency', 'linker',
                            'segfault', 'natives', 'internal' ]))
    f = Gene( traits=set([ 'render', 'shader', 'particle', 'buffer', 
                                'stencil', 'vbo', 'vertext', 'mesh', 'screen' ]))
    Genes = [a, b, c, d, e, f] 
    def get_genes():
        gs = {}
        i = 0
        for g in Genes:
            x = deepcopy(g)
            x.trait = choice(list(x.possible_traits))
            gs[str(i)] = x
            i += 1

        return gs

    def len_eval(genes):
        i = 0
        for k,v in genes.items():
            #print v.trait
            i += len(v.trait)
        return i

    '''
    ia = Individual(len_eval, c)
    ib = Individual(len_eval, d)

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
        c = Chromosome(genes)
        i = Individual(c, len_eval)
        print i
        print x

