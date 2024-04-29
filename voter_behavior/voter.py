class Voter:
    def __init__(self, lean=0.5):
        self.lean = lean
    
    def __repr__(self):
        return f'<Voter lean={self.lean}>'