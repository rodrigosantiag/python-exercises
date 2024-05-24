def find_anagrams(word, candidates):
    result = []
    word = word.lower()
    word_letters = count_letters(word)

    for candidate in candidates:
        candidate_lower = candidate.lower()

        if candidate_lower == word:
            continue

        candidate_letters = count_letters(candidate_lower)

        if word_letters == candidate_letters:
            result.append(candidate)

    return result

def most_frequent_number(arr, length):
    frequency_count = {}

    for num in arr:
        if num in frequency_count:
            frequency_count[num] += 1
        else:
            frequency_count[num] = 1

    max_frequency = 0
    most_frequent_num = None

    for num, frequency in frequency_count.items():
        if frequency > max_frequency or (frequency == max_frequency and num < most_frequent_num):
            max_frequency = frequency
            most_frequent_num = num

    return most_frequent_num



def count_letters(word):
    word = word.lower()
    result = {}

    for char in word:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result
