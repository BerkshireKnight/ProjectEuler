module Main where
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


    main                        =   do  let paths = buildPaths 20 origin
                                            ans = countPaths paths
                                        putStrLn $ "There are " ++ show ans ++ " paths through that grid."
