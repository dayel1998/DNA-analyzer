#! /Desktop/python> ./gc.py
"""
This is my first python program.
It compete the GC content of a DNA sequence.
"""
# Get the DNA sequence:
DNA = input("Enter the DNA sequence, please:")
output=
# Count C's in DNA sequence
NO.C = DNA.count('C')
# Count G's in DNA sequence
NO.G = DNA,count('G')
# Get the length of the DNA sequence
DNA_length = len(DNA)
# Compute GC percentage
GC_prec = (NO_C+NO_G) * 100 / DNA_length
# Print GC% to screen
print("The DNA sequence's GC content is %5.3f%%" % GC_prec)
