import re

import init

data = init.read_data(isTest=False, )

list0, list1 = [], []

for line in data:
	nums = init.ints(line)
	list0.append(nums[0])
	list1.append(nums[1])

sor0, sor1 = sorted(list0), sorted(list1)

def part1():
	distances = []
	for key, val in enumerate(sor0):
		dist = abs(val - sor1[key])
		distances.append(dist)
	# print(distances)
	return sum(distances)


def part2():
	similarities = []
	for val in list0:
		occurances = 0
		for i in list1:
			if i == val:
				occurances += 1
		similarities.append(val*occurances)

	print(similarities)

	return sum(similarities)


print(f'Part 1: {part1()}, Part 2: {part2()}')