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


mins_pts_2 = [julen_agirrezabala, oscar_de_marcos, yeray_alvarez, daniel_vivian, yuri_berchiche, oier_zarraga, dani_garcia, iker_munian, alex_berenguer, inaki_williams, gorka_guruzeta, # Athletic Club
              jan_oblak, jose_maria_gimenez, stefan_savic, mario_hermoso, koke, marcos_llorente, yannick_carrasco, alvaro_morata, antoine_griezmann, # Atletico Madrid
              ivan_villar, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, carles_perez, gabriel_veiga, fran_beltran, haris_seferovic, iago_aspas, # Celta
              luis_hernandez, fali, alfonso_espino, ivan_alejo, fede_san_emeterio, ruben_alcaraz, ruben_sobrino, sergi_guardiola, alvaro_negredo, # Cadiz
              edgar_badia, tete_morente, helibelton_palacios, pedro_bigas, omar_mascarell, carlos_clerc, gerard_gumbau, lautaro_blanco, fidel, pere_milla, # Elche
              fernando_pacheco, ruben_sanchez_saez, sergi_gomez, cesar_montes, oscar_gil, sergi_darder, jose_gragera, martin_braithwaite, vinicius_souza, javi_puado, joselu, # Espanyol
              david_soria, damian_suarez, djene, domingos_duarte, omar_alderete, juan_iglesias, nemanja_maksimovic, luis_milla, munir_el_haddadi, borja_mayoral, enes_unal, # Getafe
              paulo_gazzaniga, arnau_martinez, santiago_bueno, david_lopez, javier_hernandez, oriol_romeu, viktor_tsygankov, borja_garcia, ivan_martin, toni_villa, valentin_castellanos, # Girona
              sergio_herrera, nacho_vidal, aridane_hernandez, unai_garcia, juan_cruz, pablo_lumbreras, lucas_torro, aimar_oroz, ruben_garcia, kike_barja, ante_budimir, # Osasuna
              marc_andre_ter_stegen, sergi_roberto, ronald_araujo, marcos_alonso, jules_kounde, jordi_alba, eric_garcia, gavi, robert_lewandowski, ferran_torres, ansu_fati,  # FC Barcelona
              predrag_rajkovic, pablo_maffeo, giovanni_gonzalez, antonio_raillo, copete, jaume_costa, inigo_ruiz_de_galarreta, iddrisu_baba, dani_rodriguez, vedat_muriqi, kang_in_lee, # Mallorca
              stole_dimitrievski, ivan_balliu, alejandro_catena, florian_lejeune, fran_garcia, oscar_valentin, santi_comesana, isi_palazon, oscar_trejo, sergio_camello, # Rayo Vallecano
              rui_silva, aitor_ruibal, luiz_felipe, german_pezzella, juan_miranda, william_carvalho, guido_rodriguez, rodri_sanchez, ayoze_perez, luiz_henrique, borja_iglesias, # Real Betis
              alex_remiro, andoni_gorosabel, robin_le_normand, igor_zubeldia, aihen_munoz, martin_zubimendi, brais_mendez, mikel_merino, david_silva, takefusa_kubo, alexander_sorloth, # Real Sociedad
              thibaut_courtois, lucas_vasquez, david_alaba, eder_militao, eduardo_camavinga, toni_kroos, aurelien_tchouameni, rodrygo, marco_asensio, karim_benzema, vinicius_junior, # Real Madrid
              sergio_asenjo, ivan_fresneda, joaquin_fernandez, jawad_el_yamiq, lucas_rosa, monchu, gonzalo_plata, sergio_leon, # Real Valladolid
              marko_dmitrovic, jesus_navas, nemanja_gudelj, loic_bade, marcos_acuna, pape_gueye, joan_jordan, lucas_ocampos, ivan_rakitic, bryan_gil, youssef_ennesyri, # Sevilla
              fernando_martinez, alex_centelles, rodrigo_ely, srdan_babic, chumi, samuel_costa, lucas_robertone, gonzalo_melero, leo_baptistao, luis_suarez, arnau_puigmal, # Almeria
              giorgi_mamardashvili, thierry_correia, cenk_ozkacar, mouctar_diakhaby, jose_luis_gaya, andre_almeida, hugo_guillamon, edinson_cavani, samuel_lino, justin_kluivert, # Valencia
              pepe_reina, juan_foyth, pau_torres, aissa_mandi, alfonso_pedraza, ramon_terrats, dani_parejo, alejandro_baena, samuel_chukwueze, jose_luis_morales, yeremy_pino,  # Villareal
              ]

