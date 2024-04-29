import numpy 
numpy.random.seed(1337)

class Voter:
    def __init__(self, lean_distribution=None):
        if lean_distribution is None:
            raise AttributeError('Must choose lean distribution')
        
        if lean_distribution == 'uniform':
            self.lean = numpy.random.random()
    
    def __repr__(self):
        return f'<Voter lean={self.lean}>'