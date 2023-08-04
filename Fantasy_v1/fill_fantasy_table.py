import pandas as pd
import sys

updating = False

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
marcos_llorente = "Marcos Llorente"
axel_witsel = "Axel Witsel"
koke = "Koke"
thomas_lemar = "Thomas Lemar"
nahuel_molina = "Nahuel Molina"
pablo_barrios = "Pablo Barrios"
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
mamadou_mbaye = "Mamadou Mbaye"
isaac_carcelen = "Isaac Carcelen"
alfonso_espino = "Alfonso Espino"
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
ivan_villar = "Ivan Villar"
hugo_mallo = "Hugo Mallo"
fran_beltran = "Fran Beltran"
franco_cervi = "Franco Cervi"
kevin_vasquez = "Kevin Vasquez"
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
gonzalo_verdu = "Gonzalo Verdu"
helibelton_palacios = "Helibelton Palacios"
federico_fernandez = "Federico Fernandez"
omar_mascarell = "Omar Mascarell"
gerard_gumbau = "Gerard Gumbau"
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
javier_pastore = "Javier Pastore"
lucas_boye = "Lucas Boye"
raul_guti = "Raul Guti"
carlos_clerc = "Carlos Clerc"

# Espanyol
benjamin_lecomte = "Benjamin Lecomte"
alvaro_fernandez = "Alvaro Fernandez"
oscar_gil = "Oscar Gil"
sergi_gomez = "Sergi Gomez"
leandro_cabrera = "Leandro Cabrera"
ronael_pierre_gabriel = "Ronael Pierre-Gabriel"
aleix_vidal = "Aleix Vidal"
cesar_montes = "Cesar Montes"
jose_gragera = "Jose Gragera"
brian_olivan = "Brian Olivan"
vinicius_souza = "Vinicius Souza"
fernando_calero = "Fernando Calero"
sergi_darder = "Sergi Darder"
denis_suarez = "Denis Suarez"
ruben_sanchez_saez = "Ruben Sanchez Saez"
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
andreas_christensen = "Andreas Christensen"
alejandro_balde = "Alejandro Balde"
ronald_araujo = "Ronald Araujo"
gerard_pique = "Gerard Pique"
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
luis_milla = "Luis Milla"
jaime_mata = "Jaime Mata"
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
ivan_martin = "Ivan Martin"
samu_saiz = "Samu Saiz"
borja_garcia = "Borja Garcia"
rodrigo_riquelme = "Rodrigo Riquelme"
valentin_castellanos = "Valentin Castellanos"
arnau_martinez = "Arnau Martinez"
miguel_gutierrez = "Miguel Gutierrez"
yangel_herrera = "Yangel Herrera"
christian_stuani = "Christhian Stuani"
oscar_urena = "Oscar Urena"
viktor_tsygankov = "Viktor Tsygankov"
reinier = "Reinier"
javier_hernandez = "Javier Hernandez"
joel_roca = "Joel Roca"
paulo_gazzaniga = "Paulo Gazzaniga"
oriol_romeu = "Oriol Romeu"
bernardo_espinos = "Bernardo Espinos"
manu_vallejo = "Manu Vallejo"

# Rayo Vallecano
oscar_trejo = "Oscar Trejo"
stole_dimitrievski = "Stole Dimitrievski"
diego_lopez = "Diego Lopez"
ivan_balliu = "Ivan Balliu"
florian_lejeune = "Florian Lejeune"
alejandro_catena = "Alejandro Catena"
abdul_mumin = "Abdul Mumin"
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
martin_montoya = "Martin Montoya"
felix_marti = "Felix Marti"
victor_ruiz = "Victor Ruiz"
abner_vinicius = "Abner Vinicius"
edgar_gonzalez = "Edgar Gonzalez"
german_pezzella = "German Pezzella"
juan_miranda = "Juan Miranda"
fran_delgado = "Fran Delgado"
paul_akouokou = "Paul Akouokou"
aitor_ruibal = "Aitor Ruibal"
william_carvalho = "William Carvalho"
ayoze_perez = "Ayoze Perez"
guido_rodriguez = "Guido Rodriguez"
rodri_sanchez = "Rodri Sanchez"
nabil_fekir = "Nabil Fekir"
sergio_canales = "Sergio Canales"
juanmi = "Juanmi"
borja_iglesias = "Borja Iglesias"
loren_moron = "Loren Moron"
rober_gonzalez = "Rober Gonzalez"
luiz_felipe = "Luiz Felipe"
juan_cruz_betis = "Juan Cruz Betis"
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
antonio_raillo = "Antonio Raillo"
ludwig_augustinsson = "Ludwig Augustinsson"
franco_russo = "Franco Russo"
giovanni_gonzalez = "Giovanni Gonzalez"
brian_cufre = "Brian Cufre"
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
alexander_sorloth = "Alexander Sorloth"
carlos_fernandez = "Carlos Fernandez"
alex_sola = "Alex Sola"

