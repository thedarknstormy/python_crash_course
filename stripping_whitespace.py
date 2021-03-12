#this is accidental whitespace
favorite_language = 'python '
print(favorite_language)

#this is how to temporarily strip the whitespace on the right end of a string
print(favorite_language.rstrip())

#this is how to permanently strip the whitespace on the right end of a string
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

#this is how to permanently strip the whitespace on the left end of a string
favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print(favorite_language)

#this is how to permanently strip whitespace on both sides of a string
favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)