# Question 1.1 - What about 42 = n?
print('Question 1.1')
# 42=n # Invalid left-hand side in assignment

# Question 1.2 - How about x = y = 1?
print('Question 1.2 - x, y')
x = y = 1
print(x)
print(y)

# Question 1.3 - Semi-colon affection?
print('Question 1.3 - semi-colon'); # no affection

# Question 1.4 - Put period at the end of a statement?
# print('Question 1.4 - period in the end'). # Invalid Syntax

# Question 1.5 - Math notation xy = x * y , how about in python?
print('Question 1.5 - xy = x * y')
# print(xy) # x=1, y=1, xy = not defined

# Question 2.1 - Volume of a sphere is 4/3πr^3, 
#                get volume of a sphere with radius 5.
print('Question 2.1 - volume of sphere with radius 5')
radius = 5
pi = 3.141592
volumeOfSphere = (4/3) * pi * (radius ** 3)
print(volumeOfSphere)

# Question 2.2 - Cover price of a book is $24.95, but you got a 40% discount.
#                Shipping costs $3 for first copy and 75cents for each additional.
#                What is the total wholesale cost for 60 copies ?

coverPrice = 24.95
discount = 40/100
firstShippingCost = 3
nextShippingCost = 0.75
copies = 60

discountedPrice = coverPrice * discount
totalPrice = (discountedPrice + firstShippingCost) + (( discountedPrice + nextShippingCost) * (copies-1))
print(totalPrice)
# Question 2.3 - Leaving time : 6:52 am, 1 mile easy pace ( 8:15 per mile ),
#                then 3 miles at tempo ( 7:12 per mile ) and 1 mile easy pace again.
#                What time is the end of running?

leavingTimeToSec = ((6 * 60) + 52) * 60
easypaceSec = (8 * 60) + 15
tempoSec = (7 * 60) + 12
endTime = leavingTimeToSec + (easypaceSec * 2) + (tempoSec * 3)
hour = endTime // (60 * 60)
minute = (endTime % (60 * 60)) // 60
second = (endTime % (60 * 60)) % 60
print(hour,minute,second)
