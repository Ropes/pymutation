#!/usr/bin/python

from base import *

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
    x = Gene('x', 'action', set(['action', 'inaction', 'protection']))
    y = Gene('y', 'love', set(['love', 'hate', 'kindness', 'malice']))
    z = Gene('z', 'fire', set(['fire', 'water', 'earth', 'wind']))
    
    X = Gene('x', 'inaction', set(['action', 'inaction', 'protection']))
    Y = Gene('y', 'hate', set(['love', 'hate', 'kindness', 'malice']))
    Z = Gene('z', 'earth', set(['fire', 'water', 'earth', 'wind']))
    
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

    print 'len test:', len_eval(gy)

    ia = Individual(len_eval, c)
    ib = Individual(len_eval, d)
    
    print c
    print d

    x = c.crossover(0.5, d)
    print x



