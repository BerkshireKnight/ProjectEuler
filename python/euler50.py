
import utils.factors as f


def euler50(x):
    primes = [2]

    sequences = {}
    sequences[0] = {0:2}

    i = 1
    for n in range(3, x+1):
        if f.is_prime(n):
            primes.append(n)
            sequences[i] = {}

            for j in sequences.keys():
                for k in sequences[j].keys():
                    sequences[i][k] = sequences[j][k] + n

            i += 1

    return primes, sequences


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        euler50(1000000)
    else:
        x = int(sys.argv[1])
        euler50(x)
