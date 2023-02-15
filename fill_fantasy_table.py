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


mins_pts_2 = [unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, inigo_lekue, oihan_sancet, mikel_vesga, iker_munian, nico_williams, raul_garcia, # Athletic Club
              jan_oblak, nahuel_molina, stefan_savic, mario_hermoso, reinildo, koke, rodrigo_de_paul, marcos_llorente, antoine_griezmann, alvaro_morata, # Atletico Madrid
              ivan_villar, oscar_mingueza, joseph_aidoo, renato_tapia, javi_galan, carles_perez, luca_de_la_torre, gabriel_veiga, fran_beltran, jorgen_larsen, iago_aspas, # Celta
              jeremias_ledesma, isaac_carcelen, luis_hernandez, fali, alfonso_espino, gonzalo_escalante, ruben_alcaraz, brian_ocampo, theo_bongonda, sergi_guardiola, roger_marti, # Cadiz
              edgar_badia, jose_angel_carmona, diego_gonzalez, carlos_clerc, gerard_gumbau, randy_nteka, ezequiel_ponce, # Elche
              alvaro_fernandez, leandro_cabrera, brian_olivan, sergi_darder, aleix_vidal, vinicius_souza, martin_braithwaite, javi_puado, # Espanyol
              david_soria, portu, domingos_duarte, omar_alderete, gaston_alvarez, mauro_arambarri, borja_mayoral, enes_unal, # Getafe
              paulo_gazzaniga, arnau_martinez, santiago_bueno, miguel_gutierrez, ivan_martin, aleix_garcia, oriol_romeu, valentin_castellanos, # Girona
              aitor_fernandez, aridane_hernandez, manuel_sanchez, juan_cruz, jon_moncayola, moi_gomez, lucas_torro, pablo_lumbreras, kike_barja, chimy, ante_budimir, # Osasuna
              marc_andre_ter_stegen, ronald_araujo, jules_kounde, andreas_christensen, alejandro_balde, frenkie_de_jong, gavi, pedri, franck_kessie, robert_lewandowski, raphinha,  # FC Barcelona
              predrag_rajkovic, pablo_maffeo, ludwig_augustinsson, antonio_raillo, martin_valjent, matija_nastasic, inigo_ruiz_de_galarreta, iddrisu_baba, dani_rodriguez, kang_in_lee, vedat_muriqi, # Mallorca
              stole_dimitrievski, alejandro_catena, florian_lejeune, fran_garcia, oscar_valentin, santi_comesana, oscar_trejo, isi_palazon, alvaro_garcia, sergio_camello, # Rayo Vallecano
              rui_silva, youssouf_sabaly, german_pezzella, edgar_gonzalez, abner_vinicius, andres_guardado, guido_rodriguez, rodri_sanchez, sergio_canales, juanmi, borja_iglesias, # Real Betis
              alex_remiro, ander_barrenetxea, robin_le_normand, igor_zubeldia, diego_rico, asier_illaramendi, martin_zubimendi, brais_mendez, takefusa_kubo, mikel_oyarzabal, alexander_sorloth, # Real Sociedad
              andriy_lunin, daniel_carvajal, nacho_fernandez, eder_militao, david_alaba, dani_ceballos, federico_valverde, eduardo_camavinga, rodrygo, marco_asensio, karim_benzema, # Real Madrid
              jordi_masip, luis_perez, martin_hongla, javi_sanchez, lucas_olaza, kike_perez, gonzalo_plata, oscar_plano, darwin_machis, sergio_leon, # Real Valladolid
              bono, tanguy_nianzou, loic_bade, nemanja_gudelj, bryan_gil, fernando, oliver_torres, pape_gueye, suso, youssef_ennesyri, # Sevilla
              fernando_martinez, srdan_babic, sergio_akieme_rodriguez, inigo_eguaras, samuel_costa, francisco_portillo, luis_suarez, adrian_embarba, # Almeria
              giorgi_mamardashvili, dimitri_foulquier, eray_comert, mouctar_diakhaby, jose_luis_gaya, andre_almeida, ilaix_moriba, yunus_musah, samu_castillejo, samuel_lino, # Valencia
              pepe_reina, juan_foyth, raul_albiol, pau_torres, alberto_moreno, dani_parejo, etienne_capoue, alejandro_baena, jose_luis_morales, yeremy_pino,  # Villareal
              ]

