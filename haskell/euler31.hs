
coins                       ::  [Int]
coins                      =   [200, 100, 50, 20, 10, 5, 2, 1]


coinSums                    ::  Int -> [Int] -> Int
coinSums 0 _                =   1
coinSums t [1]              =   1
coinSums t (c:cs)
    | c > t                 =   coinSums t cs
    | otherwise             =   sum1 + sum2
                                where
                                    sum1 = coinSums t cs         -- no coins of denom. c
                                    sum2 = coinSums (t-c) (c:cs) -- 1+ coins of denom. c


main                        ::  IO ()
main                        =   putStrLn . show $ coinSums 200 coins