# Real Valladolid
sergio_asenjo = "Sergio Asenjo"
jordi_masip = "Jordi Masip"
luis_perez = "Luis Perez"
joaquin_fernandez = "Joaquin Fernandez"
martin_hongla = "Martin Hongla"
jawad_el_yamiq = "Jawad El Yamiq"
sergio_escudero = "Sergio Escudero"
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
sergi_guardiola = "Sergi Guardiola"
anuar = "Anuar"
cyle_larin = "Cyle Larin"
shon_weissman = "Shon Weissman"

# Sevilla
bono = "Bono"
marko_dmitrovic = "Marko Dmitrovic"
alex_telles = "Alex Telles"
nemanja_gudelj = "Nemanja Gudelj"
marcao = "Marcao"
karim_rekik = "Karim Rekik"
marcos_acuna = "Marcos Acuna"
loic_bade = "Loic Bade"
jesus_navas = "Jesus Navas"
kike_salas = "Kike Salas"
jesus_corona = "Jesus Corona"
fernando = "Fernando"
thomas_delaney = "Thomas Delaney"
papu_gomez = "Papu Gomez"
pape_gueye = "Pape Gueye"
isco = "Isco"
erik_lamela = "Erik Lamela"
ivan_rakitic = "Ivan Rakitic"
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
lazaro = "Lazaro"
marko_milovanovic = "Marko Milovanovic"

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
justin_kluivert = "Justin Kluivert"
edinson_cavani = "Edinson Cavani"
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

df = pd.read_csv("fantasy.csv", index_col=0)

weekly_df = df.copy()
# Initialize all values for weekly df
for col in weekly_df.columns:
    if col == "Name" or col == "Position" or col == "Team":
        continue
    else:
        weekly_df[col].values[:] = 0


mins_pts_2 = [unai_simon, oscar_de_marcos, daniel_vivian, yuri_berchiche, mikel_vesga, oihan_sancet, alex_berenguer, ander_herrera, inaki_williams, gorka_guruzeta, # Athletic Club
              ivo_grbic, nahuel_molina, stefan_savic, axel_witsel, mario_hermoso, sergio_reguilon, koke, pablo_barrios, saul_niguez, antoine_griezmann, angel_correa, # Atletico Madrid
              ivan_villar, oscar_mingueza, unai_nunez, javi_galan, fran_beltran, oscar_rodriguez, carles_perez, gabriel_veiga, haris_seferovic, # Celta
              jeremias_ledesma, isaac_carcelen, luis_hernandez, alfonso_espino, gonzalo_escalante, fede_san_emeterio, ruben_sobrino, # Cadiz
              edgar_badia, josan, enzo_roco, lautaro_blanco, gerard_gumbau, fidel, tete_morente, lucas_boye, randy_nteka, # Elche
              ronael_pierre_gabriel, cesar_montes, edu_exposito, sergi_darder, brian_olivan, javi_puado, nicolas_melamed, denis_suarez, martin_braithwaite, # Espanyol
              david_soria, juan_iglesias, omar_alderete, stefan_mitrovic, gaston_alvarez, damian_suarez, mauro_arambarri, nemanja_maksimovic, carles_alena, jaime_mata, juanmi_latasa, # Getafe
              paulo_gazzaniga, arnau_martinez, david_lopez, bernardo_espinos, miguel_gutierrez, oriol_romeu, ivan_martin, viktor_tsygankov, valentin_castellanos, # Girona
              aitor_fernandez, ruben_pena, aridane_hernandez, manuel_sanchez, juan_cruz, jon_moncayola, lucas_torro, aimar_oroz, kike_barja, ante_budimir, abdessamad_ezzalzouli, # Osasuna
              marc_andre_ter_stegen, sergi_roberto, jules_kounde, marcos_alonso, franck_kessie, eric_garcia, frenkie_de_jong, raphinha, robert_lewandowski, ferran_torres, # FC Barcelona
              martin_valjent, pablo_maffeo, antonio_raillo, copete, jaume_costa, dani_rodriguez, inigo_ruiz_de_galarreta, kang_in_lee, vedat_muriqi, # Mallorca
              stole_dimitrievski, ivan_balliu, abdul_mumin, alejandro_catena, fran_garcia, oscar_valentin, isi_palazon, alvaro_garcia, raul_de_tomas, # Rayo Vallecano
              claudio_bravo, german_pezzella, edgar_gonzalez, juan_miranda, william_carvalho, guido_rodriguez, ayoze_perez, sergio_canales, joaquin, borja_iglesias, # Real Betis
              alex_remiro, andoni_gorosabel, igor_zubeldia, jon_pacheco, takefusa_kubo, brais_mendez, martin_zubimendi, ander_barrenetxea, alexander_sorloth, # Real Sociedad
              thibaut_courtois, daniel_carvajal, eder_militao, nacho_fernandez, antonio_rudiger, toni_kroos, vinicius_junior, karim_benzema, rodrygo, # Real Madrid
              jordi_masip, luis_perez, jawad_el_yamiq, lucas_olaza, kike_perez, roque_mesa, alvaro_aguado, gonzalo_plata, cyle_larin, darwin_machis, # Real Valladolid
              marko_dmitrovic, loic_bade, pape_gueye, jesus_navas, erik_lamela, oliver_torres, rafa_mir, # Sevilla
              fernando_martinez, alejandro_pozo, rodrigo_ely, srdan_babic, alex_centelles, gonzalo_melero, samuel_costa, lucas_robertone, lazaro, el_bilal_toure, adrian_embarba,  # Almeria
              giorgi_mamardashvili, mouctar_diakhaby, gabriel_paulista, jose_luis_gaya, nico_gonzalez, diego_lopez, andre_almeida, justin_kluivert, # Valencia
              aissa_mandi, pau_torres, alberto_moreno, dani_parejo, etienne_capoue, samuel_chukwueze, manu_trigueros, yeremy_pino, nicolas_jackson,  # Villareal
              ]

