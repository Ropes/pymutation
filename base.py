
import random

class Gene(object):
    def __init__(self, key, trait, traits,):
        self.trait = trait
        self.possible_traits = traits

    def __str__(self):
        return '{} {})'.format(self.trait, self.possible_traits)
    
    def mutate(self):
        self.trait = random.choice(list(self.possible_traits))


class Chromosome(object):
    def __init__(self, genes):
        self.genes = genes

    def __str__(self):
        x = self.__repr__() + '\n'
        for k,v in self.genes.items():
            x += k.ljust(5) + str(v) + '\n'
        return x

    def mutate(self, prob):
        for k,v in self.genes.items():
            if prob <= random.random():
                v.mutate()
                print v

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

