from voter_behavior.voter import Voter
import numpy

class Election:
    def __init__(self, num_voters=10, lean_distribution=None):
        self.lean_distributions = lean_distribution
        if lean_distribution is None:
            raise AttributeError('Must choose lean distribution')

        self.voters = []
        for i in range(0,num_voters):
            self.voters.append(Voter(lean_distribution))

    def avg_lean(self):
        return numpy.mean([v.lean for v in self.voters])
    
    def vote(self, candidates):     
        tally = {}   
        for c in candidates:
            tally[c.name] = 0

        for voter in self.voters:
            chosen = min(candidates, key= lambda candidate: abs(candidate.lean - voter.lean))
            tally[chosen.name] += 1
        
        print(f'The final tally in {self.lean_distributions}: {tally}')
            
        
                
    
    def __repr__(self):
        return f'<Election num_voters={len(self.voters)} avg_lean={self.avg_lean()} >'