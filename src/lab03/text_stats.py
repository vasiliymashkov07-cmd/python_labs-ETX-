import sys
from defsfromtext import normalize,tokenize,top_n,count_freq

def stats(text:str):
    normalized_text = normalize(text)
    splittedwords = normalized_text.split()\
    
    list_count = len(splittedwords)
    unique_list_count = len(set(splittedwords))
    top_words = top_n(normalized_text, 5)

    print(f"Всего слов: {list_count}")
    print(f"Уникальных слов: {unique_list_count}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

text_in = sys.stdin.read