# A different kind of while loop and how to use the any keyword:

"""While loops are not just for True or False, as if it can only be an on/off switch. Instead, expand your view
of the while loop. What if we keep doing something or do a certain thing if a particular input is received or
if a specified condition (counter, formula result, input received, game status, player or characer status, etc.).
Now...a whole new world begins to open up to us. Let's look at a few examples."""

tired = ['sleep', 'tired', 'sluggish', 'rest', 'lazy', 'nap', 'couch', "don't care", 'snooze', "can't", 'snack', 'lack', 'too hard', 'negative']
energy = ['yes', 'can', 'energy', 'work', 'hard work', 'goal', 'do it', 'mindset', 'excel', 'succeed', 'hope', 'hopeful']

how = input("How feel you? ")
how = how.split(" ")
if any(word in how for word in tired):  # Any = 'If any slice in cake is equal to slice in the other cake.'
	print("Avoid negativity.")
if any(word in how for word in energy):
	print("Excellent, your great attitude will take you to new heights!")
else:
	print("Okay")

sel = input("Pick 3 numbers (separate each by one space): ").split(" ")
sel = [int(x) for x in sel]

numbers = [25, 47, 88, 903, 601, 1000]

if any(num in sel for num in numbers):
	print("GOOD")
else:
	print("NOT FOUND")

matches = []
for s in sel:
	if s in numbers:
		matches.append(s)
if len(matches) > 2:
	for i, mat in enumerate(matches):
		matches[i] = str(mat)
	print(", ".join(matches), end="")
	print(" were all in my list of favorite numbers.")
elif len(matches) > 1:
	print(f"{matches[0]} and {matches[1]}, ", end="")
	print("were both in my list of favorite numbers.")
elif len(matches) == 1:
	print(f"{matches[0]} was in my list of favorite numbers.")
else:
	print("No matches were found in my list of favorite numbers.")
