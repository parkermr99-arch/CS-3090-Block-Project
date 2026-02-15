"""
This is a simple encryption tool used for demonstrating an ethical hacking/security concept for CS 3090: Ethics in Computing.
Please keep in mind that this tool is intentionally simple, and only works for a specific set of characters. This tool is
meant for educational purposes!

Author: Parker Rowe
Updated: February 13, 2026
"""


def encrypt_message(message: str) -> str:
    """
    This function encrypts the given message by mapping each character to a hexadecimal value. If the number is even, it
    divides the number by two, and if the number is odd, it subtracts 50 from that number. This just demonstrates some
    mappings and simple math to encrypt a message of characters into numbers that are less easily decipherable to read.
    :param message: the message to be encrypted.
    :return: a string of numbers representing the encrypted version of the message.
    """

    # The string that will hold the encrypted message.
    encrypted_message = ""

    # The dictionary of character : hexadecimal mappings.
    hex_dictionary = {'A': 0xA01, 'B': 0xA02, 'C': 0xA03, 'D': 0xA04, 'E': 0xA05, 'F': 0xA06, 'G': 0xA07, 'H': 0xA08, 'I': 0xA09,
                      'J': 0xA10, 'K': 0xA11, 'L': 0xA12, 'M': 0xA13, 'N': 0xA14, 'O': 0xA15, 'P': 0xA16, 'Q': 0xA17, 'R': 0xA18,
                      'S': 0xA19, 'T': 0xA20, 'U': 0xA21, 'V': 0xA22, 'W': 0xA23, 'X': 0xA24, 'Y': 0xA25, 'Z': 0xA26, 'a': 0xB01,
                      'b': 0xB02, 'c': 0xB03, 'd': 0xB04, 'e': 0xB05, 'f': 0xB06, 'g': 0xB07, 'h': 0xB08, 'i': 0xB09, 'j': 0xB10,
                      'k': 0xB11, 'l': 0xB12, 'm': 0xB13, 'n': 0xB14, 'o': 0xB15, 'p': 0xB16, 'q': 0xB17, 'r': 0xB18, 's': 0xB19,
                      't': 0xA20, 'u': 0xA21, 'v': 0xA22, 'w': 0xA23, 'x': 0xA24, 'y': 0xA25, 'z': 0xA26, '0': 0xD01, '1': 0xD02,
                      '2': 0xD03, '3': 0xD04, '4': 0xD05, '5': 0xD06, '6': 0xD07, '7': 0xD08, '8': 0xD09, '9': 0xD10, '!': 0xE01,
                      '@': 0xE02, '#': 0xE03, '$': 0xE04, '%': 0xE05, '^': 0xE06, '&': 0xE09, '*': 0xE10, ' ': 0xE11}

    # Perform the encryption process for the given message.
    for character in message:
        hex_value = hex_dictionary[character]

        if hex_value % 2 == 0:
            hex_value = hex_value // 2
        else:
            hex_value -= 50

        encrypted_message += str(hex_value)
        encrypted_message += " "

    return encrypted_message


def main():
    """
    Prompts the user to input a message they want to encrypt and then prints the resulting encrypted message. When given
    an empty message, an error message will be printed and the function returns. This also assumes that the user only
    inputs characters that are valid as defined in the print messages. (This is for simplicity purposes!)
    """
    print("Welcome to my simple encryption tool!")
    print("This encryption works for lowercase letters, uppercase letters, digits, spaces, and the following special characters: ! @ # $ % ^ & *")
    print("If your message contains anything other than the characters specified above, the encryption will not work properly!")
    input_message = input("Type your message to be encrypted here: ")

    # Empty messages are not accepted.
    if input_message == "":
        print("Error: Message cannot be empty. Please try again.")
        return

    encrypted_message = encrypt_message(input_message)
    print(f"Your encrypted message is: {encrypted_message}")


if __name__ == "__main__":
    main()
