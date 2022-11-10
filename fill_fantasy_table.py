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
aitor_fernandez = "Aitor Fernandez"
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
jordan_amavi = "Jordan Amavi"
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
claudio_bravo = "Claudio Bravo"
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
jawad_el_yamiq = "Jawad El Yamiq"
sergio_escudero = "Sergio Escudero"
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
adnan_januzaj = "Adnan Januzaj"
gonzalo_montiel = "Gonzalo Montiel"
oliver_torres = "Oliver Torres"
joan_jordan = "Joan Jordan"
tanguy_nianzou = "Tanguy Nianzou"
jose_angel_carmona = "Jose Angel Carmona"
suso = "Suso"
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


mins_pts_2 = [unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, inigo_lekue, mikel_vesga, oihan_sancet, ander_herrera, nico_williams, inaki_williams, gorka_guruzeta, # Athletic Club
              jan_oblak, reinildo, stefan_savic, felipe, rodrigo_de_paul, axel_witsel, marcos_llorente, antoine_griezmann, alvaro_morata, angel_correa, # Atletico Madrid
              agustin_marchesin, oscar_mingueza, joseph_aidoo, unai_nunez, javi_galan, kevin_vasquez, renato_tapia, gabriel_veiga, franco_cervi, goncalo_paciencia, carles_perez, # Celta
              jeremias_ledesma, isaac_carcelen, fali, alfonso_espino, ruben_sobrino, fede_san_emeterio, alex_fernandez, anthony_lozano, # Cadiz
              edgar_badia, pol_lirola, enzo_roco, diego_gonzalez, carlos_clerc, omar_mascarell, alex_collado, pere_milla, lucas_boye, # Elche
              benjamin_lecomte, oscar_gil, fernando_calero, sergi_gomez, brian_olivan, vinicius_souza, keidi_bare, sergi_darder, martin_braithwaite, javi_puado, joselu, # Espanyol
              david_soria, djene, stefan_mitrovic, juan_iglesias, luis_milla, carles_alena, borja_mayoral, enes_unal, # Getafe
              paulo_gazzaniga, santiago_bueno, david_lopez, javier_hernandez, arnau_martinez, aleix_garcia, oriol_romeu, valery_fernandez, toni_villa, valentin_castellanos, # Girona
              aitor_fernandez, nacho_vidal, david_garcia, unai_garcia, juan_cruz, ruben_garcia, aimar_oroz, moi_gomez, jon_moncayola, chimy, # Osasuna
              marc_andre_ter_stegen, alejandro_balde, andreas_christensen, marcos_alonso, jordi_alba, frenkie_de_jong, sergio_busquets, pedri, ousmane_dembele, ferran_torres, # FC Barcelona
              predrag_rajkovic, jaume_costa, antonio_raillo, martin_valjent, copete, giovanni_gonzalez, inigo_ruiz_de_galarreta, kang_in_lee, antonio_sanchez, vedat_muriqi, # Mallorca
              stole_dimitrievski, ivan_balliu, alejandro_catena, florian_lejeune, fran_garcia, oscar_valentin, santi_comesana, alvaro_garcia, unai_lopez, # Rayo Vallecano
              rui_silva, youssouf_sabaly, edgar_gonzalez, victor_ruiz, alex_moreno, luiz_henrique, sergio_canales, juan_cruz_betis, willian_jose, # Real Betis
              alex_remiro, alex_sola, robin_le_normand, jon_pacheco, diego_rico, brais_mendez, david_silva, alexander_sorloth, # Real Sociedad
              thibaut_courtois, lucas_vasquez, eder_militao, david_alaba, ferland_mendy, luka_modric, aurelien_tchouameni, toni_kroos, federico_valverde, rodrygo, vinicius_junior, # Real Madrid
              jordi_masip, ivan_fresneda, jawad_el_yamiq, zouhair_feddal, lucas_olaza, gonzalo_plata, monchu, kike_perez, sergi_guardiola, # Real Valladolid
              bono, jesus_navas, alex_telles, nemanja_gudelj, oliver_torres, erik_lamela, rafa_mir, # Sevilla
              fernando_martinez, alejandro_pozo, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, cesar_de_la_hoz, lucas_robertone, gonzalo_melero, leo_baptistao, adrian_embarba, el_bilal_toure, # Almeria
              giorgi_mamardashvili, thierry_correia, eray_comert, cenk_ozkacar, jose_luis_gaya, yunus_musah, nico_gonzalez, andre_almeida, samuel_lino, hugo_duro, samu_castillejo, # Valencia
              geronimo_rulli, kiko_femenia, raul_albiol, alberto_moreno, dani_parejo, etienne_capoue, samuel_chukwueze, manu_trigueros, arnaut_danjuma, yeremy_pino,  # Villareal
              ]

