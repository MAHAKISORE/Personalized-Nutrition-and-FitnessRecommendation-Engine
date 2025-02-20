import time
import random
import string

# Levenshtein Distance function (from before)
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# Jaro-Winkler Distance function (from before)
def jaro_distance(s1, s2):
    len1, len2 = len(s1), len(s2)
    
    if len1 == 0:
        return 0.0 if len2 == 0 else 1.0
    
    match_distance = max(len1, len2) // 2 - 1
    matches = [False] * len2  # Use len2 to match against s2
    transpositions = 0
    matches_count = 0
    
    # Matching characters within the match distance
    for i in range(len1):
        start = max(0, i - match_distance)
        end = min(len2, i + match_distance + 1)
        
        for j in range(start, end):
            if s1[i] == s2[j] and not matches[j]:
                matches[j] = True
                matches_count += 1
                break
    
    if matches_count == 0:
        return 0.0
    
    # Calculate transpositions
    m_index = 0
    for i in range(len1):
        if matches[i]:
            while not matches[m_index]:
                m_index += 1
            if s1[i] != s2[m_index]:
                transpositions += 1
            m_index += 1
    
    jaro = (matches_count / len1 + matches_count / len2 + (matches_count - transpositions // 2) / matches_count) / 3
    return jaro

def jaro_winkler(s1, s2, p=0.1, max_prefix_len=4):
    jaro_score = jaro_distance(s1, s2)
    prefix_len = 0
    
    # Count the common prefix length (up to max 4 characters)
    for i in range(min(len(s1), len(s2), max_prefix_len)):
        if s1[i] == s2[i]:
            prefix_len += 1
        else:
            break
    
    return jaro_score + p * prefix_len * (1 - jaro_score)

# Function to get suggestions using Levenshtein Distance
def get_suggestions_levenshtein(input_word, word_list, top_n=5):
    similarities = [(word, levenshtein_distance(input_word, word)) for word in word_list]
    sorted_suggestions = sorted(similarities, key=lambda x: x[1])
    return [word for word, score in sorted_suggestions[:top_n]]

# Function to get suggestions using Jaro-Winkler Distance
def get_suggestions_jaro_winkler(input_word, word_list, top_n=5):
    similarities = [(word, jaro_winkler(input_word, word)) for word in word_list]
    sorted_suggestions = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [word for word, score in sorted_suggestions[:top_n]]

# Benchmarking function
def benchmark(input_word, word_list):
    print(f"Benchmarking for input word: {input_word}")
    
    # Levenshtein Distance
    start_time = time.time()
    levenshtein_suggestions = get_suggestions_levenshtein(input_word, word_list)
    lev_time = time.time() - start_time
    print(f"Levenshtein Distance Suggestions: {levenshtein_suggestions} (Time: {lev_time:.5f} seconds)")
    
    # Jaro-Winkler Distance
    start_time = time.time()
    jaro_winkler_suggestions = get_suggestions_jaro_winkler(input_word, word_list)
    jw_time = time.time() - start_time
    print(f"Jaro-Winkler Distance Suggestions: {jaro_winkler_suggestions} (Time: {jw_time:.5f} seconds)")

# Example usage
if __name__ == "__main__":
    # Create a word list for testing
    word_list = ["apple", "banana", "grape", "applause", "orange", "application", "apply", "application", "appeal", "appetizer", "appetizing"]
    
    # Random input word to test
    input_word = "apl"
    
    # Run benchmark
    benchmark(input_word, word_list)
