ISS Position Tracker (CLI)
A simple cli python tool for tracking the position of the International Space Station (ISS) in real time as well as how many people are currently in space!

Run the program named 'iss-tracker' using python and run use the desired commands, exits gracefully with Ctrl + C.

Available commands:
    help - Lists all commands.
    track {parameter}
        {-t} - Returns position data for the ISS until interupted.
        {[num]} - Returns position data for the ISS [num] times.
    people - Returns the number of people that are currently in space.

Notes:
-Requires an internet connection
-API response speed and success may vary
-Continuous tracking (-t) runs until manually stopped (Ctrl + C)

(this project uses the public open notify API)