module Main where
    import Factors (prime)

    -- resolves the quadratic formula n^2 + an + b
    quadratic           ::  Int -> Int -> Int -> Int
    quadratic n a b     =   n*n + a*n + b

    -- counts the number of consecutive prime numbers obtained from resolving
    -- the quadratic formula with the given values of n, a, and b
    consec_primes       ::  Int -> Int -> Int -> Int
    consec_primes n a b =   if prime $ quadratic (n+1) a b
                                then consec_primes (n+1) a b
                                else n+1


