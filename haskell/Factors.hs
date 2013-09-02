module Factors (factors, pfactors, ntfactors, prime) where
    import Data.List (sort, nub)

    -- returns a list of the factors of n
    factors             ::  Int -> [Int]
    factors n           =   sort . nub $ fs where
                                fs  =   concat [[m,n `div` m] | m <- [1..lim+1], n `mod` m == 0]
                                lim =   floor . sqrt . fromIntegral $ n

    -- returns a list of the proper factors of n
    pfactors            ::  Int -> [Int]
    pfactors n          =   init . factors $ n

    -- returns a list of the non-trivial factors of n
    ntfactors           ::  Int -> [Int]
    ntfactors  n        =   tail . pfactors $ n

    -- returns True if n is prime, False if not
    prime               ::  Int -> Bool
    prime n | n <= 0    =   False
            | otherwise =   (length . factors $ n) == 2
