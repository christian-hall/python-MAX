import math
import random

# Chapter 3 (computations, formatting)

# max and min
print(max(2, 3, 4, 5, 6, 7))
print(min(2, 3, 4, 5, 6, 7))

# sum([list])
print(sum([1, 2, 3, 4]))

# round
print(round(7.2))
print(round(-1.2))
print(round(7.8))
# the second parameter specifies what decimal place to round it to
print(round(.349, 2))
print(round(3.14157, 3))

# ceiling & floor
print('ceil:', math.ceil(4.2))  # rounds up
print('floor:', math.floor(4.9))  # rounds down

# random
die = random.randint(1, 6)
print('die:', die)

# format a currency, this rounds
car_price = 34782.45209
car_price_formatted = '${:,.2f}'.format(car_price)
print('formatted car price', car_price_formatted)

# format a percent, this rounds
interest_pct = .0378645
interest_pct_formatted = '{:.4%}'.format(interest_pct)
print('pct:', interest_pct_formatted)
