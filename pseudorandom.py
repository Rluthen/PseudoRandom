import nacl.utils

rand = nacl.utils.random(128)
rand_str = ""

for i in rand:
    rand_str += hex(i)[2:] + " "
print(rand_str)