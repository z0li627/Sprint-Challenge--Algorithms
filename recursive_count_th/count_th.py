'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word = "ojndcthlhtwkencthth"

def count_th(word, i = 0, counter = 0):
    if len(word) < 2:
        return 0
    if (word[i] + word[i+1]) == "th":
        counter += 1
        i += 1
    else:
        counter = counter
        i += 1
    return counter + count_th(word[i:])


print(count_th(word))


