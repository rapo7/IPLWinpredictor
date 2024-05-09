import streamlit as st
import sklearn
import pandas as pd
import pickle
pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')
teams = sorted(['Royal Challengers Bengaluru','Kings XI Punjab','Delhi Capitals',
 'Mumbai Indians','Kolkata Knight Riders','Rajasthan Royals',
 'Sunrisers Hyderabad','Chennai Super Kings','Kochi Tuskers Kerala',
 'Rising Pune Supergiant','Gujarat Lions','Punjab Kings',
 'Lucknow Super Giants'])

col1,col2 = st.columns(2)

with col1:
    batting_team =st.selectbox('Select the batting team',teams)
teams.remove(batting_team)
with col2:
    bowling_team = st.selectbox('Select the bowling team',teams)
    
Venues = sorted(['Arun Jaitley Stadium', 'Barabati Stadium', 'Barsapara Cricket Stadium, Guwahati', 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow', 'Brabourne Stadium, Mumbai', 'Buffalo Park', 'De Beers Diamond Oval', 'Dr DY Patil Sports Academy, Mumbai', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam', 'Dubai International Cricket Stadium', 'Eden Gardens, Kolkata', 'Feroz Shah Kotla', 'Green Park', 'Himachal Pradesh Cricket Association Stadium, Dharamsala', 'Holkar Cricket Stadium', 'JSCA International Stadium Complex', 'Kingsmead', 'M Chinnaswamy Stadium, Bengaluru', 'MA Chidambaram Stadium, Chepauk, Chennai', 'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur', 'Maharashtra Cricket Association Stadium, Pune', 'Narendra Modi Stadium, Ahmedabad', 'Nehru Stadium', 'New Wanderers Stadium', 'Newlands', 'OUTsurance Oval', 'Punjab Cricket Association IS Bindra Stadium', 'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh', 'Rajiv Gandhi International Stadium, Uppal, Hyderabad', 'Sardar Patel Stadium, Motera', 'Saurashtra Cricket Association Stadium', 'Sawai Mansingh Stadium, Jaipur', 'Shaheed Veer Narayan Singh International Stadium', 'Sharjah Cricket Stadium', 'Sheikh Zayed Stadium', "St George's Park", 'Subrata Roy Sahara Stadium', 'SuperSport Park', 'Vidarbha Cricket Association Stadium, Jamtha', 'Wankhede Stadium, Mumbai', 'Zayed Cricket Stadium, Abu Dhabi'])

selected_city = st.selectbox('Stadium',sorted(Venues))

target = st.number_input('Target',min_value=0)

col3,col4,col5 = st.columns(3)
with col3 :
    score =st.number_input('Score',min_value=0)
with col4 :
    wickets =st.number_input('Wickets',min_value=0,max_value=9)
with col5 :
    overs = st.number_input('Overs completed',min_value=1,max_value=20)
    
if st.button('Predict Probability'):

    runs_left = target-score
    balls_left = 120 - overs*6
    wickets = 10-wickets
    crr = score/overs
    rrr = runs_left*6/balls_left
    runs_left = target-score
    # 'Batting team', 'Bowling team', 'Venue', 'runs_scored_x
    df =pd.DataFrame({'Batting team':[batting_team],'Bowling team':[bowling_team],'Venue':[selected_city],'runs_scored_x':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr],'runs_left':[runs_left]})    
    result = pipe.predict_proba(df)
    r_1 = round(result[0][0]*100)
    r_2 = round(result[0][1]*100)
    st.header('Wining Probabilty ')
    st.header(f"{batting_team}  : {r_2} %")
    st.header(f"{bowling_team}  : {r_1} %")