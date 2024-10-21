def criptografar(text, key):
    result = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                number = int(ord(letter))
                newNumber = (number - ord('A') + key) % 26 + ord('A')
            else:
                number = int(ord(letter))
                newNumber = (number - ord('a') + key) % 26 + ord('a')
            newLetter = chr(newNumber)
            result += newLetter
        else:
            result += letter    
    return result
def descriptografar(text, key):
    result = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                number = int(ord(letter))
                newNumber = (number - ord('A') - key) % 26 + ord('A')
            else:
                number = int(ord(letter))
                newNumber = (number - ord('a') - key) % 26 + ord('a')
            newLetter = chr(newNumber)
            result += newLetter
        else:
            result += letter    
    return result

text = str(input("Digite sua mensagem: "))
operation = int(input("\no que deseja? (digite apenas o numero) \n1 - criptografar\n2 - descriptografar \n: "))
if operation == 1: 
    chave = int(input("\ninforme o índice de deslocamento: "))
    print("\nMensagem criptografada -> (-", criptografar(text, chave),"-)\n")
else:
    chave = int(input("\ninforme o índice de \ndeslocamento da cifra: "))
    print("\nMensagem descriptografada -> (-", descriptografar(text, chave),"-)\n")