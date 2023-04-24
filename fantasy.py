# If player not found in database / new player --> Add in fantasy main CSV + as a variable in both .py


# Future ideas:

# Add a way that if I see a player inj to add a flag in UI
# Add a code to calculate bench score if player asese ma leeib
# Ghayyir clean sheet b tari2a hot l fari2 w automatically yenzedo lal corresponding players
# Formation change?


# Steps: - Add missing variable of player in both .py files (if any missing)
# - Add goals/assists/stats of all players
# - Check if starting players played or not for all users
# - Change updating variable in fill_fantasy_table.py to True
# - Run fill_fantasy_table.py code
# - Change updating variable to False
# - Change updated_points in this file to True
# - Commit all fantasy files to Github
# - Refresh link for updates and check if all correct
# - Change updated_points in this file to False
# - Manually change standings.csv
# - Commit this file + standings.csv to Github


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
ander_herrera = "Ander Herrera"

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
pablo_barrios = "Pablo Barrios"
marcos_llorente = "Marcos Llorente"
axel_witsel = "Axel Witsel"
koke = "Koke"
thomas_lemar = "Thomas Lemar"
nahuel_molina = "Nahuel Molina"
geoffrey_kondogbia = "Geoffrey Kondogbia"
daniel_wass = "Daniel Wass"
matt_doherty = "Matt Doherty"
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
sergio_reguilon = "Sergio Reguilon"

# Cadiz
jeremias_ledesma = "Jeremias Ledesma"
joseba_zaldua = "Joseba Zaldua"
luis_hernandez = "Luis Hernandez"
victor_chust = "Victor Chust"
alfonso_espino = "Alfonso Espino"
mamadou_mbaye = "Mamadou Mbaye"
isaac_carcelen = "Isaac Carcelen"
ruben_alcaraz = "Ruben Alcaraz"
alberto_perea = "Alberto Perea"
fali = "Fali"
jose_mari = "Jose Mari"
santiago_arzamendia = "Santiago Arzamendia"
gonzalo_escalante = "Gonzalo Escalante"
lucas_perez = "Lucas Perez"
anthony_lozano = "Anthony Lozano"
awer_mabil = "Awer Mabil"
ivan_alejo = "Ivan Alejo"
tomas_alarcon = "Tomas Alarcon"
alvaro_negredo = "Alvaro Negredo"
mamady_diarra = "Mamady Diarra"
fede_san_emeterio = "Fede San Emeterio"
antonio_blanco = "Antonio Blanco"
alex_fernandez = "Alex Fernandez"
brian_ocampo = "Brian Ocampo"
alvaro_gimenez = "Alvaro Gimenez"
ruben_sobrino = "Ruben Sobrino"
theo_bongonda = "Theo Bongonda"

# Celta
agustin_marchesin = "Agustin Marchesin"
javi_galan = "Javi Galan"
unai_nunez = "Unai Nunez"
joseph_aidoo = "Joseph Aidoo"
hugo_mallo = "Hugo Mallo"
ivan_villar = "Ivan Villar"
fran_beltran = "Fran Beltran"
kevin_vasquez = "Kevin Vasquez"
franco_cervi = "Franco Cervi"
oscar_rodriguez = "Oscar Rodriguez"
augusto_solari = "Augusto Solari"
goncalo_paciencia = "Goncalo Paciencia"
iago_aspas = "Iago Aspas"
oscar_mingueza = "Oscar Mingueza"
renato_tapia = "Renato Tapia"
gabriel_veiga = "Gabriel Veiga"
carles_perez = "Carles Perez"
luca_de_la_torre = "Luca De La Torre"
carlos_dominguez = "Carlos Dominguez"
jorgen_larsen = "Jorgen Larsen"
haris_seferovic = "Haris Seferovic"

