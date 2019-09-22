from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
HQ1_ENGINEERING_CONFERENCE_CAL_ID = 'nanohmics.com_2d3133373939333234353437@resource.calendar.google.com'

def main():
    """Show basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    try:
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print('refresh creds\n')
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('/home/pi/RaspberryPi/python3/credentials.json', SCOPES)
                try:
                    creds = flow.run_local_server(port=0)
                except Exception as e:
                    print('creds doesnt work' + str(e))

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
                
        service = build('calendar', 'v3', credentials=creds)
        
        # Call the Calendar API
        now = datetime.datetime.now().isoformat() + 'Z' # 'Z' needed make service.events() work
        # Sets the time stamp to 12am (00:00:00 military time) so full day of meetings is
        # always displayed.
        print(now)
        NOW = list(now)
        for i in range(11, 18):
            if i != 13 and i != 16:
                NOW[i] = '0'
        NOW[18] = '1'
        now = ''.join(NOW)
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId=HQ1_ENGINEERING_CONFERENCE_CAL_ID,
                                              showDeleted=False, timeMin=now, maxResults=10,
                                              singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
   
        events_temp = [] # Temporary list to store event data
        if not events:
            print('No upcoming events found.')
        
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            events_temp.append((event['summary'], start, end))
            print(start, end, event['summary'])

        return events_temp
    
    except Exception as e:
        print('exception: ' + str(e))
        main()
        
if __name__ == '__main__':
    main()
