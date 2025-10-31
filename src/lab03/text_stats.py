import sys
from defsfromtext import normalize, tokenize, count_freq, top_n
def main():
    
    text = "Привет, мир! Привет!!!"
    

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    total_words = len(tokens)
    freq_dict = count_freq(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
   
    for word, count in top_words:
        print(f"{word}:{count}")

main() 


