# Steps:
# - Run fill_fantasy_table_v2.py code
# - Change updated_points in this file to True
# - Commit all fantasy files to Github
# - Refresh link for updates and check if all correct
# - Change updated_points in this file to False
# - Manually change standings.csv
# - Commit this file + standings.csv to Github
import sys

import streamlit as st
import pandas as pd

hidden_color = "black"
weekly_df = pd.read_csv("fantasy_weekly_v2.csv", index_col=0)
standings_df = pd.read_csv("standings_v2.csv", index_col=0)


updated_points = True


#######################################################################################################################
############################################### USERS TEAMS ###########################################################
#######################################################################################################################
charbel = [{
    "G1": "Sergio Herrera",
    "D1": "Jules Koundé",
    "D2": "Nacho Fernández",
    "D3": "Axel Witsel",
    "D4": "Sokratis",
    "M1": "Nico Williams",
    "M2": "Álvaro García",
    "M3": "Facundo Pellistri",
    "F1": "Lamine Yamal",
    "F2": "Antoine Griezmann",
    "F3": "Alexander Sørloth",
    "G2": "Álex Remiro",
    "D5": "Cristhian Mosquera",
    "M4": "Jude Bellingham",
    "F4": "Youssef En-Nesyri",
}]

ralph = [{
    "G1": "Jan Oblak",
    "D1": "Mario Hermoso",
    "D2": "Daniel Carvajal",
    "D3": "David García",
    "D4": "Héctor Bellerín",
    "M1": "Takefusa Kubo",
    "M2": "Alejandro Baena",
    "M3": "Mason Greenwood",
    "F1": "Rodrygo",
    "F2": "Borja Mayoral",
    "F3": "Hugo Duro",
    "G2": "Andriy Lunin",
    "D5": "Miguel Gutiérrez",
    "M4": "Sávio",
    "F4": "Mikel Oyarzabal",
}]

george = [{
    "G1": "Stole Dimitrievski",
    "D1": "Daley Blind",
    "D2": "Aitor Paredes",
    "D3": "Ronald Araújo",
    "D4": "Antonio Rüdiger",
    "M1": "Toni Kroos",
    "M2": "Nabil Fekir",
    "M3": "Oihan Sancet",
    "F1": "Robert Lewandowski",
    "F2": "Artem Dovbyk",
    "F3": "João Félix",
    "G2": "Marc-André ter Stegen",
    "D5": "Aihen Muñoz",
    "M4": "Bryan Zaragoza",
    "F4": "Gerard Moreno",
}]

rene = [{
    "G1": "Rui Silva",
    "D1": "João Cancelo",
    "D2": "Robin Le Normand",
    "D3": "Óscar de Marcos",
    "D4": "Ferland Mendy",
    "M1": "İlkay Gündoğan",
    "M2": "Iñaki Williams",
    "M3": "Brais Méndez",
    "F1": "Memphis Depay",
    "F2": "Ante Budimir",
    "F3": "Vinícius Júnior",
    "G2": "Unai Simón",
    "D5": "Alejandro Baldé",
    "M4": "Pepelu",
    "F4": "Álvaro Morata",
}]


#######################################################################################################################
############################################### UNCHANGED UI ###########################################################
#######################################################################################################################

st.set_page_config(page_title="Fantasy La Liga", layout="wide")
st.title("Fantasy La Liga")
# st.image("https://iscreativestudio.com/wp-content/uploads/2016/08/logotipos4.jpg", width=100)

st.header("Charbel")
# Charbel - Team Structure
cols = st.columns(5)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[1].write("%s" % charbel[0]["G1"])
G1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["G1"], 'Pts']
G1_weekly_pts_c = G1_weekly_pts_c.reset_index()
G1_weekly_pts_c = G1_weekly_pts_c["Pts"][0]
cols[1].write("%i" % G1_weekly_pts_c)

cols[0].write("%s" % charbel[0]["D1"])
D1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D1"], 'Pts']
D1_weekly_pts_c = D1_weekly_pts_c.reset_index()
D1_weekly_pts_c = D1_weekly_pts_c["Pts"][0]
cols[0].write("%i" % D1_weekly_pts_c)

cols[1].write("%s" % charbel[0]["D2"])
D2_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D2"], 'Pts']
D2_weekly_pts_c = D2_weekly_pts_c.reset_index()
D2_weekly_pts_c = D2_weekly_pts_c["Pts"][0]
cols[1].write("%i" % D2_weekly_pts_c)