mins_pts_1 = [oier_zarraga, alex_berenguer, raul_garcia, iker_munian, # Athletic Club
              thomas_lemar, alvaro_morata, # Atletico Madrid
              kevin_vasquez, franco_cervi, renato_tapia, iago_aspas, # Celta
              theo_bongonda, sergi_guardiola, anthony_lozano, roger_marti, fali, ivan_alejo, jose_mari, # Cadiz
              mamadou_mbaye, gonzalo_verdu, ezequiel_ponce, pere_milla, # Elche
              oscar_gil, vinicius_souza, # Espanyol
              domingos_duarte, angel_algobia, fabrizio_angileri, # Getafe
              rodrigo_riquelme, aleix_garcia, reinier, christian_stuani, yan_couto, # Girona
              david_garcia, ruben_garcia, chimy, moi_gomez, pablo_lumbreras, # Osasuna
              andreas_christensen, gavi, ousmane_dembele, ansu_fati, # FC Barcelona
              antonio_sanchez, yangel_herrera, abdon_prats, giovanni_gonzalez, # Mallorca
              sergio_camello, radamel_falcao, salvi, mario_suarez, angel_rodriguez, iddrisu_baba, # Rayo Vallecano
              youssouf_sabaly, rodri_sanchez, aitor_ruibal, andres_guardado, juanmi, # Real Betis
              mikel_merino, mikel_oyarzabal, carlos_fernandez, mohamed_ali_cho, # Real Sociedad
              dani_ceballos, eduardo_camavinga, aurelien_tchouameni, marco_asensio, luka_modric, lucas_vasquez,  # Real Madrid
              javi_sanchez, sergio_leon, kenedy, sergio_escudero, lucas_rosa, # Real Valladolid
              gonzalo_montiel, nemanja_gudelj, tanguy_nianzou, alex_telles, suso, jesus_corona, # Sevilla
              francisco_portillo, sergio_akieme_rodriguez, cesar_de_la_hoz, dyego_sousa, largie_ramazani, # Almeria
              thierry_correia, samuel_lino, dimitri_foulquier, jesus_vasquez, yunus_musah,  # Valencia
              kiko_femenia, alejandro_baena, gio_lo_celso, johan_mojica, # Villareal
              ]

goals = [angel_rodriguez, copete, vedat_muriqi, reinier, ante_budimir, ante_budimir, karim_benzema, oihan_sancet, erik_lamela,
         mohamed_ali_cho, brais_mendez, angel_correa, nicolas_jackson, ansu_fati, gabriel_veiga, gabriel_veiga, lucas_boye,
         gonzalo_escalante, adrian_embarba, adrian_embarba, ronael_pierre_gabriel, javi_puado, el_bilal_toure, diego_lopez,
         ayoze_perez]

