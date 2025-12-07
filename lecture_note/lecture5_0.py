odds = [1,3,5,7,9]
new_list = [x+1 for x in odds]
new_list1 = [x for x in odds if 25 % x == 0]
print(new_list1)