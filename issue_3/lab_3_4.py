inData = str(input('Введите сообщение на английском языке: '))

print(len(inData))  # выводим длину фразы
inDataLower = inData.lower()
print(inDataLower)  # нижний регистр


def count_vowels(inData):  # считаем гласные
    vowels = 'aeiouAEIOU'
    count = 0
    for char in inData:
        if char in vowels:
            count += 1
    return count


print("Кол-во гласных в предложении: ", count_vowels(inData))

if 'ugly' in inDataLower:
    inDataReplace = inDataLower.replace('ugly', 'beauty')
    print('Программа заменила триггер-слово: ' + inDataReplace)

inDataStart = inDataLower.startswith('the')
if inDataStart == 1:
    print('Предложение начинается с the')

inDataEnd = inDataLower.endswith('end')
if inDataEnd == 1:
    print('Предложение оканчивается на end')
