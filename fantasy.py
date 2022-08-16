# If player not found in database / new player --> Add in fantasy main CSV + as a variable in both .py

#TODO:
# Need to check if there is a faster way then changing updated_points every time to True then to False while each time uploading on Github (and making sure no one refreshes the app)

# Future idea: Do a dropdown or search on Streamlit to choose a player and show a line graph of his points every gw OR
# Do a 3rd df which includes all the players and 38 cols for each gw pts they got.
# Add a way that if I see a player inj to add a flag in UI
# Add a code to calculate bench score if player asese ma leeib
# Ghayyir clean sheet b tari2a hot l fari2 w automatically yenzedo lal corresponding players
# Formation change?


# Steps: - Add missing variable of player in both .py files.
# - Change updating variable in fill_fantasy_table.py to True
# - Add goals/assists/stats of all players
# - Check if starting players played or not for all users
# - Run code
# - Change updating variable to False
# - Change updated_points in this file to True
# - Commit all fantasy files to github
# - Refresh link for updates and check if all correct
# - Change updated_points in this file to False
# - Commit this file to github


import streamlit as st
import pandas as pd

hidden_color = "black"
weekly_df = pd.read_csv("fantasy_weekly.csv", index_col=0)
standings_df = pd.read_csv("standings.csv", index_col=0)

#######################################################################################################################
############################################### ALL PLAYERS ###########################################################
#######################################################################################################################

# Athletic Club
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

# Atletico Madrid
antoine_griezmann = "Antoine Griezmann"
joao_felix = "Joao Felix"
alvaro_morata = "Alvaro Morata"
angel_correa = "Angel Correa"
matheus_cunha = "Matheus Cunha"
marcos_paulo = "Marcos Paulo"
carlos_martin = "Carlos Martin"
rodrigo_de_paul = "Rodrigo De Paul"
saul_niguez = "Saul Niguez"
yannick_carrasco = "Yannick Carrasco"
marcos_llorente = "Marcos Llorente"
axel_witsel = "Axel Witsel"
koke = "Koke"
thomas_lemar = "Thomas Lemar"
nahuel_molina = "Nahuel Molina"
geoffrey_kondogbia = "Geoffrey Kondogbia"
daniel_wass = "Daniel Wass"
jose_maria_gimenez = "Jose Gimenez"
renan_lodi = "Renan Lodi"
santiago_arias = "Santiago Arias"
reinildo = "Reinildo"
felipe = "Felipe"
stefan_savic = "Stefan Savic"
mario_hermoso = "Mario Hermoso"
jan_oblak = "Jan Oblak"
ivo_grbic = "Ivo Grbic"
antonio_gomis = "Antonio Gomis"

# Cadiz
jeremias_ledesma = "Jeremias Ledesma"
joseba_zaldua = "Joseba Zaldua"
luis_hernandez = "Luis Hernandez"
victor_chust = "Victor Chust"
alfonso_espino = "Alfonso Espino"
alberto_perea = "Alberto Perea"
fali = "Fali"
jose_mari = "Jose Mari"
santiago_arzamendia = "Santiago Arzamendia"
lucas_perez = "Lucas Perez"
anthony_lozano = "Anthony Lozano"
awer_mabil = "Awer Mabil"
ivan_alejo = "Ivan Alejo"
tomas_alarcon = "Tomas Alarcon"
alvaro_negredo = "Alvaro Negredo"
mamady_diarra = "Mamady Diarra"

# Celta
agustin_marchesin = "Agustin Marchesin"
javi_galan = "Javi Galan"
unai_nunez = "Unai Nunez"
joseph_aidoo = "Joseph Aidoo"
hugo_mallo = "Hugo Mallo"
fran_beltran = "Fran Beltran"
franco_cervi = "Franco Cervi"
oscar_rodriguez = "Oscar Rodriguez"
augusto_solari = "Augusto Solari"
goncalo_paciencia = "Goncalo Paciencia"
iago_aspas = "Iago Aspas"
oscar_mingueza = "Oscar Mingueza"
renato_tapia = "Renato Tapia"
gabriel_veiga = "Gabriel Veiga"
carles_perez = "Carles Perez"