# Elche
edgar_badia = "Edgar Badia"
john_donald = "John Donald"
enzo_roco = "Enzo Roco"
lautaro_blanco = "Lautaro Blanco"
pedro_bigas = "Pedro Bigas"
helibelton_palacios = "Helibelton Palacios"
federico_fernandez = "Federico Fernandez"
omar_mascarell = "Omar Mascarell"
gerard_gumbau = "Gerard Gumbau"
gonzalo_verdu = "Gonzalo Verdu"
johan_mojica = "Johan Mojica"
pere_milla = "Pere Milla"
roger_marti = "Roger Marti"
fidel = "Fidel"
nicolas_fernandez = "Nicolas Fernandez"
diego_gonzalez = "Diego Gonzalez"
tete_morente = "Tete Morente"
josan = "Josan"
ezequiel_ponce = "Ezequiel Ponce"
alejandro_alfaro = "Alejandro Alfaro"
pol_lirola = "Pol Lirola"
alex_collado = "Alex Collado"
domingos_quina = "Domingos Quina"
lucas_boye = "Lucas Boye"
javier_pastore = "Javier Pastore"
raul_guti = "Raul Guti"
carlos_clerc = "Carlos Clerc"

# Espanyol
benjamin_lecomte = "Benjamin Lecomte"
alvaro_fernandez = "Alvaro Fernandez"
oscar_gil = "Oscar Gil"
sergi_gomez = "Sergi Gomez"
ronael_pierre_gabriel = "Ronael Pierre-Gabriel"
leandro_cabrera = "Leandro Cabrera"
cesar_montes = "Cesar Montes"
brian_olivan = "Brian Olivan"
aleix_vidal = "Aleix Vidal"
vinicius_souza = "Vinicius Souza"
fernando_calero = "Fernando Calero"
jose_gragera = "Jose Gragera"
sergi_darder = "Sergi Darder"
ruben_sanchez_saez = "Ruben Sanchez Saez"
denis_suarez = "Denis Suarez"
joselu = "Joselu"
nicolas_melamed = "Nicolas Melamed"
adrian_embarba = "Adrian Embarba"
edu_exposito = "Edu Exposito"
luca_koleosho = "Luca Koleosho"
nabil_touaizi = "Nabil Touaizi"
raul_de_tomas = "Raul De Tomas"
javi_puado = "Javi Puado"
keidi_bare = "Keidi Bare"
dani_gomez = "Dani Gomez"
martin_braithwaite = "Martin Braithwaite"
omar_el_hilali = "Omar El Hilali"
simo = "Simo"

# Osasuna
sergio_herrera = "Sergio Herrera"
aitor_fernandez = "Aitor Fernandez"
juan_cruz = "Juan Cruz"
david_garcia = "David Garcia"
unai_garcia = "Unai Garcia"
diego_moreno = "Diego Moreno"
aridane_hernandez = "Aridane Hernandez"
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
ruben_garcia = "Ruben Garcia"
ante_budimir = "Ante Budimir"
roberto_torres = "Roberto Torres"
abdessamad_ezzalzouli = "Abdessamad Ezzalzouli"


# FC Barcelona
marc_andre_ter_stegen = "Ter Stegen"
jordi_alba = "Jordi Alba"
eric_garcia = "Eric Garcia"
gerard_pique = "Gerard Pique"
andreas_christensen = "Andreas Christensen"
alejandro_balde = "Alejandro Balde"
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
ferran_torres = "Ferran Torres"
marcos_alonso = "Marcos Alonso"
hector_bellerin = "Hector Bellerin"
memphis_depay = "Memphis Depay"

