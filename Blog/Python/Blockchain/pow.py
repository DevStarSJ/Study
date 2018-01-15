from hashlib import sha256

x = 4
y = 0

hash_value = sha256(str(x*y).encode()).hexdigest()

while hash_value[-1] != '0':
    print(x, y, hash_value)
    y += 1
    hash_value = sha256(str(x * y).encode()).hexdigest()

print("The solution is y = {0}".format(y))