# Elche
edgar_badia = "Edgar Badia"
john_donald = "John Donald"
enzo_roco = "Enzo Roco"
pedro_bigas = "Pedro Bigas"
helibelton_palacios = "Helibelton Palacios"
omar_mascarell = "Omar Mascarell"
gerard_gumbau = "Gerard Gumbau"
johan_mojica = "Johan Mojica"
pere_milla = "Pere Milla"
roger_marti = "Roger Marti"
fidel = "Fidel"
diego_gonzalez = "Diego Gonzalez"
tete_morente = "Tete Morente"
josan = "Josan"
ezequiel_ponce = "Ezequiel Ponce"
alejandro_alfaro = "Alejandro Alfaro"

# Espanyol
benjamin_lecomte = "Benjamin Lecomte"
oscar_gil = "Oscar Gil"
sergi_gomez = "Sergi Gomez"
leandro_cabrera = "Leandro Cabrera"
brian_olivan = "Brian Olivan"
vinicius_souza = "Vinicius Souza"
fernando_calero = "Fernando Calero"
sergi_darder = "Sergi Darder"
ruben_sanchez_saez = "Ruben Sanchez Saez"
joselu = "Joselu"
nicolas_melamed = "Nicolas Melamed"
adrian_embarba = "Adrian Embarba"
edu_exposito = "Edu Exposito"
luca_koleosho = "Luca Koleosho"
nabil_touaizi = "Nabil Touaizi"
raul_de_tomas = "Raul De Tomas"

# Osasuna
sergio_herrera = "Sergio Herrera"
juan_cruz = "Juan Cruz"
david_garcia = "David Garcia"
unai_garcia = "Unai Garcia"
ruben_pena = "Ruben Pena"
pablo_lumbreras = "Pablo Lumbreras"
manuel_sanchez = "Manuel Sanchez"
nacho_vidal = "Nacho Vidal"
moi_gomez = "Moi Gomez"
lucas_torro = "Lucas Torro"
jon_moncayola = "Jon Moncayola"
darko_brasanac = "Darko Brasanac"
kike_barja = "Kike Barja"
aimar_oroz = "Aimar Oroz"
chimy = "Chimy"
kike_garcia = "Kike Garcia"


# FC Barcelona
marc_andre_ter_stegen = "Ter Stegen"
jordi_alba = "Jordi Alba"
eric_garcia = "Eric Garcia"
andreas_christensen = "Andreas Christensen"
ronald_araujo = "Ronald Araujo"
sergio_busquets = "Sergio Busquets"
sergi_roberto = "Sergi Roberto"
frenkie_de_jong = "Frenkie De Jong"
franck_kessie = "Franck Kessie"
gavi = "Gavi"
jules_kounde = "Jules Kounde"
raphinha = "Raphinha"
pedri = "Pedri"
robert_lewandowski = "Robert Lewandowski"
ousmane_dembele = "Ousmane Dembele"
ansu_fati = "Ansu Fati"
pierre_emerick_aubameyang = "Pierre-Emerick Aubameyang"

# Getafe
david_soria = "David Soria"
fabrizio_angileri = "Fabrizio Angileri"
domingos_duarte = "Domingos Duarte"
stefan_mitrovic = "Stefan Mitrovic"
djene = "Djene"
juan_iglesias = "Juan Iglesias"
nemanja_maksimovic = "Nemanja Maksimovic"
mauro_arambarri = "Mauro Arambarri"
carles_alena = "Carles Alena"
enes_unal = "Enes Unal"
borja_mayoral = "Borja Mayoral"
jaime_seoane = "Jaime Seoane"
portu = "Portu"
jaime_mata = "Jaime Mata"
moi_parra = "Moi Parra"