assists = [dani_rodriguez, kang_in_lee, dani_rodriguez, viktor_tsygankov, jon_moncayola, kike_barja, suso, alexander_sorloth,
           ander_barrenetxea, antoine_griezmann, antoine_griezmann, ousmane_dembele, carles_perez, haris_seferovic,
           gerard_gumbau, fede_san_emeterio, keidi_bare, samuel_costa, brian_olivan, sergi_darder, alex_centelles,
           nico_gonzalez, juan_miranda]

clean_sheets = [
    takefusa_kubo, # Part of Real Sociedad
    gabriel_veiga, # Part of Celta
    # unai_simon, ander_capa, inigo_martinez, yeray_alvarez, yuri_berchiche, mikel_vesga, dani_garcia, oihan_sancet, # Athletic Club
    # ivo_grbic, nahuel_molina, axel_witsel, jose_maria_gimenez, mario_hermoso, koke, rodrigo_de_paul, yannick_carrasco, saul_niguez, # Atletico Madrid
    # jeremias_ledesma, isaac_carcelen, luis_hernandez, alfonso_espino, gonzalo_escalante, theo_bongonda, ruben_alcaraz,  # Cadiz
    # ivan_villar, hugo_mallo, renato_tapia, joseph_aidoo, javi_galan, gabriel_veiga, fran_beltran, luca_de_la_torre, carles_perez, # Celta
    # marc_andre_ter_stegen, andreas_christensen, jules_kounde, jordi_alba, gavi, sergio_busquets, frenkie_de_jong, sergi_roberto,   # FC Barcelona
    # aitor_fernandez, ruben_pena, aridane_hernandez, david_garcia, manuel_sanchez, jon_moncayola, lucas_torro, kike_barja, aimar_oroz, # Osasuna
    david_soria, juan_iglesias, damian_suarez, stefan_mitrovic, omar_alderete, gaston_alvarez, mauro_arambarri, nemanja_maksimovic, jaime_mata, carles_alena, juanmi_latasa, # Getafe
    # paulo_gazzaniga, yan_couto, santiago_bueno, juanpe, javier_hernandez, miguel_gutierrez, oriol_romeu, viktor_tsygankov, ivan_martin, rodrigo_riquelme, # Girona
    # edgar_badia, josan, lautaro_blanco, carlos_clerc, gerard_gumbau, tete_morente, fidel, # Elche
    # alex_remiro, andoni_gorosabel, robin_le_normand, jon_pacheco, aihen_munoz, martin_zubimendi, takefusa_kubo, mikel_merino, brais_mendez,  # Real Sociedad
    # claudio_bravo, youssouf_sabaly, german_pezzella, luiz_felipe, abner_vinicius, william_carvalho, guido_rodriguez, ayoze_perez, sergio_canales, # Real Betis
    # fernando_pacheco, oscar_gil, sergi_gomez, fernando_calero, nicolas_melamed, sergi_darder, denis_suarez,  # Espanyol
    # stole_dimitrievski, ivan_balliu, abdul_mumin, florian_lejeune, fran_garcia, oscar_valentin, santi_comesana, oscar_trejo, isi_palazon, alvaro_garcia,  # Rayo Vallecano
    jordi_masip, luis_perez, jawad_el_yamiq, lucas_olaza, kike_perez, roque_mesa, alvaro_aguado, gonzalo_plata,  # Real Valladolid
    # giorgi_mamardashvili, thierry_correia, eray_comert, cenk_ozkacar, jose_luis_gaya, nico_gonzalez, andre_almeida,  # Valencia
    # fernando_martinez, alejandro_pozo, rodrigo_ely, srdan_babic, alex_centelles, samuel_costa, lucas_robertone, gonzalo_melero, # Almeria
    # thibaut_courtois, lucas_vasquez, nacho_fernandez, eder_militao, dani_ceballos, eduardo_camavinga, aurelien_tchouameni, federico_valverde,# Real Madrid
    martin_valjent, antonio_raillo, pablo_maffeo, copete, jaume_costa, dani_rodriguez, inigo_ruiz_de_galarreta, kang_in_lee, vedat_muriqi,# Mallorca
    # marko_dmitrovic, gonzalo_montiel, nemanja_gudelj, karim_rekik, alex_telles, ivan_rakitic, pape_gueye, erik_lamela, papu_gomez,  # Sevilla
    # pepe_reina, kiko_femenia, pau_torres, aissa_mandi, alberto_moreno, manu_trigueros, dani_parejo, gio_lo_celso, yeremy_pino, # Villareal
]

