# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:53:28 2022

@author: Mehr

inplace sorting tool (very slow)
"""

#importing
import random
import time
import numpy as np

#function to check the amount of time elapsed
start_time = time.process_time()

class Values():
    def __init__(self):
        self.reset()
    
    def reset(self):
        #create a random list of numbers and converting it to a numpy array
        self.list_length = 1000
        self.random_list = random.sample(range(2*self.list_length), self.list_length)
        self.random_array = np.asarray(self.random_list)
        print("--- original list ---")
        print(self.random_array)
        
class Sort():
    def __init__(self):
        pass

    def inplacesort(self, array):
        #create results list to fill with boleans, to check when to end.
        res = []
        while True:
            for idx in range(1, array.size):
                #compare array element with previous element, swap if previous is larger.
                if array[idx - 1] > array[idx]:
                    array[idx - 1], array[idx] = array[idx], array[idx - 1]
                    res.append(False)
                else:
                    res.append(True)
            #if results list is filled with True, end program.
            if all(res) == True:
                break
            res.clear()
        return array

class Main():
    def __init__(self):
        self.values = Values()
        self.sort = Sort()
        
    def run(self):
        self.sort.inplacesort(self.values.random_array)
        print("--- sorted list ---")
        print(self.values.random_array)


main = Main()
main.run()

#second part of the time checking function
print("--- %s seconds ---" % (time.process_time() - start_time))