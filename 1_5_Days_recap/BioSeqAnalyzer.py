import random

# Generate a list of random DNA sequences
def generate_random_sequence(length):
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choice(bases) for _ in range(length))

num_sequences = 10
sequence_length = 20

random_sequences = [generate_random_sequence(sequence_length) for _ in range(num_sequences)]

# Filter sequences based on criteria
filtered_sequences = []
for sequence in random_sequences:
    if 'ATG' in sequence and 'TAA' in sequence:
        filtered_sequences.append(sequence)

# Print the results
print("Generated random sequences:")
for i, sequence in enumerate(random_sequences):
    print(f"Sequence {i + 1}: {sequence}")

print("\nFiltered sequences with 'ATG' and 'TAA':")
for i, sequence in enumerate(filtered_sequences):
    print(f"Filtered Sequence {i + 1}: {sequence}")
