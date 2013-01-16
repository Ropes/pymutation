#!/usr/bin/python
from random import choice

class Gene(object):
    def __init__(self, key, trait, traits,):
        self.key = key
        self.trait = trait
        self.possible_traits = traits

    def __str__(self):
        return '{}::{} {})'.format(self.key, self.trait,
                                    self.possible_traits)
    
    def mutate(self):
        self.trait = choice(list(self.possible_traits))


class Chromosome(object):
    def __init__(self, Genes):
        self.genes = Genes

    def __str__(self):
        x = self.__repr__() + '\n'
        for k,v in self.genes.items():
            x += k.ljust(5) + str(v) + '\n'
        return x

    def mutate(self, prob, gene2):
        pass


    def cross(self, prob, gene2):
        pass

    def split(self, percentage_point):
        x = int(len(self.genes) * percentage_point)
        print x
        i = 0
        a = {}
        b = {}
        for k,v in self.genes.items():
           if i >= x:
               b[k] = v
           else:
               a[k] = v
           i += 1
        return (a, b)
        

class Lifeform(object):
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
    #print d
    #print c.split(0.4)

    g = Gene('x', 'active', frozenset(('active', 'inactive', 'dead')))
    print g
    print g.possible_traits
    g.mutate()
    print g


