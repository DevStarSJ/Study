users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user["friends"])

def total_connections(users):
    return sum(number_of_friends(user) for user in users)

def avg_connections(users):
    return total_connections(users) / len(users) 

def sort_by_numFriend(users):
    num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
    return sorted(num_friends_by_id, key = lambda num_friend : num_friend[1], reverse=True)

def friends_of_friend_ids_bad(user):
    return [foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]]

def not_the_same(user, other_user):
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    l = [not_the_same(friend, other_user) for friend in user["friends"]]
    print(l)
    return all([not_the_same(friend, other_user) for friend in user["friends"]])

#print(not_friends(users[0], users[1]))
l = [not_the_same(friend, users[1]) for friend in users[0]["friends"]]
