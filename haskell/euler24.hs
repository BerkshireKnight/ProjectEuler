module Main where
    import Data.List(sort, permutations)

    ps          ::  [[Int]]
    ps          =   sort . permutations $ [0..9]

    euler24     ::  [Int]
    euler24     =   ps !! 999999


    main        =   putStrLn $ "The millionth permutation is " ++ show euler24
