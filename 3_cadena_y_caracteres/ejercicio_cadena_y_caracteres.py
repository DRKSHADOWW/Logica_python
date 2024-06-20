#EJERCICIO

# Crea un programa que analice dos palabras diferentes y realice comprobraciones para descrubir si son:
# 1. Palíndromas
# 2. Anagramas
# 3. Igual


word1 = input("escribe una palabra: ")
word2 = input("escribe una palabra: ")

def check(word1: str, word2: str):
    
    #Palindromos
    if word1 == word2[::-1]: # (slicing)
        print(f"{word1} es un palíndromo de {word2}")
    else:
        print(f"{word1} no es un palíndromo de {word2}")
        
    # Anagramas
    if sorted(word1) == sorted(word2): # sorted() ordena las letras
        print(f"{word1} es un anagrama de {word2}")
    else:
        print(f"{word1} no es un anagrama de {word2}")
    
    # Isogramas
    def isogram(word: str) -> bool:
        word_dict = {}
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1
            
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
            
        return isogram
        
    print(f"¿{word1} es un isograma?: {isogram(word1)}")    
    print(f"¿{word2} es un isograma?: {isogram(word2)}")    
        
        
        
    
check(word1, word2)
    
   
        
            
    
         
            
        
        
        
    
    
   
        
                    
        
       
           
           
    
   
        
        
        

            