mins_pts_1 = [ander_capa, mikel_vesga, nico_williams, oihan_sancet, raul_garcia, # Athletic Club
              thomas_lemar, nahuel_molina, axel_witsel, pablo_barrios, saul_niguez, angel_correa, rodrigo_de_paul, # Atletico Madrid
              luca_de_la_torre, renato_tapia, franco_cervi, jorgen_larsen, goncalo_paciencia, # Celta
              theo_bongonda, jose_mari, anthony_lozano, # Cadiz
              jose_angel_carmona, raul_guti, nicolas_fernandez, josan, ezequiel_ponce, # Elche
              ronael_pierre_gabriel, fernando_calero, nicolas_melamed, keidi_bare, denis_suarez, # Espanyol
              portu, angel_algobia, carles_alena, juanmi_latasa, # Getafe
              miguel_gutierrez, rodrigo_riquelme, christian_stuani, # Girona
              diego_moreno, jon_moncayola, moi_gomez, abdessamad_ezzalzouli, kike_garcia,  # Osasuna
              franck_kessie, # FC Barcelona
              matija_nastasic, antonio_sanchez, tino_kadewere, # Mallorca
              alvaro_garcia, abdul_mumin, salvi, unai_lopez, raul_de_tomas, # Rayo Vallecano
              juanmi, joaquin, willian_jose, # Real Betis
              alex_sola, asier_illaramendi, mikel_oyarzabal, ander_barrenetxea, mohamed_ali_cho, # Real Sociedad
              alvaro_odriozola, dani_ceballos, eden_hazard,  # Real Madrid
              david_torres, kike_perez, alvaro_aguado, oscar_plano, # Real Valladolid
              alex_telles, suso, oliver_torres, erik_lamela, # Sevilla
              kaiky, alejandro_pozo, cesar_de_la_hoz, largie_ramazani, lazaro, # Almeria
              nico_gonzalez, ilaix_moriba, samu_castillejo, yunus_musah, hugo_duro, # Valencia
              alberto_moreno, manu_trigueros, gio_lo_celso, nicolas_jackson,  # Villareal
              ]

goals = [arnau_martinez, martin_braithwaite, christian_stuani, lucas_ocampos, youssef_ennesyri, robert_lewandowski,
         ansu_fati, robert_lewandowski, ferran_torres, srdan_babic, haris_seferovic, arnau_puigmal, carles_perez, rodrygo,
         karim_benzema, karim_benzema, karim_benzema, marco_asensio, lucas_vasquez, dani_parejo, nicolas_jackson, angel_correa,
         santi_comesana, justin_kluivert]

assists = [javi_puado, bryan_gil, ronald_araujo, ferran_torres, gavi, robert_lewandowski, lucas_robertone, gabriel_veiga,
           luis_suarez, marco_asensio, vinicius_junior, vinicius_junior, rodrygo, rodrygo, eden_hazard, yeremy_pino,
           alvaro_garcia]