mins_pts_1 = [jon_morcillo, iker_munian, asier_villalibre, raul_garcia, unai_vencedor, # Athletic Club
              yannick_carrasco, nahuel_molina, thomas_lemar, sergio_reguilon, koke, # Atletico Madrid
              oscar_rodriguez, fran_beltran, iago_aspas, # Celta
              jose_mari, brian_ocampo, lucas_perez, ivan_alejo, ruben_alcaraz, alvaro_negredo, theo_bongonda, # Cadiz
              pedro_bigas, raul_guti, josan, nicolas_fernandez, ezequiel_ponce, gerard_gumbau, roger_marti, # Elche
              aleix_vidal, edu_exposito, nicolas_melamed, jose_carlos_lazo, dani_gomez, # Espanyol
              jordan_amavi, nemanja_maksimovic, juanmi_latasa, munir_el_haddadi, # Getafe
              ramon_terrats, yangel_herrera, bernardo_espinos, rodrigo_riquelme, christian_stuani, ivan_martin, # Girona
              lucas_torro, darko_brasanac, ruben_pena, kike_garcia, ante_budimir, kike_barja, # Osasuna
              robert_lewandowski, gavi, raphinha, ansu_fati, # FC Barcelona
              iddrisu_baba, matija_nastasic, rodrigo_battaglia, abdon_prats, amath_ndiaye, # Mallorca
              salvi, ismaila_ciss, randy_nteka, oscar_trejo, sergio_camello, isi_palazon, radamel_falcao, # Rayo Vallecano
              german_pezzella, aitor_ruibal, william_carvalho, guido_rodriguez, paul_akouokou, rodri_sanchez, # Real Betis
              martin_zubimendi, mikel_merino, carlos_fernandez, igor_zubeldia, pablo_marin, takefusa_kubo, robert_navarro, # Real Sociedad
              nacho_fernandez, eduardo_camavinga, dani_ceballos, # Real Madrid
              lucas_rosa, alvaro_aguado, oscar_plano, ivan_sanchez, sergio_leon, shon_weissman, # Real Valladolid
              tanguy_nianzou, ivan_rakitic, karim_rekik, isco, kike_salas, thomas_delaney, adnan_januzaj, joan_jordan, youssef_ennesyri, # Sevilla
              samuel_costa, francisco_portillo, inigo_eguaras, largie_ramazani, dyego_sousa, # Almeria
              dimitri_foulquier, justin_kluivert, hugo_guillamon, marcos_andre, # Valencia
              juan_foyth, alejandro_baena, francis_coquelin, gerard_moreno,  # Villareal
              ]

goals = [pol_lirola, ivan_martin, valentin_castellanos, gorka_guruzeta, gorka_guruzeta, daniel_vivian, david_garcia, pedri,
         raphinha, alexander_sorloth, brais_mendez, rafa_mir, leo_baptistao, vedat_muriqi, andre_almeida, hugo_guillamon,
         justin_kluivert, eder_militao, toni_kroos, lucas_perez]

assists = [alex_collado, javier_hernandez, arnau_martinez, mikel_vesga, iker_munian, ruben_garcia, frenkie_de_jong, mikel_merino,
           mikel_merino, alex_telles, adrian_embarba, jaume_costa, jose_luis_gaya, toni_kroos]

