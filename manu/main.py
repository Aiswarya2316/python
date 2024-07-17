from admin import admin_actions
from user import register_user, passenger_actions

def main():
    print('METRO TICKET BOOKING')
    users = [{'username': 's', 'phno': 123456, 'password': '123'}]
    stations = {1: 'stationA', 2: 'stationB', 3: 'stationC', 4: 'stationD'}

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register_user(users)

        elif choice == 2:
            choic = str(input('Enter type (admin / passenger): ')).strip().lower()

            if choic == 'admin':
                admin_name = input('Enter username: ')
                admin_password = input('Enter password: ')
                admin1 = {'username': 'admin', 'password': 'asdf'}

                if admin_name == admin1['username'] and admin_password == admin1['password']:
                    admin_actions(stations)
                else:
                    print("Invalid admin credentials!")

            elif choic == 'passenger':
                passenger_actions(users, stations)

            else:
                print("Invalid type! Choose between 'admin' or 'passenger'.")

        elif choice == 3:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
