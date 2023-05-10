import pickle
import pandas as pd
import streamlit as st
import requests
import json

cities = ['Ahmedabad', 'Kolkata', 'Mumbai', 'Pune', 'Navi Mumbai', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

# Define the API endpoint
url = "https://api.cricapi.com/v1/currentMatches?apikey=889bafcf-96c9-4cad-bf6c-d9b8ab3184a3&offset=0"

headers = {
    "apikey": "889bafcf-96c9-4cad-bf6c-d9b8ab3184a3"
}

# Make the API request
response = requests.get(url, headers=headers)

data = response.json()

myId = "8e3d0b98-0b9b-491b-bbf4-d455303aa020"
permission  = "yes"

pipe = pickle.load(open('pipe11.pkl','rb'))

# Define custom CSS style for medium font and text color
medium_css = "font-size: 25px; color: rgb(37, 97, 174);"
medium_css1 = "font-size: 24px; color: rgb(238 116 41);"
medium_css2 = "font-size: 24px; color: rgb(55 3 129);"
team1_css = "font-size: 24px; color: rgb(0 87 226);"
team2_css = "font-size: 24px; color: rgb(221 31 45);"

if permission == "yes":
       match_id = data['data'][4]['id']
       match_name = data['data'][4]['name']
       match_city = data['data'][4]['venue']
       target_score = data['data'][4]['score'][0]['r']
       current_score = data['data'][4]['score'][1]['r']
       fall_wickets = data['data'][4]['score'][1]['w']
       over_completed = data['data'][4]['score'][1]['o']
       batting_team = data['data'][4]['teams'][1]
       bowling_team = data['data'][4]['teams'][0]
       if myId == match_id:
           st.title('IPL Win Predictor')
           # Display the string in medium font and text color
           st.markdown("<p style='{}'>{}</p>".format(medium_css1, "The Batting Team : " + "  " + batting_team),unsafe_allow_html=True)
           st.markdown("<p style='{}'>{}</p>".format(medium_css1, "Current Score : " + "  " + str(current_score)),unsafe_allow_html=True)
           st.markdown("<p style='{}'>{}</p>".format(medium_css1, "Wickets : " + "  " + str(fall_wickets)),unsafe_allow_html=True)
           st.markdown("<p style='{}'>{}</p>".format(medium_css, "The Bowling Team : " + "  " + bowling_team),unsafe_allow_html=True)
           st.markdown("<p style='{}'>{}</p>".format(medium_css, "Match Target : " + "  " + str(target_score)),unsafe_allow_html=True)
           st.markdown("<p style='{}'>{}</p>".format(medium_css, "Over Completed : " + "  " + str(over_completed)),unsafe_allow_html=True)
           select_city = st.selectbox('Select host City',sorted(cities))
       
       if st.button('Predict Future'):
              
              try:
                     
                     runs_left = target_score - current_score
                     balls_left = 120 - (over_completed * 6)
                     wicketss = 10 - fall_wickets
                     crr = current_score / over_completed
                     rrr = (runs_left * 6) / balls_left
                     data_df = pd.DataFrame({
                            'BattingTeam':[batting_team],
                            'BowlingTeam':[bowling_team],
                            'City':[select_city],
                            'runs_left':[runs_left],
                            'balls_left':[balls_left],
                            'wickets':[wicketss],
                            'total_run_x':[target_score],
                            'crr':[crr],
                            'rrr':[rrr]
                     })
                     result = pipe.predict_proba(data_df)
                     loss = result[0][0]
                     win = result[0][1]
                     st.header(batting_team + "- " + str(round(win * 100)) + "%")
                     st.header(bowling_team + "- " + str(round(loss * 100)) + "%")
              except NameError:         
                     st.write(" ")
elif permission == "wait":
       st.header("38th Match • Indian Premier League 2023")
       st.markdown("<p style='{}'>{}</p>".format(team1_css, "Lacknow Super Giants"),unsafe_allow_html=True)
       st.header("VS")
       st.markdown("<p style='{}'>{}</p>".format(team2_css, "Punjab Kings"),unsafe_allow_html=True)
       st.header("Prediction will strats from 2nd Innings")
elif permission == "match_start":
       st.header("38th Match • Indian Premier League 2023")
       st.markdown("<p style='{}'>{}</p>".format(team1_css, "Lacknow Super Giants"),unsafe_allow_html=True)
       st.header("VS")
       st.markdown("<p style='{}'>{}</p>".format(team2_css, "Punjab Kings"),unsafe_allow_html=True)
       st.header("Match will start on 7:30 PM")

# col1, col2 = st.columns(2)
#
# with col1:
#     bat_team = st.selectbox('Select the Batting team',sorted(teams))
# with col2:
#     bol_team = st.selectbox('Select the Bowling team',sorted(teams))
#
# select_city = st.selectbox('Select host City',sorted(cities))
#
# target = st.number_input('Target')
#
# col3,col4,col5 = st.columns(3)
#
# with col3:
#     score = st.number_input('Score')
# with col4:
#     overs = st.number_input('Overs Completed')
# with col5:
#     wickets = st.number_input('Wicket Out')

# if st.button('Predict Future'):
#        try:
#               runs_left = target_score - current_score
#               balls_left = 120 - (over_completed * 6)
#               wicketss = 10 - fall_wickets
#               crr = current_score / over_completed
#               rrr = (runs_left * 6) / balls_left
#               data_df = pd.DataFrame({
#                      'BattingTeam':[batting_team],
#                      'BowlingTeam':[bowling_team],
#                      'City':[select_city],
#                      'runs_left':[runs_left],
#                      'balls_left':[balls_left],
#                      'wickets':[wicketss],
#                      'total_run_x':[target_score],
#                      'crr':[crr],
#                      'rrr':[rrr]
#               })
#               result = pipe.predict_proba(data_df)
#               loss = result[0][0]
#               win = result[0][1]
#               st.header(batting_team + "- " + str(round(win * 100)) + "%")
#               st.header(bowling_team + "- " + str(round(loss * 100)) + "%")
#        except NameError:
#               st.write(" ")