clean_sheets = [
    unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, inigo_lekue, oihan_sancet, mikel_vesga, ander_herrera, # Athletic Club
    # jan_oblak, nahuel_molina, jose_maria_gimenez, stefan_savic, reinildo, thomas_lemar, geoffrey_kondogbia, koke, rodrigo_de_paul, # Atletico Madrid
    # jeremias_ledesma, luis_hernandez, alfonso_espino, fede_san_emeterio, theo_bongonda, alex_fernandez, brian_ocampo, # Cadiz
    agustin_marchesin, kevin_vasquez, joseph_aidoo, unai_nunez, oscar_mingueza, javi_galan, renato_tapia, gabriel_veiga, franco_cervi, # Celta
    # marc_andre_ter_stegen, alejandro_balde, gerard_pique, marcos_alonso, jordi_alba, sergio_busquets, frenkie_de_jong, pedri,  # FC Barcelona
    # aitor_fernandez, manuel_sanchez, david_garcia, unai_garcia, ruben_pena, lucas_torro, aimar_oroz, moi_gomez, kike_barja,  # Osasuna
    # david_soria, portu, djene, stefan_mitrovic, juan_iglesias, luis_milla, carles_alena, nemanja_maksimovic, # Getafe
    # benjamin_lecomte, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, # Espanyol
    # alex_remiro, andoni_gorosabel, aritz_elustondo, jon_pacheco, diego_rico, david_silva, mikel_merino, brais_mendez, takefusa_kubo, # Real Sociedad
    # rui_silva, youssouf_sabaly, edgar_gonzalez, german_pezzella, alex_moreno, paul_akouokou, andres_guardado, nabil_fekir, sergio_canales, # Real Betis
                # alvaro_fernandez, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, javi_puado, # Espanyol
    stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, oscar_valentin, santi_comesana, unai_lopez, alvaro_garcia, # Rayo Vallecano
    # jordi_masip, lucas_rosa, jawad_el_yamiq, joaquin_fernandez, javi_sanchez, sergio_escudero, monchu, # Real Valladolid
    giorgi_mamardashvili, thierry_correia, cenk_ozkacar, eray_comert, jose_luis_gaya, nico_gonzalez, yunus_musah, andre_almeida, samu_castillejo, samuel_lino, # Valencia
    fernando_martinez, alejandro_pozo, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, cesar_de_la_hoz, leo_baptistao, lucas_robertone, gonzalo_melero, adrian_embarba, # Almeria
    # andriy_lunin, daniel_carvajal, eder_militao, antonio_rudiger, david_alaba, luka_modric, toni_kroos, federico_valverde, # Real Madrid
    predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, giovanni_gonzalez, inigo_ruiz_de_galarreta, kang_in_lee, antonio_sanchez, # Real Mallorca
    # bono, gonzalo_montiel, tanguy_nianzou, marcao, alex_telles, ivan_rakitic, nemanja_gudelj, oliver_torres, isco, erik_lamela, # Sevilla
    geronimo_rulli, kiko_femenia, raul_albiol, alberto_moreno, dani_parejo, etienne_capoue, samuel_chukwueze, manu_trigueros, yeremy_pino,  # Villareal
]

