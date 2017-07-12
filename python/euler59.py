
import string


def encrypt_decrypt(msg, key):
    msg1 = []
    m, k = 0, 0

    while m < len(msg):
        c = chr(ord(msg[m]) ^ ord(key[k]))
        msg1.append(c)

        m += 1
        k = (k+1) % len(key)

    return ''.join(msg1)


def possible_keys():
    triples = [(x,y,z)
               for x in string.lowercase
               for y in string.lowercase
               for z in string.lowercase
               ]

    return [''.join(cs) for cs in triples]
