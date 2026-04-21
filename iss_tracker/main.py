import requests
import time


#gets the number of people in space
def getPeopData():
    api = "http://api.open-notify.org/astros.json"
    try:
        raw_data = (requests.get(api, timeout = 5)).json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")
        return None

    num = raw_data["number"]

    return num

#gets postion data of the ISS
def getPosData():
    api = "http://api.open-notify.org/iss-now.json"
    try:
        raw_data = (requests.get(api, timeout = 5)).json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")
        return None

    lat = raw_data["iss_position"]["latitude"]
    lon = raw_data["iss_position"]["longitude"]

    return (lat, lon)

#help command
def help():
    return '''command list:
    help - Lists all commands.
    track {parameter}
        {-t} - Returns position data for the ISS until interupted.
        {[num]} - Returns position data for the ISS [num] times.
    people - Returns the number of people that are currently in space.'''

#track command
def track(par):
    if par == "-t":
        print("\n!Displaying Position Data for infinite requests.\n")
        try:
            while True:
                data = getPosData()
                if data != None:
                    lat, lon = data
                    print(f"------ISS position------\nLatitude: {lat}\nLongitude: {lon}\n")
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nExiting...\n")
    else:
        try:
            t  = int(par)
            print(f"\n!Displaying Position Data for {t} request(s).\n")
            for i in range(t):
                data = getPosData()
                if data != None:
                    lat, lon = data
                    print(f"------ISS position------\nLatitude: {lat}\nLongitude: {lon}\n")
                time.sleep(1)
        except TypeError as e:
            print("Error: Incorrect parammeters")

#people command
def people():
    data = getPeopData()
    if data != None:
        print(f"\nThere are currently {data} people in space!\n")

#main Program
def main():
    print('''\033[34m
              ooo
             / : \\
       _____"~~~~~"_____
       \\+##|U *^* U|##+/
        \\..!('ISS')!../
         ^--o|   |o--^
      +====}:^ ^ ^:{====+
       ___. .| ! |. .___
      |####:/" " "\\:####|
      |####=|  O  |=####|
      |####>\\_____/<####|
       ‾‾‾˙   | |   ˙‾‾‾
              o o
    \033[0m    
    * ISS Position Tracker *
    ''')

    while True:
        try:
            command = input(">").split()

            #help command
            if len(command) == 1 and command[0] == "help":
                print(help())

            #track command
            elif len(command) in (1,2) and command[0] == "track":
                par = command[1] if len(command) > 1 and command[1] else 1
                track(par)

            elif len(command) == 1 and command[0] == "people":
                people()

            #invalid command
            else:
                print("!Invalid command. Enter 'help' to display command list.")
        except KeyboardInterrupt:
            print("\nExiting...\n")
            break


if __name__ == "__main__":
    main()