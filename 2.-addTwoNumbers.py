class Problem():
	def main(self, l1, l2):
		if l1[0] == 0 or l2[0] == 0:
			return [0]

		elif len(l1) == len(l2):
			for i in range(len(l1)):
				if l1[i] + l2[i] <= 9:
					l1[i] += l2[i]
				elif l1[i] + l2[i] > 9:
					l1[i] += l2[i] - 10
					if i < len(l1)-1:
						l1[i +1] += 1
					if i == len(l1)-1:
                                                l1.append(1)

			return l1
		elif len(l1) != len(l2):
			max_list = max(l1,l2, key=len)
			min_list = min(l1,l2, key=len)
			rest = len(max_list) - len(min_list)
			for i in range(rest):
				min_list.append(0)
			return Problem.main(self, max_list, min_list)

solution = Problem()
result = solution.main

print(result([2,4,3], [5,6,4]))
print(f"espc = {[7,0,8]}")
print(" ")

print(result([2,4,3,1], [5,6,8,1]))
print(f"espc = {[7,0,2,3]}")
print(" ")

print(result([3,4,7], [5,4,9]))
print(f"espc = {[8,8,6,1]}")
print(" ")

print(result([0], [0]))
print(f"espc = {[0]}")
print(" ")

print(result([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 0, 0, 0]))
print(f"espc = {[8, 9, 9, 9, 0, 0, 0, 1]}")
print(" ")

print(result([9,9,9,9,9,9,9], [9,9,9,9]))
print(f"espc = {[8,9,9,9,0,0,0,1]}")
print(" ")
