module Main where
    import Factors (pfactors)

    factor_sum      ::  Int -> Int
    factor_sum n    =   sum . pfactors $ n

    amicable        ::  (Int,Int) -> Bool
    amicable (n,m)  =   factor_sum n == m && factor_sum m == n

    amic_list       ::  Int -> [(Int,Int)]
    amic_list n     =   [(x,factor_sum x) | x <- [1..n], amicable (x,factor_sum x), x < factor_sum x]

    main            =   print . sum $ [x+y | (x,y) <- amic_list 9999]