# Girona
juan_carlos = "Juan Carlos"
juanpe = "Juanpe"
david_lopez = "David Lopez"
santiago_bueno = "Santiago Bueno"
valery_fernandez = "Valery Fernandez"
aleix_garcia = "Aleix Garcia"
ramon_terrats = "Ramon Terrats"
yan_couto = "Yan Couto"
samu_saiz = "Samu Saiz"
rodrigo_riquelme = "Rodrigo Riquelme"
valentin_castellanos = "Valentin Castellanos"
arnau_martinez = "Arnau Martinez"
miguel_gutierrez = "Miguel Gutierrez"
yangel_herrera = "Yangel Herrera"
christian_stuani = "Christhian Stuani"
oscar_urena = "Oscar Urena"

# Rayo Vallecano
oscar_trejo = "Oscar Trejo"
stole_dimitrievski = "Stole Dimitrievski"
ivan_balliu = "Ivan Balliu"
florian_lejeune = "Florian Lejeune"
alejandro_catena = "Alejandro Catena"
fran_garcia = "Fran Garcia"
unai_lopez = "Unai Lopez"
ismaila_ciss = "Ismaila Ciss"
isi_palazon = "Isi Palazon"
alvaro_garcia = "Alvaro Garcia"
sergio_camello = "Sergio Camello"
oscar_valentin = "Oscar Valentin"
salvi = "Salvi"
jose_pozo = "Jose Pozo"
radamel_falcao = "Radamel Falcao"

# Real Betis
rui_silva = "Rui Silva"
alex_moreno = "Alex Moreno"
edgar_gonzalez = "Edgar Gonzalez"
german_pezzella = "German Pezzella"
juan_miranda = "Juan Miranda"
fran_delgado = "Fran Delgado"
paul_akouokou = "Paul Akouokou"
aitor_ruibal = "Aitor Ruibal"
william_carvalho = "William Carvalho"
guido_rodriguez = "Guido Rodriguez"
rodri_sanchez = "Rodri Sanchez"
nabil_fekir = "Nabil Fekir"
sergio_canales = "Sergio Canales"
juanmi = "Juanmi"
borja_iglesias = "Borja Iglesias"
loren_moron = "Loren Moron"
rober_gonzalez = "Rober Gonzalez"

# Real Madrid
thibaut_courtois = "Thibaut Courtois"
lucas_vasquez = "Lucas Vasquez"
eder_militao = "Eder Militao"
antonio_rudiger = "Antonio Rudiger"
nacho_fernandez = "Nacho Fernandez"
ferland_mendy = "Ferland Mendy"
david_alaba = "David Alaba"
daniel_carvajal = "Daniel Carvajal"
eduardo_camavinga = "Eduardo Camavinga"
luka_modric = "Luka Modric"
casemiro = "Casemiro"
dani_ceballos = "Dani Ceballos"
aurelien_tchouameni = "Aurelien Tchouameni"
toni_kroos = "Toni Kroos"
federico_valverde = "Federico Valverde"
vinicius_junior = "Vinicius Junior"
eden_hazard = "Eden Hazard"
karim_benzema = "Karim Benzema"

# Real Mallorca
predrag_rajkovic = "Predrag Rajkovic"
pablo_maffeo = "Pablo Maffeo"
martin_valjent = "Martin Valjent"
antonio_raillo = "Antonio Raillo"
copete = "Copete"
jaume_costa = "Jaume Costa"
kang_in_lee = "Kang-in Lee"
clement_grenier = "Clement Grenier"
rodrigo_battaglia = "Rodrigo Battaglia"
dani_rodriguez = "Dani Rodriguez"
vedat_muriqi = "Vedat Muriqi"
antonio_sanchez = "Antonio Sanchez"
iddrisu_baba = "Iddrisu Baba"
lago_junior = "Lago Junior"
abdon_prats = "Abdon Prats"


