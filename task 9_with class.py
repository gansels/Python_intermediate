#task 9-with class
import pickle
import csv
import json
class Notebook:
    def __init__(self):
        self.list_row = []
            
    def add_row(self, row):
       self.list_row.append(row)
    
    def remove_row(self,row_num):
        self.list_row.pop(row_num)
    
    def change_row(self, row_nums, new_row):
        self.list_row[row_nums] = new_row
    
# saving via pickle module

    def save_note(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    def load_note(self, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

# saving via csv module
    def save_notes(self, filename):
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerows(self.list_row)

    def load_notes(self, filename):
        with open(filename, "r") as file:
            csv.reader(self.list_row)

# saving via JSON module
    def save_notes(self, filename):
        with open(filename,"w") as file_01:
            json.dump(self.list_row, file_01)
    
    def load_notes(self, filename):
        with open(filename.json, "r") as openfile:
            self.list_row = json.load(openfile)


    def get_user_choice(self):

        print("1. add_row")
        print("2. list_row")
        print("3. remove_row")
        print("4. change_row")
        print("5. save_note in pickle")
        print("6. load_note in pickle")
        print("7. save_notes to csv")
        print("8. load_notes in csv")
        print("9. save_note in JSON")
        print("10. load_note in JSON")
        print("0. exit")

        choice = input("Enter the choice of user : ")
        return int(choice)
    
def main():

    notebook = Notebook

    choice = notebook.get_user_choice()

    while choice != 0:
        if choice == 1:
            user_row = input("Enter the row: ")
            notebook.add_row(user_row)

        elif choice == 2:
            print("The list of rows in notebook: ")

        elif choice == 3:
            user_row_num = int(input("Enter the row which you want remove : "))
            notebook.remove_row(user_row_num)

        elif choice == 4:
            user_row_change = int(input("Enter the row which you want to change: "))
            user_new_row = input("Enter the row: ")
            notebook.change_row (user_row_change, user_new_row)

        elif choice == 5:
            user_filename = input("Enter the file name: ")
            notebook.save_note(user_filename)
        
        elif choice == 6:
            user_filename_load = input("Enter the file name: ")
            notebook =  notebook.load_note(user_filename_load)
        
        elif choice == 7:
            user_filename_csv = input("Enter the file name: ")
            notebook.save_notes(user_filename_csv)
        
        elif choice == 8:
            user_filename_csv_load = input("Enter the file name: ")
            notebook.load_notes(user_filename_csv_load)

        elif choice == 9:
            user_filename_json = input("Enter the file name: ")
            notebook.save_notes(user_filename_json)
        
        elif choice == 10:
            user_filename_json_load = input("Enter the file name: ")
            notebook.loaad_notes(user_filename_json_load)
        
        else:
            print("Wrong choice")

        choice = notebook.get_user_choice()


if __name__ == "__main__":
    main()

            



