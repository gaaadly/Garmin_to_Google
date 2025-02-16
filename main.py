from garminconnect import Garmin
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def calculate_pace(distance_m, duration_s):
    ''' Calculates average running pace, returns string 'min:sec/km'  '''
    
    pace_per_km = (duration_s / distance_m) * 1000 if distance_m > 0 else 0

    minutes = int(pace_per_km // 60)
    seconds = int(pace_per_km % 60)

    return f"{minutes}:{seconds:02d}/km"

def make_summary(duration_s, avg_hr, distance_m):
    '''Creates summary of running activity, returns string in format '{duration}min@ {average HR}BPM, {km} km@{pace}/km' '''

    # Convert duration to hours and minutes
    total_minutes = int(duration_s // 60)
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)

    # Format duration based on length
    if total_minutes >= 70:
        duration_str = f"{hours}H {minutes}min"
    else:
        duration_str = f"{total_minutes}min"

    # Calculate pace
    pace_per_km = (duration_s / distance_m) * 1000 if distance_m > 0 else 0
    pace_min = int(pace_per_km // 60)
    pace_sec = int(pace_per_km % 60)

    # Convert distance to km with 2 decimal places
    distance_km = round(distance_m / 1000, 2)

    return f"{duration_str}@{int(avg_hr)} BPM, {distance_km:.2f} km@{pace_min}:{pace_sec:02d}/km"

# Garmin API - Fetch Activity Data
email = "your_email@provider.com"   # replace with your Garmin email
password = "password"               # replace with your Garmin password 
client = Garmin(email, password)
client.login()

# Fetch 10 recent activities
activities = client.get_activities(30, 10)  # Choose range for activities (which last activity, how many activities since last chosen)
activity_data = [
    [activity["startTimeLocal"], activity["distance"], activity["duration"], activity['averageHR'], 
     calculate_pace(activity["distance"], activity["duration"]), make_summary(activity["duration"], activity["averageHR"], activity["distance"])]
    for activity in activities
]

# Google Sheets API - Write Data to Sheet
# Load credentials from JSON key file
SERVICE_ACCOUNT_FILE = "path/to/your-service-account.json"   # Update with the path to your JSON key file
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Connect to the Google Sheets API
spreadsheet_id = "your_spreadsheet_id"   # Replace with your Google Sheet ID
sheet_name = "Sheet1"                    # Update with the target sheet name
range_name = f"{sheet_name}!A1"

# Create the service
service = build("sheets", "v4", credentials=credentials)
sheet = service.spreadsheets()

# Prepare data for the Google Sheet
headers = ["Start Time", "Distance (m)", "Duration (s)", "Average HR (BPM)", "Average pace (min/km)", "Summary"]
values = [headers] + activity_data

# Write data to the Google Sheet
body = {
    "values": values
}

sheet.values().update(
    spreadsheetId=spreadsheet_id,
    range=range_name,
    valueInputOption="RAW",
    body=body
).execute()

print("Data transferred successfully!")