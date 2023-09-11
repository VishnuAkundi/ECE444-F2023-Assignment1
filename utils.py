class utils:
	def reversed(self, n):
		'''
		Takes in number n and returns reversed number as int
		'''
		if isinstance(n, int):
			if n < 0:
				temp = str(n)[1:]
				ans = int("-" + temp[::-1])
			else:
				ans = int(str(n)[::-1])
			
			return ans
		else:
			return False
	
	def formatter(self, n):
		'''
		Takes an integer and returns tuple of bin and oct versions of integer
		'''
		if isinstance(n, int):
			return bin(n), oct(n)
		return False

