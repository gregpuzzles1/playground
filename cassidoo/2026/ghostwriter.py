# Cassidoo question of the week:
# October 19th, 2026
#
# Question:
# There's a ghost in your keyboard! It keeps typing weird symbols
# in your words. Given a string you typed (with the ghost),
# # deletes the last character and ~ duplicates it, if one exists.
# Return the final text.


def ghostwriter(text):
    result = []

    for char in text:
        if char == "#":
            if result:
                result.pop()
        elif char == "~":
            if result:
                result.append(result[-1])
        else:
            result.append(char)

    return "".join(result)


print(ghostwriter("ghost"))   # ghost
print(ghostwriter("a#~b"))     # b
print(ghostwriter("ab~c#"))    # abb
print(ghostwriter("BBB##O~"))  # BOO
