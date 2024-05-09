def load_expenses():
    try:
        with open("text/7_2.txt", "r") as file:
            lines = file.readlines()
            expenses = [eval(line.strip()) for line in lines]
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses):
    with open("text/7_2.txt", "w") as file:
        for expense in expenses:
            file.write(str(expense) + "\n")

def add_expense():
    category = input("Введите категорию расхода: ")
    amount_of_expense = float(input("Введите сумму расхода: "))
    date = input("Введите дату расходов (в формате гггг-мм-дд): ")

    expense = {"Категория": category, "Сумма расходов": amount_of_expense, "Дата": date}
    return expense

def print_ledger(expenses):
    if expenses:
        print("\n--- Список расходов ---")
        for expense in expenses:
            print(f"Категория: {expense['Категория']}, Сумма расходов: {expense['Сумма расходов']}, Дата расхода: {expense['Дата']}")
        print("-------------------------\n")
    else:
        print("Расходы отсутствуют.")

def main():
    expenses = load_expenses()

    while True:
        print("1. Добавить расход")
        print("2. Посмотреть расходы")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            expense = add_expense()
            expenses.append(expense)
            save_expenses(expenses)
            print("Расходы добавлены.")
        elif choice == "2":
            print_ledger(expenses)
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Вы промахнулись по клавишам, попробуйте снова")

if __name__ == "__main__":
    main()