two_GC = [
    # unai_simon, oscar_de_marcos, inigo_martinez, yeray_alvarez, mikel_balenziaga, # Athletic Club
    jeremias_ledesma, isaac_carcelen, fali, alfonso_espino, #Cadiz
    rui_silva, youssouf_sabaly, victor_ruiz, edgar_gonzalez, alex_moreno, # Real Betis
          # predrag_rajkovic, jaume_costa, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, predrag_rajkovic, jaume_costa, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, # Real Mallorca
    # agustin_marchesin, unai_nunez, joseph_aidoo, oscar_mingueza, javi_galan, # Celta
    # jan_oblak, reinildo, axel_witsel, stefan_savic, nahuel_molina, # Atletico Madrid
    # marc_andre_ter_stegen, sergi_roberto, jules_kounde, eric_garcia, alejandro_balde, # FC Barcelona
    edgar_badia, enzo_roco, diego_gonzalez, pol_lirola, carlos_clerc, # Elche
    # benjamin_lecomte, brian_olivan, leandro_cabrera, sergi_gomez, # Espanyol
    # david_soria, juan_iglesias, djene, domingos_duarte, stefan_mitrovic, damian_suarez, # Getafe
    # juan_carlos, arnau_martinez, santiago_bueno, bernardo_espinos, miguel_gutierrez, # Girona
    # fernando_martinez, houboulang_mendes, rodrigo_ely, chumi, sergio_akieme_rodriguez, # Almeria
    # thibaut_courtois, daniel_carvajal, eder_militao, david_alaba, ferland_mendy, # Read Madrid
    # alex_remiro, andoni_gorosabel, jon_pacheco, diego_rico, # Real Sociedad
    jordi_masip, lucas_olaza, zouhair_feddal, jawad_el_yamiq, ivan_fresneda, # Real Valladolid
    # stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, # Rayo Vallecano
    aitor_fernandez, unai_garcia, david_garcia, juan_cruz, nacho_vidal, # Osasuna
    bono, jesus_navas, tanguy_nianzou, karim_rekik, alex_telles, # Sevilla
    # giorgi_mamardashvili, thierry_correia, gabriel_paulista, jose_luis_gaya, # Valencia
    # geronimo_rulli, kiko_femenia, raul_albiol, pau_torres, alberto_moreno, # Villareal
]

yellow = [toni_villa, josan, gerard_gumbau, christian_stuani, diego_gonzalez, monchu, gorka_guruzeta, ander_herrera,
          unai_vencedor, jordi_alba, juan_cruz, david_garcia, lucas_torro, jon_moncayola, alejandro_balde, mikel_merino,
          jesus_navas, oliver_torres, jon_pacheco, carles_alena, leo_baptistao, cesar_de_la_hoz, lucas_robertone, munir_el_haddadi,
          fernando_martinez, srdan_babic, largie_ramazani, juan_iglesias, etienne_capoue, yeremy_pino, nicolas_melamed,
          raul_albiol, nahuel_molina, iddrisu_baba, kang_in_lee, rodrigo_de_paul, inigo_ruiz_de_galarreta,
          clement_grenier, martin_valjent, stefan_savic, santi_comesana, alvaro_garcia, radamel_falcao, florian_lejeune,
          goncalo_paciencia, oscar_valentin, salvi, alejandro_catena, samu_castillejo, paul_akouokou, eder_militao, fali,
          vinicius_junior, david_alaba, ruben_sobrino, ivan_alejo]

red = [robert_lewandowski, ivan_rakitic, tanguy_nianzou, rodrigo_ely, edgar_gonzalez]

own_goals = [benjamin_lecomte]
missed_pen = []
pen_save = []

saves_pts_1 = [
    jordi_masip, benjamin_lecomte, predrag_rajkovic, stole_dimitrievski, agustin_marchesin, rui_silva, thibaut_courtois, jeremias_ledesma
]
saves_pts_2 = [
    bono, geronimo_rulli
]
saves_pts_3 = []
saves_pts_4 = []

bonus_1 = [
    valentin_castellanos, javier_hernandez, arnau_martinez, daniel_vivian, david_garcia, frenkie_de_jong, alexander_sorloth, dani_parejo, yeremy_pino, sergi_gomez, brian_olivan, predrag_rajkovic, agustin_marchesin, giorgi_mamardashvili, federico_valverde
]
bonus_2 = [
    aleix_garcia, inigo_lekue, pedri, brais_mendez, alejandro_pozo, srdan_babic, leo_baptistao, raul_albiol, stole_dimitrievski, justin_kluivert, eder_militao
]
bonus_3 = [
    alex_collado, gorka_guruzeta, raphinha, mikel_merino, luis_milla, geronimo_rulli, copete, antoine_griezmann, javi_galan, jose_luis_gaya, toni_kroos
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