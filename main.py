# letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
# let_list = letters.rsplit(" ")
# print(let_list)

let_list = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# morse_let_list = ".- / -... / -.-. / -.. / . / ..-. / --. / .... / .. / .--- / -.- / .-.. / -- / -. / --- / .--. / --.- / .-. / ... / - / ..- / ...- / .-- / -..- / -.-- / --..".rsplit(" / ")
# print(morse_let_list)

morse_let_list = ['/', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

# myDict = { k:v for (k,v) in zip(let_list, morse_let_list)}
# print(myDict)

dict = {' ': '/', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

while True:
    list = []
    str =" "
    req = input("Text to convert (Q to exit): (No fancy characters please "
                  "only space and letters): ").lower()
    for let in req:
        list.append(dict[f"{let}"])
    print(str.join(list))

    if req == "q":
        break



