from translate import Translator
translator= Translator(to_lang="es")
try:
    with open('ta/tap.txt', mode='r') as my_file:
        # text = 'Hey Tapty, Do you love me?'
        # text = my_file.write('Hey Tapty, Do you love me?')
        # print(text)
        text = my_file.read()
        translated = translator.translate(text)
        # writefile =  my_file.write(text)
        # print(writefile)
        print(translated)
except FileNotFoundError as err:
    print('File does not found')