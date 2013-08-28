-- returns a list of the factors (divisors) of n
factors             ::  Int -> [Int]
factors n           =   [m | m <- [1..n], n `mod` m == 0]

-- returns the number of factors (divisors) of n
num_factors         ::  Int -> Int
num_factors n       =   length . factors $ n

-- returns the nth triangle number
triangle            ::  Int -> Int
triangle n          =   sum [1..n]

-- finds the first triangle number with over 500 factors (divisors)
euler12                         ::  Int -> Int
euler12 n | num_factors n > 500 =   n
          | otherwise           =   euler12 . triangle $ n+1
