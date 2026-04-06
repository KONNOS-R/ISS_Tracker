import requests
import time


api = "http://api.open-notify.org/iss-now.json"


def getData():
    try:
        raw_data = (requests.get(api, timeout = 5)).json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")
        return None

    lat = raw_data["iss_position"]["latitude"]
    lon = raw_data["iss_position"]["longitude"]

    return (lat, lon)


def help():
    return '''command list:
    help  - Lists all commands.
    track {parameter}
        {-t}  - Returns position data for the ISS until interupted.
        {[num]}  - Returns position data for the ISS [num] times.}'''


def track(par):
    if par == "-t":
        print("\n!Displaying Position Data for infinite requests.\n")
        try:
            while True:
                data = getData()
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
                data = getData()
                if data != None:
                    lat, lon = data
                    print(f"------ISS position------\nLatitude: {lat}\nLongitude: {lon}\n")
                time.sleep(1)
        except TypeError as e:
            print("Error: Incorrect parammeters")


#Main Programme
print('''
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
      
* ISS Position Tracker *
''')

while __name__ == "__main__":
    command = input(">").lstrip()
    
    #help command
    if command.strip() == "help":
        print(help())

    #track command
    elif command[:5] == "track":
        par = command[5:].strip()
        if par == "":
            par = 1
        track(par)

    #invalid command
    else:
        print("!Invalid command. Enter 'help' to display command list.")

