def register_user(users):
    username = input("Enter username: ")
    phno = int(input('Enter phone number: '))
    password = input("Enter password: ")

    # Check if the phone number already exists
    for user in users:
        if user['phno'] == phno:
            print("Phone number already exists!")
            return

    users.append({'username': username, 'phno': phno, 'password': password})
    print("Registration successful!")

def passenger_actions(users, stations):
    phnon = int(input("Enter phone number: "))
    password = input("Enter password: ")

    # Check if the phone number and password match
    login_success = False
    for user in users:
        if user['phno'] == phnon and user['password'] == password:
            login_success = True
            break

    if login_success:
        while True:
            print('1. Book Ticket\n2. Exit')
            paschoice = int(input('Enter your choice: '))

            if paschoice == 1:
                for station_id, station_name in stations.items():
                    print(f"{station_id}: {station_name}")
                print('Each station carries RS10!')

                entry_station = int(input('Enter your entry station: '))
                exit_station = int(input('Enter your exit station: '))
                tickets = int(input('Number of tickets you need: '))

                if entry_station in stations and exit_station in stations:
                    distance = abs(exit_station - entry_station)
                    price = distance * tickets * 10
                    print('Total price:', price, 'RS')
                else:
                    print('Invalid station! Please enter a valid station number.')

            elif paschoice == 2:
                print('You have exited.')
                break

            else:
                print('Invalid choice! Please enter 1 or 2.')

    else:
        print("Invalid phone number or password!")
