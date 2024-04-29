import numpy 
numpy.random.seed(1337)

class Voter:
    def __init__(self, lean_distribution=None):
        if lean_distribution is None:
            raise AttributeError('Must choose lean distribution')
        
        if lean_distribution == 'uniform':
            self.lean = numpy.random.random()-0.5

        if lean_distribution == 'normal':
            self.lean = numpy.random.normal(0, 0.25)
        
        if lean_distribution == 'bimodal':
            flip = numpy.random.random()-0.5
            if flip < 0:
                self.lean = numpy.random.normal(-0.5, 0.25) 
            else:
                self.lean = numpy.random.normal(0.5, 0.25) 

    
    def __repr__(self):
        return f'<Voter lean={self.lean}>'