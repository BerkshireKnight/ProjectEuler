{-|
Module:         Factors
Description:    Provides functions to generate the factors of any given number.
Copyright:      Copyright (c) 2013-14 Ian Knight
Maintainer:     ian.knight.1990@gmail.com

This module provides functions to efficiently calculate the factors (divisors)
of any Integral value. It also provides a function to check for prime numbers.
-}
module Factors (factors, pfactors, ntfactors, prime) where

import Data.List (sort, nub)


-- |Returns a list of every factor of the given number.
factors             ::  Integral a => a -- ^The number to find factors of
                        -> [a] -- ^The list of factors
factors n           =   sort . nub $ fs where
                            fs  =   concat [[m,n `div` m] | m <- [1..lim+1], n `mod` m == 0]
                            lim =   floor . sqrt . fromIntegral $ n


-- |Returns the proper factors of the given number. Proper factors
-- do not include the number itself.
pfactors            ::  Integral a => a -- ^The number to find factors of
                        -> [a] -- ^The list of proper factors
pfactors            =   init . factors


-- |Returns the non-trivial factors of the given number. Non-trivial
-- factors do not include the number 1, or the number itself.
ntfactors           ::  Integral a => a -- ^The number to find factors of
                        -> [a] -- ^The list of non-trivial factors
ntfactors           =   tail . pfactors


-- |Determines whether the given number is prime or not.
prime               ::  Integral a => a -- ^The number to test
                        -> Bool -- ^True if the number is prime, False if not
prime n | n <= 1    =   False
        | otherwise =   case factors n of
                            [1,_] -> True
                            _     -> False