# Getafe
david_soria = "David Soria"
fabrizio_angileri = "Fabrizio Angileri"
domingos_duarte = "Domingos Duarte"
stefan_mitrovic = "Stefan Mitrovic"
jordan_amavi = "Jordan Amavi"
omar_alderete = "Omar Alderete"
damian_suarez = "Damian Suarez"
djene = "Djene"
juan_iglesias = "Juan Iglesias"
nemanja_maksimovic = "Nemanja Maksimovic"
mauro_arambarri = "Mauro Arambarri"
carles_alena = "Carles Alena"
angel_algobia = "Angel Algobia"
enes_unal = "Enes Unal"
borja_mayoral = "Borja Mayoral"
jaime_seoane = "Jaime Seoane"
portu = "Portu"
jaime_mata = "Jaime Mata"
luis_milla = "Luis Milla"
moi_parra = "Moi Parra"
gaston_alvarez = "Gaston Alvarez"
juanmi_latasa = "Juanmi Latasa"
munir_el_haddadi = "Munir El Haddadi"

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
ivan_martin = "Ivan Martin"
borja_garcia = "Borja Garcia"
miguel_gutierrez = "Miguel Gutierrez"
yangel_herrera = "Yangel Herrera"
christian_stuani = "Christhian Stuani"
oscar_urena = "Oscar Urena"
reinier = "Reinier"
javier_hernandez = "Javier Hernandez"
viktor_tsygankov = "Viktor Tsygankov"
joel_roca = "Joel Roca"
paulo_gazzaniga = "Paulo Gazzaniga"
oriol_romeu = "Oriol Romeu"
bernardo_espinos = "Bernardo Espinos"
manu_vallejo = "Manu Vallejo"

# Rayo Vallecano
oscar_trejo = "Oscar Trejo"
diego_lopez = "Diego Lopez"
stole_dimitrievski = "Stole Dimitrievski"
ivan_balliu = "Ivan Balliu"
florian_lejeune = "Florian Lejeune"
abdul_mumin = "Abdul Mumin"
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
mario_suarez = "Mario Suarez"
randy_nteka = "Randy Nteka"
santi_comesana = "Santi Comesana"
bebe = "Bebe"
kenedy = "Kenedy"
ivan_fresneda = "Ivan Fresneda"

# Real Betis
rui_silva = "Rui Silva"
claudio_bravo = "Claudio Bravo"
alex_moreno = "Alex Moreno"
edgar_gonzalez = "Edgar Gonzalez"
felix_marti = "Felix Marti"
martin_montoya = "Martin Montoya"
abner_vinicius = "Abner Vinicius"
victor_ruiz = "Victor Ruiz"
german_pezzella = "German Pezzella"
juan_miranda = "Juan Miranda"
fran_delgado = "Fran Delgado"
paul_akouokou = "Paul Akouokou"
aitor_ruibal = "Aitor Ruibal"
william_carvalho = "William Carvalho"
guido_rodriguez = "Guido Rodriguez"
rodri_sanchez = "Rodri Sanchez"
ayoze_perez = "Ayoze Perez"
nabil_fekir = "Nabil Fekir"
sergio_canales = "Sergio Canales"
juan_cruz_betis = "Juan Cruz Betis"
juanmi = "Juanmi"
borja_iglesias = "Borja Iglesias"
loren_moron = "Loren Moron"
rober_gonzalez = "Rober Gonzalez"
luiz_felipe = "Luiz Felipe"
andres_guardado = "Andres Guardado"
luiz_henrique = "Luiz Henrique"
youssouf_sabaly = "Youssouf Sabaly"
joaquin = "Joaquin"
willian_jose = "Willian Jose"

# Real Madrid
thibaut_courtois = "Thibaut Courtois"
andriy_lunin = "Andriy Lunin"
lucas_vasquez = "Lucas Vasquez"
eder_militao = "Eder Militao"
antonio_rudiger = "Antonio Rudiger"
nacho_fernandez = "Nacho Fernandez"
alvaro_odriozola = "Alvaro Odriozola"
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
marco_asensio = "Marco Asensio"
rodrygo = "Rodrygo"
alvaro_rodriguez = "Alvaro Rodriguez"
mariano_diaz = "Mariano Diaz"

