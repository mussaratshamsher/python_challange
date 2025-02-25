

# User input 
user_sentence = input("Write down your sentence: ")  

# wirds in Sentence  
word_count = len(user_sentence.split())  

# Arranging Words into reverse order 
reversed_words = ' '.join(user_sentence.split()[::-1])  

# to print Count and reversed words 
print(f"Your sentence has total {word_count} words.")  
print("your message in reverse order:")  
print(reversed_words)