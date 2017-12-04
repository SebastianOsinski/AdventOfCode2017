file = open("day4_input", "r")

passphrases = file.readlines()

def count_valid_passphrases(passphrases, is_valid):
    valid_count = 0
    for passphrase in passphrases:
        words = passphrase.rstrip("\n").split(" ")
        if is_valid(words):
            valid_count += 1
    return valid_count

# Part 1

def has_no_duplicates(passphrase_words):
    return len(passphrase_words) == len(set(passphrase_words))

print(count_valid_passphrases(passphrases, has_no_duplicates))

# Part 2

def are_anagrams(word_1, word_2):
    if len(word_1) != len(word_2):
        return False
    return sorted(word_1) == sorted(word_2)

def has_no_anagrams(passphrase_words):
    no_of_words = len(passphrase_words)
    for i in range(0, no_of_words):
        for j in range(0, no_of_words):
            if i == j:
                continue
            if are_anagrams(passphrase_words[i], passphrase_words[j]):
                return False
    return True

print(count_valid_passphrases(passphrases, has_no_anagrams))
