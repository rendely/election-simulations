from voter_behavior.election import Election
from voter_behavior.candidate import Candidate

if __name__ == '__main__':
    print('Starting simulation')

    # Create candidate scenarios
    candidates = [
        Candidate(name='A', lean=-0.5),
        Candidate(name='B', lean=0.5)
    ]

    # Creates uniform electorate
    e_unfiorm = Election(num_voters=10000, lean_distribution='uniform')
    e_unfiorm.vote(candidates)

    # Creates normal electorate
    e_normal = Election(num_voters=10000, lean_distribution='normal')
    e_normal.vote(candidates)

    # Creates bimodal electorate 
