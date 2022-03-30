def convert_letter(letter): # Converte as vogais para os símbolos

   letter = letter.upper()

   if(letter == 'A'):

       return '@'

   if(letter == 'E'):

       return '&'

   if(letter == 'I'):

       return '!'

   if(letter == 'O'):

       return '#'

   if(letter == 'U'):

       return '*'

def main():

   nome = input("Digite seu nome: ")

   new_name = ''

   for i in nome: # Realiza a iteração sobre as letras da palavra

       #print(i.upper())

       if(i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U'): #Aqui verificamos se a letra é uma vogal ou não

           new_name += convert_letter(i.upper()) #Função que é chamada para converter a letra

       else:

           new_name += i.upper()


   print(new_name)

if __name__ == '__main__':
    main()   