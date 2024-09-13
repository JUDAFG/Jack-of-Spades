import os
import sys
import threading
from colorama import Fore, Style, init
import time

# Инициализация colorama
init(autoreset=True)

# Глобальная переменная для остановки работы Мидаса
midas_running = False

def main_menu():
    print(Fore.MAGENTA + "1. Midas ♠" + Style.RESET_ALL)
    print(Fore.RED + "2. Option 2" + Style.RESET_ALL)
    print(Fore.RED + "3. Option 3" + Style.RESET_ALL)
    print(Fore.RED + "4. Exit" + Style.RESET_ALL)
    
    try:
        choice = int(input(Fore.RED + "Enter your choice (1-4): " + Style.RESET_ALL))
        
        if choice == 1:
            start_midas()
        elif choice == 2:
            option_2()
        elif choice == 3:
            option_3()
        elif choice == 4:
            stop_midas()  # Остановка процесса Мидаса перед выходом
            print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

def midas_function():
    global midas_running
    print(Fore.MAGENTA + "You selected Midas ♠" + Style.RESET_ALL)
    print(Fore.YELLOW + "Midas is running in the background..." + Style.RESET_ALL)
    midas_running = True
    # Эмуляция работы программы
    while midas_running:
        print(Fore.YELLOW + "Midas is working..." + Style.RESET_ALL)
        time.sleep(5)  # Задержка между итерациями, чтобы эмулировать фоновую работу

def start_midas():
    # Запуск Мидаса в отдельном потоке
    midas_thread = threading.Thread(target=midas_function, daemon=True)
    midas_thread.start()

def stop_midas():
    global midas_running
    midas_running = False
    print(Fore.RED + "Midas has been stopped." + Style.RESET_ALL)

def option_2():
    print(Fore.GREEN + "You selected Option 2" + Style.RESET_ALL)
    filename = input(Fore.YELLOW + "Enter the filename to read: " + Style.RESET_ALL)
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(Fore.CYAN + "File Content:\n" + content + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "File not found!" + Style.RESET_ALL)

def option_3():
    print(Fore.GREEN + "You selected Option 3" + Style.RESET_ALL)

if __name__ == "__main__":
    text = "× Jack of Spades ×"
    print(Fore.BLUE + text + Style.RESET_ALL)
    
    # Показать меню
    while True:
        main_menu()