mins_pts_1 = [alex_berenguer, oier_zarraga, inaki_williams, dani_garcia, gorka_guruzeta, # Athletic Club
              pablo_barrios, saul_niguez, axel_witsel, yannick_carrasco, memphis_depay, angel_correa, # Atletico Madrid
              goncalo_paciencia, oscar_rodriguez, franco_cervi, haris_seferovic, # Celta
              ruben_sobrino, fede_san_emeterio, anthony_lozano, ivan_alejo,alex_fernandez, # Cadiz
              pol_lirola, gonzalo_verdu, tete_morente, lucas_boye, raul_guti, fidel, enzo_roco, # Elche
              oscar_gil, fernando_calero, nicolas_melamed, sergi_gomez, ruben_sanchez_saez, jose_carlos_lazo, denis_suarez, # Espanyol
              luis_milla, carles_alena, jaime_seoane, angel_algobia, juanmi_latasa, munir_el_haddadi, # Getafe
              bernardo_espinos, toni_villa, borja_garcia, rodrigo_riquelme, # Girona
              darko_brasanac, ruben_garcia, kike_garcia, # Osasuna
              jordi_alba, ferran_torres, # FC Barcelona
              tino_kadewere, abdon_prats, amath_ndiaye, # Mallorca
              ismaila_ciss, unai_lopez, raul_de_tomas,  # Rayo Vallecano
              victor_ruiz, luiz_henrique, ayoze_perez, # Real Betis
              alex_sola, pablo_marin, mikel_merino, carlos_fernandez, robert_navarro, # Real Sociedad
              alvaro_odriozola, luka_modric, aurelien_tchouameni, mariano_diaz,  # Real Madrid
              monchu, roque_mesa, alvaro_aguado, ivan_sanchez, cyle_larin, # Real Valladolid
              jesus_navas, gonzalo_montiel, marcos_acuna, lucas_ocampos, ivan_rakitic, joan_jordan, # Sevilla
              alejandro_pozo, rodrigo_ely, gonzalo_melero, houboulang_mendes, chumi, largie_ramazani, lazaro, el_bilal_toure, # Almeria
              edinson_cavani, toni_lato, justin_kluivert, hugo_duro, # Valencia
              johan_mojica, samuel_chukwueze, manu_trigueros,  # Villareal
              ]

goals = [gonzalo_escalante, sergi_guardiola, rodri_sanchez, luis_suarez, sergio_canales, samuel_costa, andres_guardado,
         youssef_ennesyri, bryan_gil, samu_castillejo, nico_williams, oihan_sancet, enes_unal, memphis_depay, pedri,
         takefusa_kubo, alexander_sorloth, sergi_darder, brian_olivan, marco_asensio, karim_benzema, karim_benzema,
         luka_modric]

assists = [theo_bongonda, theo_bongonda, rodri_sanchez, sergio_canales, pape_gueye, ilaix_moriba, oscar_de_marcos, inaki_williams,
           robert_lewandowski, mikel_oyarzabal, jose_carlos_lazo, marco_asensio]

