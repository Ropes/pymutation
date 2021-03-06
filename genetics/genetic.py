#!/usr/bin/python

from base import *
from copy import deepcopy
from random import choice
import pdb

evalfitness = None

class Population(object):
    def __init__(self, indivs, size=20):
        self.size = size
        self.indivs = indivs

    def crossover(self):
        prob = 5.0
        pass

    def mutation(self, prob=0.09):
        for i in self.indivs:
            i.chromosome.mutate(prob)

    def evolve(self, proletariat=0.6):
        evals = [ (i.fitness, i) for i in self.indivs ]
        evals.sort(reverse=True)

        indies = []
        #Eliteism used to pick best two parentsPick the best, mate them
        schmexya = evals.pop(0)[1]
        schmexyb = evals.pop(0)[1]
        messiah = Individual( schmexya.mate(schmexyb), schmexya.eval_fitness)
        messiah2 = Individual( schmexya.mate(schmexyb), schmexya.eval_fitness)
        
        self.indivs = [messiah, messiah2]
        #for i in self.indivs:
        #    print i.fitness, [ v.trait for k,v in i.chromosome.genes.items()]
        print(self.indivs)
        print(len(self.indivs), len(evals), self.size)
        while len(self.indivs) < self.size:
            #NOTE: currently parrents are swingers and just randomly have children
            randa = int(len(evals) * random.random())
            randb = int(len(evals) * random.random())
            #print 'randoms:', randa, randb
            a = evals[randa][1]
            b = evals[randb][1]
            c = a.mate(b)
            print(c)
            self.indivs.append(Individual(c, evalfitness))
            #self.indivs.append(Individual(a.mate(b), evalfitness))

        for i in self.indivs:
            print( i.fitness, [ v.trait for k,v in i.chromosome.genes.items()] )
        #print self.indivs
            

if __name__ == '__main__':
    global evalfitness
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

    print
    print
    print
    print
    print
    print
    print
    print
    print

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
            i += len(v.trait)
        return i
    evalfitness = len_eval

    indies = []
    for x in range(0, 20):
        genes = get_genes()
        c = Chromosome(genes)
        pdb.set_trace()
        indies.append( Individual(c, len_eval) )

    pop = Population(indies, size=12)
    for i in range(0, 10):
        print('GENERATION ===============================================')
        print(pop.indivs)
        pop.mutation(prob=0.3)
        pdb.set_trace()
        pop.evolve()
    

