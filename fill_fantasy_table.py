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


mins_pts_2 = [unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, yuri_berchiche, mikel_vesga, dani_garcia, oihan_sancet, nico_williams, inaki_williams, gorka_guruzeta, # Athletic Club
              jan_oblak, stefan_savic, jose_maria_gimenez, geoffrey_kondogbia, pablo_barrios, marcos_llorente, antoine_griezmann, alvaro_morata, joao_felix, # Atletico Madrid
              agustin_marchesin, hugo_mallo, oscar_mingueza, joseph_aidoo, unai_nunez, javi_galan, franco_cervi, fran_beltran, gabriel_veiga, iago_aspas, jorgen_larsen, # Celta
              jeremias_ledesma, isaac_carcelen, luis_hernandez, fali, alfonso_espino, ruben_sobrino, ruben_alcaraz, alex_fernandez, brian_ocampo, # Cadiz
              edgar_badia, helibelton_palacios, pedro_bigas, diego_gonzalez, carlos_clerc, omar_mascarell, raul_guti, pere_milla, roger_marti, lucas_boye, # Elche
              alvaro_fernandez, oscar_gil, leandro_cabrera, sergi_gomez, brian_olivan, vinicius_souza, sergi_darder, martin_braithwaite, joselu, # Espanyol
              david_soria, damian_suarez, djene, domingos_duarte, omar_alderete, portu, luis_milla, carles_alena, angel_algobia, borja_mayoral, enes_unal, # Getafe
              paulo_gazzaniga, santiago_bueno, david_lopez, miguel_gutierrez, arnau_martinez, aleix_garcia, oriol_romeu, ivan_martin, yan_couto, rodrigo_riquelme, valentin_castellanos, # Girona
              aitor_fernandez, ruben_pena, david_garcia, unai_garcia, juan_cruz, manuel_sanchez, moi_gomez, lucas_torro, jon_moncayola, chimy, # Osasuna
              marc_andre_ter_stegen, sergi_roberto, andreas_christensen, marcos_alonso, jordi_alba, frenkie_de_jong, pedri, raphinha, robert_lewandowski, ansu_fati, # FC Barcelona
              predrag_rajkovic, jaume_costa, antonio_raillo, franco_russo, copete, pablo_maffeo, iddrisu_baba, kang_in_lee, dani_rodriguez, vedat_muriqi, # Mallorca
              stole_dimitrievski, ivan_balliu, abdul_mumin, florian_lejeune, fran_garcia, ismaila_ciss, santi_comesana, alvaro_garcia, oscar_trejo, isi_palazon, sergio_camello, # Rayo Vallecano
              rui_silva, youssouf_sabaly, luiz_felipe, felix_marti, alex_moreno, william_carvalho, andres_guardado, luiz_henrique, sergio_canales, nabil_fekir, borja_iglesias, # Real Betis
              alex_remiro, aritz_elustondo, robin_le_normand, igor_zubeldia, diego_rico, martin_zubimendi, brais_mendez, david_silva, takefusa_kubo, alexander_sorloth, mohamed_ali_cho, # Real Sociedad
              thibaut_courtois, antonio_rudiger, david_alaba, ferland_mendy, dani_ceballos, toni_kroos, federico_valverde, marco_asensio, karim_benzema, vinicius_junior, # Real Madrid
              jordi_masip, ivan_fresneda, joaquin_fernandez, javi_sanchez, roque_mesa, alvaro_aguado, monchu, oscar_plano, sergio_leon, # Real Valladolid
              bono, jesus_navas, jose_angel_carmona, nemanja_gudelj, kike_salas, marcos_acuna, joan_jordan, fernando, oliver_torres, rafa_mir, # Sevilla
              fernando_martinez, alejandro_pozo, chumi, srdan_babic, sergio_akieme_rodriguez, cesar_de_la_hoz, lucas_robertone, gonzalo_melero, leo_baptistao, largie_ramazani, el_bilal_toure, # Almeria
              giorgi_mamardashvili, thierry_correia, eray_comert, mouctar_diakhaby, jose_luis_gaya, nico_gonzalez, andre_almeida, samuel_lino, edinson_cavani, samu_castillejo, # Valencia
              pepe_reina, raul_albiol, pau_torres, alberto_moreno, dani_parejo, etienne_capoue, alejandro_baena, samuel_chukwueze, gerard_moreno, yeremy_pino,  # Villareal
              ]

