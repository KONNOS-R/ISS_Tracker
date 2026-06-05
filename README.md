# ISS Position Tracker (CLI)

A simple cli python tool for tracking the position of the International Space Station (ISS) in real time as well as how many people are currently in space!

---

## Features

- **Real-time ISS Tracking** - Get live latitude and longitude coordinates of the ISS
- **Crew Counter** - Display the current number of people aboard the ISS
- **Flexible Tracking Modes**:
  - Single request
  - Multiple requests (specify count)
  - Continuous tracking (until interrupted)
- **Error Handling** - Graceful handling of network issues and API errors

---

## Requirements

- Python 3.8+
- Internet connection (for API access)

---

## Installation and Usage

- PyPI page: [Click here](https://pypi.org/project/iss-tracker-cli/)

<br>

- Install the CLI application
```
pip install iss-tracker-cli
```

- Launch the CLI application:
```
iss-tracker
```

---

## Commands

- `help` - Lists all commands.

- `track {parameter}`
    - `{-t}` - Returns position data for the ISS until interrupted.
    - `{[num]}` - Returns position data for the ISS [num] times.

- `people` - Returns the number of people that are currently in space.

---

## Notes

- Uses the public Open Notify API
- Requires an internet connection
- API response speed and reliability may vary
- Continuous tracking (`-t`) runs until manually stopped (Ctrl+C)