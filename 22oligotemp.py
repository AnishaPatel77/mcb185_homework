# 22oligotemp.py by Anisha Patel

def tm(A, C, G, T):
	oligo = A + C + G + T
	if oligo <= 13:
		melting_temp = (A + T) * 2 + (G + C) * 4
	elif oligo > 13:
		melting_temp = (64.9 + (41 * (G + C - 16.4))) / (A + T + G + C)
	return melting_temp 
	
print("Tm:", tm(1, 2, 3, 4), "degrees") # oligo length < 13
print("Tm:", tm(1, 3, 4, 5), "degrees") # oligo length = 13
print("Tm:", tm(3, 4, 5, 6), "degrees") # oligo length > 13