# Real Mallorca
predrag_rajkovic = "Predrag Rajkovic"
pablo_maffeo = "Pablo Maffeo"
martin_valjent = "Martin Valjent"
brian_cufre = "Brian Cufre"
ludwig_augustinsson = "Ludwig Augustinsson"
giovanni_gonzalez = "Giovanni Gonzalez"
franco_russo = "Franco Russo"
antonio_raillo = "Antonio Raillo"
copete = "Copete"
matija_nastasic = "Matija Nastasic"
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
inigo_ruiz_de_galarreta = "Inigo Ruiz de Galarreta"
javi_llabres = "Javi Llabres"
angel_rodriguez = "Angel Rodriguez"
amath_ndiaye = "Amath Ndiaye"
tino_kadewere = "Tino Kadewere"


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
andoni_gorosabel = "Andoni Gorosabel"
benat_turrientes = "Benat Turrientes"
pablo_marin = "Pablo Marin"
robert_navarro = "Robert Navarro"
jon_pacheco = "Jon Pacheco"
carlos_fernandez = "Carlos Fernandez"
alex_sola = "Alex Sola"
alexander_sorloth = "Alexander Sorloth"

# Real Valladolid
sergio_asenjo = "Sergio Asenjo"
jordi_masip = "Jordi Masip"
luis_perez = "Luis Perez"
joaquin_fernandez = "Joaquin Fernandez"
jawad_el_yamiq = "Jawad El Yamiq"
sergio_escudero = "Sergio Escudero"
martin_hongla = "Martin Hongla"
david_torres = "David Torres"
zouhair_feddal = "Zouhair Feddal"
lucas_rosa = "Lucas Rosa"
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
javi_sanchez = "Javi Sanchez"
darwin_machis = "Darwin Machis"
cyle_larin = "Cyle Larin"
sergi_guardiola = "Sergi Guardiola"
anuar = "Anuar"
shon_weissman = "Shon Weissman"

# Sevilla
bono = "Bono"
marko_dmitrovic = "Marko Dmitrovic"
alex_telles = "Alex Telles"
nemanja_gudelj = "Nemanja Gudelj"
karim_rekik = "Karim Rekik"
marcos_acuna = "Marcos Acuna"
marcao = "Marcao"
loic_bade = "Loic Bade"
jesus_navas = "Jesus Navas"
jesus_corona = "Jesus Corona"
kike_salas = "Kike Salas"
fernando = "Fernando"
thomas_delaney = "Thomas Delaney"
papu_gomez = "Papu Gomez"
isco = "Isco"
erik_lamela = "Erik Lamela"
ivan_rakitic = "Ivan Rakitic"
pape_gueye = "Pape Gueye"
youssef_ennesyri = "Youssef En-Nesyri"
lucas_ocampos = "Lucas Ocampos"
rafa_mir = "Rafa Mir"
ivan_romero = "Ivan Romero"
adnan_januzaj = "Adnan Januzaj"
gonzalo_montiel = "Gonzalo Montiel"
oliver_torres = "Oliver Torres"
joan_jordan = "Joan Jordan"
tanguy_nianzou = "Tanguy Nianzou"
jose_angel_carmona = "Jose Angel Carmona"
suso = "Suso"
bryan_gil = "Bryan Gil"
kasper_dolberg = "Kasper Dolberg"

# Almeria
fernando_martinez = "Fernando Martinez"
fernando_pacheco = "Fernando Pacheco"
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
leo_baptistao = "Leo Baptistao"
alex_centelles = "Alex Centelles"
alejandro_pozo = "Alejandro Pozo"
cesar_de_la_hoz = "Cesar de la Hoz"
houboulang_mendes = "Houboulang Mendes"
gonzalo_melero = "Gonzalo Melero"
el_bilal_toure = "El Bilal Toure"
luis_suarez = "Luis Suarez"
marko_milovanovic = "Marko Milovanovic"
lazaro = "Lazaro"

