def lengthOfLongestSubstring(s):
	if s == "":
		return 0
	else:
		list = []
		maxl = []
		for i in s:
			if list.count(i) == 0:
				list.append(i)
				
			else:
				if len(list) > len(maxl):
					maxl = list.copy()
				list.clear()
				list.append(i)
		return  len(maxl) #len(max(maxl, list, key=len))

print('Result:  ', lengthOfLongestSubstring("abcabcbbxxyza"), '	Expected: 3')
print('Result:  ', lengthOfLongestSubstring("bbbb"), '	Expected: 1')
print('Result:  ', lengthOfLongestSubstring("bbabb"), '  Expected: 2')
print('Result:  ', lengthOfLongestSubstring("pwwkew"), '	Expected: 3')
print('Result:  ', lengthOfLongestSubstring(""), '	Expected: 0')
