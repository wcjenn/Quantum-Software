import numpy as np
import copy as cp
import random
import montecarlo

class metropolis:
    def __init__(self,ham):
        self.ham = ham
        self.N = ham.num_sites


    def run(self, T,n_samples, n_burn):
        M = []
        E = []
        e = 2.7182818
        bs = montecarlo.BitString(self.N)
        en = self.ham.energy(bs)

        for i in range(n_samples+n_burn):
            
            for j in range(self.N):
                bs.flip_site(j)
                deltaE = self.ham.energy(bs) - en
                prob = e ** (-deltaE/ T) if deltaE > 0 else 1
                if random.random() < prob :
                    en += deltaE
                else:
                    bs.flip_site(j)
            if i >= n_burn:
                E.append(en)
                M.append(self.ham.compute_mag(bs))
            
        return E,M
    

