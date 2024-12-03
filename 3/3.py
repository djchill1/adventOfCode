import init
import re

data = init.read_data(isTest=False, value="str")

print(data)



def part1():
	output = []
	# for line in data:
	# 	x = re.findall('mul\([0-9]+\,[0-9]+\)', line)
	# 	print(x)
	# 	for entry in x:
	# 		vals = init.ints(entry)
	# 		print(vals)
	# 		output.append(vals[0]*vals[1])
	return sum(output)


def part2():
	output = []
	enabled = True
	for line in data:
		x = re.findall('mul\([0-9]+\,[0-9]+\)' + '|' + 'do\(\)' + '|' +  'don\'t\(\)', line)
		print(x)
		for entry in x:
			if entry[0] == 'm' and enabled:
				vals = init.ints(entry)
				print(vals)
				output.append(vals[0]*vals[1])
			elif entry == 'don\'t()':
				print('disabled')
				enabled = False
			elif entry == 'do()':
				print('enabled')
				enabled = True
	return sum(output)


print(f'Part 1: {part1()}, Part 2: {part2()}')