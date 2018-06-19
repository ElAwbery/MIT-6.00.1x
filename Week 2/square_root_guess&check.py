# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 # In the square root program, if the square root of a value between 0 and 1 is sought, the 
 # incremental program written to find the square root of an integer greater than 1 will fail. 
 # This is because if the answer starts at 0 and increments, it will always be greater than 0. 
 
    # the condition that stops the program running is that the answer variable exceeds the size of x before it gets near the 
    # value of the correct square root, because the square root value in this instance is larger than the answer
    
 # The program can be rewritten to decrement, and then it will work. As written here: 




x = 0.25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 1.0
while abs(ans**2 - x) >= epsilon and ans >= x:
    ans = ans - step
    numGuesses += 1
print ("numGuesses =", numGuesses)

if abs(ans**2 - x) >= epsilon:
    print ("failed on square root of:", x)
else:
    print (ans, "is close to square root of", x)
    
   
# But the point to be understood is that the test for the answer has to include the range of values near the answer
# Obviously, if the window for the answer is not reached before the loop terminates, then it won't work
    
    



















 
