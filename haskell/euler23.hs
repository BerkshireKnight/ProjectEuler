
module Main where

import qualified Data.Set as Set
import Factors (pfactors)


abundantSums            ::  Set.Set Int
abundantSums            =   Set.fromList [n + m | n <- ns, m <- ns]
                            where
                                ns  = [n | n <- [1..28124], f n]
                                f n = sum (pfactors n) > n


addNonAbundantSums      ::  Int
addNonAbundantSums      =   addHelp 28124 0

addHelp                 ::  Int -> Int -> Int
addHelp 0 n             =   n
addHelp i n             =   if i `member` xs
                                then addHelp (i-1) n
                                else addHelp (i-1) (n+i)
                            where xs = abundantSums


main                    ::  IO ()
main                    =   putStrLn . show $ addNonAbundantSums
