def read_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            if not data:
                raise Exception("Файл пустой")
            else:
                print("Информация из файла:")
                print(data)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print("Ошибка:", e)

info = "Попытка считать данные: "

print(info)
read_file("text/emptyFile.txt")

print(info)
read_file("text/dataFile.txt")

print(info)
read_file("text/none.txt")