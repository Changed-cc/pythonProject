letters = input()
letters.lower()
vowel_letter = 0
consonant_letter = 0
for letter in letters:
  if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    vowel_letter += 1
  else:
    consonant_letter += 1
print(vowel_letter)
print(consonant_letter)