clean_sheets = [
    oscar_trejo, # Part of Vallecano
    julen_agirrezabala, oscar_de_marcos, yeray_alvarez, daniel_vivian, yuri_berchiche, oier_zarraga, dani_garcia, iker_munian, alex_berenguer,
    jan_oblak, jose_maria_gimenez, stefan_savic, mario_hermoso, koke, marcos_llorente, yannick_carrasco, # Atletico Madrid
    # jeremias_ledesma, isaac_carcelen, luis_hernandez, fali, alfonso_espino, gonzalo_escalante, fede_san_emeterio, ruben_sobrino, theo_bongonda, alex_fernandez,  # Cadiz
    # ivan_villar, kevin_vasquez, joseph_aidoo, unai_nunez, javi_galan, carles_perez, gabriel_veiga, fran_beltran, luca_de_la_torre,# Celta
    marc_andre_ter_stegen, sergi_roberto, ronald_araujo, marcos_alonso, jules_kounde, jordi_alba, eric_garcia, gavi, # FC Barcelona
    sergio_herrera, nacho_vidal, aridane_hernandez, unai_garcia, juan_cruz, pablo_lumbreras, lucas_torro, aimar_oroz, ruben_garcia, # Osasuna
    david_soria, damian_suarez, djene, domingos_duarte, omar_alderete, juan_iglesias, nemanja_maksimovic, luis_milla, # Getafe
    # paulo_gazzaniga, valery_fernandez, bernardo_espinos, santiago_bueno, miguel_gutierrez, ivan_martin, aleix_garcia, oriol_romeu, toni_villa, borja_garcia,  # Girona
    # edgar_badia, helibelton_palacios, gonzalo_verdu, pedro_bigas, carlos_clerc, gerard_gumbau, omar_mascarell,  # Elche
    # alex_remiro, andoni_gorosabel, robin_le_normand, igor_zubeldia, aihen_munoz, martin_zubimendi, brais_mendez, asier_illaramendi, david_silva, takefusa_kubo, # Real Sociedad
    # rui_silva, youssouf_sabaly, edgar_gonzalez, german_pezzella, juan_miranda, andres_guardado, guido_rodriguez, rodri_sanchez, ayoze_perez, sergio_canales,  # Real Betis
    # alvaro_fernandez, oscar_gil, leandro_cabrera, cesar_montes, brian_olivan, aleix_vidal, vinicius_souza, sergi_darder, javi_puado,  # Espanyol
    # stole_dimitrievski, ivan_balliu, abdul_mumin, florian_lejeune, fran_garcia, oscar_valentin, santi_comesana, oscar_trejo, isi_palazon, alvaro_garcia,  # Rayo Vallecano
    # jordi_masip, luis_perez, martin_hongla, javi_sanchez, lucas_olaza, kike_perez, gonzalo_plata, oscar_plano, darwin_machis, # Real Valladolid
    # giorgi_mamardashvili, dimitri_foulquier, cenk_ozkacar, mouctar_diakhaby, jose_luis_gaya, andre_almeida, hugo_guillamon, yunus_musah, justin_kluivert,  # Valencia
    # fernando_martinez, chumi, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, cesar_de_la_hoz, lucas_robertone, inigo_eguaras, # Almeria
    thibaut_courtois, lucas_vasquez, david_alaba, eder_militao, eduardo_camavinga, toni_kroos, aurelien_tchouameni, marco_asensio,# Real Madrid
    predrag_rajkovic, pablo_maffeo, giovanni_gonzalez, antonio_raillo, copete, jaume_costa, inigo_ruiz_de_galarreta, iddrisu_baba, dani_rodriguez, kang_in_lee,  # Mallorca
    marko_dmitrovic, jesus_navas, nemanja_gudelj, loic_bade, marcos_acuna, pape_gueye, joan_jordan, lucas_ocampos, ivan_rakitic, bryan_gil, # Sevilla
    pepe_reina, juan_foyth, pau_torres, aissa_mandi, alfonso_pedraza, ramon_terrats, dani_parejo, alejandro_baena, samuel_chukwueze, # Villareal
]

