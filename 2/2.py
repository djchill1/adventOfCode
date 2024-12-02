import init

data = init.read_data(isTest=False, )

reports = []
for line in data:
	reports.append(init.ints(line))

print(reports)


def isIncreasing(report):
	return all(i < j for i, j in zip(report, report[1:]))


def isDecreasing(report):
	return all(i > j for i, j in zip(report, report[1:]))


def adjacentDiffers(report):
	return all(0 < abs(j - i) < 4 for i, j in zip(report, report[1:]))


def part1():
	safes = []
	for report in reports:
		if adjacentDiffers(report) and (isIncreasing(report) or isDecreasing(report)):
			safes.append(1)
			print(report, 1)
		else:
			safes.append(0)
			print(report, 0)
	return sum(safes)


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
