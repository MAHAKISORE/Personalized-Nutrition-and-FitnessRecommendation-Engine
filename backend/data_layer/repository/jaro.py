import json

class JaroWrinklerSearching():
    def __init__(self,datas:list):
        self.datas:list = datas

    def jaro_similarity(self,s1, s2):
        """Compute the Jaro similarity between two strings."""
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 == 0 and len_s2 == 0:
            return 1.0

        match_distance = max(len_s1, len_s2) // 2 - 1
        s1_matches = [False] * len_s1
        s2_matches = [False] * len_s2

        matches = 0
        transpositions = 0

        # Step 1: Count matches
        for i in range(len_s1):
            start = max(0, i - match_distance)
            end = min(i + match_distance + 1, len_s2)

            for j in range(start, end):
                if s2_matches[j]:
                    continue
                if s1[i] == s2[j]:
                    s1_matches[i] = True
                    s2_matches[j] = True
                    matches += 1
                    break

        if matches == 0:
            return 0.0

        # Step 2: Count transpositions
        s1_match_chars = [s1[i] for i in range(len_s1) if s1_matches[i]]
        s2_match_chars = [s2[j] for j in range(len_s2) if s2_matches[j]]

        for i in range(len(s1_match_chars)):
            if s1_match_chars[i] != s2_match_chars[i]:
                transpositions += 1

        transpositions //= 2  # Since each transposition counts twice

        jaro_score = (matches / len_s1 + matches / len_s2 + (matches - transpositions) / matches) / 3
        return jaro_score

    def jaro_winkler_similarity(self,s1, s2, prefix_scale=0.1):
        """Compute the Jaro-Winkler similarity between two strings."""
        jaro_sim = self.jaro_similarity(s1, s2)

        # Step 3: Compute prefix scaling
        prefix_length = 0
        max_prefix_length = min(4, min(len(s1), len(s2)))  # Winkler suggests up to 4 characters

        for i in range(max_prefix_length):
            if s1[i] == s2[i]:
                prefix_length += 1
            else:
                break

        return jaro_sim + (prefix_length * prefix_scale * (1 - jaro_sim))

    def hybrid_search(self,query, top_n=5):
        """Hybrid search using Jaro-Winkler similarity, tokenization, and substring matching."""
        query_lower = query.lower()
        results = []

        for name in self.datas:
            
            name_lower = str(name.name)
            print(name_lower)

            # Compute Jaro-Winkler similarity
            similarity = self.jaro_winkler_similarity(query_lower, name_lower)

            # Tokenize the name
            name_tokens = name_lower.split()

            # **Prefix Match Boost:** If any word starts with the query
            for token in name_tokens:
                if token.startswith(query_lower):
                    similarity += 0.2  # Strong boost for direct word match

            # **Substring Boost:** If the query appears anywhere in the name
            if query_lower in name_lower:
                similarity += 0.1  # Small boost for partial matches
            name.similarity = similarity
            results.append(name)

        # Sort by similarity score (higher is better)
    
        # results.sort(key=lambda x: x.similarity, reverse=True)
        for i in range(0,len(results)):
            for j in range(0,len(results)-1):
                if(results[j].similarity < results[j+1].similarity):
                    temp = results[j]
                    results[j] =  results[j+1]
                    results[j+1] = temp
        return results[:top_n]  # Return top matches


