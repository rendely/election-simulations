from voter_behavior.voter import Voter
import numpy

class Election:
    def __init__(self, num_voters=100, lean_distribution=None):
        if lean_distribution is None:
            raise AttributeError('Must choose lean distribution')

        self.voters = []
        for i in range(0,num_voters):
            self.voters.append(Voter(lean_distribution))

    def avg_lean(self):
        return numpy.mean([v.lean for v in self.voters])
    
    def __repr__(self):
        return f'<Election num_voters={len(self.voters)} avg_lean={self.avg_lean()} >'