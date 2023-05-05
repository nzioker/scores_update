from datetime import datetime
import http.client
import json 
from winotify import Notification, audio


class Football:
    EPL_ID = 39
    CL_ID = 2
    api_url = "v3.football.api-sports.io"
    

    def __init__(self, current_date, season, league):
        self.current_date = current_date
        self.season = season
        self.league = league
        

    @staticmethod
    def get_todays_date():
        try:
            return datetime.now().strftime("%Y-%m-%d")
        except AttributeError as e:
            return e
        except:
            return "Error"

    def check_league(self):
        if self.league == Football(self.current_date, self.season, self.league).EPL_ID:
            res = self.get_matches(Football(self.current_date, self.season, self.league).EPL_ID)
            self.notification_msg(self.league, res)
        if self.league == Football(self.current_date, self.season, self.league).CL_ID:
            res = self.get_matches(Football(self.current_date, self.season, self.league).CL_ID)
            self.notification_msg(self.league, res)

    def get_matches(self, id):
        # Pick matches from the api url on line 11
        headers = {
            'x-rapidapi-host': Football(self.current_date, self.season, id).api_url,
            'x-rapidapi-key': "1f35446fd0c5651d0e01f3f963cad130"
            }
        
        conn = http.client.HTTPSConnection(Football(self.current_date, self.season, id).api_url)
        conn.request("GET", f"/fixtures?season={self.season}&league={id}&date={self.current_date}", headers=headers)
        
        data = json.loads(conn.getresponse().read())
        
        for i in data["response"]:
            home_team = i["teams"]["home"]["name"]
            away_team = i["teams"]["away"]["name"]
            kickoff_time = datetime.fromtimestamp(i["fixture"]["timestamp"]).strftime("%H:%M:%S")
            return f"{home_team} vs {away_team} to be played on {self.current_date} at {kickoff_time}" 
        return "No game to be played today"
    

    def notification_msg(self, id, message): 
        # send notification to you
        title="Today's Games"
        msg = message
        if id == 2:
            app_id="Champions league"
            toast = Notification(app_id=app_id, title=title, msg=msg, icon=r"C:\Users\HP\Downloads\cleague.png")
            toast.set_audio(audio.Reminder, loop=False)
            toast.show()
        if id == 39:
            app_id="Premier league"
            toast = Notification(app_id=app_id, title=title, msg=msg, icon=r"C:\Users\HP\Downloads\pl.jpg")
            toast.set_audio(audio.Reminder, loop=False)
            toast.show()
        