# Real Sociedad
alex_remiro = "Alex Remiro"
diego_rico = "Diego Rico"
robin_le_normand = "Robin Le Normand"
aihen_munoz = "Aihen Munoz"
igor_zubeldia = "Igor Zubeldia"
mikel_merino = "Mikel Merino"
asier_illaramendi = "Asier Illarramendi"
aritz_elustondo = "Aritz Elustondo"
martin_zubimendi = "Martin Zubimendi"
brais_mendez = "Brais Mendez"
david_silva = "David Silva"
takefusa_kubo = "Takefusa Kubo"
ander_barrenetxea = "Ander Barrenetxea"
jon_karrikaburu = "Jon Karrikaburu"
alexander_isak = "Alexander Isak"
mikel_oyarzabal = "Mikel Oyarzabal"
mohamed_ali_cho = "Mohamed-Ali Cho"

# Real Valladolid
sergio_asenjo = "Sergio Asenjo"
luis_perez = "Luis Perez"
joaquin_fernandez = "Joaquin Fernandez"
jawad_el_yamiq = "Jawad El Yamiq"
sergio_escudero = "Sergio Escudero"
monchu = "Monchu"
gonzalo_plata = "Gonzalo Plata"
roque_mesa = "Roque Mesa"
alvaro_aguado = "Alvaro Aguado"
toni_villa = "Toni Villa"
sergio_leon = "Sergio Leon"
lucas_olaza = "Lucas Olaza"
ivan_sanchez = "Ivan Sanchez"
oscar_plano = "Oscar Plano"
kike_perez = "Kike Perez"
sekou_gassama = "Sekou Gassama"

# Sevilla
bono = "Bono"
alex_telles = "Alex Telles"
nemanja_gudelj = "Nemanja Gudelj"
karim_rekik = "Karim Rekik"
marcos_acuna = "Marcos Acuna"
jesus_navas = "Jesus Navas"
jesus_corona = "Jesus Corona"
fernando = "Fernando"
thomas_delaney = "Thomas Delaney"
papu_gomez = "Papu Gomez"
isco = "Isco"
erik_lamela = "Erik Lamela"
ivan_rakitic = "Ivan Rakitic"
youssef_ennesyri = "Youssef En-Nesyri"
lucas_ocampos = "Lucas Ocampos"
rafa_mir = "Rafa Mir"
ivan_romero = "Ivan Romero"

# Almeria
fernando_martinez = "Fernando Martinez"
chumi = "Chumi"
kaiky = "Kaiky"
rodrigo_ely = "Rodrigo Ely"
srdan_babic = "Srdan Babic"
sergio_akieme_rodriguez = "Sergio Akieme Rodriguez"
lucas_robertone = "Lucas Robertone"
inigo_eguaras = "Inigo Eguaras"
samuel_costa = "Samuel Costa"
largie_ramazani = "Largie Ramazani"
umar_sadiq = "Umar Sadiq"
dyego_sousa = "Dyego Sousa"
arnau_puigmal = "Arnau Puigmal"
jose_carlos_lazo = "Jose Carlos Lazo"
curro = "Curro"
francisco_portillo = "Francisco Portillo"

# Valencia
giorgi_mamardashvili = "Giorgi Mamardashvili"
thierry_correia = "Thierry Correia"
jose_luis_gaya = "Jose Luis Gaya"
dimitri_foulquier = "Dimitri Foulquier"
christian_mosquera = "Cristhian Mosquera"
toni_lato = "Toni Lato"
nico_gonzalez = "Nico Gonzalez"
eray_comert = "Eray Comert"
mouctar_diakhaby = "Mouctar Diakhaby"
jesus_vasquez = "Jesus Vazquez"
yunus_musah = "Yunus Musah"
hugo_guillamon = "Hugo Guillamon"
samu_castillejo = "Samu Castillejo"
carlos_soler = "Carlos Soler"
hugo_duro = "Hugo Duro"
samuel_lino = "Samuel Lino"
maximiliano_gomez = "Maximiliano Gomez"

