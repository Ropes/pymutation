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
    g0 = {'x': 0, 'y': 1, 'z': 2, 'xx': 12, 'yy': 84, 'zz': 34}
    g1 = {'x': 5, 'y': 4, 'z': 9, 'xx': 43, 'yy': 193, 'zz': 81}
    c = Chromosome(g0)
    d = Chromosome(g1)

    x = Gene('x', 'action', set(['action', 'inaction', 'protection']))
    y = Gene('y', 'love', set(['love', 'hate', 'kindness',
                                'spite', 'malice', 'adoration']))
    z = Gene('z', 'fire', set(['fire', 'water', 'earth', 'wind']))

    genes = {'x': x, 'y': y, 'z': z}
    c = Chromosome(genes)
    print c
    c.mutate(0.30)
    print c
    c.mutate(0.30)
    print c
    c.mutate(0.30)
    print c




