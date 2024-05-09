def count_statistics(file_name):
    total_letters = 0
    total_words = 0
    total_lines = 0

    with open(file_name, 'r') as file:
        for line in file:
            total_letters += sum(1 for char in line if char.isalpha())
            total_words += len(line.split())
            total_lines += 1

    return total_letters, total_words, total_lines

def main():
    file_name = "text/7_3.txt"
    letters, words, lines = count_statistics(file_name)
    print("Input file contains:")
    print(f"{letters} letters")
    print(f"{words} words")
    print(f"{lines} lines")

if __name__ == "__main__":
    main()
