import random
from collections import defaultdict

def get_index(probabilities):
    max = sum(probabilities)
    
    acc = 0
    rand = random.random() * max
    for idx, percent in enumerate(probabilities):
        acc += percent
        if rand < acc:
            return idx
    return len(probabilities)

GBB = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):

    index = 0

    if len(records) == 0:
        index = get_index([1,1,1])
    else:
        enemyChoice = defaultdict(int)
        #enemyScore = defaultdict(int)

        for hand, score in records:
            enemyChoice[hand] += 1
            #enemyScore[hand] += score
    
        reference = [ enemyChoice['bo'], enemyChoice['gawi'],enemyChoice['bawi'] ] 
        index = get_index(reference)

    return GBB[index]

if __name__ == '__main__':
    records = []
    print(show_me_the_hand(records))

    print(show_me_the_hand([('gawi',1), ('bo',1)]))

