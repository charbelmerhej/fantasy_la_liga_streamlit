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
luiz_felipe = "Luiz Felipe"
andres_guardado = "Andres Guardado"
luiz_henrique = "Luiz Henrique"
youssouf_sabaly = "Youssouf Sabaly"
joaquin = "Joaquin"
willian_jose = "Willian Jose"

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
marco_asensio = "Marco Asensio"
rodrygo = "Rodrygo"

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
inigo_ruiz_de_galarreta = "Inigo Ruiz de Galarreta"
javi_llabres = "Javi Llabres"


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
el_bilal_toure = "El Bilal Toure"
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


mins_pts_2 = [unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, inigo_lekue, mikel_vesga, oihan_sancet, iker_munian, alex_berenguer, inaki_williams, # Athletic Club
              jan_oblak, reinildo, axel_witsel, jose_maria_gimenez, rodrigo_de_paul, koke, marcos_llorente, yannick_carrasco, joao_felix, alvaro_morata, # Atletico Madrid
              agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, fran_beltran, franco_cervi, oscar_rodriguez, iago_aspas, # Celta
              jeremias_ledesma, joseba_zaldua, luis_hernandez, victor_chust, alfonso_espino, fede_san_emeterio, ivan_alejo, antonio_blanco, tomas_alarcon, brian_ocampo, anthony_lozano, # Cadiz
              edgar_badia, enzo_roco, pedro_bigas, carlos_clerc, tete_morente, omar_mascarell, helibelton_palacios, alex_collado, # Elche
              alvaro_fernandez, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, javi_puado, joselu, martin_braithwaite, # Espanyol
              david_soria, juan_iglesias, domingos_duarte, fabrizio_angileri, mauro_arambarri, borja_mayoral, enes_unal, # Getafe
              juan_carlos, juanpe, santiago_bueno, arnau_martinez, miguel_gutierrez, aleix_garcia, david_lopez, oriol_romeu, christian_stuani, valentin_castellanos, reinier, # Girona
              sergio_herrera, juan_cruz, david_garcia, unai_garcia, nacho_vidal, moi_gomez, ante_budimir, jon_moncayola, aimar_oroz, chimy, # Osasuna
              marc_andre_ter_stegen, ronald_araujo, jules_kounde, alejandro_balde, pedri, sergio_busquets, gavi, ousmane_dembele, robert_lewandowski, raphinha, # FC Barcelona
              predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, dani_rodriguez, rodrigo_battaglia, antonio_sanchez, kang_in_lee, vedat_muriqi, # Mallorca
              stole_dimitrievski, ivan_balliu, alejandro_catena, florian_lejeune, fran_garcia, ismaila_ciss, oscar_valentin, alvaro_garcia, oscar_trejo, sergio_camello, # Rayo Vallecano
              rui_silva, youssouf_sabaly, luiz_felipe, edgar_gonzalez, alex_moreno, guido_rodriguez, andres_guardado, sergio_canales, juanmi, borja_iglesias, # Real Betis
              alex_remiro, aihen_munoz, robin_le_normand, igor_zubeldia, andoni_gorosabel, martin_zubimendi, mikel_merino, brais_mendez, david_silva, mohamed_ali_cho, # Real Sociedad
              thibaut_courtois, daniel_carvajal, eder_militao, david_alaba, ferland_mendy, aurelien_tchouameni, luka_modric, eduardo_camavinga, rodrygo, karim_benzema, vinicius_junior, # Real Madrid
              sergio_asenjo, luis_perez, javi_sanchez, joaquin_fernandez, sergio_escudero, alvaro_aguado, kike_perez, roque_mesa, ivan_sanchez, sergi_guardiola, # Real Valladolid
              bono, gonzalo_montiel, tanguy_nianzou, marcos_acuna, fernando, ivan_rakitic, erik_lamela, isco, # Sevilla
              fernando_martinez, cesar_de_la_hoz, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, samuel_costa, alejandro_pozo, lucas_robertone, leo_baptistao, largie_ramazani, # Almeria
              giorgi_mamardashvili, thierry_correia, eray_comert, mouctar_diakhaby, toni_lato, yunus_musah, hugo_guillamon, nico_gonzalez, samu_castillejo, samuel_lino, # Valencia
              geronimo_rulli, kiko_femenia, raul_albiol, pau_torres, alfonso_pedraza, yeremy_pino, etienne_capoue, dani_parejo, gio_lo_celso, gerard_moreno] # Villareal

