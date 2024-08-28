
def reverse_word(word):
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

if __name__ == "__main__":
    user_input = input("Enter a word to reverse: ")
    reversed_word = reverse_word(user_input)
    print("Reversed word:", reversed_word)
