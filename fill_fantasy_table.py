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
luca_de_la_torre = "Luca De La Torre"
carlos_dominguez = "Carlos Dominguez"
jorgen_larsen = "Jorgen Larsen"

# Elche
edgar_badia = "Edgar Badia"
john_donald = "John Donald"
enzo_roco = "Enzo Roco"
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
aleix_vidal = "Aleix Vidal"
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
javi_puado = "Javi Puado"
keidi_bare = "Keidi Bare"
dani_gomez = "Dani Gomez"
martin_braithwaite = "Martin Braithwaite"
omar_el_hilali = "Omar El Hilali"
simo = "Simo"

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
samu_saiz = "Samu Saiz"
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
alex_moreno = "Alex Moreno"
martin_montoya = "Martin Montoya"
victor_ruiz = "Victor Ruiz"
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

# Real Mallorca
predrag_rajkovic = "Predrag Rajkovic"
pablo_maffeo = "Pablo Maffeo"
martin_valjent = "Martin Valjent"
antonio_raillo = "Antonio Raillo"
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
robert_navarro = "Robert Navarro"
jon_pacheco = "Jon Pacheco"
alexander_sorloth = "Alexander Sorloth"
alex_sola = "Alex Sola"

# Real Valladolid
sergio_asenjo = "Sergio Asenjo"
jordi_masip = "Jordi Masip"
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
javi_sanchez = "Javi Sanchez"
sergi_guardiola = "Sergi Guardiola"
anuar = "Anuar"
shon_weissman = "Shon Weissman"

# Sevilla
bono = "Bono"
marko_dmitrovic = "Marko Dmitrovic"
alex_telles = "Alex Telles"
nemanja_gudelj = "Nemanja Gudelj"
marcao = "Marcao"
karim_rekik = "Karim Rekik"
marcos_acuna = "Marcos Acuna"
jesus_navas = "Jesus Navas"
kike_salas = "Kike Salas"
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
gonzalo_montiel = "Gonzalo Montiel"
oliver_torres = "Oliver Torres"
joan_jordan = "Joan Jordan"
tanguy_nianzou = "Tanguy Nianzou"
jose_angel_carmona = "Jose Angel Carmona"
suso = "Suso"
kasper_dolberg = "Kasper Dolberg"

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
leo_baptistao = "Leo Baptistao"
alex_centelles = "Alex Centelles"
alejandro_pozo = "Alejandro Pozo"
cesar_de_la_hoz = "Cesar de la Hoz"
houboulang_mendes = "Houboulang Mendes"
gonzalo_melero = "Gonzalo Melero"
el_bilal_toure = "El Bilal Toure"
lazaro = "Lazaro"
marko_milovanovic = "Marko Milovanovic"

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
gabriel_paulista = "Gabriel Paulista"
marcos_andre = "Marcos Andre"
justin_kluivert = "Justin Kluivert"
edinson_cavani = "Edinson Cavani"
andre_almeida = "Andre Almeida"
ilaix_moriba = "Ilaix Moriba"

# Villareal
geronimo_rulli = "Geronimo Rulli"
juan_foyth = "Juan Foyth"
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


