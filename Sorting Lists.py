#  Learning the differences between using list.sort() and sorted(). Contains practice code with results for each function.
milk = [12, 80, 70 ,69 ,32 ,11, 25, 14, 77, 18, 26]
x = sorted(milk)
cookies = [12, 80, 70 ,69 ,32 ,11, 25, 14, 77, 18, 26]
#z = cookies.sort()  # ".sort() cannot be directly stored in a variable; it does not return a value that can be stored by it does change the orig list itself like a quasi void func
# instead you have to perform the list.sort() func, and then assign a new variable to the name of the list that was sorted
print (milk)  # milk will always be in the original order
print(milk[2])  # prints item 2 based on orig order of milk not the new sorted list
print(x)  # this sorted func actually does return a value and can be stored in a variable directly as in line 2
print(x[2])  # prints item 2 based on the new sorted order of milk list
print(cookies)  # so now cookies is sorted by act of calling a quasi void func in line 4 although the new list cannont be assigned to a variable in this manner directly
cookies.sort(reverse=True)  # comment out line 4 so the ascending sort is not called; now with this line 11 you are calling the descending sort
print(cookies) #descending sort is printed; you can now assign this new sorted list to a variable and then change cookies back by entering False
cookies.sort(reverse=False)  # or same as cookies.sort() 
print(cookies)
#print(z)  #prints z = None because  the method in line 4 cannot store the new sorted list from line 4 in a direct manner (only indirect - see lines 20 & 21)
#print(cookies)  # cookies is still sorted
#cookies.sort()  #sorts cookies
#print(cookies[2])  # prints based on the sorted list so item 2 is 14
#print(cookies) #prints sorted list
#z1 = cookies  # so you can assign a list.sort() result to a variable but ONLY AFTER you perform the command func in line 4 but preferred way is as in line 17
#print(z1)
#x = sorted(milk, reverse = True)  #this is how to change our list "milk" to descending order
#print(x)  # OR simply...
print(sorted(milk, reverse = True))  # this does not permanently change "milk" but "cookies" are changed such that you cannot get its original order back
print(milk)  #better to leave milk alone so you have the original order and just work with the new variable for sorting
print(sorted(x, reverse = False))  # x will always be sorted ascending or descending; print "milk" to get original list order
print(sorted(x, reverse = True))  # x will always be sorted ascending or descending; print "milk" to get original list order
sorted(milk, reverse = False)
print(milk)
#  I suggest you comment out various lines of this code to experiment until you understand precisely how each func works:  list.sort() vs. sorted(list)
