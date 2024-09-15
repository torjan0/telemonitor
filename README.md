# telemonitor

# Telegram User Activity Monitor

This Python project uses the [Telethon](https://github.com/LonamiWebs/Telethon) library to monitor a specific user's activity on Telegram. It logs when a user is online or when they were last seen offline. The project can handle exceptions such as rate limits imposed by Telegram.

## Key Features
- **Activity Monitoring**: Tracks the user's online status (`UserStatusOnline`) and their last seen time (`UserStatusOffline`).
- **Logging**: Logs user activity to a file (`user_activity.log`) and also outputs to the console. The logs are configured with a weekly rotation system to manage the log size efficiently.
- **Flood Wait Handling**: Catches `FloodWaitError` exceptions to handle Telegram's rate-limiting mechanism, pausing the program for the required wait time.

## Project Components
1. **Logging Configuration**: 
   - Logs are stored in `user_activity.log`, with a weekly rotation (configurable) and a backup of 5 weeks.
     
2. **Telethon Client Setup**:
   - Uses your Telegram API credentials (`api_id`, `api_hash`) to authenticate.
   - Monitors a specified user via their username.
     
3. **Monitor Logic**:
   - Continuously checks the user's status every 60 seconds.
   - Logs whether the user is currently online or when they were last seen.
     
4. **Error Handling**:
   - Handles flood wait errors by automatically waiting for the required duration before resuming.
   - Logs unexpected errors to ensure no interruption in monitoring.

## Setup Instructions
1. **Install Requirements**:
   ```bash
   pip install telethon

2. **Configure API Credentials**: 

*Get your API credentials here: https://my.telegram.org/auth*

Replace the placeholders in the script with your api_id and api_hash.

3. **Run the script**: 
   ```bash
   python3 telemonitor.py

## Example Log Output

      2023-09-14 14:23:00 - @xyz is online.
      2023-09-14 12:45:00 - @xyz was last seen at 2023-09-14 12:40 PM.


## Disclaimer

This project was created for educational and statistical purposes. It is designed to showcase how to utilize the Telethon API to monitor user activity on Telegram. It should not be used for unauthorized tracking or monitoring. Always ensure you are complying with the laws and terms of service when using such tools. The authors take no responsibility for misuse or legal consequences resulting from the improper use of this script.
