from typing import List

from populations.individual import Individual

class Population:
  individuals = []
  best = None

  def __init__(self, popSize = None, factory = None):
    if popSize is not None and factory is not None:
        for _ in range(popSize):
            self.individuals.append(factory())

  def getBest(self, nodes):
    self.best = min(self.individuals, key=lambda x: x.calcFitness(nodes))
    return self.best