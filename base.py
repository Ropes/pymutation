import random

class Gene(object):
    def __init__(self, trait=None, traits=None,):
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

    def crossover(self, prob, chrom2):
        i = 0
        split = int(len(self.genes)*prob)
        offspring = {}
        for k,v in self.genes.items():
            if i > split:
                offspring[k] = chrom2.genes[k] 
            else:
                offspring[k] = self.genes[k]

        #print offspring
        return Chromosome(offspring)
        
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
    def __init__(self, chrom, fitness_func=None ):
        self.chromosome = chrom 
        self.eval_fitness = fitness_func 

    def __str__(self):
       
        x = 'Individual: ' + str(self.chromosome)
        x += str(self.eval_fitness)
        return x

    def mate(self, male):
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