two_GC = [
    # unai_simon, oscar_de_marcos, yeray_alvarez, yuri_berchiche, # Athletic Club
    fali, luis_hernandez, alfonso_espino, #Cadiz
    # claudio_bravo, aitor_ruibal, german_pezzella, luiz_felipe, abner_vinicius, # Real Betis
    # predrag_rajkovic, jaume_costa, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, # Real Mallorca
    ivan_villar, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, # Celta
    # jan_oblak, reinildo, axel_witsel, stefan_savic, nahuel_molina, # Atletico Madrid
    # marc_andre_ter_stegen, sergi_roberto, jules_kounde, eric_garcia, alejandro_balde, # FC Barcelona
    edgar_badia, tete_morente, helibelton_palacios, pedro_bigas, omar_mascarell, carlos_clerc, edgar_badia, tete_morente, helibelton_palacios, pedro_bigas, omar_mascarell, carlos_clerc, # Elche
    fernando_pacheco, oscar_gil, cesar_montes, sergi_gomez, ruben_sanchez_saez, # Espanyol
    # david_soria, djene, domingos_duarte, omar_alderete, juan_iglesias, # Getafe
    # paulo_gazzaniga, arnau_martinez, santiago_bueno, david_lopez, # Girona
    fernando_martinez, alex_centelles, rodrigo_ely, srdan_babic, chumi, # Almeria
    # thibaut_courtois, antonio_rudiger, eder_militao, daniel_carvajal, # Read Madrid
    alex_remiro, andoni_gorosabel, igor_zubeldia, robin_le_normand, aihen_munoz, # Real Sociedad
    sergio_asenjo, ivan_fresneda, joaquin_fernandez, jawad_el_yamiq, sergio_asenjo, ivan_fresneda, joaquin_fernandez, jawad_el_yamiq, sergio_asenjo, ivan_fresneda, joaquin_fernandez, jawad_el_yamiq, # Real Valladolid
    # stole_dimitrievski, florian_lejeune, alejandro_catena, fran_garcia, # Rayo Vallecano
    # aitor_fernandez, aridane_hernandez, david_garcia, manuel_sanchez, # Osasuna
    # bono, jesus_navas, nemanja_gudelj, loic_bade, marcos_acuna, # Sevilla
    # giorgi_mamardashvili, dimitri_foulquier, eray_comert, cenk_ozkacar, jose_luis_gaya, # Valencia
    # pepe_reina, juan_foyth, raul_albiol, pau_torres, johan_mojica, # Villareal
]

yellow = [angel_rodriguez, iddrisu_baba, nacho_vidal, inigo_ruiz_de_galarreta, giovanni_gonzalez, kang_in_lee, antonio_raillo,
          ante_budimir, jaume_costa, diego_moreno, oriol_romeu, ivan_martin, valentin_castellanos, denis_suarez, fernando_calero,
          arnau_martinez, loic_bade, ivan_alejo, ruben_sobrino, lucas_ocampos, bryan_gil, pape_gueye, gavi, ronald_araujo,
          robert_lewandowski, leo_baptistao, arnau_puigmal, carles_perez, fernando_martinez, samuel_costa, luis_suarez,
          iago_aspas, gabriel_veiga, ivan_fresneda, ramon_terrats, igor_zubeldia, pepe_reina, juan_foyth, martin_zubimendi,
          david_silva, nahuel_molina, ayoze_perez, willian_jose, oscar_valentin, thierry_correia, justin_kluivert, ivan_balliu,
          alejandro_catena]

red = [copete, reinier, sergi_gomez, nicolas_jackson]

own_goals = []
missed_pen = []
pen_save = []

saves_pts_1 = [
    david_soria, marko_dmitrovic, fernando_martinez, pepe_reina, stole_dimitrievski
]
saves_pts_2 = [
    rui_silva,
]
saves_pts_3 = []
saves_pts_4 = [sergio_asenjo]

bonus_1 = [
    predrag_rajkovic, antonio_raillo, joselu, martin_braithwaite, christian_stuani, david_soria, gavi, srdan_babic, arnau_puigmal, carles_perez, hugo_mallo, samuel_chukwueze, jose_maria_gimenez, mario_hermoso, santi_comesana
]
bonus_2 = [
    pablo_maffeo, javier_hernandez, munir_el_haddadi, marko_dmitrovic, bryan_gil, iago_aspas, rodrygo, marco_asensio, alejandro_baena, rui_silva, samuel_lino
]
bonus_3 = [
    aridane_hernandez, arnau_martinez, iker_munian, youssef_ennesyri, robert_lewandowski, ferran_torres, javi_galan, karim_benzema, juan_foyth, antoine_griezmann, samu_castillejo
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