import string
import random

vowels = 'aeiou'
consonants = 'bcdfghijklmnpqrstvwxz'


def get_letter(last_letter=None):
    # Check if last letter generated was a consonant
    if last_letter:
        last_letter = ''.join(last_letter)
        last_letter_was_consonant = last_letter in consonants
    else:
        last_letter_was_consonant = False

    # If last letter was a vowel, make it 50% chance to generate a consonant
    if not last_letter_was_consonant and bool(random.randint(0, 1)):
        last_was_consonant = True
        yield random.choice(consonants)
    else:
        last_was_consonant = False
        yield random.choice(vowels)


def generate_word(length, spread=0):
    word = list()

    for i in range(length + random.randint(1, spread)):
        word.append(next(get_letter(last_letter=word[-1:])))

    return ''.join(word).capitalize()


if __name__ == '__main__':
    print('Generating 10 random names:')
    for i in range(10):
        print(generate_word(length=5, spread=3))