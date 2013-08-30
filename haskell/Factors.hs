module Factors where
    -- returns a list of the factors of n
    factors         ::  Int -> [Int]
    factors n       =   [m | m <- [1..n], n `mod` m == 0]

    -- returns a list of the proper factors of n
    pfactors        ::  Int -> [Int]
    pfactors n      =   [m | m <- [1..n-1], n `mod` m == 0]

    -- returns a list of the non-trivial factors of n
    ntfactors       ::  Int -> [Int]
    ntfactors  n    =   [m | m <- [2..n-1], n `mod` m == 0]