clean_sheets = [
    brais_mendez, # Part of Sociedad
    # unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, yuri_berchiche, mikel_vesga, oier_zarraga, oihan_sancet, # Athletic Club
    jan_oblak, nahuel_molina, stefan_savic, mario_hermoso, reinildo, koke, rodrigo_de_paul, marcos_llorente, # Atletico Madrid
    jeremias_ledesma, isaac_carcelen, luis_hernandez, fali, alfonso_espino, gonzalo_escalante, ruben_alcaraz, brian_ocampo, theo_bongonda,  # Cadiz
    # agustin_marchesin, oscar_mingueza, joseph_aidoo, unai_nunez, javi_galan, carles_perez, luca_de_la_torre, gabriel_veiga,  # Celta
    marc_andre_ter_stegen, ronald_araujo, jules_kounde, andreas_christensen, alejandro_balde, frenkie_de_jong, gavi, pedri, franck_kessie, raphinha,  # FC Barcelona
    aitor_fernandez, aridane_hernandez, manuel_sanchez, juan_cruz, jon_moncayola, moi_gomez, lucas_torro, pablo_lumbreras, kike_barja, # Osasuna
    # david_soria, portu, damian_suarez, djene, domingos_duarte, omar_alderete, luis_milla, carles_alena, angel_algobia, # Getafe
    # paulo_gazzaniga, valery_fernandez, bernardo_espinos, santiago_bueno, miguel_gutierrez, ivan_martin, aleix_garcia, oriol_romeu, toni_villa, borja_garcia,  # Girona
    # benjamin_lecomte, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, # Espanyol
    # alex_remiro, aritz_elustondo, robin_le_normand, igor_zubeldia, asier_illaramendi, martin_zubimendi, takefusa_kubo, # Real Sociedad
    # rui_silva, youssouf_sabaly, german_pezzella, luiz_felipe, juan_miranda, william_carvalho, guido_rodriguez, luiz_henrique, sergio_canales, rodri_sanchez,  # Real Betis
    # alvaro_fernandez, oscar_gil, leandro_cabrera, cesar_montes, brian_olivan, aleix_vidal, vinicius_souza, sergi_darder, javi_puado,  # Espanyol
    # stole_dimitrievski, ivan_balliu, alejandro_catena, florian_lejeune, fran_garcia, oscar_valentin, santi_comesana, oscar_trejo, isi_palazon, # Rayo Vallecano
    jordi_masip, luis_perez, martin_hongla, javi_sanchez, lucas_olaza, kike_perez, gonzalo_plata, oscar_plano, darwin_machis, # Real Valladolid
    # giorgi_mamardashvili, thierry_correia, cenk_ozkacar, eray_comert, jose_luis_gaya, nico_gonzalez, yunus_musah, andre_almeida, samu_castillejo, samuel_lino, # Valencia
    # fernando_martinez, alejandro_pozo, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, cesar_de_la_hoz, leo_baptistao, lucas_robertone, gonzalo_melero, adrian_embarba, # Almeria
<<<<<<< HEAD
    andriy_lunin, daniel_carvajal, nacho_fernandez, eder_militao, david_alaba, dani_ceballos, federico_valverde, eduardo_camavinga, rodrygo, marco_asensio, # Real Madrid
=======
    # thibaut_courtois, nacho_fernandez, eder_militao, antonio_rudiger, dani_ceballos, federico_valverde, eduardo_camavinga, toni_kroos,  # Real Madrid
>>>>>>> dc36b222130aca57ca441db45d080ebbf639581f
    # predrag_rajkovic, pablo_maffeo, jaume_costa, antonio_raillo, giovanni_gonzalez, matija_nastasic, inigo_ruiz_de_galarreta, iddrisu_baba, dani_rodriguez, kang_in_lee,  # Mallorca
    bono, tanguy_nianzou, loic_bade, nemanja_gudelj, bryan_gil, fernando, oliver_torres, pape_gueye, suso, # Sevilla
    alvaro_odriozola
    ]
