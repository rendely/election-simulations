from voter_behavior.election import Election
from voter_behavior.candidate import Candidate
from utils import histogram_plot, show_plot

if __name__ == '__main__':
    print('Starting simulation')

    # Create candidate scenarios
    candidates = [
        Candidate(name='A', lean=-0.5),
        Candidate(name='B', lean=0.5)
    ]    

    # Creates uniform electorate
    e_unfiorm = Election(num_voters=10000, lean_distribution='uniform')
    histogram_plot([v.lean for v in e_unfiorm.voters], 'uniform voters')
    e_unfiorm.vote(candidates)

    # Creates normal electorate
    e_normal = Election(num_voters=10000, lean_distribution='normal')
    histogram_plot([v.lean for v in e_normal.voters], 'normal voters')
    e_normal.vote(candidates)

    # Creates bimodal electorate 

    # Show all plots
    show_plot()