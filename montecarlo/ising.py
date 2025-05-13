import numpy as np
import networkx as nx
from .bitstring import BitString

class IsingHamiltonian:


    

    def __init__(self,graph):
        


        self.G = graph
        self.num_sites = graph.number_of_nodes()
        self.N = graph.number_of_nodes()
        self.mu = np.zeros(self.num_sites)
  
        
    
    def set_mu(self, mu_values):


        if len(mu_values) != self.num_sites:
            raise ValueError(f"Expected{self.num_sites} mu values, got {len(mu_values)}")
        
        self.mu = np.array(mu_values)
        return self


    def energy(self, bs: BitString):



        spins = 2*bs.config - 1
        E = 0
        A = nx.adjacency_matrix(self.G).todense()
        for rows in range(self.num_sites):
            for columns in range(rows):
                if(A[rows][columns]):
                    e = (rows, columns)
                    E +=self.G.edges[e]['weight'] * spins[rows] * spins[columns]
                else: 
                    E += 0

        E_mu = -sum(self.mu[i] * bs.config[i] for i in range(self.num_sites))

        return E + E_mu
    
    
    def compute_average_values(self,  T: float):

        E  = 0.0
        M  = 0.0
        Z  = 0.0
        EE = 0.0
        MM = 0.0

        bs = BitString(self.num_sites)

        Config = 2**(len(bs))-1

        e=2.71828
        B=1/(T)
        for j in range(Config):
            bs.set_integer_config(j)
            Z += e ** (-B*self.energy(bs))
        for i in range(Config):
            bs.set_integer_config(i)
            probA = (e ** (-B * self.energy(bs)))/Z
            E += self.energy(bs)*probA
            M += self.compute_mag(bs)*probA
            EE += self.energy(bs)**2*probA
            MM += self.compute_mag(bs) ** 2 * probA

        HC = (EE - (E**2))*(T**(-2))
        MS = (MM - (M**2))*(T**(-1))


        return E, M, HC, MS
    
    def compute_mag(self, bs:BitString):
        M = 0.0
        numConf = len(bs)
        for i in range(self.num_sites):
            if(bs.config[i] ==1):
                M += 1
            else:
                M-=1
        return M