class Candidate:
    def __init__(self, name=None, lean=None):
        if name is None:
            raise AttributeError('Must choose name')
        
        if lean is None:
            raise AttributeError('Must choose lean')
        
        self.name = name
        self.lean = lean
        print(self)
    
    def __repr__(self):
        return f'<Candidate name={self.name} lean={self.lean}>'