two_GC = [
    # unai_simon, daniel_vivian, yuri_berchiche, # Athletic Club
    # jeremias_ledesma, isaac_carcelen, fali, luis_hernandez, mamadou_mbaye, alfonso_espino, jeremias_ledesma, isaac_carcelen, luis_hernandez, mamadou_mbaye, alfonso_espino, #Cadiz
    rui_silva, youssouf_sabaly, german_pezzella, edgar_gonzalez, abner_vinicius, # Real Betis
    predrag_rajkovic, ludwig_augustinsson, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, # Real Mallorca
    # oscar_mingueza, joseph_aidoo, unai_nunez, javi_galan, # Celta
    # jan_oblak, reinildo, axel_witsel, stefan_savic, nahuel_molina, # Atletico Madrid
    # marc_andre_ter_stegen, sergi_roberto, jules_kounde, eric_garcia, alejandro_balde, # FC Barcelona
    edgar_badia, jose_angel_carmona, diego_gonzalez, enzo_roco, pedro_bigas, carlos_clerc, edgar_badia, jose_angel_carmona, diego_gonzalez, enzo_roco, pedro_bigas, carlos_clerc, # Elche
    alvaro_fernandez, leandro_cabrera, brian_olivan, # Espanyol
    # david_soria, djene, domingos_duarte, # Getafe
    paulo_gazzaniga, arnau_martinez, santiago_bueno, miguel_gutierrez, # Girona
    fernando_martinez, alejandro_pozo, chumi, srdan_babic, sergio_akieme_rodriguez, # Almeria
    # thibaut_courtois, antonio_rudiger, eder_militao, david_alaba, ferland_mendy, # Read Madrid
    alex_remiro, igor_zubeldia, robin_le_normand, diego_rico, # Real Sociedad
    # jordi_masip, luis_perez, javi_sanchez, jawad_el_yamiq, david_torres, lucas_olaza, # Real Valladolid
    # stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, # Rayo Vallecano
    # aitor_fernandez, unai_garcia, david_garcia, juan_cruz, ruben_pena, manuel_sanchez, # Osasuna
    # bono, gonzalo_montiel, loic_bade, nemanja_gudelj, karim_rekik, # Sevilla
    giorgi_mamardashvili, dimitri_foulquier, eray_comert, mouctar_diakhaby, jose_luis_gaya, # Valencia
    # pepe_reina, juan_foyth, raul_albiol, johan_mojica, # Villareal
]

yellow = [bernardo_espinos, luis_hernandez, alfonso_espino, gonzalo_escalante, miguel_gutierrez, arnau_martinez,
          anthony_lozano, inigo_eguaras, srdan_babic, edgar_gonzalez, andres_guardado, guido_rodriguez, kang_in_lee,
          iddrisu_baba, bryan_gil, gonzalo_montiel, joan_jordan, nemanja_gudelj, hugo_duro, nico_williams,
          oscar_de_marcos, samu_castillejo, santi_comesana, oscar_valentin, alvaro_garcia, gaston_alvarez, ivan_balliu,
          mauro_arambarri, joseph_aidoo, gabriel_veiga, reinildo, nahuel_molina, juan_cruz, darwin_machis, manuel_sanchez,
          chimy, pau_torres, ronald_araujo, alejandro_baena, frenkie_de_jong, jules_kounde, dani_parejo, alberto_moreno,
          raphinha, oscar_gil, martin_braithwaite, carlos_fernandez, enzo_roco, gerard_gumbau, diego_gonzalez, mariano_diaz]

red = [carles_alena, stefan_savic, leandro_cabrera]

own_goals = [mauro_arambarri, leandro_cabrera]
missed_pen = [borja_mayoral, raul_de_tomas]
pen_save = [david_soria]

saves_pts_1 = [
    fernando_martinez, predrag_rajkovic, david_soria, jan_oblak, jordi_masip, aitor_fernandez, pepe_reina, alex_remiro
]
saves_pts_2 = [
    rui_silva, unai_simon
]
saves_pts_3 = [edgar_badia]
saves_pts_4 = []

bonus_1 = [
    rodri_sanchez, oihan_sancet, david_soria, jan_oblak, ronald_araujo, mikel_oyarzabal, marco_asensio
]
bonus_2 = [
    sergio_canales, nemanja_gudelj, jesus_navas, unai_simon, florian_lejeune, rodrigo_de_paul, aitor_fernandez, pedri, takefusa_kubo, rodrygo
]
bonus_3 = [
    gonzalo_escalante, isaac_carcelen, sergi_guardiola, samuel_costa, pape_gueye, jose_luis_gaya, enes_unal, javi_galan, jordi_masip, aridane_hernandez, robert_lewandowski, vinicius_souza, karim_benzema
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