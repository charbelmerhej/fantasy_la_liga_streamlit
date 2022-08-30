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
fede_san_emeterio = "Fede San Emeterio"
antonio_blanco = "Antonio Blanco"
alex_fernandez = "Alex Fernandez"

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
javi_puado = "Javi Puado"
keidi_bare = "Keidi Bare"
dani_gomez = "Dani Gomez"

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


mins_pts_2 = [unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, inigo_lekue, mikel_vesga, oihan_sancet, iker_munian, alex_berenguer, nico_williams, # Athletic Club
              jan_oblak, reinildo, axel_witsel, jose_maria_gimenez, rodrigo_de_paul, geoffrey_kondogbia, koke, marcos_llorente, joao_felix, alvaro_morata, # Atletico Madrid
              agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, renato_tapia, fran_beltran, franco_cervi, oscar_rodriguez, carles_perez, iago_aspas, # Celta
              jeremias_ledesma, joseba_zaldua, luis_hernandez, alfonso_espino, ivan_alejo, antonio_blanco, santiago_arzamendia, alvaro_negredo, anthony_lozano, # Cadiz
              edgar_badia, enzo_roco, pedro_bigas, tete_morente, omar_mascarell, johan_mojica, alex_collado, ezequiel_ponce, roger_marti, # Elche
              benjamin_lecomte, oscar_gil, fernando_calero, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, edu_exposito, ruben_sanchez_saez, javi_puado, joselu, # Espanyol
              david_soria, juan_iglesias, djene, domingos_duarte, gaston_alvarez, portu, mauro_arambarri, jaime_seoane, carles_alena, borja_mayoral, enes_unal, # Getafe
              juan_carlos, juanpe, santiago_bueno, yan_couto, miguel_gutierrez, aleix_garcia, david_lopez, christian_stuani, valentin_castellanos, # Girona
              sergio_herrera, juan_cruz, david_garcia, unai_garcia, nacho_vidal, ruben_pena, moi_gomez, lucas_torro, jon_moncayola, aimar_oroz, chimy, # Osasuna
              marc_andre_ter_stegen, ronald_araujo, jules_kounde, eric_garcia, alejandro_balde, pedri, sergio_busquets, gavi, ousmane_dembele, robert_lewandowski, raphinha, # FC Barcelona
              predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, dani_rodriguez, rodrigo_battaglia, clement_grenier, kang_in_lee, vedat_muriqi, # Mallorca
              stole_dimitrievski, ivan_balliu, alejandro_catena, fran_garcia, ismaila_ciss, oscar_valentin, alvaro_garcia, radamel_falcao, # Rayo Vallecano
              rui_silva, aitor_ruibal, german_pezzella, edgar_gonzalez, alex_moreno, guido_rodriguez, william_carvalho, nabil_fekir, juanmi, borja_iglesias, # Real Betis
              alex_remiro, aihen_munoz, robin_le_normand, igor_zubeldia, andoni_gorosabel, martin_zubimendi, mikel_merino, brais_mendez, david_silva, takefusa_kubo, mohamed_ali_cho, # Real Sociedad
              thibaut_courtois, lucas_perez, eder_militao, david_alaba, antonio_rudiger, aurelien_tchouameni, toni_kroos, karim_benzema, vinicius_junior, # Real Madrid
              jordi_masip, luis_perez, javi_sanchez, joaquin_fernandez, sergio_escudero, anuar, kike_perez, ivan_sanchez, sergi_guardiola, # Real Valladolid
              bono, jesus_navas, tanguy_nianzou, alex_telles, fernando, erik_lamela, papu_gomez, rafa_mir, # Sevilla
              fernando_martinez, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, samuel_costa, alejandro_pozo, lucas_robertone, umar_sadiq, largie_ramazani, # Almeria
              giorgi_mamardashvili, thierry_correia, eray_comert, mouctar_diakhaby, toni_lato, yunus_musah, hugo_guillamon, carlos_soler, samu_castillejo, samuel_lino, marcos_andre, # Valencia
              geronimo_rulli, raul_albiol, pau_torres, alfonso_pedraza, etienne_capoue, dani_parejo, gio_lo_celso, gerard_moreno] # Villareal

mins_pts_1 = [inaki_williams, gorka_guruzeta, raul_garcia, dani_garcia, jon_morcillo, aitor_casamichana, # Athletic Club
              saul_niguez, yannick_carrasco, thomas_lemar, angel_correa, antoine_griezmann, matheus_cunha, # Atletico Madrid
              gabriel_veiga, goncalo_paciencia, augusto_solari, carlos_dominguez, # Celta
              fali, jose_mari, victor_chust, fede_san_emeterio, awer_mabil, alex_fernandez, lucas_perez, # Cadiz
              helibelton_palacios, pol_lirola, gerard_gumbau, domingos_quina, pere_milla, lucas_boye, raul_guti,  # Elche
              nicolas_melamed, keidi_bare, dani_gomez, # Espanyol
              nemanja_maksimovic, jaime_mata, juanmi_latasa, # Getafe
              samu_saiz, ramon_terrats, javier_hernandez, reinier, joel_roca, yangel_herrera, oscar_urena, # Girona
              manuel_sanchez, ante_budimir, kike_garcia, kike_barja, ruben_garcia, # Osasuna
              frenkie_de_jong, sergi_roberto, franck_kessie, ansu_fati, ferran_torres, # FC Barcelona
              antonio_sanchez, abdon_prats, inigo_ruiz_de_galarreta, javi_llabres, # Mallorca
              salvi, unai_lopez, oscar_trejo, sergio_camello, jose_pozo, randy_nteka, bebe, santi_comesana, # Rayo Vallecano
              sergio_canales, rodri_sanchez, luiz_henrique, luiz_felipe, andres_guardado, # Real Betis
              aritz_elustondo, asier_illaramendi, jon_karrikaburu, ander_barrenetxea, jon_pacheco, # Real Sociedad
              luka_modric, federico_valverde, dani_ceballos, daniel_carvajal, eduardo_camavinga, rodrygo, # Real Madrid
              sergio_leon, toni_villa, alvaro_aguado, roque_mesa, monchu, oscar_plano, # Real Valladolid
              oliver_torres, karim_rekik, joan_jordan, lucas_ocampos, youssef_ennesyri, isco, thomas_delaney, jose_angel_carmona,  # Sevilla
              inigo_eguaras, chumi, houboulang_mendes, curro, cesar_de_la_hoz, leo_baptistao, # Almeria
              dimitri_foulquier, nico_gonzalez, maximiliano_gomez, # Valencia
              yeremy_pino, juan_foyth, jose_luis_morales, francis_coquelin, samuel_chukwueze, alejandro_baena, nicolas_jackson, kiko_femenia] # Villareal

goals = [iago_aspas, borja_iglesias, brais_mendez, vedat_muriqi, kang_in_lee, oliver_torres, largie_ramazani, umar_sadiq,
         robert_lewandowski, pedri, robert_lewandowski, sergi_roberto, vinicius_junior, joselu, karim_benzema, karim_benzema,
         inaki_williams, gorka_guruzeta, alex_berenguer, gorka_guruzeta, antoine_griezmann]

assists = [carles_perez, alex_moreno, martin_zubimendi, dani_rodriguez, alex_telles, alejandro_pozo, raphinha, ousmane_dembele,
           ousmane_dembele, aurelien_tchouameni, rodrygo, inigo_lekue, nico_williams, jon_morcillo, thomas_lemar]

clean_sheets = [# stole_dimitrievski, ivan_balliu, alejandro_catena, fran_garcia, ismaila_ciss, unai_lopez, alvaro_garcia, # Rayo Vallecano
                # sergio_herrera, ruben_pena, unai_garcia, david_garcia, juan_cruz, jon_moncayola, lucas_torro, moi_gomez, aimar_oroz, # Osasuna
                geronimo_rulli, alfonso_pedraza, pau_torres, raul_albiol, etienne_capoue, dani_parejo, gio_lo_celso, # Villareal
                david_soria, juan_iglesias, domingos_duarte, djene, gaston_alvarez, carles_alena, jaime_seoane, mauro_arambarri, portu, # Getafe
                agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, renato_tapia, oscar_rodriguez, fran_beltran, franco_cervi, # Celta
                jan_oblak, jose_maria_gimenez, reinildo, axel_witsel, rodrigo_de_paul, geoffrey_kondogbia, koke, marcos_llorente, # Atletico Madrid
                alex_remiro, andoni_gorosabel, robin_le_normand, igor_zubeldia, aihen_munoz, martin_zubimendi, mikel_merino, brais_mendez, david_silva, takefusa_kubo, # Real Sociedad
                rui_silva, aitor_ruibal, german_pezzella, edgar_gonzalez, alex_moreno, guido_rodriguez, william_carvalho, nabil_fekir, juanmi, # Real Betis
                marc_andre_ter_stegen, ronald_araujo, jules_kounde, eric_garcia, alejandro_balde, pedri, gavi, sergio_busquets, raphinha, # FC Barcelona
                # giorgi_mamardashvili, thierry_correia, mouctar_diakhaby, jesus_vasquez, yunus_musah, hugo_guillamon, carlos_soler, samu_castillejo, # Valencia
                predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, dani_rodriguez, rodrigo_battaglia, clement_grenier, kang_in_lee, # Real Mallorca
                unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, inigo_lekue, mikel_vesga, iker_munian, alex_berenguer] # Athletic Club

two_GC = [benjamin_lecomte, brian_olivan, leandro_cabrera, fernando_calero, oscar_gil, #Espanyol
          jeremias_ledesma, joseba_zaldua, luis_hernandez, victor_chust, alfonso_espino, jeremias_ledesma, joseba_zaldua, luis_hernandez, #Cadiz
          # predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, # Real Mallorca
          # agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, # Celta
          # jan_oblak, reinildo, nahuel_molina, # Atletico Madrid
          # alex_remiro, aihen_munoz, robin_le_normand, igor_zubeldia, aritz_elustondo, # Real Sociedad
          # david_soria, juan_iglesias, djene, stefan_mitrovic, domingos_duarte, fabrizio_angileri, # Getafe
          # fernando_martinez, chumi, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez # Almeria
          jordi_masip, luis_perez, joaquin_fernandez, javi_sanchez, sergio_escudero, jordi_masip, luis_perez, joaquin_fernandez, javi_sanchez, sergio_escudero, # Real Valladolid
          stole_dimitrievski, ivan_balliu, alejandro_catena, fran_garcia, # Rayo Vallecano
          bono, alex_telles, karim_rekik, tanguy_nianzou, jesus_navas, # Sevilla
          # edgar_badia, enzo_roco, pedro_bigas, helibelton_palacios, johan_mojica, # Elche
]

yellow = [david_lopez, juanpe, renato_tapia, aimar_oroz, unai_garcia, david_garcia, gerard_gumbau, tete_morente, mikel_merino,
          igor_zubeldia, johan_mojica, jon_karrikaburu, clement_grenier, oscar_valentin, antonio_sanchez, copete,
          erik_lamela, karim_rekik, inigo_eguaras, rafa_mir, jesus_navas, jose_angel_carmona, kaiky, cesar_de_la_hoz, isco,
          thomas_delaney, alex_telles, leo_baptistao, samuel_costa, djene, dani_parejo, raul_albiol, francis_coquelin, pau_torres,
          alfonso_pedraza, ronald_araujo, javi_sanchez, kike_perez, alfonso_espino, inigo_lekue, ivan_alejo, saul_niguez,
          marcos_andre, reinildo, thierry_correia, joao_felix, eray_comert]

red = [german_pezzella, benjamin_lecomte]

own_goals = []
missed_pen = [mikel_merino, inaki_williams]
pen_save = [edgar_badia, jeremias_ledesma]
saves_pts_1 = [juan_carlos, agustin_marchesin, edgar_badia, alex_remiro, fernando_martinez, bono, jordi_masip, thibaut_courtois, benjamin_lecomte, jeremias_ledesma, unai_simon]
saves_pts_2 = [david_soria, giorgi_mamardashvili]
saves_pts_3 = []
saves_pts_4 = []

bonus_1 = [rui_silva, moi_gomez, alex_collado, pau_torres, geronimo_rulli, robert_lewandowski, vinicius_junior, oscar_de_marcos, jose_maria_gimenez]
bonus_2 = [juan_carlos, unai_nunez, william_carvalho, martin_zubimendi, antonio_raillo, martin_valjent, pablo_maffeo, fernando_martinez, alejandro_pozo, domingos_duarte, ousmane_dembele, joselu, daniel_vivian]
bonus_3 = [david_lopez, edgar_gonzalez, alex_remiro, vedat_muriqi, sergio_akieme_rodriguez, david_soria, raphinha, karim_benzema, gorka_guruzeta, thomas_lemar, giorgi_mamardashvili]

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