class Candidate:
    def __init__(self, name=None, lean=None):
        if name is None:
            raise AttributeError('Must choose name')
        
        if lean is None:
            raise AttributeError('Must choose lean')
        
        self.name = name
        self.lean = lean
    
    def __repr__(self):
        return f'<Candidate lean={self.lean}>'