mins_pts_1 = [alex_berenguer, iker_munian, oier_zarraga, raul_garcia, # Athletic Club
              yannick_carrasco, mario_hermoso, saul_niguez, thomas_lemar, sergio_reguilon, koke, # Atletico Madrid
              oscar_rodriguez, kevin_vasquez, luca_de_la_torre, carles_perez, # Celta
              theo_bongonda, alvaro_negredo, fede_san_emeterio, lucas_perez, jose_mari, anthony_lozano, # Cadiz
              gonzalo_verdu, tete_morente, alex_collado, fidel, domingos_quina, ezequiel_ponce, # Elche
              fernando_calero, aleix_vidal, nicolas_melamed, ruben_sanchez_saez, edu_exposito, javi_puado, # Espanyol
              juan_iglesias, stefan_mitrovic, juanmi_latasa, munir_el_haddadi, jaime_seoane, # Getafe
              toni_villa, valery_fernandez, christian_stuani, samu_saiz, # Girona
              aimar_oroz, darko_brasanac, ruben_garcia, kike_garcia, abdessamad_ezzalzouli, kike_barja, # Osasuna
              jules_kounde, gavi, alejandro_balde, sergio_busquets, ousmane_dembele, ferran_torres, # FC Barcelona
              rodrigo_battaglia, matija_nastasic, antonio_sanchez, angel_rodriguez, tino_kadewere, amath_ndiaye, # Mallorca
              unai_lopez, radamel_falcao, # Rayo Vallecano
              aitor_ruibal, joaquin, juanmi, willian_jose, # Real Betis
              andoni_gorosabel, asier_illaramendi, mikel_oyarzabal, robert_navarro, # Real Sociedad
              daniel_carvajal, lucas_vasquez, eduardo_camavinga, aurelien_tchouameni, luka_modric, rodrygo, # Real Madrid
              ivan_sanchez, sergio_escudero, luis_perez, gonzalo_plata, kenedy, kike_perez, shon_weissman, # Real Valladolid
              erik_lamela, suso, youssef_ennesyri, # Sevilla
              adrian_embarba, samuel_costa, arnau_puigmal, inigo_eguaras, dyego_sousa, # Almeria
              yunus_musah, ilaix_moriba, justin_kluivert, hugo_guillamon, hugo_duro, # Valencia
              kiko_femenia, juan_foyth, alfonso_pedraza, manu_trigueros, jose_luis_morales, nicolas_jackson, # Villareal
              ]

goals = [sergio_camello, isi_palazon, valentin_castellanos, samu_saiz, joao_felix, alvaro_morata, borja_mayoral, borja_mayoral,
         gonzalo_melero, lucas_perez, gabriel_veiga, kike_salas, karim_benzema, karim_benzema, marcos_alonso, joselu,
         brais_mendez, alexander_sorloth, edinson_cavani, samuel_chukwueze, juan_foyth]

assists = [sergio_camello, antoine_griezmann, antoine_griezmann, enes_unal, iago_aspas, joan_jordan, eduardo_camavinga,
           andreas_christensen, brais_mendez, gerard_moreno, dani_parejo]

clean_sheets = [
    gonzalo_melero, lucas_robertone, # Part of Almeria
    raphinha, # Part of Barca
    unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, yuri_berchiche, oihan_sancet, mikel_vesga, dani_garcia, # Athletic Club
    jan_oblak, stefan_savic, jose_maria_gimenez, geoffrey_kondogbia, pablo_barrios, marcos_llorente, # Atletico Madrid
    # jeremias_ledesma, luis_hernandez, alfonso_espino, fede_san_emeterio, theo_bongonda, alex_fernandez, brian_ocampo, # Cadiz
    # agustin_marchesin, kevin_vasquez, joseph_aidoo, unai_nunez, oscar_mingueza, javi_galan, renato_tapia, gabriel_veiga, franco_cervi, # Celta
    # marc_andre_ter_stegen, alejandro_balde, gerard_pique, marcos_alonso, jordi_alba, sergio_busquets, frenkie_de_jong, pedri,  # FC Barcelona
    # aitor_fernandez, manuel_sanchez, david_garcia, unai_garcia, ruben_pena, lucas_torro, aimar_oroz, moi_gomez, kike_barja,  # Osasuna
    david_soria, portu, damian_suarez, djene, domingos_duarte, omar_alderete, luis_milla, carles_alena, angel_algobia, # Getafe
    # benjamin_lecomte, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, # Espanyol
    alex_remiro, aritz_elustondo, igor_zubeldia, robin_le_normand, diego_rico, david_silva, martin_zubimendi, brais_mendez, takefusa_kubo, # Real Sociedad
    rui_silva, youssouf_sabaly, luiz_felipe, felix_marti, alex_moreno, william_carvalho, andres_guardado, nabil_fekir, sergio_canales, # Real Betis
                # alvaro_fernandez, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, javi_puado, # Espanyol
    # stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, oscar_valentin, santi_comesana, unai_lopez, alvaro_garcia, # Rayo Vallecano
    # jordi_masip, lucas_rosa, jawad_el_yamiq, joaquin_fernandez, javi_sanchez, sergio_escudero, monchu, # Real Valladolid
    # giorgi_mamardashvili, thierry_correia, cenk_ozkacar, eray_comert, jose_luis_gaya, nico_gonzalez, yunus_musah, andre_almeida, samu_castillejo, samuel_lino, # Valencia
    # fernando_martinez, alejandro_pozo, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, cesar_de_la_hoz, leo_baptistao, lucas_robertone, gonzalo_melero, adrian_embarba, # Almeria
    thibaut_courtois, ferland_mendy, antonio_rudiger, david_alaba, dani_ceballos, toni_kroos, federico_valverde, marco_asensio, # Real Madrid
    # predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, giovanni_gonzalez, inigo_ruiz_de_galarreta, kang_in_lee, antonio_sanchez, # Real Mallorca
    # bono, gonzalo_montiel, tanguy_nianzou, marcao, alex_telles, ivan_rakitic, nemanja_gudelj, oliver_torres, isco, erik_lamela, # Sevilla
    # geronimo_rulli, kiko_femenia, raul_albiol, alberto_moreno, dani_parejo, etienne_capoue, samuel_chukwueze, manu_trigueros, yeremy_pino,  # Villareal
]

