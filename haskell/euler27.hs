module Main where
    import Factors (prime)

    -- resolves the quadratic formula n^2 + an + b
    quadratic           ::  Int -> Int -> Int -> Int
    quadratic n a b     =   n*n + a*n + b

    -- counts the number of consecutive prime numbers obtained from resolving
    -- the quadratic formula with the given values of n, a, and b
    consec_primes       ::  Int -> Int -> Int -> Int
    consec_primes n a b =   if prime $ quadratic (n+1) a b
                                then consec_primes (n+1) a b
                                else n+1

    -- returns a list of pairs of values for a and b, paired with the number of
    -- consecutive primes produced by those pairs
    consec_list         ::  Int -> Int -> [((Int,Int),Int)]
    consec_list min max =   [((a,b),consec_primes 0 a b) | a <- [min..max], b <- [min..max], consec_primes 0 a b > 40]

    -- sorts the results of consec_list accordng to the number of consecutive primes produced
    qsort               ::  [((Int,Int),Int)] -> [((Int,Int),Int)]
    qsort []            =   []
    qsort (x:xs)        =   (qsort ys) ++ [x] ++ (qsort zs) where
                                ys  =   [y | y <- xs, snd y <= snd x]
                                zs  =   [z | z <- xs, snd z > snd x]

    -- obtains the pair of coefficients between -999 and 999 which produce the greatest number
    -- of consecutive primes
    solution            ::  ((Int,Int),Int)
    solution            =   last $ qsort $ consec_list (-999) 999

    main                =   do  let coefficients = fst solution
                                    a = fst coefficients
                                    b = snd coefficients
                                    p = a * b
                                    x = snd solution
                                putStrLn ("The coefficients are a=" ++ show a ++ ", b=" ++ show b)
                                putStrLn ("They produce " ++ show x ++ " consecutive primes")
                                putStrLn ("Their product is " ++ show p)