mins_pts_1 = [nico_williams, gorka_guruzeta, raul_garcia, unai_vencedor, jon_morcillo, # Athletic Club
              saul_niguez, geoffrey_kondogbia, mario_hermoso, ivo_grbic, angel_correa, antoine_griezmann, # Atletico Madrid
              gabriel_veiga, oscar_mingueza, luca_de_la_torre, augusto_solari, jorgen_larsen, renato_tapia, carles_perez, # Celta
              alex_fernandez, lucas_perez, ruben_sobrino, theo_bongonda, alvaro_gimenez, # Cadiz
              raul_guti, ezequiel_ponce, lucas_boye, josan, gerard_gumbau, domingos_quina, pere_milla, roger_marti,  # Elche
              edu_exposito, jose_carlos_lazo, keidi_bare, dani_gomez, omar_el_hilali, simo, # Espanyol
              djene, carles_alena, jaime_seoane, portu, nemanja_maksimovic, jaime_mata, gaston_alvarez, stefan_mitrovic, munir_el_haddadi, # Getafe
              samu_saiz, javier_hernandez, toni_villa, bernardo_espinos, manu_vallejo, # Girona
              lucas_torro, pablo_lumbreras, darko_brasanac, kike_garcia, abdessamad_ezzalzouli, ruben_garcia, # Osasuna
              eric_garcia, jordi_alba, frenkie_de_jong, sergi_roberto, ansu_fati, ferran_torres, # FC Barcelona
              clement_grenier, abdon_prats, inigo_ruiz_de_galarreta, # Mallorca
              salvi, isi_palazon, radamel_falcao, santi_comesana, # Rayo Vallecano
              luiz_henrique, aitor_ruibal, joaquin, willian_jose, nabil_fekir, # Real Betis
              aritz_elustondo, umar_sadiq, ander_barrenetxea, takefusa_kubo, alex_sola, alexander_sorloth, # Real Sociedad
              toni_kroos, federico_valverde, dani_ceballos, antonio_rudiger, # Real Madrid
              sergio_leon, gonzalo_plata, monchu, oscar_plano, shon_weissman, # Real Valladolid
              nemanja_gudelj, joan_jordan, youssef_ennesyri, papu_gomez, thomas_delaney, jose_angel_carmona, suso, kasper_dolberg,  # Sevilla
              kaiky, adrian_embarba, francisco_portillo, dyego_sousa, marko_milovanovic, # Almeria
              marcos_andre, dimitri_foulquier, christian_mosquera, hugo_duro, andre_almeida, ilaix_moriba, # Valencia
              jose_luis_morales, francis_coquelin, samuel_chukwueze, alejandro_baena, nicolas_jackson, aissa_mandi] # Villareal

goals = [iago_aspas, oscar_rodriguez, iago_aspas, antonio_raillo, samu_saiz, vinicius_junior, sergio_canales, rodrygo,
         alvaro_morata, umar_sadiq, raphinha, robert_lewandowski, eric_garcia, aimar_oroz, florian_lejeune, ruben_garcia,
         martin_braithwaite, gerard_moreno, gio_lo_celso, francis_coquelin, jose_luis_morales, toni_lato, samuel_lino, samu_castillejo,
         nico_gonzalez, hugo_duro, gaston_alvarez, shon_weissman]

assists = [gabriel_veiga, jorgen_larsen, franco_cervi, kang_in_lee, david_alaba, borja_iglesias, federico_valverde, mohamed_ali_cho,
           jules_kounde, jules_kounde, darko_brasanac, abdessamad_ezzalzouli, nicolas_jackson, hugo_guillamon, yunus_musah,
           hugo_guillamon, yunus_musah]

clean_sheets = [# stole_dimitrievski, ivan_balliu, alejandro_catena, fran_garcia, ismaila_ciss, unai_lopez, alvaro_garcia, # Rayo Vallecano
                # sergio_herrera, ruben_pena, unai_garcia, david_garcia, juan_cruz, jon_moncayola, lucas_torro, moi_gomez, aimar_oroz, # Osasuna
                geronimo_rulli, alfonso_pedraza, pau_torres, raul_albiol, kiko_femenia, etienne_capoue, dani_parejo, gio_lo_celso, yeremy_pino, # Villareal
                # david_soria, juan_iglesias, domingos_duarte, djene, gaston_alvarez, carles_alena, jaime_seoane, mauro_arambarri, portu, # Getafe
                agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, oscar_rodriguez, fran_beltran, franco_cervi, # Celta
                # jan_oblak, jose_maria_gimenez, reinildo, axel_witsel, rodrigo_de_paul, geoffrey_kondogbia, koke, marcos_llorente, # Atletico Madrid
                # alex_remiro, andoni_gorosabel, robin_le_normand, igor_zubeldia, aihen_munoz, martin_zubimendi, mikel_merino, brais_mendez, david_silva, takefusa_kubo, # Real Sociedad
                # rui_silva, aitor_ruibal, german_pezzella, edgar_gonzalez, alex_moreno, guido_rodriguez, william_carvalho, nabil_fekir, juanmi, # Real Betis
                marc_andre_ter_stegen, ronald_araujo, jules_kounde, alejandro_balde, pedri, gavi, sergio_busquets, raphinha, # FC Barcelona
                alvaro_fernandez, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, javi_puado, # Espanyol
                sergio_asenjo, luis_perez, joaquin_fernandez, javi_sanchez, sergio_escudero, alvaro_aguado, roque_mesa, kike_perez, ivan_sanchez, # Real Valladolid
                # giorgi_mamardashvili, thierry_correia, mouctar_diakhaby, jesus_vasquez, yunus_musah, hugo_guillamon, carlos_soler, samu_castillejo, # Valencia
                # predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, dani_rodriguez, rodrigo_battaglia, clement_grenier, kang_in_lee, # Real Mallorca
                # unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, inigo_lekue, mikel_vesga, iker_munian, alex_berenguer # Athletic Club
    ]

