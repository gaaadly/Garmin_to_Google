# Garmin_to_Google
Simple export from Garmin to Google Sheets (for running mainly)

This script fetches recent activities from your Garmin account and exports them to a Google Sheets document using the Google Sheets API.

## Features
- Fetches recent activities from Garmin Connect.
- Calculates average running pace.
- Generates a summary for each activity.
- Writes the data to a Google Sheets document.

## Prerequisites
Before running the script, ensure you have:

- A Garmin account.
- A Google Cloud Project with Google Sheets API enabled.
- A service account JSON key file for Google Sheets API authentication.

## Installation
1. **Clone the Repository** (or copy the script to your working directory):
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Required Python Libraries**:
   ```sh
   pip install garminconnect google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

## Setup Instructions
### 1. Obtain Google Sheets API Credentials
Follow these steps to create a service account and get your credentials:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or use an existing one).
3. Navigate to **APIs & Services > Library** and enable the **Google Sheets API**.
4. Go to **APIs & Services > Credentials**.
5. Click **Create Credentials > Service Account**.
6. Assign a role such as **Editor**.
7. Click **Create and Continue**.
8. In the **Keys** section, click **Add Key > JSON**, then download and save the file (e.g., `your-service-account.json`).
9. Move the JSON key file to your project directory and update the script with its path.

### 2. Share Google Sheets with the Service Account
1. Open your Google Sheets document.
2. Click **Share** and add the email from your service account JSON file.
3. Grant **Editor** access.
4. Copy the Google Sheet ID from the URL (it appears after `/d/` and before `/edit`).

### 3. Update the Script with Credentials
Edit the script to include:
- Your Garmin email and password.
- The path to your Google service account JSON file.
- Your Google Sheet ID.

## Running the Script
Execute the script using:
```sh
python script.py
```

If configured correctly, the script will fetch recent Garmin activities and write them to your Google Sheet.

## Output Format
The Google Sheet will contain the following columns:
1. **Start Time** (Timestamp of the activity)
2. **Distance (m)** (Total distance in meters)
3. **Duration (s)** (Total duration in seconds)
4. **Average HR (BPM)** (Average heart rate in BPM)
5. **Average Pace (min/km)** (Pace calculated in minutes per kilometer)
6. **Summary** (A formatted string summary of the activity)

Output example: ![Example](https://github.com/gaaadly/Garmin_to_Google/blob/main/Example.png)

## Troubleshooting
- Ensure that your Garmin login credentials are correct.
- Verify that the service account has permission to access the Google Sheet.
- Check that the JSON key file path is correct.

## License
This script is released under the MIT License.
