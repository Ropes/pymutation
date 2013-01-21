#!/usr/bin/python

from base import *
from copy import deepcopy

class Being(object):
    def __init__(self, chrom_list=None, gen_chrom=None):
        #TODO: Create a list of random chromosomes if none provided and generation func provided 
        pass

    def f(self):
        '''Evaluate fitness of the population'''
        pass

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
    a = Gene('x', traits=set(['action', 'inaction', 'protection']))
    b = Gene('y', traits=set(['love', 'hate', 'kindness', 'malice']))
    c = Gene('z', traits=set(['fire', 'water', 'earth', 'wind']))

    x = deepcopy(a) 
    y = deepcopy(b) 
    z = deepcopy(c)
    x.trait = 'action'
    y.trait = 'love'
    z.trait = 'fire'
    
    X = deepcopy(a) 
    Y = deepcopy(b) 
    Z = deepcopy(c)
    X.trait = 'inaction'
    Y.trait = 'hate'
    Z.trait = 'earth'

    
    genes = {'x': x, 'y': y, 'z': z}
    gy = {'x': X, 'y': Y, 'z': Z}

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
    print ia
    print ib

    print
    
    print c
    print d

    x = c.crossover(0.5, d)
    print x



