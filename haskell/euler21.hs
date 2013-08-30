factors         ::  Int -> [Int]
factors n       =   [m | m <- [1..n-1], n `mod` m == 0]

amicable        ::  (Int,Int) -> Bool
amicable (n,m)  =   (sum (factors n) == m) && (sum (factors m) == n)

amic_list       ::  Int -> [(Int,Int)]
amic_list n     =   [(x,y) | x <- [1..n], y <- [x+1..n], amicable (x,y)]

euler21         ::  Int
euler21         =   sum [x+y | (x,y) <- amic_list 9999]
