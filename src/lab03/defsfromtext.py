import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str: 
    result = text
    result = result.replace('\t' , ' ').replace('\n', ' ').replace('\r',' ')
    if casefold == True:
        result = result.casefold()

    if yo2e == True:
        result = result.replace('Ё','Е').replace('ё','е')

    result = result.strip()
    
    if '  ' in result:
        result = result.replace('  ', '')
    
    return result


def tokenize(text: str) -> list[str]: 
    symbols = r'\w+(?:-\w+)*\b'         # /w+ (ищет слова) ?:-\w+ (ищет слова с дефисами) 
                                        # * (ноль и более раз дефис) \b (граница слова)
    tokens = re.findall(symbols,text)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for tok in tokens:
        if tok in freq_dict:
            freq_dict[tok] += 1
        else:
            freq_dict[tok] = 1
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    
    
    items = list(freq.items())
    
   
    items.sort(key=lambda x: (-x[1], x[0]))
    
    
    return items[:2]











    






