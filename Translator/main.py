'''Импортируем необходимые модули: tkinter для создания графического интерфейса, ttk для использования стилизованных виджетов, и Translator из библиотеки googletrans для перевода текста.'''
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Создаем словарь для отображения кодов языков в их русские названия
LANGUAGES_RU = {
    'af': 'Африкаанс',
    'sq': 'Албанский',
    'am': 'Амхарский',
    'ar': 'Арабский',
    'hy': 'Армянский',
    'az': 'Азербайджанский',
    'eu': 'Баскский',
    'be': 'Белорусский',
    'bn': 'Бенгальский',
    'bs': 'Боснийский',
    'bg': 'Болгарский',
    'ca': 'Каталанский',
    'ceb': 'Себуанский',
    'ny': 'Чева',
    'zh-cn': 'Китайский (упрощенный)',
    'zh-tw': 'Китайский (традиционный)',
    'co': 'Корсиканский',
    'hr': 'Хорватский',
    'cs': 'Чешский',
    'da': 'Датский',
    'nl': 'Голландский',
    'en': 'Английский',
    'eo': 'Эсперанто',
    'et': 'Эстонский',
    'tl': 'Филиппинский',
    'fi': 'Финский',
    'fr': 'Французский',
    'fy': 'Фризский',
    'gl': 'Галисийский',
    'ka': 'Грузинский',
    'de': 'Немецкий',
    'el': 'Греческий',
    'gu': 'Гуджарати',
    'ht': 'Гаитянский креольский',
    'ha': 'Хауса',
    'haw': 'Гавайский',
    'he': 'Иврит',
    'hi': 'Хинди',
    'hmn': 'Хмонг',
    'hu': 'Венгерский',
    'is': 'Исландский',
    'ig': 'Игбо',
    'id': 'Индонезийский',
    'ga': 'Ирландский',
    'it': 'Итальянский',
    'ja': 'Японский',
    'jv': 'Яванский',
    'kn': 'Каннада',
    'kk': 'Казахский',
    'km': 'Кхмерский',
    'rw': 'Киньяруанда',
    'ko': 'Корейский',
    'ku': 'Курдский',
    'ky': 'Киргизский',
    'lo': 'Лаосский',
    'la': 'Латынь',
    'lv': 'Латышский',
    'lt': 'Литовский',
    'lb': 'Люксембургский',
    'mk': 'Македонский',
    'mg': 'Малагасийский',
    'ms': 'Малайский',
    'ml': 'Малаялам',
    'mt': 'Мальтийский',
    'mi': 'Маори',
    'mr': 'Маратхи',
    'mn': 'Монгольский',
    'my': 'Бирманский',
    'ne': 'Непальский',
    'no': 'Норвежский',
    'ps': 'Пушту',
    'fa': 'Персидский',
    'pl': 'Польский',
    'pt': 'Португальский',
    'pa': 'Панджаби',
    'ro': 'Румынский',
    'ru': 'Русский',
    'sm': 'Самоанский',
    'gd': 'Шотландский (гэльский)',
    'sr': 'Сербский',
    'st': 'Сесото',
    'sn': 'Шона',
    'sd': 'Синдхи',
    'si': 'Сингальский',
    'sk': 'Словацкий',
    'sl': 'Словенский',
    'so': 'Сомали',
    'es': 'Испанский',
    'su': 'Сунданский',
    'sw': 'Суахили',
    'sv': 'Шведский',
    'tg': 'Таджикский',
    'ta': 'Тамильский',
    'te': 'Телугу',
    'th': 'Тайский',
    'tr': 'Турецкий',
    'uk': 'Украинский',
    'ur': 'Урду',
    'ug': 'Уйгурский',
    'uz': 'Узбекский',
    'vi': 'Вьетнамский',
    'cy': 'Уэльский',
    'xh': 'Коса',
    'yi': 'Идиш',
    'yo': 'Йоруба',
    'zu': 'Зулу'
}

''' Определяем функцию translate_text(), которая будет вызываться при нажатии кнопки "Перевести". 
Получаем текст из текстового поля, получаем коды выбранных языков для перевода, вызываем функцию translate() для выполнения перевода, очищаем и выводим переведенный текст. '''
def translate_text():
    # Получаем текст из текстового поля
    text_to_translate = text_input.get("1.0", tk.END).strip()

    # Получаем выбранные языки для перевода
    source_language_code = [key for key, value in LANGUAGES_RU.items() if value == source_lang_combobox.get()][0]
    target_language_code = [key for key, value in LANGUAGES_RU.items() if value == target_lang_combobox.get()][0]

    # Переводим текст
    translated_text = translate(text_to_translate, source_language_code, target_language_code)

    # Очищаем текстовое поле с переводом и вставляем в него переведенный текст
    translated_output.delete("1.0", tk.END)
    translated_output.insert(tk.END, translated_text)

''' Определяем функцию translate(), которая использует Translator для выполнения перевода текста с исходного языка на целевой. '''
def translate(text, source_language, target_language):
    # Создаем экземпляр класса Translator
    translator = Translator()

    # Переводим текст на указанный язык
    translated_text = translator.translate(text, src=source_language, dest=target_language)

    # Возвращаем переведенный текст
    return translated_text.text


# Создаем основное окно
baseWindow = tk.Tk()

# Устанавливаем заголовок
baseWindow.title("Переводчик")

# Создаем фрейм для ввода текста
input_frame = ttk.Frame(baseWindow)
# размещаем с отступом в 10 пикселей
input_frame.pack(pady=10)

# Создаем метку и текстовое поле для ввода текста
ttk.Label(input_frame, text="Введите текст для перевода:").pack(side="left")
text_input = tk.Text(input_frame, width=40, height=5)
text_input.pack(side="left")

# Создаем фрейм для выбора языков
language_frame = ttk.Frame(baseWindow)
language_frame.pack(pady=5)

# Создаем метки и выпадающие списки для выбора языков
ttk.Label(language_frame, text="Исходный язык:").pack(side="left")
source_lang_combobox = ttk.Combobox(language_frame, values=list(LANGUAGES_RU.values()))
source_lang_combobox.pack(side="left")
source_lang_combobox.set("Английский")

ttk.Label(language_frame, text="Язык перевода:").pack(side="left")
target_lang_combobox = ttk.Combobox(language_frame, values=list(LANGUAGES_RU.values()))
target_lang_combobox.pack(side="left")
target_lang_combobox.set("Русский")

# Создаем кнопку для перевода текста
translate_button = ttk.Button(baseWindow, text="Перевести", command=translate_text)
translate_button.pack(pady=5)

# Создаем фрейм для вывода переведенного текста
output_frame = ttk.Frame(baseWindow)
output_frame.pack(pady=10)

# Создаем метку и текстовое поле для вывода переведенного текста
ttk.Label(output_frame, text="Переведенный текст:").pack(side="left")
translated_output = tk.Text(output_frame, width=40, height=5)
translated_output.pack(side="left")

# Запускаем главный цикл приложения
baseWindow.mainloop()