two_GC = [# benjamin_lecomte, brian_olivan, leandro_cabrera, fernando_calero, oscar_gil, #Espanyol
          jeremias_ledesma, joseba_zaldua, luis_hernandez, victor_chust, alfonso_espino, #Cadiz
          rui_silva, youssouf_sabaly, luiz_felipe, edgar_gonzalez, alex_moreno, # Real Betis
          # predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, # Real Mallorca
          # agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, # Celta
          # jan_oblak, reinildo, nahuel_molina, # Atletico Madrid
          # alex_remiro, aihen_munoz, robin_le_normand, igor_zubeldia, aritz_elustondo, # Real Sociedad
          david_soria, juan_iglesias, djene, domingos_duarte, fabrizio_angileri, david_soria, juan_iglesias, domingos_duarte, fabrizio_angileri, # Getafe
          # fernando_martinez, chumi, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez # Almeria
          # jordi_masip, luis_perez, joaquin_fernandez, javi_sanchez, sergio_escudero, # Real Valladolid
          stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, # Rayo Vallecano
          bono, marcos_acuna, tanguy_nianzou, gonzalo_montiel, # Sevilla
          edgar_badia, enzo_roco, pedro_bigas, helibelton_palacios, carlos_clerc, edgar_badia, enzo_roco, pedro_bigas, helibelton_palacios, carlos_clerc, # Elche
]

yellow = [anthony_lozano, jorgen_larsen, joseba_zaldua, rodrigo_battaglia, valentin_castellanos, vedat_muriqi, oriol_romeu,
          antonio_sanchez, copete, edgar_gonzalez, saul_niguez, rodrigo_de_paul, martin_zubimendi, mohamed_ali_cho, marcos_llorente,
          igor_zubeldia, alvaro_morata, andoni_gorosabel, mikel_merino, ousmane_dembele, alejandro_balde, joan_jordan,
          jose_angel_carmona, ronald_araujo, sergi_roberto, juan_cruz, ismaila_ciss, alvaro_garcia, unai_garcia, leandro_cabrera,
          oihan_sancet, oscar_de_marcos, dani_gomez, unai_vencedor, nicolas_jackson, raul_guti, pere_milla, enzo_roco,
          carles_alena, samu_castillejo, borja_mayoral, munir_el_haddadi, stefan_mitrovic, sergio_akieme_rodriguez,
          cesar_de_la_hoz, adrian_embarba, kaiky, javi_sanchez, samuel_costa, marko_milovanovic]

red = [ilaix_moriba, mauro_arambarri]

own_goals = []
missed_pen = []
pen_save = []

saves_pts_1 = [predrag_rajkovic, juan_carlos, thibaut_courtois, jan_oblak, marc_andre_ter_stegen, stole_dimitrievski, alvaro_fernandez, giorgi_mamardashvili, david_soria, fernando_martinez]
saves_pts_2 = [alex_remiro, edgar_badia]
saves_pts_3 = []
saves_pts_4 = []

bonus_1 = [joseph_aidoo, aleix_garcia, luka_modric, rodrygo, jose_maria_gimenez, marcos_llorente, marc_andre_ter_stegen, alvaro_fernandez, oscar_gil, pau_torres, alfonso_pedraza, luis_perez, monchu]
bonus_2 = [oscar_rodriguez, antonio_raillo, alvaro_morata, moi_gomez, alejandro_catena, alex_berenguer, francis_coquelin, hugo_guillamon, toni_lato, kike_perez]
bonus_3 = [iago_aspas, kang_in_lee, aurelien_tchouameni, sergio_canales, mohamed_ali_cho, jules_kounde, raphinha, florian_lejeune, sergi_darder, raul_albiol, yunus_musah, joaquin_fernandez]

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