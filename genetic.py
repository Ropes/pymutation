#!/usr/bin/python

from base import *
from copy import deepcopy
from random import choice


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

    def selection(self, proletariat=0.6):
        evals = [ (i.fitness, i) for i in self.indivs ]
        evals.sort(reverse=True)
        print evals

        indies = []
        #Eliteism used to pick best two parentsPick the best, mate them
        schmexya = evals.pop()
        schmexyb = evals.pop()
        messiah = schmexya.mate(schmexyb, schmexya.eval_fitneess)
        self.indivs = [schmexya, schmexyb, messiah]
        
        while len(self.indivs) < self.size:
            #NOTE: currently parrents are swingers and just randomly have children
            a = evals.pop(int(len(evals) * random.random()) )
            b = evals.pop(int(len(evals) * random.random()) )

            self.indivs.append(a.mate(b, a.eval_fitness))
            

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
    ic = Individual( ia.mate(ib), len_eval )
    ''' 
    
    indies = []
    for x in range(0, 10):
        genes = get_genes()
        c = Chromosome(genes)
        indies.append( Individual(c, len_eval) )

    pop = Population(indies, size=3)
    pop.mutation()
    pop.selection()
    

