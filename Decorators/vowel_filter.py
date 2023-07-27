def vowel_filter(function):
    vowels = 'aeiou'

    def wrapper():
        return [a for a in function() if a in vowels]

    return wrapper