two_GC = [
    # julen_agirrezabala, oscar_de_marcos, daniel_vivian, yuri_berchiche, # Athletic Club
    # jeremias_ledesma, isaac_carcelen, luis_hernandez, alfonso_espino, #Cadiz
    # rui_silva, martin_montoya, edgar_gonzalez, german_pezzella, juan_miranda, rui_silva, martin_montoya, edgar_gonzalez, german_pezzella, # Real Betis
    # martin_valjent, copete, pablo_maffeo, # Real Mallorca
    # ivan_villar, joseph_aidoo, javi_galan, unai_nunez, # Celta
    # ivo_grbic, nahuel_molina, axel_witsel, jose_maria_gimenez, mario_hermoso, # Atletico Madrid
    sergi_roberto, jules_kounde, marcos_alonso, eric_garcia, # FC Barcelona
    # josan, carlos_clerc, lautaro_blanco, tete_morente, # Elche
    ronael_pierre_gabriel, cesar_montes, brian_olivan, # Espanyol
    # david_soria, djene, domingos_duarte, omar_alderete, portu, # Getafe
    paulo_gazzaniga, arnau_martinez, bernardo_espinos, david_lopez, miguel_gutierrez, # Girona
    fernando_martinez, alejandro_pozo, rodrigo_ely, srdan_babic, alex_centelles, # Almeria
    # thibaut_courtois, antonio_rudiger, eder_militao, nacho_fernandez,  # Read Madrid
    # alex_remiro, igor_zubeldia, robin_le_normand, aihen_munoz, # Real Sociedad
    # jordi_masip, joaquin_fernandez, javi_sanchez, jawad_el_yamiq, martin_hongla,  # Real Valladolid
    stole_dimitrievski, ivan_balliu, abdul_mumin, alejandro_catena, fran_garcia, # Rayo Vallecano
    # sergio_herrera, ruben_pena, aridane_hernandez, david_garcia, manuel_sanchez, # Osasuna
    marko_dmitrovic, loic_bade, jesus_navas, # Sevilla
    # giorgi_mamardashvili, thierry_correia, gabriel_paulista, mouctar_diakhaby, jose_luis_gaya, # Valencia
    pau_torres, aissa_mandi, alberto_moreno, # Villareal
]

yellow = [paulo_gazzaniga, christian_stuani, yan_couto, jon_moncayola, bernardo_espinos, yangel_herrera, daniel_carvajal,
          yuri_berchiche, oihan_sancet, dani_ceballos, angel_correa, alejandro_baena, pablo_barrios, etienne_capoue,
          alberto_moreno, renato_tapia, franco_cervi, raphinha, ferran_torres, fali, gerard_gumbau, isaac_carcelen,
          fede_san_emeterio, tete_morente, largie_ramazani, samuel_costa, cesar_montes, alejandro_pozo, brian_olivan,
          gonzalo_melero, andres_guardado, borja_iglesias, juan_cruz, juanmi_latasa, gaston_alvarez, jawad_el_yamiq,
          juan_iglesias]

red = [
    axel_witsel, yunus_musah
]

own_goals = []
missed_pen = [mikel_vesga]
pen_save = [thibaut_courtois]

saves_pts_1 = [
    paulo_gazzaniga, aitor_fernandez, marko_dmitrovic, alex_remiro, ivo_grbic, jeremias_ledesma, fernando_martinez
]
saves_pts_2 = [
    thibaut_courtois, marc_andre_ter_stegen
]
saves_pts_3 = []
saves_pts_4 = []

bonus_1 = [
    aitor_fernandez, oihan_sancet, igor_zubeldia, ivo_grbic, marc_andre_ter_stegen, enzo_roco, lucas_robertone, nico_gonzalez, diego_lopez, stefan_mitrovic, jawad_el_yamiq
]
bonus_2 = [
    dani_rodriguez, abdessamad_ezzalzouli, eder_militao, erik_lamela, antoine_griezmann, carles_perez, gonzalo_escalante, ronael_pierre_gabriel, alvaro_aguado
]
bonus_3 = [
    copete, ante_budimir, thibaut_courtois, brais_mendez, angel_correa, gabriel_veiga, gerard_gumbau, adrian_embarba, sergio_canales, juan_miranda, gonzalo_plata
]

