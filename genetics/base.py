from __future__ import print_function
from __future__ import unicode_literals

import random
from sys import stderr
from pprint import pformat

class Gene(object):
    '''Each gene encodes a trait, for example color of eyes. 
    Possible settings for a trait (e.g. blue, brown) are called alleles.'''
    def __init__(self, trait=None, traits=None,):
        self.alleles = traits
        if trait:
            self.trait = trait
        else:
            self.mutate()

    def __str__(self):
        return '{} {}'.format(self.trait, pformat(self.alleles))
    
    def mutate(self):
        if hasattr(self, 'trait'):
            options = self.alleles - {self.trait}
            self.trait = random.choice(list(options))
        else:
            self.trait = random.choice(list(self.alleles))


class Chromosome(object):
    '''Chromosomes are strings of DNA and serves as a model for the whole
    organism. A chromosome consist of genes, blocks of DNA.'''

    def __init__(self, genes):
        '''genes: dictionary of Gene objects'''
        self.genes = {}
        if type(genes) is list:
            for idx, g in enumerate(genes):
                self.genes[idx] = g
        elif type(genes) is dict:
            self.genes = genes
        else:
            print('Unhandled gene initialization format.\n'+\
            'Required: list[Genes] or dict{trait:Gene}', file=stderr)
        assert self.genes

    def __str__(self):
        x = self.__repr__() + '\n'
        for k, v in self.genes.items():
            x += '  {}:{}\n'.format(k, v)
        return x

    def mutate(self, prob):
        '''Potentially mutate all the genes given a probability.
                prob: Float probability for genes to mutate
        '''
        for v in self.genes.values():
            rand = random.random()
            if prob >= rand:
                orig = v.trait
                v.mutate()
                #print('Mutated: {}, orig: {}'.format(v, orig), file=stderr)

    def crossover(self, chrom2, prob,):
        i = 0
        split = int(len(self.genes)*prob)
        #print('Split: {}'.format(split), file=stderr)
        crossed = {}
        for k,v in self.genes.items():
            if i <= split:
                crossed[k] = self.genes[k]
            else:
                crossed[k] = chrom2.genes[k] 
            #print('{} {}'.format(k, i <= split), file=stderr)
            i += 1

        return Chromosome(crossed)

    def swap(self, chrom2, prob):
        crossed = {} 
        for k,v in self.genes.items():
            i = random.random()
            if i >= prob:
                crossed[k] = self.genes[k]
                #print('chose self: {},{}, {}'.format(k, crossed[k], i), file=stderr)
            else:
                crossed[k] = chrom2.genes[k] 
                #print('chose mate: {},{}, {}'.format(k, crossed[k], i), file=stderr)
            i += 1

        return Chromosome(crossed)
        
        
    def split(self, percentage_point):
        x = int(len(self.genes) * percentage_point)
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

class Individual(object):
    def __init__(self, chrom, fitness_func=None):
        self.chromosome = chrom 
        self.eval_fitness = fitness_func 
        assert self.chromosome

    def __str__(self):
       
        x = 'Individual: \n'
        for k,v in self.chromosome.genes.items():
            x += '   {}  {}\n'.format(k, v.trait)
        x += 'Fitness: {}'.format(unicode(self.fitness))
        return x

    def mate(self, partner_chroms, exchange=0.5):

       return Individual(self.chromosome.swap(partner_chroms.chromosome, exchange),\
                            self.eval_fitness)
        

    def wat_mate(self, male):
        #TODO: Not exactly sure why this function became so complicated...
        '''Take current indevidual and mate them with another indevidual.
            Returns a Chromosome object to be inserted in new individual. 
        '''

        i = 0
        c = Chromosome(self.chromosome.genes)
        chosen = None
        for k,v in self.chromosome.genes.items():
            if i <= 0:
                i = int((len(male.chromosome.genes) * random.random())*0.4)+1
                if random.random() > 0.5: 
                    chosen = self
                else:
                    chosen = male
                c.genes[k].trait = chosen.chromosome.genes[k].trait
            else:
                i -= 1
                c.genes[k].trait = chosen.chromosome.genes[k].trait
        return c

    @property
    def fitness(self):
        return self.eval_fitness(self.chromosome.genes)

