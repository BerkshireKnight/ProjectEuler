module Primes (prime, primes_upto) where
    import Factors (factors)

    -- determines whether n is prime or not
    prime           ::  Int -> Bool
    prime n         =   (length . factors $ n) == 2

    -- returns a list of all prime numbers less than or equal to n
    primes_upto     ::  Int -> [Int]
    primes_upto n   =   [x | x <- [1..n], prime x]
