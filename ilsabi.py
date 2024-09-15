#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from itertools import product

# Initial consonant (choseong) Romanization
initial_consonants = {
    'ㄱ': ['g', 'k'],
    'ㄲ': ['kk'],
    'ㄴ': ['n'],
    'ㄷ': ['d', 't'],
    'ㄸ': ['tt'],
    'ㄹ': ['r', 'l'],
    'ㅁ': ['m'],
    'ㅂ': ['b', 'p'],
    'ㅃ': ['pp'],
    'ㅅ': ['s'],
    'ㅆ': ['ss'],
    'ㅇ': [''],  # Silent as initial consonant
    'ㅈ': ['j'],
    'ㅉ': ['jj'],
    'ㅊ': ['ch'],
    'ㅋ': ['k'],
    'ㅌ': ['t'],
    'ㅍ': ['p'],
    'ㅎ': ['h'],
}

# Medial vowel (jungseong) Romanization
medial_vowels = {
    'ㅏ': ['a'],
    'ㅐ': ['ae'],
    'ㅑ': ['ya'],
    'ㅒ': ['yae'],
    'ㅓ': ['eo'],
    'ㅔ': ['e'],
    'ㅕ': ['yeo'],
    'ㅖ': ['ye'],
    'ㅗ': ['o'],
    'ㅘ': ['wa'],
    'ㅙ': ['wae'],
    'ㅚ': ['oe'],
    'ㅛ': ['yo'],
    'ㅜ': ['u'],
    'ㅝ': ['wo'],
    'ㅞ': ['we'],
    'ㅟ': ['wi'],
    'ㅠ': ['yu'],
    'ㅡ': ['eu'],
    'ㅢ': ['ui'],
    'ㅣ': ['i'],
}

# Final consonant (jongseong) Romanization
final_consonants = {
    '': [''],  # No final consonant
    'ㄱ': ['k', 'g'],
    'ㄲ': ['k'],
    'ㄳ': ['ks'],
    'ㄴ': ['n'],
    'ㄵ': ['nch'],
    'ㄶ': ['nh'],
    'ㄷ': ['t', 'd'],
    'ㄹ': ['l', 'r'],
    'ㄺ': ['lk', 'rg'],
    'ㄻ': ['lm', 'rm'],
    'ㄼ': ['lp', 'rb'],
    'ㄽ': ['ls', 'rs'],
    'ㄾ': ['lt'],
    'ㄿ': ['lp'],
    'ㅀ': ['lh'],
    'ㅁ': ['m'],
    'ㅂ': ['p', 'b'],
    'ㅄ': ['ps'],
    'ㅅ': ['t', 's'],
    'ㅆ': ['t', 'ss'],
    'ㅇ': ['ng', ''],
    'ㅈ': ['t', 'j'],
    'ㅊ': ['t', 'ch'],
    'ㅋ': ['k'],
    'ㅌ': ['t'],
    'ㅍ': ['p'],
    'ㅎ': ['h'],
}

# Generate Romanizations for a syllable block
def romanize_syllable(initial, medial, final=''):
    initial_options = initial_consonants.get(initial, [initial])
    medial_options = medial_vowels.get(medial, [medial])
    final_options = final_consonants.get(final, ['']) if final else ['']
    return [''.join(combo) for combo in product(initial_options, medial_options, final_options)]

# Hangul to English keyboard mapping
hangul_to_english = {
    'ㅂ': 'q', 'ㅈ': 'w', 'ㄷ': 'e', 'ㄱ': 'r', 'ㅅ': 't', 'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o', 'ㅔ': 'p',
    'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k', 'ㅣ': 'l',
    'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm',
    'ㅃ': 'Q', 'ㅉ': 'W', 'ㄸ': 'E', 'ㄲ': 'R', 'ㅆ': 'T', 'ㅒ': 'O', 'ㅖ': 'P',
}

# Decompose a Korean syllable
def decompose_hangul(syllable):
    # Unicode constants for Hangul composition
    BASE_CODE, CHOSEONG, JUNGSEONG = 44032, 588, 28

    # Choseong, Jungseong, and Jongseong (initial, medial, final ranges)
    initial_list = list(initial_consonants.keys())
    medial_list = list(medial_vowels.keys())
    final_list = list(final_consonants.keys())

    # Convert syllable into a Unicode integer
    char_code = ord(syllable) - BASE_CODE

    # Decompose the syllable into its three parts
    initial = char_code // CHOSEONG
    medial = (char_code % CHOSEONG) // JUNGSEONG
    final = char_code % JUNGSEONG

    # Map to Hangul components
    return initial_list[initial], medial_list[medial], final_list[final]

# Convert a Hangul string to an English-typed version
def hangul_to_english_typed(input_str):
    english_typed = []
    for syllable in input_str:
        if '\uac00' <= syllable <= '\ud7a3':  # Check if the character is a Hangul syllable block
            initial, medial, final = decompose_hangul(syllable)
            english_typed.append(hangul_to_english.get(initial, ''))
            english_typed.append(hangul_to_english.get(medial, ''))
            if final != '':  # Include final consonant if it exists
                english_typed.append(hangul_to_english.get(final, ''))
        else:
            english_typed.append(syllable)  # If it's not Hangul, keep it as-is
    return ''.join(english_typed)

# Romanize a string, handling both English and Korean characters
def romanize_string(input_str):
    romanized_name = []
    
    for char in input_str:
        if '\uac00' <= char <= '\ud7a3':  # Check if the character is Korean
            initial, medial, final = decompose_hangul(char)
            romanized_syllables = romanize_syllable(initial, medial, final)
            romanized_name.append(romanized_syllables)
        else:
            romanized_name.append([char])  # If it's not Korean, keep it as-is

    # Generate all combinations of romanized syllables and original characters
    full_name_variations = [''.join(combo) for combo in product(*romanized_name)]
    return full_name_variations

