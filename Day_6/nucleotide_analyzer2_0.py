while True:
    dna_sequence = input("Enter a DNA sequence (or 'exit' to quit): ")
    
    if dna_sequence.lower() == 'exit':
        print("Exiting the program.")
        break
    
    nucleotide_to_count = "A"
    
    count = 0
    
    for nucleotide in dna_sequence:
        if nucleotide == nucleotide_to_count:
            count += 1
    
    print(f"The nucleotide {nucleotide_to_count} appears {count} times in the DNA sequence.\n")