mins_pts_2 = [unai_simon, oscar_de_marcos, yeray_alvarez, inigo_martinez, inigo_lekue, oihan_sancet, mikel_vesga, iker_munian, nico_williams, alex_berenguer, inaki_williams, # Athletic Club
              jan_oblak, nahuel_molina, reinildo, stefan_savic, jose_maria_gimenez, thomas_lemar, koke, geoffrey_kondogbia, rodrigo_de_paul, antoine_griezmann, alvaro_morata, # Atletico Madrid
              agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, fran_beltran, gabriel_veiga, oscar_rodriguez, franco_cervi, iago_aspas, jorgen_larsen, # Celta
              jeremias_ledesma, isaac_carcelen, luis_hernandez, victor_chust, alfonso_espino, ruben_alcaraz, ruben_sobrino, ivan_alejo, alex_fernandez, # Cadiz
              edgar_badia, helibelton_palacios, enzo_roco, carlos_clerc, raul_guti, omar_mascarell, tete_morente, pere_milla, # Elche
              benjamin_lecomte, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, edu_exposito, joselu, aleix_vidal, javi_puado, # Espanyol
              david_soria, damian_suarez, domingos_duarte, djene, stefan_mitrovic, luis_milla, carles_alena, borja_mayoral, enes_unal, # Getafe
              juan_carlos, arnau_martinez, santiago_bueno, bernardo_espinos, miguel_gutierrez, aleix_garcia, oriol_romeu, yangel_herrera, valentin_castellanos, rodrigo_riquelme, # Girona
              sergio_herrera, juan_cruz, david_garcia, nacho_vidal, lucas_torro, darko_brasanac, jon_moncayola, moi_gomez, chimy, kike_garcia, # Osasuna
              marc_andre_ter_stegen, alejandro_balde, eric_garcia, jules_kounde, sergi_roberto, pedri, sergio_busquets, frenkie_de_jong, raphinha, ousmane_dembele, robert_lewandowski, # FC Barcelona
              predrag_rajkovic, brian_cufre, copete, antonio_raillo, martin_valjent, pablo_maffeo, antonio_sanchez, inigo_ruiz_de_galarreta, kang_in_lee, # Mallorca
              stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, oscar_valentin, santi_comesana, isi_palazon, alvaro_garcia, oscar_trejo, sergio_camello, # Rayo Vallecano
              rui_silva, youssouf_sabaly, luiz_felipe, victor_ruiz, alex_moreno, guido_rodriguez, william_carvalho, sergio_canales, luiz_henrique, rodri_sanchez, borja_iglesias, # Real Betis
              alex_remiro, andoni_gorosabel, igor_zubeldia, robin_le_normand, martin_zubimendi, david_silva, brais_mendez, takefusa_kubo, alexander_sorloth, # Real Sociedad
              andriy_lunin, daniel_carvajal, eder_militao, david_alaba, ferland_mendy, luka_modric, aurelien_tchouameni, toni_kroos, federico_valverde, karim_benzema, vinicius_junior, # Real Madrid
              jordi_masip, lucas_olaza, javi_sanchez, sergio_escudero, roque_mesa, monchu, oscar_plano, kike_perez, sergio_leon, ivan_sanchez, # Real Valladolid
              bono, gonzalo_montiel, marcao, tanguy_nianzou, nemanja_gudelj, ivan_rakitic, alex_telles, erik_lamela, isco, oliver_torres, # Sevilla
              fernando_martinez, houboulang_mendes, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, cesar_de_la_hoz, gonzalo_melero, inigo_eguaras, leo_baptistao, largie_ramazani, el_bilal_toure, # Almeria
              giorgi_mamardashvili, thierry_correia, eray_comert, gabriel_paulista, jose_luis_gaya, yunus_musah, nico_gonzalez, andre_almeida, samuel_lino, justin_kluivert, # Valencia
              geronimo_rulli, aissa_mandi, raul_albiol, pau_torres, alfonso_pedraza, dani_parejo, yeremy_pino, alejandro_baena, nicolas_jackson, arnaut_danjuma  # Villareal
              ]

mins_pts_1 = [daniel_vivian, oier_zarraga, dani_garcia, asier_villalibre, raul_garcia, # Athletic Club
              ivo_grbic, axel_witsel, saul_niguez, angel_correa, joao_felix, # Atletico Madrid
              oscar_mingueza, carles_perez, goncalo_paciencia, # Celta
              fede_san_emeterio, alvaro_negredo, joseba_zaldua, jose_mari, anthony_lozano, brian_ocampo, # Cadiz
              josan, pedro_bigas, alex_collado, nicolas_fernandez, domingos_quina, ezequiel_ponce, gonzalo_verdu, # Elche
              nicolas_melamed, jose_carlos_lazo, keidi_bare, # Espanyol
              fabrizio_angileri, nemanja_maksimovic, portu, juan_iglesias, angel_algobia, jaime_mata, # Getafe
              javier_hernandez, valery_fernandez, toni_villa, manu_vallejo, christian_stuani, # Girona
              manuel_sanchez, aimar_oroz, ruben_garcia, ante_budimir, abdessamad_ezzalzouli, # Osasuna
              jordi_alba, franck_kessie, gavi, ferran_torres, ansu_fati, # FC Barcelona
              iddrisu_baba, abdon_prats, dani_rodriguez, lago_junior, rodrigo_battaglia, angel_rodriguez, # Mallorca
              unai_lopez, bebe, jose_pozo, radamel_falcao, # Rayo Vallecano
              juan_cruz, andres_guardado, aitor_ruibal, joaquin, willian_jose, # Real Betis
              diego_rico, aritz_elustondo, mikel_merino, robert_navarro, ander_barrenetxea, # Real Sociedad
              antonio_rudiger, eduardo_camavinga, marco_asensio, rodrygo, # Real Madrid
              alvaro_aguado, joaquin_fernandez, sergi_guardiola, shon_weissman, # Real Valladolid
              jesus_navas, marcos_acuna, jose_angel_carmona, papu_gomez, suso, youssef_ennesyri, # Sevilla
              alejandro_pozo, lucas_robertone, francisco_portillo, dyego_sousa, lazaro, # Almeria
              edinson_cavani, jesus_vasquez, toni_lato, ilaix_moriba, hugo_duro, # Valencia
              manu_trigueros, samuel_chukwueze, jose_luis_morales,  # Villareal
              ]