# Add capitalization variations
def capitalize_variations(romanized_names):
    capitalized_variants = set()
    for name in romanized_names:
        capitalized_variants.add(name)
        capitalized_variants.add(name.capitalize())
        capitalized_variants.add(name.upper())
    return capitalized_variants

# Main wordlist generation
def generate_wordlist(user_data):
    wordlist = set()

    # Romanized versions of surname and first name
    surname_romanized = romanize_string(user_data['surname'])
    firstname_romanized = romanize_string(user_data['firstname'])

    surname_variants = capitalize_variations(surname_romanized)
    firstname_variants = capitalize_variations(firstname_romanized)

    # Add combinations of surname and first name
    for s in surname_variants:
        for f in firstname_variants:
            wordlist.add(s + f)
            wordlist.add(f + s)

    # Add other fields like nickname, partner's name, birthday, company, etc.
    other_fields = ['nickname', 'partner_name', 'kid_name', 'pet_name', 'company_name', 'uni']
    for field in other_fields:
        if user_data[field]:
            field_variants = capitalize_variations(romanize_string(user_data[field]))
            for variant in field_variants:
                for s in surname_variants:
                    wordlist.add(s + variant)
                for f in firstname_variants:
                    wordlist.add(f + variant)

    # Add random numbers and special characters (optional)
    if user_data['add_numbers']:
        numbers = ['123', '456', '789', '000']
        for num in numbers:
            for s in surname_variants:
                wordlist.add(s + num)
            for f in firstname_variants:
                wordlist.add(f + num)

    if user_data['add_special_chars']:
        special_chars = ['!', '@', '#', '$']
        for char in special_chars:
            for s in surname_variants:
                wordlist.add(s + char)
            for f in firstname_variants:
                wordlist.add(f + char)

    # Add prepend and append characters (optional)
    if user_data['prepend_append']:
        prepend_append_chars = ['xx', '00', '123']  
        for char in prepend_append_chars:
            for s in surname_variants:
                wordlist.add(char + s + char)
            for f in firstname_variants:
                wordlist.add(char + f + char)

    # Add English-typed versions of Hangul names (e.g., "박지민 = wkawlals")
    surname_english_typed = hangul_to_english_typed(user_data['surname'])
    firstname_english_typed = hangul_to_english_typed(user_data['firstname'])

    # Apply the same logic for English-typed versions (wlalsqkr, etc.)
    if surname_english_typed:
        wordlist.add(surname_english_typed)
    if firstname_english_typed:
        wordlist.add(firstname_english_typed)
    if surname_english_typed and firstname_english_typed:
        wordlist.add(surname_english_typed + firstname_english_typed)
        wordlist.add(firstname_english_typed + surname_english_typed)

    # Apply numbers, special characters, prepend/append to English-typed names
    if user_data['add_numbers']:
        for num in numbers:
            wordlist.add(surname_english_typed + num)
            wordlist.add(firstname_english_typed + num)
            wordlist.add(num + surname_english_typed)
            wordlist.add(num + firstname_english_typed)

    if user_data['add_special_chars']:
        for char in special_chars:
            wordlist.add(surname_english_typed + char)
            wordlist.add(firstname_english_typed + char)
            wordlist.add(char + surname_english_typed)
            wordlist.add(char + firstname_english_typed)

    if user_data['prepend_append']:
        for char in prepend_append_chars:
            wordlist.add(char + surname_english_typed + char)
            wordlist.add(char + firstname_english_typed + char)

    return wordlist

# Prompts to enter user information
def interactive_input():
    print("==== ILSABI 일반 사용자 비번 프로파일러 ====")
    user_data = {}

    # Basic information
    user_data['surname'] = input("Surname (Korean/English): ").strip()
    user_data['firstname'] = input("First name (Korean/English): ").strip()
    user_data['nickname'] = input("Nickname (optional, Korean/English): ").strip()

    # Additional fields
    user_data['partner_name'] = input("Partner's name (optional, Korean/English): ").strip()
    user_data['kid_name'] = input("Kid's name (optional, Korean/English): ").strip()
    user_data['pet_name'] = input("Pet's name (optional, Korean/English): ").strip()
    user_data['company_name'] = input("Company name (optional, Korean/English): ").strip()
    user_data['uni'] = input("University/school name (optional, Korean/English): ").strip()
    user_data['birthday'] = input("Birthday (optional, e.g., 19900101): ").strip()

    # Options for adding numbers and special characters
    add_numbers = input("Do you want to add random numbers at the end (Y/n)? ").strip().lower()
    user_data['add_numbers'] = add_numbers == 'y' or add_numbers == ''

    add_special_chars = input("Do you want to add special characters at the end (Y/n)? ").strip().lower()
    user_data['add_special_chars'] = add_special_chars == 'y' or add_special_chars == ''

    prepend_append = input("Do you want to prepend/append common characters (Y/n)? ").strip().lower()
    user_data['prepend_append'] = prepend_append == 'y' or prepend_append == ''

    return user_data

# Save the generated wordlist to a file
def save_wordlist(wordlist, filename='wordlist.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for word in wordlist:
            f.write(word + '\n')
    print(f"[+] Wordlist saved to {filename}")

# Main function
def main():
    # Interactive input from the user
    user_data = interactive_input()

    # Generate the wordlist based on the input
    wordlist = generate_wordlist(user_data)
    
    # Save the wordlist to a file
    save_wordlist(wordlist, 'wordlist.txt')

if __name__ == "__main__":
    main()

