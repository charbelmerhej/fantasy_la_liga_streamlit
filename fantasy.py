# If player not found in database / new player --> Add in both CSV + as a variable in both .py

#TODO:
# Need to check if there is a faster way then changing updated_points every time to True then to False while each time uploading on Github (and making sure no one refreshes the app)
# Start putting variables for all players

# Future idea: Do a dropdown or search on Streamlit to choose a player and show a line graph of his points every gw OR
# Do a 3rd df which includes all the players and 38 cols for each gw pts they got.


import streamlit as st
import pandas as pd

hidden_color = "black"
weekly_df = pd.read_csv("fantasy_weekly.csv", index_col=0)
standings_df = pd.read_csv("standings.csv", index_col=0)


#######################################################################################################################
############################################### ALL PLAYERS ###########################################################
#######################################################################################################################
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"
i = "i"
j = "j"
k = "k"
l = "l"
m = "m"
n = "n"
o = "o"

inaki_williams = "Inaki Williams"
nico_williams = "Nico Williams"
raul_garcia = "Raul Garcia"
oihan_sancet = "Oihan Sancet"
asier_villalibre = "Asier Villalibre"
gorka_guruzeta = "Gorka Guruzeta"
luis_bilbao = "Luis Bilbao"
malcom_ares = "Malcom Ares"
iker_munian = "Iker Munian"
alex_berenguer = "Alex Berenguer"
unai_vencedor = "Unai Vencedor"
dani_garcia = "Dani Garcia"
mikel_vesga = "Mikel Vesga"
nico_serrano = "Nico Serrano"
oier_zarraga = "Oier Zarraga"
jon_morcillo = "Jon Morcillo"
inigo_martinez = "Inigo Martinez"
yuri_berchiche = "Yuri Berchiche"
yeray_alvarez = "Yeray Alvarez"
daniel_vivian = "Daniel Vivian"
ander_capa = "Ander Capa"
oscar_de_marcos = "Oscar De Marcos"
mikel_balenziaga = "Mikel Balenziaga"
inigo_lekue = "Inigo Lekue"
peru_esnal = "Peru Esnal"
alex_petxa = "Alex Petxa"
aitor_casamichana = "Aitor Casamichana"
jon_sillero = "Jon Sillero"
unai_simon = "Unai Simon"
julen_agirrezabala = "Julen Agirrezabala"
alex_padilla = "Alex Padilla"
ander_iru = "Ander Iru"


#######################################################################################################################
############################################### USERS TEAMS ###########################################################
#######################################################################################################################
charbel = [{
    "G1": a,
    "D1": a,
    "D2": a,
    "D3": a,
    "D4": a,
    "M1": a,
    "M2": a,
    "M3": a,
    "F1": a,
    "F2": a,
    "F3": a,
    "G2": a,
    "D5": a,
    "M5": a,
    "F4": a,
}]

ralph = [{
    "G1": a,
    "D1": a,
    "D2": a,
    "D3": a,
    "D4": a,
    "M1": a,
    "M2": a,
    "M3": a,
    "F1": a,
    "F2": a,
    "F3": a,
    "G2": a,
    "D5": a,
    "M5": a,
    "F4": a,
}]

george = [{
    "G1": a,
    "D1": a,
    "D2": a,
    "D3": a,
    "D4": a,
    "M1": a,
    "M2": a,
    "M3": a,
    "F1": a,
    "F2": a,
    "F3": a,
    "G2": a,
    "D5": a,
    "M5": a,
    "F4": a,
}]

rene = [{
    "G1": b,
    "D1": a,
    "D2": a,
    "D3": a,
    "D4": a,
    "M1": a,
    "M2": a,
    "M3": a,
    "F1": a,
    "F2": a,
    "F3": a,
    "G2": a,
    "D5": a,
    "M5": a,
    "F4": b,
}]


#######################################################################################################################
############################################### UNCHANGED UI ###########################################################
#######################################################################################################################

st.title("Fantasy La Liga")
st.image("https://iscreativestudio.com/wp-content/uploads/2016/08/logotipos4.jpg", width=100)

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
cols[2].write("_%s_" % charbel[0]["M5"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == charbel[0]["M5"], 'Pts'])
cols[3].write("_%s_" % charbel[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == charbel[0]["F4"], 'Pts'])

charbel_weekly_pts = G1_weekly_pts_c + D1_weekly_pts_c + D2_weekly_pts_c + D3_weekly_pts_c + D4_weekly_pts_c \
                     + M1_weekly_pts_c + M2_weekly_pts_c + M3_weekly_pts_c + F1_weekly_pts_c + F2_weekly_pts_c + F3_weekly_pts_c
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
cols[2].write("_%s_" % ralph[0]["M5"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == ralph[0]["M5"], 'Pts'])
cols[3].write("_%s_" % ralph[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == ralph[0]["F4"], 'Pts'])

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
cols[2].write("_%s_" % george[0]["M5"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == george[0]["M5"], 'Pts'])
cols[3].write("_%s_" % george[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == george[0]["F4"], 'Pts'])

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
cols[2].write("_%s_" % rene[0]["M5"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == rene[0]["M5"], 'Pts'])
cols[3].write("_%s_" % rene[0]["F4"])
cols[3].write("%i" % weekly_df.loc[weekly_df["Name"] == rene[0]["F4"], 'Pts'])

rene_weekly_pts = G1_weekly_pts_re + D1_weekly_pts_re + D2_weekly_pts_re + D3_weekly_pts_re + D4_weekly_pts_re \
                     + M1_weekly_pts_re + M2_weekly_pts_re + M3_weekly_pts_re + F1_weekly_pts_re + F2_weekly_pts_re + F3_weekly_pts_re
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

df = pd.read_csv("fantasy.csv", index_col=0)
st.dataframe(df)


st.header("Weekly Player Stats")
st.dataframe(weekly_df)

st.header("Standings")
updated_points = False
if not updated_points:
    old_standings_df = pd.read_csv("standings.csv", index_col=0)
    st.dataframe(old_standings_df)
if updated_points:
    st.dataframe(standings_df)
    standings_df.to_csv("standings.csv")

st.subheader("Past Standings")
past_data = {'year': ["2019/2020", "2020/2021", "2021/2022"], 'Charbel': ["1276", "1378", "1588"], 'Ralph': ["1203", "1429", "1511"], 'George': ["1315", "1470", "1377"] ,'Rene': ["1209", "1690", "1603"]}
past_df = pd.DataFrame(past_data)
st.dataframe(past_df)
