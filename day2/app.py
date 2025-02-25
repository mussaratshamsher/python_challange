

# User se input lena  
user_sentence = input("Write down your sentence: ")  

# Sentence mein words ko count karna  
word_count = len(user_sentence.split())  

# Words ko reverse order mein arrange karna  
reversed_words = ' '.join(user_sentence.split()[::-1])  

# Count aur reversed words ko print karna  
print(f"Your sentence has total {word_count} words.")  
print("your message in reverse order:")  
print(reversed_words)