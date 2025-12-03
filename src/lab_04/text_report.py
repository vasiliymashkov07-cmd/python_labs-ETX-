import sys

sys.path.append(r"C:\GitHub_Misis\python_labs-ETX-\src\lib")
from text import normalize, tokenize, top_n, count_freq

from io_txt_csv import read_text, write_csv


def text_stats(text_optimisation):
    text_optimisation01 = normalize(text_optimisation)
    text_optimisation02 = tokenize(text_optimisation01)
    words_sum = len(text_optimisation02)
    count_freqtext = count_freq(text_optimisation02)
    uni_words = len(count_freqtext)
    top5 = top_n(count_freqtext)

    print(f"Всего слов: {words_sum}")
    print(f"Уникальных слов: {uni_words}")
    print("Топ-5:")

    for word, count in top5:
        print(f"{word}:{count}")


txt01 = read_text("src/data/lab_04/input.txt")
text_stats(txt01)

write_csv(
    top_n(count_freq(tokenize(normalize(txt01))), 100),
    path=r"C:\GitHub_Misis\python_labs-ETX-\src\data\lab_04\check2.csv",
    header=["Слова", "Подсчёт"],
)
