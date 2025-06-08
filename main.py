from tracker import add_item 
from tracker import add_note
from tracker import view_report
from tracker import view_notes

def main():
    while True:
        print("\n-----WELCOME TO PRICE TRACKER-----")
        print("\n1. Add Item \n2. Add Note \n3. View Price Report \n4. View Item Notes \n5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            add_note()
        elif choice == "3":
            view_report()
        elif choice == "4":
            view_notes()
        elif choice == "5":
            print("Thankyou for using price tracker.\nSee you again!!")
            break;
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()

