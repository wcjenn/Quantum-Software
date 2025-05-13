import numpy as np



class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)
    
    def __str__(self):
        return self.__repr__()
    

    def on(self):
        return sum(self.config)

    def off(self):
        return len(self.config) - sum(self.config)
    

    def flip_site(self,i):
        self.config[i] = 1-self.config[i]
        
    
    def integer(self):
        integer = 0
        n = len(self.config)
        for i in range(n):
            integer += self.config[i] * (2 ** (n - 1 - i))
        return integer
        
 

    def set_config(self, s:list[int]):
        for i in range(len(s)):
            self.config[i] = int(s[i])
       
        """
        
        """
    def set_integer_config(self, dec:int):
        self.config = np.zeros(self.N, dtype=int)
        n = 1
        while dec > 0:
            remain = dec % 2
            if remain > 0:
                self.config[-n] = 1-self.config[-n]
            n = n + 1
            dec = dec // 2
        return self.config
        
    
    
    
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """

