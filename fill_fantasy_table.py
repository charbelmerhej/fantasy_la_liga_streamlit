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


mins_pts_2 = [unai_simon, oscar_de_marcos, yeray_alvarez, inigo_martinez, inigo_lekue, dani_garcia, oihan_sancet, iker_munian, nico_williams, alex_berenguer, inaki_williams, # Athletic Club
              jan_oblak, nahuel_molina, reinildo, axel_witsel, stefan_savic, jose_maria_gimenez, marcos_llorente, koke, saul_niguez, matheus_cunha, alvaro_morata, # Atletico Madrid
              agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, fran_beltran, gabriel_veiga, oscar_rodriguez, carles_perez, # Celta
              jeremias_ledesma, isaac_carcelen, luis_hernandez, victor_chust, alfonso_espino, ruben_alcaraz, ruben_sobrino, ivan_alejo, # Cadiz
              edgar_badia, pol_lirola, helibelton_palacios, federico_fernandez, diego_gonzalez, carlos_clerc, raul_guti, gerard_gumbau, lucas_boye, roger_marti, # Elche
              alvaro_fernandez, fernando_calero, sergi_gomez, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, edu_exposito, joselu, martin_braithwaite, # Espanyol
              david_soria, damian_suarez, domingos_duarte, djene, gaston_alvarez, juan_iglesias, mauro_arambarri, carles_alena, borja_mayoral, enes_unal, # Getafe
              juan_carlos, juanpe, santiago_bueno, bernardo_espinos, arnau_martinez, miguel_gutierrez, aleix_garcia, oriol_romeu, valentin_castellanos, rodrigo_riquelme, # Girona
              sergio_herrera, juan_cruz, david_garcia, unai_garcia, nacho_vidal, lucas_torro, darko_brasanac, moi_gomez, jon_moncayola, abdessamad_ezzalzouli, kike_garcia, # Osasuna
              marc_andre_ter_stegen, jordi_alba, andreas_christensen, gerard_pique, alejandro_balde, gavi, sergio_busquets, franck_kessie, ansu_fati, ousmane_dembele, robert_lewandowski, # FC Barcelona
              predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, antonio_sanchez, inigo_ruiz_de_galarreta, iddrisu_baba, kang_in_lee, vedat_muriqi, # Mallorca
              stole_dimitrievski, ivan_balliu, alejandro_catena, florian_lejeune, fran_garcia, santi_comesana, oscar_valentin, alvaro_garcia, oscar_trejo, isi_palazon, sergio_camello, # Rayo Vallecano
              rui_silva, martin_montoya, edgar_gonzalez, alex_moreno, paul_akouokou, sergio_canales, rodri_sanchez, # Real Betis
              alex_remiro, aihen_munoz, jon_pacheco, aritz_elustondo, martin_zubimendi, mikel_merino, david_silva, brais_mendez, takefusa_kubo, alexander_sorloth, # Real Sociedad
              andriy_lunin, daniel_carvajal, antonio_rudiger, david_alaba, ferland_mendy, toni_kroos, karim_benzema, rodrygo, vinicius_junior, # Real Madrid
              jordi_masip, ivan_fresneda, javi_sanchez, sergio_escudero, alvaro_aguado, roque_mesa, gonzalo_plata, kike_perez, sergio_leon, oscar_plano, # Real Valladolid
              bono, jose_angel_carmona, tanguy_nianzou, nemanja_gudelj, alex_telles, erik_lamela, isco, oliver_torres, kasper_dolberg, # Sevilla
              fernando_martinez, houboulang_mendes, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, samuel_costa, lucas_robertone, # Almeria
              giorgi_mamardashvili, thierry_correia, gabriel_paulista, mouctar_diakhaby, jose_luis_gaya, ilaix_moriba, hugo_guillamon, andre_almeida, samuel_lino, edinson_cavani, # Valencia
              geronimo_rulli, kiko_femenia, raul_albiol, pau_torres, alfonso_pedraza, etienne_capoue, dani_parejo, francis_coquelin, gio_lo_celso, alejandro_baena, nicolas_jackson,  # Villareal
              ]

mins_pts_1 = [ander_herrera, oier_zarraga, asier_villalibre, mikel_vesga, # Athletic Club
              geoffrey_kondogbia, yannick_carrasco, angel_correa, antoine_griezmann, joao_felix, # Atletico Madrid
              jorgen_larsen, augusto_solari, oscar_mingueza, luca_de_la_torre, renato_tapia, goncalo_paciencia, iago_aspas, # Celta
              fede_san_emeterio, alvaro_negredo, theo_bongonda, joseba_zaldua, alex_fernandez, jose_mari, anthony_lozano, lucas_perez, # Cadiz
              domingos_quina, tete_morente, enzo_roco, pere_milla, ezequiel_ponce, # Elche
              nicolas_melamed, javi_puado, aleix_vidal, keidi_bare, simo, # Espanyol
              angel_algobia, stefan_mitrovic, jaime_seoane, juanmi_latasa, munir_el_haddadi, # Getafe
              valery_fernandez, yangel_herrera, oscar_urena, manu_vallejo, yan_couto, # Girona
              manuel_sanchez, ruben_pena, aimar_oroz, ante_budimir, # Osasuna
              sergi_roberto, pedri, raphinha, ferran_torres, # FC Barcelona
              dani_rodriguez, lago_junior, # Mallorca
              jose_pozo, unai_lopez, ismaila_ciss, salvi, radamel_falcao, # Rayo Vallecano
              luiz_felipe, luiz_henrique, borja_iglesias, william_carvalho, german_pezzella, joaquin, aitor_ruibal, nabil_fekir, willian_jose, # Real Betis
              andoni_gorosabel, alex_sola, benat_turrientes, robert_navarro, # Real Sociedad
              dani_ceballos, aurelien_tchouameni, eder_militao, eduardo_camavinga, federico_valverde, marco_asensio, # Real Madrid
              joaquin_fernandez, jawad_el_yamiq, ivan_sanchez, shon_weissman, # Real Valladolid
              kike_salas, karim_rekik, thomas_delaney, jesus_navas, ivan_rakitic, youssef_ennesyri, papu_gomez, # Sevilla
              francisco_portillo, largie_ramazani, lazaro, inigo_eguaras, adrian_embarba, arnau_puigmal, leo_baptistao, dyego_sousa, # Almeria
              samu_castillejo, eray_comert, justin_kluivert, nico_gonzalez, marcos_andre, hugo_duro, # Valencia
              samuel_chukwueze, arnaut_danjuma, jose_luis_morales  # Villareal
              ]

goals = [inaki_williams, oihan_sancet, nico_williams, mikel_vesga, sergio_leon, borja_mayoral, damian_suarez, sergio_leon,
         oscar_plano, marcos_llorente, alvaro_morata, robert_lewandowski, gabriel_paulista, joselu, sergi_darder, eray_comert,
         gabriel_veiga, alexander_sorloth, rodrigo_riquelme, arnau_martinez, alexander_sorloth, valentin_castellanos, brais_mendez,
         martin_zubimendi, takefusa_kubo, vinicius_junior, kike_garcia, lucas_boye, sergio_camello, unai_lopez]

assists = [nico_williams, oscar_de_marcos, inaki_williams, mauro_arambarri, domingos_duarte, kike_perez, koke, matheus_cunha,
           ansu_fati, jose_luis_gaya, martin_braithwaite, fran_beltran, takefusa_kubo, aleix_garcia, bernardo_espinos,
           martin_zubimendi, manu_vallejo, mikel_merino, alexander_sorloth, david_alaba, unai_garcia, gerard_gumbau, oscar_trejo]

clean_sheets = [
    unai_simon, oscar_de_marcos, inigo_martinez, yeray_alvarez, inigo_lekue, dani_garcia, iker_munian, alex_berenguer, # Athletic Club
    jan_oblak, nahuel_molina, jose_maria_gimenez, stefan_savic, reinildo, axel_witsel, saul_niguez, koke, marcos_llorente, # Atletico Madrid
    jeremias_ledesma, isaac_carcelen, luis_hernandez, victor_chust, alfonso_espino, ruben_alcaraz, ivan_alejo, ruben_sobrino, # Cadiz
    agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, oscar_rodriguez, fran_beltran, gabriel_veiga, # Celta
    marc_andre_ter_stegen, andreas_christensen, gerard_pique, alejandro_balde, jordi_alba, gavi, sergio_busquets, franck_kessie, # FC Barcelona
                # sergio_herrera, nacho_vidal, unai_garcia, david_garcia, juan_cruz, darko_brasanac, lucas_torro, moi_gomez, ruben_garcia, # Osasuna
                # david_soria, juan_iglesias, domingos_duarte, stefan_mitrovic, gaston_alvarez, damian_suarez, carles_alena, nemanja_maksimovic, mauro_arambarri, # Getafe
                # alex_remiro, andoni_gorosabel, robin_le_normand, igor_zubeldia, aihen_munoz, martin_zubimendi, mikel_merino, brais_mendez, david_silva, takefusa_kubo, # Real Sociedad
                # rui_silva, youssouf_sabaly, german_pezzella, luiz_felipe, alex_moreno, guido_rodriguez, william_carvalho, rodri_sanchez, sergio_canales, luiz_henrique, # Real Betis
                # alvaro_fernandez, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, javi_puado, # Espanyol
    # santi_comesana, isi_palazon, oscar_trejo, oscar_valentin, # Rayo Vallecano
                # sergio_asenjo, luis_perez, joaquin_fernandez, javi_sanchez, sergio_escudero, alvaro_aguado, roque_mesa, kike_perez, ivan_sanchez, # Real Valladolid
                # giorgi_mamardashvili, thierry_correia, mouctar_diakhaby, eray_comert, jose_luis_gaya, hugo_guillamon, ilaix_moriba, andre_almeida, samu_castillejo, # Valencia
                # predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, clement_grenier, inigo_ruiz_de_galarreta, kang_in_lee, # Real Mallorca
    geronimo_rulli, alfonso_pedraza, pau_torres, raul_albiol, kiko_femenia, etienne_capoue, dani_parejo, gio_lo_celso, francis_coquelin, alejandro_baena # Villareal
    ]

two_GC = [
          # unai_simon, oscar_de_marcos, yeray_alvarez, inigo_martinez, inigo_lekue, # Athletic Club
          # jeremias_ledesma, joseba_zaldua, luis_hernandez, mamadou_mbaye, alfonso_espino, jeremias_ledesma, joseba_zaldua, luis_hernandez, mamadou_mbaye, alfonso_espino, #Cadiz
          # rui_silva, youssouf_sabaly, luiz_felipe, edgar_gonzalez, alex_moreno, # Real Betis
          # predrag_rajkovic, jaume_costa, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, predrag_rajkovic, jaume_costa, matija_nastasic, antonio_raillo, martin_valjent, pablo_maffeo, # Real Mallorca
          # agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, # Celta
          # jan_oblak, reinildo, felipe, # Atletico Madrid
    edgar_badia, pol_lirola, helibelton_palacios, federico_fernandez, diego_gonzalez, carlos_clerc, # Elche
    alvaro_fernandez, brian_olivan, leandro_cabrera, sergi_gomez, # Espanyol
    david_soria, juan_iglesias, djene, domingos_duarte, gaston_alvarez, damian_suarez, # Getafe
    juan_carlos, santiago_bueno, bernardo_espinos, juanpe, arnau_martinez, miguel_gutierrez, juan_carlos, santiago_bueno, bernardo_espinos, juanpe, arnau_martinez, miguel_gutierrez, # Girona
    fernando_martinez, houboulang_mendes, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, fernando_martinez, houboulang_mendes, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, # Almeria
    alex_remiro, aihen_munoz, jon_pacheco, aritz_elustondo, # Real Sociedad
    jordi_masip, joaquin_fernandez, javi_sanchez, sergio_escudero, # Real Valladolid
          # stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, # Rayo Vallecano
          # sergio_herrera, unai_garcia, david_garcia, juan_cruz, # Osasuna
    bono, jose_angel_carmona, tanguy_nianzou, nemanja_gudelj, alex_telles, # Sevilla
    giorgi_mamardashvili, thierry_correia, mouctar_diakhaby, jose_luis_gaya, # Valencia
]

yellow = [yeray_alvarez, lucas_robertone, kaiky, arnau_puigmal, ruben_alcaraz, geronimo_rulli, francis_coquelin, ivan_alejo,
          alejandro_baena, shon_weissman, kike_perez, joaquin_fernandez, djene, david_soria, alvaro_aguado, jordi_masip,
          isco, thomas_delaney, axel_witsel, nemanja_gudelj, joao_felix, andreas_christensen, gerard_pique, jaume_costa,
          franck_kessie, sergio_busquets, martin_valjent, sergi_darder, brian_olivan, mouctar_diakhaby, gabriel_veiga, jorgen_larsen,
          german_pezzella, javi_galan, sergio_canales, nabil_fekir, oscar_mingueza, oriol_romeu, miguel_gutierrez, mikel_merino,
          valentin_castellanos, dani_ceballos, abdessamad_ezzalzouli, kike_garcia, diego_gonzalez, oscar_trejo,
          domingos_quina, edgar_badia, lucas_boye, pol_lirola, ezequiel_ponce, tete_morente, carlos_clerc]

red = [isaac_carcelen, marcos_andre, martin_braithwaite, luiz_felipe, david_garcia]

own_goals = []
missed_pen = [enes_unal, karim_benzema]
pen_save = [jordi_masip]

saves_pts_1 = [jordi_masip, david_soria, jan_oblak, bono, marc_andre_ter_stegen, alvaro_fernandez, giorgi_mamardashvili, rui_silva, agustin_marchesin, alex_remiro, sergio_herrera, edgar_badia]
saves_pts_2 = [jeremias_ledesma]
saves_pts_3 = []
saves_pts_4 = []

bonus_1 = [
    alfonso_pedraza, damian_suarez, gavi, andreas_christensen, joselu, gabriel_veiga, takefusa_kubo, kike_garcia
]
bonus_2 = [
    nico_williams, mikel_vesga, pau_torres, jordi_masip, alvaro_morata, ivan_rakitic, marc_andre_ter_stegen, jose_luis_gaya, edgar_gonzalez, alexander_sorloth, toni_kroos, oscar_valentin, sergio_camello
]
bonus_3 = [
    inaki_williams, jeremias_ledesma, sergio_leon, marcos_llorente, robert_lewandowski, sergi_darder, agustin_marchesin, martin_zubimendi, vinicius_junior, unai_lopez
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