# Villareal
geronimo_rulli = "Geronimo Rulli"
juan_foyth = "Juan Foyth"
raul_albiol = "Raul Albiol"
pau_torres = "Pau Torres"
aissa_mandi = "Aissa Mandi"
alfonso_pedraza = "Alfonso Pedraza"
dani_parejo = "Dani Parejo"
manu_trigueros = "Manu Trigueros"
yeremy_pino = "Yeremy Pino"
etienne_capoue = "Etienne Capoue"
samuel_chukwueze = "Samuel Chukwueze"
alejandro_baena = "Alejandro Baena"
francis_coquelin = "Francis Coquelin"
arnaut_danjuma = "Arnaut Danjuma"
nicolas_jackson = "Nicolas Jackson"
jose_luis_morales = "Jose Luis Morales"
gerard_moreno = "Gerard Moreno"


#######################################################################################################################
############################################### USERS TEAMS ###########################################################
#######################################################################################################################
charbel = [{
    "G1": unai_simon,
    "D1": jules_kounde,
    "D2": eder_militao,
    "D3": alex_moreno,
    "D4": pau_torres,
    "M1": nabil_fekir,
    "M2": jesus_corona,
    "M3": yannick_carrasco,
    "F1": robert_lewandowski,
    "F2": antoine_griezmann,
    "F3": alexander_isak,
    "G2": alex_remiro,
    "D5": jose_maria_gimenez,
    "M4": sergi_darder,
    "F4": arnaut_danjuma,
}]

ralph = [{
    "G1": jan_oblak,
    "D1": david_alaba,
    "D2": reinildo,
    "D3": yeray_alvarez,
    "D4": jose_luis_gaya,
    "M1": raphinha,
    "M2": samu_castillejo,
    "M3": sergio_canales,
    "F1": gerard_moreno,
    "F2": iago_aspas,
    "F3": youssef_ennesyri,
    "G2": bono,
    "D5": daniel_carvajal,
    "M4": isco,
    "F4": raul_de_tomas,
}]

george = [{
    "G1": marc_andre_ter_stegen,
    "D1": ronald_araujo,
    "D2": aritz_elustondo,
    "D3": antonio_rudiger,
    "D4": alex_telles,
    "M1": juanmi,
    "M2": iker_munian,
    "M3": dani_parejo,
    "F1": enes_unal,
    "F2": ousmane_dembele,
    "F3": vinicius_junior,
    "G2": geronimo_rulli,
    "D5": stefan_savic,
    "M4": oscar_trejo,
    "F4": ansu_fati,
}]

rene = [{
    "G1": thibaut_courtois,
    "D1": jordi_alba,
    "D2": jesus_navas,
    "D3": inigo_martinez,
    "D4": robin_le_normand,
    "M1": pedri,
    "M2": carlos_soler,
    "M3": thomas_lemar,
    "F1": karim_benzema,
    "F2": alvaro_morata,
    "F3": lucas_ocampos,
    "G2": rui_silva,
    "D5": renan_lodi,
    "M4": manu_trigueros,
    "F4": mikel_oyarzabal,
}]


#######################################################################################################################
############################################### UNCHANGED UI ###########################################################
#######################################################################################################################

# TRY THIS
# st.set_page_config(page_title="Fantasy La Liga", layout="wide")

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
cols[2].write("_%s_" % charbel[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == charbel[0]["M4"], 'Pts'])
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
cols[2].write("_%s_" % ralph[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == ralph[0]["M4"], 'Pts'])
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
cols[2].write("_%s_" % george[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == george[0]["M4"], 'Pts'])
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
cols[2].write("_%s_" % rene[0]["M4"])
cols[2].write("%i" % weekly_df.loc[weekly_df["Name"] == rene[0]["M4"], 'Pts'])
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
