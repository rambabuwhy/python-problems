def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for c in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if c.isalpha():
			new_string = c.lower()+new_string
			reverse_string = reverse_string + c.lower()
	# Compare the strings
	#print(new_string)
	#print(reverse_string)
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True