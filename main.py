from voter_behavior.election import Election
from voter_behavior.candidate import Candidate
from utils import histogram_plot, show_plot

if __name__ == '__main__':
    print('Starting simulation')

    # Create candidate scenarios
    candidates = [
        Candidate(name='A', lean=-0.5),
        Candidate(name='B', lean=0.4)
    ]    

    # Creates uniform electorate
    e_unfiorm = Election(num_voters=10000, lean_distribution='uniform')
    result = e_unfiorm.vote(candidates)
    histogram_plot([v.lean for v in e_unfiorm.voters], 'uniform voters', candidates[0].lean, candidates[1].lean, result)

    # Creates normal electorate
    e_normal = Election(num_voters=10000, lean_distribution='normal')
    result = e_normal.vote(candidates)
    histogram_plot([v.lean for v in e_normal.voters], 'normal voters', candidates[0].lean, candidates[1].lean, result)

    # Creates bimodal electorate 
    e_bimodal = Election(num_voters=10000, lean_distribution='bimodal')
    result = e_bimodal.vote(candidates)
    histogram_plot([v.lean for v in e_bimodal.voters], 'bimodal', candidates[0].lean, candidates[1].lean, result)

    # Show all plots
    show_plot()