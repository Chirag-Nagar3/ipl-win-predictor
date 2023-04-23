import pickle
import pandas as pd
import streamlit as st

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Gujarat Titans',
'Lucknow Super Giants']

cities = ['Ahmedabad', 'Kolkata', 'Mumbai', 'Pune', 'Navi Mumbai', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

pipe = pickle.load(open('pipe11.pkl','rb'))

st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    bat_team = st.selectbox('Select the Batting team',sorted(teams))
with col2:
    bol_team = st.selectbox('Select the Bowling team',sorted(teams))

select_city = st.selectbox('Select host City',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs Completed')
with col5:
    wickets = st.number_input('Wicket Out')

if st.button('Predict Future'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wicketss = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    data_df = pd.DataFrame({
        'BattingTeam':[bat_team],
        'BowlingTeam':[bol_team],
        'City':[select_city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets':[wicketss],
        'total_run_x':[target],
        'crr':[crr],
        'rrr':[rrr]
    })

    # st.table(data_df)
    result = pipe.predict_proba(data_df)
    loss = result[0][0]
    win = result[0][1]

    st.header(bat_team + "- " + str(round(win * 100)) + "%")
    st.header(bol_team + "- " + str(round(loss * 100)) + "%")
