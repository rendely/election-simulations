import numpy 
numpy.random.seed(1337)

class Voter:
    def __init__(self, lean=0.5):
        self.lean = numpy.random.random()
    
    def __repr__(self):
        return f'<Voter lean={self.lean}>'