from voter_behavior.election import Election

if __name__ == '__main__':
    print('Starting simulation')
    e = Election(100, 'uniform')
    print(e)