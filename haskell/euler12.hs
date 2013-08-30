-- returns a list of the factors (divisors) of n
factors             ::  Int -> [Int]
factors n           =   foldr (++) [] [[m, n `div` m] | m <- [1..sqrt (fromIntegral n)], n `mod` m == 0]

-- returns the number of factors (divisors) of n
num_factors         ::  Int -> Int
num_factors n       =   length . factors $ n

-- returns the nth triangle number
triangle            ::  Int -> Int
triangle n          =   n * (n+1) `div` 2

-- finds the first triangle number with over 500 factors (divisors)
euler12                         ::  Int -> Int
euler12 n | num_factors n > 500 =   n
          | otherwise           =   euler12 . triangle $ n+1
