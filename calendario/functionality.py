import datetime
import os.path
import os
from django.conf import settings
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds:
      os.remove("token.json")

    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
    )
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    #Today al 00:00
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_time = today.isoformat() + "Z"
    end_time = (today + datetime.timedelta(days=1)).isoformat() + "Z"
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_time,
            timeMax=end_time,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      return "No tienes eventos programados para hoy. ¡Disfruta de tu día!"

    # Prints the start and name of the next 10 events
    event_list = []
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        event_list.append((start, event["summary"]))

    return event_list

  except HttpError as error:
    print(f"Ocurrió un error: {error}")


if __name__ == "__main__":
  main()