# Valencia
giorgi_mamardashvili = "Giorgi Mamardashvili"
thierry_correia = "Thierry Correia"
jose_luis_gaya = "Jose Luis Gaya"
dimitri_foulquier = "Dimitri Foulquier"
christian_mosquera = "Cristhian Mosquera"
toni_lato = "Toni Lato"
cenk_ozkacar = "Cenk Ozkacar"
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
gabriel_paulista = "Gabriel Paulista"
marcos_andre = "Marcos Andre"
edinson_cavani = "Edinson Cavani"
justin_kluivert = "Justin Kluivert"
andre_almeida = "Andre Almeida"
ilaix_moriba = "Ilaix Moriba"

# Villareal
geronimo_rulli = "Geronimo Rulli"
pepe_reina = "Pepe Reina"
juan_foyth = "Juan Foyth"
alberto_moreno = "Alberto Moreno"
raul_albiol = "Raul Albiol"
pau_torres = "Pau Torres"
aissa_mandi = "Aissa Mandi"
kiko_femenia = "Kiko Femenia"
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
gio_lo_celso = "Giovani Lo Celso"
gerard_moreno = "Gerard Moreno"

#######################################################################################################################
############################################### USERS TEAMS ###########################################################
#######################################################################################################################
charbel = [{
    "G1": alex_remiro,
    "D1": jules_kounde,
    "D2": pablo_maffeo,
    "D3": pau_torres,
    "D4": nacho_fernandez,
    "M1": ayoze_perez,
    "M2": lucas_ocampos,
    "M3": brais_mendez,
    "F1": robert_lewandowski,
    "F2": antoine_griezmann,
    "F3": marco_asensio,
    "G2": pepe_reina,
    "D5": nemanja_gudelj,
    "M4": isi_palazon,
    "F4": gerard_moreno,
}]

ralph = [{
    "G1": jan_oblak,
    "D1": antonio_rudiger,
    "D2": eric_garcia,
    "D3": david_alaba,
    "D4": raul_albiol,
    "M1": sergio_canales,
    "M2": sergi_darder,
    "M3": federico_valverde,
    "F1": mikel_oyarzabal,
    "F2": iago_aspas,
    "F3": memphis_depay,
    "G2": bono,
    "D5": reinildo,
    "M4": kang_in_lee,
    "F4": edinson_cavani,
}]

george = [{
    "G1": marc_andre_ter_stegen,
    "D1": antonio_raillo,
    "D2": eder_militao,
    "D3": ronald_araujo,
    "D4": alejandro_balde,
    "M1": takefusa_kubo,
    "M2": nico_williams,
    "M3": gabriel_veiga,
    "F1": vedat_muriqi,
    "F2": youssef_ennesyri,
    "F3": vinicius_junior,
    "G2": stole_dimitrievski,
    "D5": jose_maria_gimenez,
    "M4": pedri,
    "F4": ousmane_dembele,
}]

rene = [{
    "G1": thibaut_courtois,
    "D1": nahuel_molina,
    "D2": daniel_carvajal,
    "D3": oscar_de_marcos,
    "D4": marcos_alonso,
    "M1": samuel_chukwueze,
    "M2": david_silva,
    "M3": raphinha,
    "F1": joselu,
    "F2": karim_benzema,
    "F3": borja_iglesias,
    "G2": rui_silva,
    "D5": robin_le_normand,
    "M4": alvaro_garcia,
    "F4": alvaro_morata,
}]


#######################################################################################################################
############################################### UNCHANGED UI ###########################################################
#######################################################################################################################

st.set_page_config(page_title="Fantasy La Liga", layout="wide")
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


values = ("None", "Athletic Club", "Atletico Madrid", "Osasuna", "Cadiz", "Elche", "Espanyol", "FC Barcelona", "Getafe",
          "Girona", "Rayo Vallecano", "Celta Vigo", "Mallorca", "Real Betis", "Real Madrid", "Real Sociedad", "Real Valladolid",
          "Sevilla", "Almeria", "Valencia", "Villareal")
option = st.selectbox('Filter by Team', values, index=0, key="total")

values_pos = ("None", "GK", "DEF", "MID", "FWD")
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
updated_points = True
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
