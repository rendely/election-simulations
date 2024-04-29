from voter_behavior.voter import Voter

class Election:
    def __init__(self):
        self.voters = []

    def add_voter(self):
        self.voters.append(Voter())
    
    def __repr__(self):
        return f'<Election num_voters={len(self.voters)}>'