cols[2].write("%s" % charbel[0]["D3"])
D3_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D3"], 'Pts']
D3_weekly_pts_c = D3_weekly_pts_c.reset_index()
D3_weekly_pts_c = D3_weekly_pts_c["Pts"][0]
cols[2].write("%i" % D3_weekly_pts_c)

cols[3].write("%s" % charbel[0]["D4"])
D4_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D4"], 'Pts']
D4_weekly_pts_c = D4_weekly_pts_c.reset_index()
D4_weekly_pts_c = D4_weekly_pts_c["Pts"][0]
cols[3].write("%i" % D4_weekly_pts_c)

cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[0].write("%s" % charbel[0]["M1"])
M1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["M1"], 'Pts']
M1_weekly_pts_c = M1_weekly_pts_c.reset_index()
M1_weekly_pts_c = M1_weekly_pts_c["Pts"][0]
cols[0].write("%i" % M1_weekly_pts_c)

cols[1].write("%s" % charbel[0]["M2"])
M2_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["M2"], 'Pts']
M2_weekly_pts_c = M2_weekly_pts_c.reset_index()
M2_weekly_pts_c = M2_weekly_pts_c["Pts"][0]
cols[1].write("%i" % M2_weekly_pts_c)

cols[2].write("%s" % charbel[0]["M3"])
M3_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["M3"], 'Pts']
M3_weekly_pts_c = M3_weekly_pts_c.reset_index()
M3_weekly_pts_c = M3_weekly_pts_c["Pts"][0]
cols[2].write("%i" % M3_weekly_pts_c)

cols[0].write("%s" % charbel[0]["F1"])
F1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["F1"], 'Pts']
F1_weekly_pts_c = F1_weekly_pts_c.reset_index()
F1_weekly_pts_c = F1_weekly_pts_c["Pts"][0]
cols[0].write("%i" % F1_weekly_pts_c)

cols[1].write("%s" % charbel[0]["F2"])
F2_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["F2"], 'Pts']
F2_weekly_pts_c = F2_weekly_pts_c.reset_index()
F2_weekly_pts_c = F2_weekly_pts_c["Pts"][0]
cols[1].write("%i" % F2_weekly_pts_c)

cols[2].write("%s" % charbel[0]["F3"])
F3_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["F3"], 'Pts']
F3_weekly_pts_c = F3_weekly_pts_c.reset_index()
F3_weekly_pts_c = F3_weekly_pts_c["Pts"][0]
cols[2].write("%i" % F3_weekly_pts_c)

# Bench
cols[0].write("_%s_" % charbel[0]["G2"])
cols[0].write("%i" % weekly_df.loc[weekly_df["Name"] == charbel[0]["G2"], 'Pts'])
cols[1].write("_%s_" % charbel[0]["D5"])
cols[1].write("%i" % weekly_df.loc[weekly_df["Name"] == charbel[0]["D5"], 'Pts'])
cols[2].write("_%s_" % charbel[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == charbel[0]["M4"], 'Pts'])
cols[3].write("_%s_" % charbel[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == charbel[0]["F4"], 'Pts'])

