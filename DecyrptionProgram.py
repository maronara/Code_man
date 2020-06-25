
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = -3
newMessage = ''

message = input('Please enter an encrypted message: ')

for character in message:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]

    newMessage += newCharacter

print('Your decrypted message is', newMessage)