goals = [alex_fernandez, christian_stuani, pere_milla, edinson_cavani, edinson_cavani, pere_milla, nemanja_gudelj,
         antoine_griezmann, asier_illaramendi, iago_aspas, igor_zubeldia, karim_benzema, federico_valverde, rodrygo, ferran_torres,
         joselu, william_carvalho, el_bilal_toure, borja_iglesias, william_carvalho, arnaut_danjuma, arnaut_danjuma]

assists = [alvaro_negredo, andre_almeida, carlos_clerc, isco, alvaro_morata, brais_mendez, ferland_mendy, robert_lewandowski,
           brian_olivan, gonzalo_melero, joaquin, borja_iglesias, nicolas_jackson]

clean_sheets = [
    # unai_simon, oscar_de_marcos, inigo_martinez, yeray_alvarez, inigo_lekue, dani_garcia, iker_munian, alex_berenguer, # Athletic Club
    jan_oblak, nahuel_molina, jose_maria_gimenez, stefan_savic, reinildo, thomas_lemar, geoffrey_kondogbia, koke, rodrigo_de_paul, # Atletico Madrid
    # jeremias_ledesma, isaac_carcelen, luis_hernandez, victor_chust, alfonso_espino, ruben_alcaraz, ivan_alejo, ruben_sobrino, # Cadiz
    # agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, oscar_rodriguez, fran_beltran, gabriel_veiga, # Celta
    # marc_andre_ter_stegen, marcos_alonso, gerard_pique, alejandro_balde, jordi_alba, gavi, sergio_busquets, pedri, raphinha, # FC Barcelona
                # sergio_herrera, nacho_vidal, unai_garcia, david_garcia, juan_cruz, darko_brasanac, lucas_torro, moi_gomez, ruben_garcia, # Osasuna
    david_soria, domingos_duarte, stefan_mitrovic, djene, damian_suarez, carles_alena, luis_milla, # Getafe
    benjamin_lecomte, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, # Espanyol
    # alex_remiro, alex_sola, aritz_elustondo, jon_pacheco, aihen_munoz, martin_zubimendi, mikel_merino, brais_mendez, david_silva, takefusa_kubo, # Real Sociedad
    # rui_silva, victor_ruiz, alex_moreno, guido_rodriguez, william_carvalho, sergio_canales, # Real Betis
                # alvaro_fernandez, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, javi_puado, # Espanyol
    stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, oscar_valentin, santi_comesana, isi_palazon, oscar_trejo, alvaro_garcia, # Rayo Vallecano
    # jordi_masip, ivan_fresneda, joaquin_fernandez, javi_sanchez, sergio_escudero, roque_mesa, kike_perez, ivan_sanchez, oscar_plano, # Real Valladolid
                # giorgi_mamardashvili, thierry_correia, mouctar_diakhaby, eray_comert, jose_luis_gaya, hugo_guillamon, ilaix_moriba, andre_almeida, samu_castillejo, # Valencia
    # andriy_lunin, daniel_carvajal, eder_militao, antonio_rudiger, david_alaba, luka_modric, aurelien_tchouameni, eduardo_camavinga, federico_valverde, # Real Madrid
                # predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, clement_grenier, inigo_ruiz_de_galarreta, kang_in_lee, # Real Mallorca
    bono, gonzalo_montiel, tanguy_nianzou, marcao, alex_telles, ivan_rakitic, nemanja_gudelj, oliver_torres, isco, erik_lamela, # Sevilla
    geronimo_rulli, alfonso_pedraza, pau_torres, raul_albiol, aissa_mandi, dani_parejo, alejandro_baena, yeremy_pino, nicolas_jackson # Villareal
    ]

