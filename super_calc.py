#!/usr/bin/env python
import sys

def init_allowed_string():
	allowed_string = []
	for i in range(10):
		nbr =  chr(ord("0") + i) 
		allowed_string.append(nbr)
	tmp = ["-", "*", "/", "(", ")", ".", "~", "^", "|"]

	allowed_string.extend(tmp)
	print(allowed_string)
	return allowed_string

def xor2(s1, s2):
	res = ""
	for i,j in zip(s1,s2):
		res += chr(ord(i) ^ ord(j))
	return res

def xor3(s1, s2, s3):
	res = ""
	for i,j,k in zip(s1,s2,s3):
		res += chr(ord(i) ^ ord(j) ^ ord(k))
	return res

def get_xor_string(expected_string, allowed_string):
	w1 = ""
	w2 = ""
	for i in expected_string:
		for j in allowed_string:
			c = chr(ord(i) ^ ord(j))
			if c in allowed_string:
				w1 += j
				w2 += c
				break
	return w1, w2

def get_triple_xor_string(expected_string, allowed_string):
	w1 = w2 = w3 = ""
	for i in expected_string:
		ok = 0
		for j in allowed_string:
			for k in allowed_string:
				c = chr(ord(i) ^ ord(j) ^ ord(k))
				if c in allowed_string:
					w1 += j
					w2 += k
					w3 += c
					ok = 1
					break
			if ok == 1:
				break
	return w1,w2,w3


if __name__ == "__main__":
    mode = int(input("Enter mode: "))
    allowed_string = "".join(init_allowed_string())

    expected_string = input("Enter string: ")
    if (mode == 2): # XOR2
    	w1, w2 = get_xor_string(expected_string, allowed_string)
    	if (xor2(w1, w2) == expected_string):
    		print("Verified")
    		print("\'{}\'^\'{}\'".format(w1, w2))
    	else:
    		print("Not verified")
    elif (mode == 3): # XOR3
    	w1, w2, w3 = get_triple_xor_string(expected_string, allowed_string)
    	if (xor3(w1, w2, w3) == expected_string):
    		print("Verified")
    		print("***{}***".format(xor3(w1,w2,w3)))
    		print("\'{}\'^\'{}\'^\'{}\'".format(w1, w2, w3))
    	else:
    		print("Not verified")