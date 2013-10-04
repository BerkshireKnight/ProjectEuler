module Main where
    import Factors (factors)

    -- returns the number of factors (divisors) of n
    num_factors     ::  Int -> Int
    num_factors     =   length . factors

    -- returns the nth triangle number
    triangle        ::  Int -> Int
    triangle n      =   n * (n+1) `div` 2

    triangles       ::  [(Int,Int,Int)]
    triangles       =   [(n, triangle n, num_factors . triangle $ n) | n <- [1..100]]

    print_triangles         ::  [(Int,Int,Int)] -> IO ()
    print_triangles [t]     =   putStrLn . show $ t
    print_triangles (t:ts)  =   do  putStrLn . show $ t
                                    print_triangles ts

    -- finds the first triangle number with over 500 factors (divisors)
    euler12                         ::  Int -> Int
    euler12 n | num_factors n > 500 =   n
              | otherwise           =   euler12 . triangle $ (n+1)

    main = print . euler12 $ 1
