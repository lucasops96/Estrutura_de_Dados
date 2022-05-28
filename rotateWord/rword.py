def rotate_word(word,value):
    word_rot = ''
    for letter in word:
        cod = ord(letter) + value
        if cod > ord('z'):
            cod -= 26
        elif cod < ord('a'):
            cod += 26
        word_rot += chr(cod)
    return word_rot

def generate_dic(address):
    text_file = open(address,'r')
    word_list = text_file.read().lower().split()
    dictionary = {}
    for i in word_list:
        dictionary[i] = None
    return dictionary

def busca_caesar(dicionario,palavra):
    for i in range(1,14):
        palavra_rot = rotate_word(palavra,i)
        if palavra_rot in dicionario:
            print(palavra,i,palavra_rot)
            return


dic_palavras = generate_dic('rotateWord\words.txt')
print('-----------------')
for palavra in dic_palavras.keys():
    busca_caesar(dic_palavras, palavra)
print('-----------------')

#print(rotate_word('ibm',-1))