if (weekly_df.loc[weekly_df["Name"] == charbel[0]["G1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    G1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["G2"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == charbel[0]["D1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == charbel[0]["D2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D2_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == charbel[0]["D3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D3_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == charbel[0]["D4"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D4_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["D5"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == charbel[0]["M1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == charbel[0]["M2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M2_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == charbel[0]["M3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M3_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["M4"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == charbel[0]["F1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F1_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == charbel[0]["F2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F2_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == charbel[0]["F3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F3_weekly_pts_c = weekly_df.loc[weekly_df["Name"] == charbel[0]["F4"], 'Pts'].reset_index()["Pts"][0]


charbel_weekly_pts = G1_weekly_pts_c + D1_weekly_pts_c + D2_weekly_pts_c + D3_weekly_pts_c + D4_weekly_pts_c \
                     + M1_weekly_pts_c + M2_weekly_pts_c + M3_weekly_pts_c + F1_weekly_pts_c + F2_weekly_pts_c \
                     + F3_weekly_pts_c

cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].write("**Total:** %i" % charbel_weekly_pts)


st.header("Ralph")
# Ralph - Team Structure
cols = st.columns(5)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[1].write("%s" % ralph[0]["G1"])
G1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["G1"], 'Pts']
G1_weekly_pts_ra = G1_weekly_pts_ra.reset_index()
G1_weekly_pts_ra = G1_weekly_pts_ra["Pts"][0]
cols[1].write("%i" % G1_weekly_pts_ra)

cols[0].write("%s" % ralph[0]["D1"])
D1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D1"], 'Pts']
D1_weekly_pts_ra = D1_weekly_pts_ra.reset_index()
D1_weekly_pts_ra = D1_weekly_pts_ra["Pts"][0]
cols[0].write("%i" % D1_weekly_pts_ra)

cols[1].write("%s" % ralph[0]["D2"])
D2_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D2"], 'Pts']
D2_weekly_pts_ra = D2_weekly_pts_ra.reset_index()
D2_weekly_pts_ra = D2_weekly_pts_ra["Pts"][0]
cols[1].write("%i" % D2_weekly_pts_ra)

cols[2].write("%s" % ralph[0]["D3"])
D3_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D3"], 'Pts']
D3_weekly_pts_ra = D3_weekly_pts_ra.reset_index()
D3_weekly_pts_ra = D3_weekly_pts_ra["Pts"][0]
cols[2].write("%i" % D3_weekly_pts_ra)

cols[3].write("%s" % ralph[0]["D4"])
D4_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D4"], 'Pts']
D4_weekly_pts_ra = D4_weekly_pts_ra.reset_index()
D4_weekly_pts_ra = D4_weekly_pts_ra["Pts"][0]
cols[3].write("%i" % D4_weekly_pts_ra)

cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[0].write("%s" % ralph[0]["M1"])
M1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["M1"], 'Pts']
M1_weekly_pts_ra = M1_weekly_pts_ra.reset_index()
M1_weekly_pts_ra = M1_weekly_pts_ra["Pts"][0]
cols[0].write("%i" % M1_weekly_pts_ra)

cols[1].write("%s" % ralph[0]["M2"])
M2_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["M2"], 'Pts']
M2_weekly_pts_ra = M2_weekly_pts_ra.reset_index()
M2_weekly_pts_ra = M2_weekly_pts_ra["Pts"][0]
cols[1].write("%i" % M2_weekly_pts_ra)

cols[2].write("%s" % ralph[0]["M3"])
M3_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["M3"], 'Pts']
M3_weekly_pts_ra = M3_weekly_pts_ra.reset_index()
M3_weekly_pts_ra = M3_weekly_pts_ra["Pts"][0]
cols[2].write("%i" % M3_weekly_pts_ra)

cols[0].write("%s" % ralph[0]["F1"])
F1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["F1"], 'Pts']
F1_weekly_pts_ra = F1_weekly_pts_ra.reset_index()
F1_weekly_pts_ra = F1_weekly_pts_ra["Pts"][0]
cols[0].write("%i" % F1_weekly_pts_ra)

cols[1].write("%s" % ralph[0]["F2"])
F2_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["F2"], 'Pts']
F2_weekly_pts_ra = F2_weekly_pts_ra.reset_index()
F2_weekly_pts_ra = F2_weekly_pts_ra["Pts"][0]
cols[1].write("%i" % F2_weekly_pts_ra)

cols[2].write("%s" % ralph[0]["F3"])
F3_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["F3"], 'Pts']
F3_weekly_pts_ra = F3_weekly_pts_ra.reset_index()
F3_weekly_pts_ra = F3_weekly_pts_ra["Pts"][0]
cols[2].write("%i" % F3_weekly_pts_ra)

# Bench
cols[0].write("_%s_" % ralph[0]["G2"])
cols[0].write("%i" % weekly_df.loc[weekly_df["Name"] == ralph[0]["G2"], 'Pts'])
cols[1].write("_%s_" % ralph[0]["D5"])
cols[1].write("%i" % weekly_df.loc[weekly_df["Name"] == ralph[0]["D5"], 'Pts'])
cols[2].write("_%s_" % ralph[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == ralph[0]["M4"], 'Pts'])
cols[3].write("_%s_" % ralph[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == ralph[0]["F4"], 'Pts'])

if (weekly_df.loc[weekly_df["Name"] == ralph[0]["G1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    G1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["G2"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == ralph[0]["D1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == ralph[0]["D2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D2_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == ralph[0]["D3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D3_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == ralph[0]["D4"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D4_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["D5"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == ralph[0]["M1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == ralph[0]["M2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M2_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == ralph[0]["M3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M3_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["M4"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == ralph[0]["F1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F1_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == ralph[0]["F2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F2_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == ralph[0]["F3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F3_weekly_pts_ra = weekly_df.loc[weekly_df["Name"] == ralph[0]["F4"], 'Pts'].reset_index()["Pts"][0]

ralph_weekly_pts = G1_weekly_pts_ra + D1_weekly_pts_ra + D2_weekly_pts_ra + D3_weekly_pts_ra + D4_weekly_pts_ra \
                     + M1_weekly_pts_ra + M2_weekly_pts_ra + M3_weekly_pts_ra + F1_weekly_pts_ra + F2_weekly_pts_ra + F3_weekly_pts_ra
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].write("**Total:** %i" % ralph_weekly_pts)


st.header("George")
# George - Team Structure
cols = st.columns(5)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[1].write("%s" % george[0]["G1"])
G1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["G1"], 'Pts']
G1_weekly_pts_g = G1_weekly_pts_g.reset_index()
G1_weekly_pts_g = G1_weekly_pts_g["Pts"][0]
cols[1].write("%i" % G1_weekly_pts_g)

cols[0].write("%s" % george[0]["D1"])
D1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D1"], 'Pts']
D1_weekly_pts_g = D1_weekly_pts_g.reset_index()
D1_weekly_pts_g = D1_weekly_pts_g["Pts"][0]
cols[0].write("%i" % D1_weekly_pts_g)

cols[1].write("%s" % george[0]["D2"])
D2_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D2"], 'Pts']
D2_weekly_pts_g = D2_weekly_pts_g.reset_index()
D2_weekly_pts_g = D2_weekly_pts_g["Pts"][0]
cols[1].write("%i" % D2_weekly_pts_g)

cols[2].write("%s" % george[0]["D3"])
D3_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D3"], 'Pts']
D3_weekly_pts_g = D3_weekly_pts_g.reset_index()
D3_weekly_pts_g = D3_weekly_pts_g["Pts"][0]
cols[2].write("%i" % D3_weekly_pts_g)

cols[3].write("%s" % george[0]["D4"])
D4_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D4"], 'Pts']
D4_weekly_pts_g = D4_weekly_pts_g.reset_index()
D4_weekly_pts_g = D4_weekly_pts_g["Pts"][0]
cols[3].write("%i" % D4_weekly_pts_g)

cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[0].write("%s" % george[0]["M1"])
M1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["M1"], 'Pts']
M1_weekly_pts_g = M1_weekly_pts_g.reset_index()
M1_weekly_pts_g = M1_weekly_pts_g["Pts"][0]
cols[0].write("%i" % M1_weekly_pts_g)

cols[1].write("%s" % george[0]["M2"])
M2_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["M2"], 'Pts']
M2_weekly_pts_g = M2_weekly_pts_g.reset_index()
M2_weekly_pts_g = M2_weekly_pts_g["Pts"][0]
cols[1].write("%i" % M2_weekly_pts_g)

cols[2].write("%s" % george[0]["M3"])
M3_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["M3"], 'Pts']
M3_weekly_pts_g = M3_weekly_pts_g.reset_index()
M3_weekly_pts_g = M3_weekly_pts_g["Pts"][0]
cols[2].write("%i" % M3_weekly_pts_g)

cols[0].write("%s" % george[0]["F1"])
F1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["F1"], 'Pts']
F1_weekly_pts_g = F1_weekly_pts_g.reset_index()
F1_weekly_pts_g = F1_weekly_pts_g["Pts"][0]
cols[0].write("%i" % F1_weekly_pts_g)

cols[1].write("%s" % george[0]["F2"])
F2_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["F2"], 'Pts']
F2_weekly_pts_g = F2_weekly_pts_g.reset_index()
F2_weekly_pts_g = F2_weekly_pts_g["Pts"][0]
cols[1].write("%i" % F2_weekly_pts_g)

cols[2].write("%s" % george[0]["F3"])
F3_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["F3"], 'Pts']
F3_weekly_pts_g = F3_weekly_pts_g.reset_index()
F3_weekly_pts_g = F3_weekly_pts_g["Pts"][0]
cols[2].write("%i" % F3_weekly_pts_g)

# Bench
cols[0].write("_%s_" % george[0]["G2"])
cols[0].write("%i" % weekly_df.loc[weekly_df["Name"] == george[0]["G2"], 'Pts'])
cols[1].write("_%s_" % george[0]["D5"])
cols[1].write("%i" % weekly_df.loc[weekly_df["Name"] == george[0]["D5"], 'Pts'])
cols[2].write("_%s_" % george[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == george[0]["M4"], 'Pts'])
cols[3].write("_%s_" % george[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == george[0]["F4"], 'Pts'])

if (weekly_df.loc[weekly_df["Name"] == george[0]["G1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    G1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["G2"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == george[0]["D1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == george[0]["D2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D2_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == george[0]["D3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D3_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == george[0]["D4"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D4_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["D5"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == george[0]["M1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == george[0]["M2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M2_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == george[0]["M3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M3_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["M4"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == george[0]["F1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F1_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == george[0]["F2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F2_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == george[0]["F3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F3_weekly_pts_g = weekly_df.loc[weekly_df["Name"] == george[0]["F4"], 'Pts'].reset_index()["Pts"][0]

george_weekly_pts = G1_weekly_pts_g + D1_weekly_pts_g + D2_weekly_pts_g + D3_weekly_pts_g + D4_weekly_pts_g \
                     + M1_weekly_pts_g + M2_weekly_pts_g + M3_weekly_pts_g + F1_weekly_pts_g + F2_weekly_pts_g + F3_weekly_pts_g
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].write("**Total:** %i" % george_weekly_pts)


st.header("Rene")
# Rene - Team Structure
cols = st.columns(5)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[0].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[2].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[1].write("%s" % rene[0]["G1"])
G1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["G1"], 'Pts']
G1_weekly_pts_re = G1_weekly_pts_re.reset_index()
G1_weekly_pts_re = G1_weekly_pts_re["Pts"][0]
cols[1].write("%i" % G1_weekly_pts_re)

cols[0].write("%s" % rene[0]["D1"])
D1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D1"], 'Pts']
D1_weekly_pts_re = D1_weekly_pts_re.reset_index()
D1_weekly_pts_re = D1_weekly_pts_re["Pts"][0]
cols[0].write("%i" % D1_weekly_pts_re)

cols[1].write("%s" % rene[0]["D2"])
D2_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D2"], 'Pts']
D2_weekly_pts_re = D2_weekly_pts_re.reset_index()
D2_weekly_pts_re = D2_weekly_pts_re["Pts"][0]
cols[1].write("%i" % D2_weekly_pts_re)

cols[2].write("%s" % rene[0]["D3"])
D3_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D3"], 'Pts']
D3_weekly_pts_re = D3_weekly_pts_re.reset_index()
D3_weekly_pts_re = D3_weekly_pts_re["Pts"][0]
cols[2].write("%i" % D3_weekly_pts_re)

cols[3].write("%s" % rene[0]["D4"])
D4_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D4"], 'Pts']
D4_weekly_pts_re = D4_weekly_pts_re.reset_index()
D4_weekly_pts_re = D4_weekly_pts_re["Pts"][0]
cols[3].write("%i" % D4_weekly_pts_re)

cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[3].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)

cols[0].write("%s" % rene[0]["M1"])
M1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["M1"], 'Pts']
M1_weekly_pts_re = M1_weekly_pts_re.reset_index()
M1_weekly_pts_re = M1_weekly_pts_re["Pts"][0]
cols[0].write("%i" % M1_weekly_pts_re)

cols[1].write("%s" % rene[0]["M2"])
M2_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["M2"], 'Pts']
M2_weekly_pts_re = M2_weekly_pts_re.reset_index()
M2_weekly_pts_re = M2_weekly_pts_re["Pts"][0]
cols[1].write("%i" % M2_weekly_pts_re)

cols[2].write("%s" % rene[0]["M3"])
M3_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["M3"], 'Pts']
M3_weekly_pts_re = M3_weekly_pts_re.reset_index()
M3_weekly_pts_re = M3_weekly_pts_re["Pts"][0]
cols[2].write("%i" % M3_weekly_pts_re)

cols[0].write("%s" % rene[0]["F1"])
F1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["F1"], 'Pts']
F1_weekly_pts_re = F1_weekly_pts_re.reset_index()
F1_weekly_pts_re = F1_weekly_pts_re["Pts"][0]
cols[0].write("%i" % F1_weekly_pts_re)

cols[1].write("%s" % rene[0]["F2"])
F2_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["F2"], 'Pts']
F2_weekly_pts_re = F2_weekly_pts_re.reset_index()
F2_weekly_pts_re = F2_weekly_pts_re["Pts"][0]
cols[1].write("%i" % F2_weekly_pts_re)

cols[2].write("%s" % rene[0]["F3"])
F3_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["F3"], 'Pts']
F3_weekly_pts_re = F3_weekly_pts_re.reset_index()
F3_weekly_pts_re = F3_weekly_pts_re["Pts"][0]
cols[2].write("%i" % F3_weekly_pts_re)

# Bench
cols[0].write("_%s_" % rene[0]["G2"])
cols[0].write("%i" % weekly_df.loc[weekly_df["Name"] == rene[0]["G2"], 'Pts'])
cols[1].write("_%s_" % rene[0]["D5"])
cols[1].write("%i" % weekly_df.loc[weekly_df["Name"] == rene[0]["D5"], 'Pts'])
cols[2].write("_%s_" % rene[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == rene[0]["M4"], 'Pts'])
cols[3].write("_%s_" % rene[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == rene[0]["F4"], 'Pts'])

if (weekly_df.loc[weekly_df["Name"] == rene[0]["G1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    G1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["G2"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == rene[0]["D1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == rene[0]["D2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D2_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == rene[0]["D3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D3_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D5"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == rene[0]["D4"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    D4_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["D5"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == rene[0]["M1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == rene[0]["M2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M2_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["M4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == rene[0]["M3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    M3_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["M4"], 'Pts'].reset_index()["Pts"][0]

if (weekly_df.loc[weekly_df["Name"] == rene[0]["F1"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F1_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == rene[0]["F2"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F2_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["F4"], 'Pts'].reset_index()["Pts"][0]
elif (weekly_df.loc[weekly_df["Name"] == rene[0]["F3"], 'Mins Pts']).reset_index()["Mins Pts"][0] == 0:
    F3_weekly_pts_re = weekly_df.loc[weekly_df["Name"] == rene[0]["F4"], 'Pts'].reset_index()["Pts"][0]

rene_weekly_pts = G1_weekly_pts_re + D1_weekly_pts_re + D2_weekly_pts_re + D3_weekly_pts_re + D4_weekly_pts_re \
                     + M1_weekly_pts_re + M2_weekly_pts_re + M3_weekly_pts_re + F1_weekly_pts_re + F2_weekly_pts_re \
                  + F3_weekly_pts_re
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].markdown("<font color=%s> . </font>" % hidden_color, unsafe_allow_html=True)
cols[4].write("**Total:** %i" % rene_weekly_pts)


# Adding to standings
charbel_total_pts = standings_df.loc[0]['Total_pts']
ralph_total_pts = standings_df.loc[1]['Total_pts']
george_total_pts = standings_df.loc[2]['Total_pts']
rene_total_pts = standings_df.loc[3]['Total_pts']

standings_df.loc[0, "Weekly_pts"] = charbel_weekly_pts
standings_df.loc[1, "Weekly_pts"] = ralph_weekly_pts
standings_df.loc[2, "Weekly_pts"] = george_weekly_pts
standings_df.loc[3, "Weekly_pts"] = rene_weekly_pts

standings_df.loc[0, "Total_pts"] = charbel_weekly_pts + charbel_total_pts
standings_df.loc[1, "Total_pts"] = ralph_weekly_pts + ralph_total_pts
standings_df.loc[2, "Total_pts"] = george_weekly_pts + george_total_pts
standings_df.loc[3, "Total_pts"] = rene_weekly_pts + rene_total_pts

#######################################################################################################################
############################################### Players DF ###########################################################
#######################################################################################################################
st.header("Total Players Stats")

df = pd.read_csv("fantasy_all_players.csv", index_col=0)
df = df.sort_values(by="Pts", ascending=False, ignore_index=True)

players_taken = [charbel[0]["G1"], charbel[0]["D1"], charbel[0]["D2"], charbel[0]["D3"], charbel[0]["D4"], charbel[0]["D5"],
                 charbel[0]["M1"], charbel[0]["M2"], charbel[0]["M3"], charbel[0]["M4"], charbel[0]["F1"], charbel[0]["F2"],
                 charbel[0]["F3"], charbel[0]["F4"], charbel[0]["G2"],
                 ralph[0]["G1"], ralph[0]["D1"], ralph[0]["D2"], ralph[0]["D3"], ralph[0]["D4"],
                 ralph[0]["D5"], ralph[0]["M1"], ralph[0]["M2"], ralph[0]["M3"], ralph[0]["M4"], ralph[0]["F1"],
                 ralph[0]["F2"], ralph[0]["F3"], ralph[0]["F4"], ralph[0]["G2"],
                 george[0]["G1"], george[0]["D1"], george[0]["D2"], george[0]["D3"], george[0]["D4"],
                 george[0]["D5"], george[0]["M1"], george[0]["M2"], george[0]["M3"], george[0]["M4"], george[0]["F1"],
                 george[0]["F2"], george[0]["F3"], george[0]["F4"], george[0]["G2"],
                 rene[0]["G1"], rene[0]["D1"], rene[0]["D2"], rene[0]["D3"], rene[0]["D4"],
                 rene[0]["D5"], rene[0]["M1"], rene[0]["M2"], rene[0]["M3"], rene[0]["M4"], rene[0]["F1"],
                 rene[0]["F2"], rene[0]["F3"], rene[0]["F4"], rene[0]["G2"]
                 ]


def color_survived(val):
    color = 'tomato' if val in players_taken else 'black'
    return f'background-color: {color}'


values = ("None", "Athletic Club", "Atlético Madrid", "Osasuna", "Cádiz", "Deportivo Alavés", "Barcelona", "Getafe",
          "Girona", "Granada", "Rayo Vallecano", "Celta Vigo", "Mallorca", "Real Betis", "Real Madrid", "Real Sociedad",
          "Sevilla", "Las Palmas", "Almería", "Valencia", "Villarreal")
option = st.selectbox('Filter by Team', values, index=0, key="total")

values_pos = ("None", "G", "D", "M", "F")
option_pos = st.selectbox('Filter by Position', values_pos, index=0, key="weekly")

show_available = st.checkbox("Show available")

if option != "None" and option_pos == "None" and show_available:
    df = df.loc[(df["Team"] == option) & (~df["Name"].isin(players_taken))]
elif option != "None" and option_pos == "None" and not show_available:
    df = df.loc[(df["Team"] == option)]
elif option == "None" and option_pos != "None" and not show_available:
    df = df.loc[df["Position"] == option_pos]
elif option == "None" and option_pos != "None" and show_available:
    df = df.loc[(df["Position"] == option_pos) & (~df["Name"].isin(players_taken))]
elif option != "None" and option_pos != "None" and not show_available:
    df = df.loc[(df["Position"] == option_pos) & (df["Team"] == option)]
elif option != "None" and option_pos != "None" and show_available:
    df = df.loc[(df["Position"] == option_pos) & (df["Team"] == option) & (~df["Name"].isin(players_taken))]
elif option == "None" and option_pos == "None" and show_available:
    df = df.loc[~df["Name"].isin(players_taken)]
else:
    pass

st.dataframe(df.style.applymap(color_survived, subset=["Name"]))


st.header("Weekly Player Stats")
weekly_df = weekly_df.sort_values(by="Pts", ascending=False, ignore_index=True)

option_weekly = st.selectbox('Filter by Team', values, index=0)
option_pos_weekly = st.selectbox('Filter by Position', values_pos, index=0)

if option_weekly != "None" and option_pos_weekly == "None":
    weekly_df = weekly_df.loc[weekly_df["Team"] == option_weekly]
elif option_weekly == "None" and option_pos_weekly != "None":
    weekly_df = weekly_df.loc[weekly_df["Position"] == option_pos_weekly]
elif option_weekly != "None" and option_pos_weekly != "None":
    weekly_df = weekly_df.loc[(weekly_df["Position"] == option_pos_weekly) & (weekly_df["Team"] == option_weekly)]
else:
    pass

st.dataframe(weekly_df)

st.header("Standings")

if not updated_points:
    old_standings_df = pd.read_csv("standings_v2.csv", index_col=0)
    st.dataframe(old_standings_df)
if updated_points:
    st.dataframe(standings_df)
    standings_df.to_csv("standings_v2.csv")

st.subheader("Past Standings")
past_data = {'year': ["2019/2020", "2020/2021", "2021/2022", "2022/2023"], 'Charbel': ["1276", "1378", "1588", "1689"],
             'Ralph': ["1203", "1429", "1511", "1172"], 'George': ["1315", "1470", "1377", "1619"],
             'Rene': ["1209", "1690", "1603", "1458"]}
past_df = pd.DataFrame(past_data)
st.dataframe(past_df)
