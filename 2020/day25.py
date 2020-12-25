card_key = 2069194
door_key = 16426071

# test
#card_key = 5764801
#door_key = 17807724

# To transform a subject number, start with the value 1. Then, a number of times called the loop size, perform the following steps:

# Set the value to itself multiplied by the subject number.
# Set the value to the remainder after dividing the value by 20201227.

def find_handshake(subject_number, key):
    result = 1
    loop_size = 0
    while(True):
        loop_size += 1
        result *= subject_number
        result = result % 20201227
        if result == key:
            return loop_size


        


# figure out the card's key

card_i = find_handshake(7, card_key)
door_i = find_handshake(7, door_key)

result = 1
for i in range(card_i):
    result *= door_key
    result = result % 20201227
print(result)
