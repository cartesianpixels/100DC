dna_sequence = input("enter the DNA sequence to calculate the nucleotides : \n")
count_a = 0
count_t = 0
count_g = 0
count_c = 0
for nucleotide in dna_sequence:
	if nucleotide == 'A':
		count_a += 1
	elif nucleotide == 'T':
		count_t += 1
	elif nucelotide == 'G':
		count_g += 1
	elif nucleotide == 'C':
		count_c += 1

print('A: ', count_a)
print('T: ', count_t)
print('G: ', count_g)
print('C: ', count_c)