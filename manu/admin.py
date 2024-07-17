def admin_actions(stations):
    while True:
        print('1. Add new station\n2. View stations\n3. Log out')
        admchoice = int(input('Enter your choice: '))

        if admchoice == 1:
            new_station_name = input('Enter new station name: ')
            new_station_id = max(stations.keys()) + 1
            if new_station_name not in stations.values():
                stations[new_station_id] = new_station_name
                print('Station added successfully!')
            else:
                print('Station already exists!')

        elif admchoice == 2:
            for station_id, station_name in stations.items():
                print(f"{station_id}: {station_name}")
            print()

        elif admchoice == 3:
            print('Logged out successfully!')
            break

        else:
            print('Invalid choice')