two_GC = [
          # unai_simon, oscar_de_marcos, yeray_alvarez, inigo_martinez, inigo_lekue, # Athletic Club
    # jeremias_ledesma, joseba_zaldua, luis_hernandez, victor_chust, alfonso_espino, #Cadiz
          # rui_silva, youssouf_sabaly, luiz_felipe, edgar_gonzalez, alex_moreno, # Real Betis
          # predrag_rajkovic, jaume_costa, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, predrag_rajkovic, jaume_costa, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, # Real Mallorca
    agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, # Celta
          # jan_oblak, reinildo, felipe, # Atletico Madrid
    marc_andre_ter_stegen, sergi_roberto, jules_kounde, eric_garcia, alejandro_balde, # FC Barcelona
    edgar_badia, josan, helibelton_palacios, enzo_roco, carlos_clerc, # Elche
    # benjamin_lecomte, brian_olivan, leandro_cabrera, sergi_gomez, fernando_calero, # Espanyol
    # david_soria, juan_iglesias, djene, domingos_duarte, gaston_alvarez, damian_suarez, # Getafe
    # juan_carlos, santiago_bueno, bernardo_espinos, javier_hernandez, # Girona
    fernando_martinez, houboulang_mendes, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, # Almeria
    # alex_remiro, aihen_munoz, jon_pacheco, aritz_elustondo, # Real Sociedad
    # jordi_masip, joaquin_fernandez, javi_sanchez, sergio_escudero, # Real Valladolid
    # diego_lopez, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, # Rayo Vallecano
    sergio_herrera, david_garcia, juan_cruz, nacho_vidal, # Osasuna
    # bono, jose_angel_carmona, tanguy_nianzou, nemanja_gudelj, alex_telles, # Sevilla
    giorgi_mamardashvili, thierry_correia, gabriel_paulista, eray_comert, jose_luis_gaya, # Valencia
]

yellow = [fabrizio_angileri, stefan_mitrovic, alejandro_catena, angel_algobia, bebe, ruben_sobrino, fede_san_emeterio,
          aleix_garcia, santiago_bueno, ruben_alcaraz, arnau_martinez, valentin_castellanos, christian_stuani, alfonso_espino,
          giorgi_mamardashvili, helibelton_palacios, eray_comert, nicolas_fernandez, yunus_musah, pere_milla, edgar_badia,
          tete_morente, gonzalo_montiel, marcao, inigo_ruiz_de_galarreta, erik_lamela, dani_rodriguez, jose_maria_gimenez,
          alvaro_morata, jan_oblak, saul_niguez, axel_witsel, ivo_grbic, asier_illaramendi, robin_le_normand, martin_zubimendi,
          jorgen_larsen, hugo_mallo, david_silva, igor_zubeldia, carles_perez, oscar_mingueza, ander_barrenetxea, agustin_marchesin,
          robert_navarro, vinicius_junior, luka_modric, gavi, franck_kessie, sergio_escudero, monchu, roque_mesa, vinicius_souza,
          gonzalo_melero, sergio_canales, darko_brasanac, sergio_herrera, juan_cruz, raul_albiol, kike_garcia, ruben_garcia,
          aimar_oroz, manu_trigueros]

red = [goncalo_paciencia]

own_goals = []
missed_pen = [oscar_trejo]
pen_save = [david_soria]

saves_pts_1 = [stole_dimitrievski, david_soria, jeremias_ledesma, edgar_badia, giorgi_mamardashvili, bono, agustin_marchesin, andriy_lunin, fernando_martinez, rui_silva, geronimo_rulli]
saves_pts_2 = [sergio_herrera]
saves_pts_3 = []
saves_pts_4 = []

bonus_1 = [
    jose_luis_gaya, andre_almeida, marcao, gonzalo_melero
]
bonus_2 = [
    stole_dimitrievski, oscar_valentin, christian_stuani, alex_fernandez, jeremias_ledesma, edinson_cavani, nemanja_gudelj, geoffrey_kondogbia, yeray_alvarez, brais_mendez, igor_zubeldia, borja_iglesias, arnaut_danjuma, geronimo_rulli
]
bonus_3 = [
    david_soria, aleix_garcia, pere_milla, bono, reinildo, iago_aspas, raphinha, rodrygo, toni_kroos, brian_olivan, sergi_darder, vinicius_souza, william_carvalho, alejandro_baena
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

    df.to_csv("fantasy.csv")
    weekly_df.to_csv("fantasy_weekly.csv")