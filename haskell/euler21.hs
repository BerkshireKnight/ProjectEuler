factors         ::  Int -> [Int]
factors n       =   [m | m <- [1..n-1], n `mod` m == 0]

factor_sum      ::  Int -> Int
factor_sum n    =   sum . factors $ n

amicable        ::  (Int,Int) -> Bool
amicable (n,m)  =   factor_sum n == m && factor_sum m == n

amic_list       ::  Int -> [(Int,Int)]
amic_list n     =   [(x,factor_sum x) | x <- [1..n], amicable (x,factor_sum x), x < factor_sum x]

euler21         ::  Int
euler21         =   sum [x+y | (x,y) <- amic_list 9999]
