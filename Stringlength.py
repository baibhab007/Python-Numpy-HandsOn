####
Try it Out - String Length
Determine the length of each defined fruit names and save it in list fruits_len.

Hint: Use list Comprehension
Display contents of fruits_len .

Find the fruit names that start with 'm' or 'p' and save it in list fruits_mp.

Hint: Use list Comprehension
Display contents of fruits_mp.
####


fruits = ['apple', 'mango', 'kiwi', 'watermelon', 'pear']
fruits_len = []
fruits_mp = []
for x in fruits:
  fruits_len.append(len(x))
  if (x.startswith('m') or x.startswith('p')):
    fruits_mp.append(x)
print(fruits_len)
print(fruits_mp)
