module Main where

    -- returns the values of the four corners of the square that is r iterations out
    -- from the centre
    cornerNumbers           ::  Int -> (Int,Int,Int,Int)
    cornerNumbers r          =   (n, n - f', n - 2*f', n - 3*f') where
                                    f   = 2*r + 1
                                    n   = f*f
                                    f'  = f - 1

    -- returns four-tuples containing the values of all corner numbers in all squares
    -- at most r iterations out from the centre
    cornersToWidth          ::  Int -> [(Int,Int,Int,Int)]
    cornersToWidth w        =   [cornerNumbers r | r <- [1..w]]

    -- sums the values of a four-tuple of integers
    quadrupleSum            ::  (Int,Int,Int,Int) -> Int
    quadrupleSum (a,b,c,d)  =   a + b + c + d


    main                    =   putStrLn (show $ sum [quadrupleSum cs | cs <- cornersToWidth 500] + 1)
