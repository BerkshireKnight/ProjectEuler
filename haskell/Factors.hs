module Factors (factors, pfactors, ntfactors, prime) where
    import Data.List (sort, nub)

    -- returns a list of the factors of n
    factors             ::  Integral a => a -> [a]
    factors n           =   sort . nub $ fs where
                                fs  =   concat [[m,n `div` m] | m <- [1..lim+1], n `mod` m == 0]
                                lim =   floor . sqrt . fromIntegral $ n

    -- returns a list of the proper factors of n
    pfactors            ::  Integral a => a -> [a]
    pfactors            =   init . factors

    -- returns a list of the non-trivial factors of n
    ntfactors           ::  Integral a => a -> [a]
    ntfactors           =   tail . pfactors

    -- returns True if n is prime, False if not
    prime               ::  Integral a => a -> Bool
    prime n | n <= 1    =   False
            | otherwise =   factors n == [1,n]
