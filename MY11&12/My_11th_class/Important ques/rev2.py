''' Programme to re-arrange the digits in any 10 digit number in such a way that :
its middle two digits get arranged at end of the number and in remaing digits , 1st pair becomes
the last and 2nd pair becomes the second last and so on..'''

n = int(input("Enter a number of 10 digits ")) # 10 digits number
q1 = n // 10000    # last 6 digits 
r1 = q1 % 10       # 5th digit from ones place
r2 = q1 % 100      # middle most two digits
q2 = r2 // 10      # 6th digit from ones place 
r3 = n % 10000     # first four digits
q3 = r3 // 100     # 4th and 3rd digit from ones place 
r4 = r3 % 100      # first two digits from ones place
q4 = n // 1000000  # last four digits
r5 = q4 % 100      # 8th and 7th digits from ones place
q5 = q4 // 100     # last two digits
new_num = q2 * 10 ** 9 + r4 * 10 ** 7 + q3 * 10 ** 5 + r5 * 10 ** 3 + q5 * 10 + r1
print(new_num)





