module TwoSum where

import Data.Map (Map)
import qualified Data.Map as Map


-- For Sorting
import Data.List

twosum			:: [Integer] -> Integer -> [Integer]
twosum nums target	= 
	    		where sortednums = sort nums