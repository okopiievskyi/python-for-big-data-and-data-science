def join_words(*words, sep=', '):
    result = ""
    for i, val in enumerate(words):
        if i == 0:
            result = f"{val}"
        else:
            result = f"{result} {sep} {val}"

    return result
string = join_words("a", "b", "c")
print(string)