two_GC = [
    # unai_simon, oscar_de_marcos, inigo_martinez, yeray_alvarez, mikel_balenziaga, # Athletic Club
    # jeremias_ledesma, isaac_carcelen, fali, alfonso_espino, #Cadiz
    # rui_silva, youssouf_sabaly, victor_ruiz, edgar_gonzalez, alex_moreno, # Real Betis
    predrag_rajkovic, jaume_costa, antonio_raillo, pablo_maffeo, # Real Mallorca
    # agustin_marchesin, unai_nunez, joseph_aidoo, oscar_mingueza, javi_galan, # Celta
    # jan_oblak, reinildo, axel_witsel, stefan_savic, nahuel_molina, # Atletico Madrid
    # marc_andre_ter_stegen, sergi_roberto, jules_kounde, eric_garcia, alejandro_balde, # FC Barcelona
    edgar_badia, helibelton_palacios, diego_gonzalez, gonzalo_verdu, pedro_bigas, carlos_clerc, # Elche
    # benjamin_lecomte, brian_olivan, leandro_cabrera, sergi_gomez, # Espanyol
    # david_soria, juan_iglesias, djene, domingos_duarte, stefan_mitrovic, damian_suarez, # Getafe
    paulo_gazzaniga, arnau_martinez, santiago_bueno, david_lopez, miguel_gutierrez, # Girona
    # fernando_martinez, houboulang_mendes, rodrigo_ely, chumi, sergio_akieme_rodriguez, # Almeria
    # thibaut_courtois, daniel_carvajal, eder_militao, david_alaba, ferland_mendy, # Read Madrid
    # alex_remiro, andoni_gorosabel, jon_pacheco, diego_rico, # Real Sociedad
    jordi_masip, javi_sanchez, joaquin_fernandez, ivan_fresneda, # Real Valladolid
    stole_dimitrievski, ivan_balliu, florian_lejeune, abdul_mumin, fran_garcia, # Rayo Vallecano
    aitor_fernandez, unai_garcia, david_garcia, juan_cruz, ruben_pena, manuel_sanchez, # Osasuna
    # bono, jesus_navas, tanguy_nianzou, karim_rekik, alex_telles, # Sevilla
    giorgi_mamardashvili, thierry_correia, eray_comert, mouctar_diakhaby, jose_luis_gaya, # Valencia
    # geronimo_rulli, kiko_femenia, raul_albiol, pau_torres, alberto_moreno, # Villareal
]

yellow = [arnau_martinez, isi_palazon, oriol_romeu, christian_stuani, radamel_falcao, mikel_vesga, oier_zarraga, yuri_berchiche,
          joaquin, daniel_vivian, roger_marti, pablo_barrios, alex_collado, vedat_muriqi, fali, jose_mari, fran_beltran,
          joan_jordan, hugo_mallo, erik_lamela, javi_sanchez, joaquin_fernandez, ansu_fati, gavi, brian_olivan, leandro_cabrera,
          vinicius_souza, edu_exposito, ferran_torres, pedri, joselu, javi_puado, unai_garcia, brais_mendez, edinson_cavani,
          yunus_musah, eray_comert, ilaix_moriba, juan_foyth]

red = [luiz_felipe, gonzalo_verdu, mario_hermoso, domingos_quina, jose_angel_carmona, sergio_leon, jordi_alba, vinicius_souza]

own_goals = []
missed_pen = []
pen_save = []

saves_pts_1 = [
    stole_dimitrievski, unai_simon, predrag_rajkovic, fernando_martinez, agustin_marchesin, bono, jordi_masip,
    thibaut_courtois, alvaro_fernandez, alex_remiro, pepe_reina
]
saves_pts_2 = [
    giorgi_mamardashvili
]
saves_pts_3 = [jeremias_ledesma]
saves_pts_4 = []

bonus_1 = [
    oriol_romeu, ivan_martin, valentin_castellanos, samu_saiz, oscar_de_marcos, joao_felix, enes_unal, lucas_perez, joan_jordan, toni_kroos, raphinha, igor_zubeldia, giorgi_mamardashvili
]
bonus_2 = [
    isi_palazon, luiz_felipe, antonio_raillo, gonzalo_melero, iago_aspas, thibaut_courtois, robin_le_normand, dani_parejo
]
bonus_3 = [
    sergio_camello, unai_simon, alvaro_morata, antoine_griezmann, borja_mayoral, jeremias_ledesma, kike_salas, karim_benzema, andreas_christensen, joselu, brais_mendez, pau_torres
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