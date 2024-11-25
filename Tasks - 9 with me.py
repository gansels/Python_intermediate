# Tasks - 9
import pickle
import csv

def add_row(row,all_rows):
    all_rows.append(row)
    return all_rows

def remove_row(row_num, all_rows):
    all_rows.pop(row_num)
    return all_rows

def change_row(row_nums, new_row, all_rows):
    all_rows [row_nums] = new_row
    return all_rows

def list_row(all_rows):
    print(all_rows)

#saving via pickle module

def save_note(all_rows, filename):
    
    with open(filename, 'wb') as file:
        pickle.dump(all_rows, file)

def load_note(filename):
    with open(filename, 'rb') as file:
        all_rows = pickle.load(file)
    return all_rows
    
#saving via csv module
def save_notes(all_rows, filename):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(all_rows)

def load_notes(filename):
    with open(filename, 'r') as file:
        all_rows = csv.reader(file)
    return all_rows
        
def get_user_choice():
    print("1. add_row")
    print("2. list_row")
    print("3. remove_row")
    print("4. change_row")
    print("5. save_note in pickle")
    print("6. load_note from pickle")
    print("7. save_notes to csv")
    print("8. load_notes from csv")
    print("0. exit")

    choice = int(input("Enter the choice of user : "))
    return choice

def main():
    collect_row = []
    choice = get_user_choice()
    while choice != 0:
        if choice == 1:
            user_row = input("Enter the row: ")
            collect_row = add_row(user_row, collect_row)
        elif choice == 2:
            list_row(collect_row)
        elif choice ==3:
            user_row_num = int(input("Enter the row which you want remove : "))
            collect_row = remove_row(user_row_num, collect_row)
        elif choice == 4:
            user_row_change = int(input("Enter the row which you want to change: "))
            user_new_row = input("Enter the row: ")
            collect_row = change_row (user_row_change, user_new_row, collect_row)

        elif choice == 5:
            user_filename = input("Enter the file name: ")
            save_note(collect_row, user_filename)
        
        elif choice == 6:
            user_filename_load = input("Enter the file name: ")
            collect_row = load_note(user_filename_load)
        
        elif choice == 7:
            user_filename_csv = input("Enter the file name: ")
            save_notes(collect_row, user_filename_csv)
        
        elif choice == 8:
            user_filename_csv_load = input("Enter the file name: ")
            collect_row = load_notes(user_filename_csv_load)
        
        else:
            print("Wrong choice")

        choice = get_user_choice()


if __name__ == "__main__":
    main()

    





    



            




