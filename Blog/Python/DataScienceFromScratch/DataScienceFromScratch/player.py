from collections import defaultdict

seed_origin = 2016
seed_limit = 20160814

def my_random(seed, limit):
    b = seed // limit
    c = b % limit
    d = (seed * b ** limit) % seed_limit 
    
    return c, d

def get_index(probabilities, seed):
    max = sum(probabilities)

    seed = seed + max
    
    acc = 0
    rand, seed = my_random(max*max, max)
    for idx, percent in enumerate(probabilities):
        acc += percent
        if rand < acc:
            return idx
    return len(probabilities)

GBB = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):

    index = 0

    if len(records) == 0:
        index = get_index([1,1,1], seed_origin)
    else:
        enemyChoice = defaultdict(int)
        enemyScore = defaultdict(int)

        for hand, score in records:
            enemyChoice[hand] += 1
            enemyScore[hand] += score
    
        reference = [ enemyChoice['bo'], enemyChoice['gawi'],enemyChoice['bawi'] ]

        seed = sum(enemyScore.values())
        index = get_index(reference, seed)

    return GBB[index]

if __name__ == '__main__':
    records = []
    print(show_me_the_hand(records))

    print(show_me_the_hand([('gawi',1), ('bo',1)]))
    print(show_me_the_hand([('gawi',1), ('bo',0)]))
    print(show_me_the_hand([('gawi',1), ('gawi',-1)]))
    print(show_me_the_hand([('gawi',1), ('gawi',-1), ('gawi',0)]))
    print(show_me_the_hand([('bo',1), ('bo',-1), ('bo',0)]))
    print(show_me_the_hand([('bawi',1), ('bawi',-1), ('bawi',0)]))

    #s = seed_origin
    #for i in range(0,100):
    #    a, s = my_random(s, 3)
    #    print(a)

