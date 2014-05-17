
module Main where

pythagorean             ::  (Int,Int,Int) -> Bool
pythagorean (a,b,c)     =   (a^2) + (b^2) == (c^2)

triangles               ::  Int -> [(Int,Int,Int)]
triangles p             =   [(a,b,c) | a <- [1..p], b <- [a..(p-a)], c <- [b..(p-a-b)], a <= b, b <= c]

tripleSum               ::  (Int,Int,Int) -> Int
tripleSum (a,b,c)       =   a + b + c

candidates              ::  Int -> [(Int,Int,Int)]
candidates p            =   filter (\t -> tripleSum t == p) . filter pythagorean . triangles $ p

pLimit                  ::  Int
pLimit                  =   1000

euler39                 ::  Int -> Int -> Int
euler39 p soln
    | p > pLimit        =   soln
    | otherwise         =   if (length . candidates $ p) > soln
                                then euler39 (p+1) p
                                else euler39 (p+1) soln

main                    ::  IO ()
main                    =   putStrLn . show . euler39 3 $ 0
