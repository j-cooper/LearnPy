# 1. create list of 100 random numbers from 0 to 1000
# 2. sort list from min to max (without using sort())
# 3. calculate average for even and odd numbers
# 4. print both average result in console

import random
import array

# variable
min_value = int(-1)
position = int(0)
even = int(0)
odd = int(0)
count_odd = int(0)

# 1. Generate and fill of array
values = array.array('i', (random.randint(1, 1000) for i in range(0, 1000)))
print('Generated array\n', values)
print('================================================================')

# 2. Sorting
print('Array BEFORE\n', values)
print('================================================================')
for i in values:
  min_value = i
  if (i % 2) == 0:
    even = even + i
  else:
    odd = odd + i
    count_odd = count_odd + 1
  for j in values[values.index(i)+1:]:
      if j < min_value:
          position = values.index(j)
          min_value = j
  if i != min_value:
    values[position] = i
    values[values.index(i)] = min_value

print('Array AFTER\n', values)
print('================================================================')

#3. Average of ODD and EVEN

if count_odd == 0: count_odd = 1

print('SUM even values', even, 'Average is', even/(len(values)-count_odd))
if count_odd == 0: count_odd = 1 # check of ZERO values
print('SUM odd values', odd, 'Average is', odd/count_odd)


