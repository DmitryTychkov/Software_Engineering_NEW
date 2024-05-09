import re
def load_censor(file_name):
    with open(file_name, 'r') as file:
        censor_words = file.read().split()
    return censor_words

def censor(text, censor_words):
    censor_text = text
    for word in censor_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        censor_text = pattern.sub('*' * len(word), censor_text)

    return censor_text

def main():
    censor_words = load_censor("text/7_4.txt")
    text = input("Введите предложение: ")
    censored_text = censor(text, censor_words)
    print("Результат: ", censored_text)

if __name__ == "__main__":
    main()
