module Main where

    cornerNumbers           ::  Int -> (Int,Int,Int,Int)
    cornerNumbers r          =   (n, n - f', n - 2*f', n - 3*f') where
                                    f   = 2*r + 1
                                    n   = f*f
                                    f'  = f - 1

    quadrupleSum            ::  (Int,Int,Int,Int) -> Int
    quadrupleSum (a,b,c,d)  =   a + b + c + d

    cornersToWidth          ::  Int -> [(Int,Int,Int,Int)]
    cornersToWidth w        =   [cornerNumbers r | r <- [1..w]]


    main                    =   do  putStrLn (show $ sum [quadrupleSum cs | cs <- cornersToWidth 500] + 1)
