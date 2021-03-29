import csv
import sys
import os

def main():
    while True:
        command = (input("What do you want to do?\n")).lower()

        if command == "quit":
            print("quit\n")
            save_status()
            return
        elif command == "add expense":
            print("add expense\n")
            save_data = Expense.add_expense(argv[1])
            save_status(save_data)
        elif command == "add sale":
            print("add sale\n")
            save_data = Card.report_sale(argv[1])
            save_status(save_data)
        elif command == "load cards":
            print("load cards\n")
            save_data = Card.load_cards(argv[1])
            save_status(save_data)
        elif command == "update pricing":
            print("update pricing\n")
            save_data = Card.update_pricing(argv[1])
            save_status(save_data)
        else:
            print("I didn't understand that command")

def save_status(save_data):
    while True:
        command = (input("Do you want to save?\n")).lower()
        
        if command == "y" or command == "yes":
            print("saved\n")
            try:
                output = open('output.txt', 'w')
                print(save_data, file=output)
                output.close()
                print("saved\n")
            except:
                print("not saved\n")   
        elif command == "n" or command == "no":
            print("not saved\n")

        return
       

def open_csv(file_to_open, mode):
    with open(file_to_open, mode) as csv_file:
        return csv.reader(csv_file, delimiter=',')

    csv_file.close()




main()