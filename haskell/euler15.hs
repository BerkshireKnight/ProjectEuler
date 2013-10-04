module Main where
    import System.IO (hFlush, stdout)

    data Coords                 =   Coords Int Int deriving Show
    data PathTree               =   EndPoint | Branch PathTree PathTree deriving Show


    -- n is the size of the grid
    buildPaths                  ::  Int -> Coords -> PathTree
    buildPaths n (Coords x y)   =   if x == n || y == n
                                        then EndPoint
                                        else Branch (buildPaths n (Coords x (y+1))) (buildPaths n (Coords (x+1) y))

    countPaths                  ::  PathTree -> Int
    countPaths (EndPoint)       =   1
    countPaths (Branch p1 p2)   =   countPaths p1 + countPaths p2

    origin                      ::  Coords
    origin                      =   Coords 0 0

    getGridSize                 ::  IO String
    getGridSize                 =   do  putStr "Enter the size of the grid: "
                                        hFlush stdout
                                        getLine

    main                        =   do  n <- getGridSize
                                        let ans = countPaths $ buildPaths (read n) origin
                                        putStrLn $ "There are " ++ show ans ++ " paths through that grid."