if updating:
    if input("are you sure? (y/n)") != "y":
        exit()
    for player in mins_pts_2:
        df.loc[df["Name"] == player, 'Mins Pts'] += 2
        weekly_df.loc[weekly_df["Name"] == player, 'Mins Pts'] += 2
    for player in mins_pts_1:
        df.loc[df["Name"] == player, 'Mins Pts'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'Mins Pts'] += 1
    for player in goals:
        df.loc[df["Name"] == player, 'G'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'G'] += 1
    for player in assists:
        df.loc[df["Name"] == player, 'A'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'A'] += 1
    for player in clean_sheets:
        df.loc[df["Name"] == player, 'CS'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'CS'] += 1
    for player in yellow:
        df.loc[df["Name"] == player, 'YC'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'YC'] += 1
    for player in red:
        df.loc[df["Name"] == player, 'RC'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'RC'] += 1
    for player in own_goals:
        df.loc[df["Name"] == player, 'OG'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'OG'] += 1
    for player in missed_pen:
        df.loc[df["Name"] == player, 'PenMiss'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'PenMiss'] += 1
    for player in saves_pts_1:
        df.loc[df["Name"] == player, 'Saves Pts'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'Saves Pts'] += 1
    for player in saves_pts_2:
        df.loc[df["Name"] == player, 'Saves Pts'] += 2
        weekly_df.loc[weekly_df["Name"] == player, 'Saves Pts'] += 2
    for player in saves_pts_3:
        df.loc[df["Name"] == player, 'Saves Pts'] += 3
        weekly_df.loc[weekly_df["Name"] == player, 'Saves Pts'] += 3
    for player in saves_pts_4:
        df.loc[df["Name"] == player, 'Saves Pts'] += 4
        weekly_df.loc[weekly_df["Name"] == player, 'Saves Pts'] += 4
    for player in pen_save:
        df.loc[df["Name"] == player, 'PenSave'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'PenSave'] += 1
    for player in bonus_1:
        df.loc[df["Name"] == player, 'Bonus'] += 1
        weekly_df.loc[weekly_df["Name"] == player, 'Bonus'] += 1
    for player in bonus_2:
        df.loc[df["Name"] == player, 'Bonus'] += 2
        weekly_df.loc[weekly_df["Name"] == player, 'Bonus'] += 2
    for player in bonus_3:
        df.loc[df["Name"] == player, 'Bonus'] += 3
        weekly_df.loc[weekly_df["Name"] == player, 'Bonus'] += 3
    for player in two_GC:
        df.loc[df["Name"] == player, '2GC'] += 1
        weekly_df.loc[weekly_df["Name"] == player, '2GC'] += 1
    df["GWs"] += 1
    weekly_df["GWs"] += 1
    for index, row in df.iterrows():
        if (row["Name"] in mins_pts_2) or (row['Name'] in mins_pts_1):
            if row["Position"] == "GK":
                df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                        row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Saves Pts"] +\
                                        row["PenSave"]*5 + row["Bonus"] + row["2GC"]*-1
            if row["Position"] == "DEF":
                df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                        row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"] + row["2GC"]*-1
            if row["Position"] == "MID":
                df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*5 + row["A"]*3 + row["CS"]*1 + row["YC"]*-1 +\
                                        row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]
            if row["Position"] == "FWD":
                df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*4 + row["A"]*3 + row["YC"]*-1 + row["RC"]*-3 +\
                                        row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]

    for index, row in weekly_df.iterrows():
        if (row["Name"] in mins_pts_2) or (row['Name'] in mins_pts_1):
            if row["Position"] == "GK":
                weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                        row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Saves Pts"] +\
                                        row["PenSave"]*5 + row["Bonus"] + row["2GC"]*-1
            if row["Position"] == "DEF":
                weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                        row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"] + row["2GC"]*-1
            if row["Position"] == "MID":
                weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*5 + row["A"]*3 + row["CS"]*1 + row["YC"]*-1 +\
                                        row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]
            if row["Position"] == "FWD":
                weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*4 + row["A"]*3 + row["YC"]*-1 + row["RC"]*-3 +\
                                        row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]

    df["Pts"] = df["Pts"].astype(int)
    df["2GC"] = df["2GC"].astype(int)
    weekly_df["Pts"] = weekly_df["Pts"].astype(int)
    weekly_df["2GC"] = weekly_df["2GC"].astype(int)
    df.to_csv("fantasy.csv")
    weekly_df.to_csv("fantasy_weekly.csv")