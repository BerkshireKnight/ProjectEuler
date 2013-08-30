import Factors (factors)

-- returns the number of factors (divisors) of n
num_factors     ::  Int -> Int
num_factors n   =   length . factors $ n

-- returns the nth triangle number
triangle        ::  Int -> Int
triangle n      =   n * (n+1) `div` 2

-- finds the first triangle number with over 500 factors (divisors)
euler12                         ::  Int -> Int
euler12 n | num_factors n > 500 =   n
          | otherwise           =   euler12 . triangle $ n+1

solution        ::  Int
solution        =   euler12 1
