from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def exchange(): # функция для загрузки информации по криптовалютам и вывода результата на интерфейс
    currency = currency_combobox.get() # в переменную записывается выбранная в выпадающем списке криптовалюта

    if currency: # проверка переменной с выбором криптовалюты
        try: # обработка исключений
            # отправка HTTP-запроса информации на API ресурс криптовалют
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies=usd')
            response.raise_for_status() # проверка статуса ответа на запрос
            data = response.json() # обрабатывается ответ в формате json и результат помещается в переменную

            if currency.lower() in data: # проверка названия криптовалюты запроса в нижнем регистре полученным данным
                target = data[currency.lower()]['usd'] # присвоение переменной значения курса криптовалюты
                label_exchange_rate.config(text=f"1 {currency} = {target} долларов США") # вывод информации в метку
            else:
                # окно отображения ошибки при отсутствии выбранной криптовалюты
                mb.showerror("Ошибка обработки данных запроса", f'Криптовалюта "{currency}" не найдена')

        except Exception as e:
            mb.showerror("Ошибка сети", f"Произошла ошибка доступа к серверу: {e}") # окно отображения ошибки HTTP-запроса
    else:
        mb.showwarning("Внимание!", "Выберите криптовалюту") # предупреждение при отсутствии выбора криптовалюты


# список основных криптовалют
currencies = (
    "Bitcoin",
    "Ethereum",
    "Ripple",
    "Litecoin",
    "Cardano"
)

# создание графического интерфейса
window = Tk() # создание главного окна
window.title("Курс криптовалюты") # заголовок окна
window.geometry("400x200") # размеры окна

# выпадающий список для выбора криптовалюты из предложенных вариантов
currency_combobox = ttk.Combobox(values=currencies, font=("Arial", 12)) # выпадающие значения выбираются из списка
currency_combobox.pack(padx=10, pady=20)

# кнопка для запуска функции отправки запроса на получение курса выбранной криптовалюты
Button(text=f"Получить курс криптовалюты", font=("Arial", 12), command=exchange).pack(padx=10, pady=5)

# метка для отображения результата запроса курса выбранной криптовалюты к доллару США
label_exchange_rate = ttk.Label(text="Выберите криптовалюту", font=("Arial", 12))
label_exchange_rate.pack(padx=10, pady=20)

# запуск главного цикла обработки событий
window.mainloop()
