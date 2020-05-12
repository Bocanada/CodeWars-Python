def anagrams(word, words):
    # your code here
    return [wrd for wrd in words if set(word) == set(wrd) and len(wrd) == len(word)]
