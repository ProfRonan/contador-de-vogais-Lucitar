"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    vogais = 0
    for letter in string:
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            vogais += 1
    return vogais
    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
