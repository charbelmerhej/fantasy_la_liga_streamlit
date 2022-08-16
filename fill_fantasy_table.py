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


# FC Barcelona
marc_andre_ter_stegen = "Ter Stegen"
jordi_alba = "Jordi Alba"
eric_garcia = "Eric Garcia"
andreas_christensen = "Andreas Christensen"
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

# Real Valladolid
sergio_asenjo = "Sergio Asenjo"
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

# Villareal
geronimo_rulli = "Geronimo Rulli"
juan_foyth = "Juan Foyth"
raul_albiol = "Raul Albiol"
pau_torres = "Pau Torres"
aissa_mandi = "Aissa Mandi"
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


mins_pts_2 = [unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, yuri_berchiche, mikel_vesga, iker_munian, inaki_williams, alex_berenguer, # Athletic Club
              jan_oblak, saul_niguez, reinildo, axel_witsel, stefan_savic, nahuel_molina, thomas_lemar, koke, marcos_llorente, joao_felix, alvaro_morata, # Atletico Madrid
              agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan, fran_beltran, franco_cervi, oscar_rodriguez, goncalo_paciencia, iago_aspas, # Celta
              jeremias_ledesma, joseba_zaldua, luis_hernandez, victor_chust, alfonso_espino, fali, jose_mari, santiago_arzamendia, lucas_perez, anthony_lozano, # Cadiz
              edgar_badia, pedro_bigas, helibelton_palacios, omar_mascarell, gerard_gumbau, johan_mojica, pere_milla, roger_marti, # Elche
              benjamin_lecomte, oscar_gil, sergi_gomez, leandro_cabrera, brian_olivan, vinicius_souza, sergi_darder, ruben_sanchez_saez, joselu, # Espanyol
              david_soria, juan_iglesias, djene, stefan_mitrovic, domingos_duarte, fabrizio_angileri, mauro_arambarri, nemanja_maksimovic, borja_mayoral, enes_unal, # Getafe
              juan_carlos, juanpe, david_lopez, santiago_bueno, yan_couto, valery_fernandez, aleix_garcia, ramon_terrats, rodrigo_riquelme, samu_saiz, valentin_castellanos, # Girona
              sergio_herrera, juan_cruz, david_garcia, unai_garcia, ruben_pena, moi_gomez, lucas_torro, jon_moncayola, aimar_oroz, chimy, # Osasuna
              marc_andre_ter_stegen, ronald_araujo, andreas_christensen, eric_garcia, jordi_alba, pedri, sergio_busquets, gavi, ousmane_dembele, robert_lewandowski, raphinha, # FC Barcelona
              predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, dani_rodriguez, rodrigo_battaglia, clement_grenier, kang_in_lee, vedat_muriqi, # Mallorca
              stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, unai_lopez, ismaila_ciss, isi_palazon, oscar_trejo, alvaro_garcia, sergio_camello, # Rayo Vallecano
              rui_silva, aitor_ruibal, german_pezzella, edgar_gonzalez, alex_moreno, guido_rodriguez, william_carvalho, rodri_sanchez, nabil_fekir, juanmi, borja_iglesias, # Real Betis
              alex_remiro, diego_rico, robin_le_normand, igor_zubeldia, aritz_elustondo, martin_zubimendi, mikel_merino, brais_mendez, david_silva, takefusa_kubo, alexander_isak, # Real Sociedad
              thibaut_courtois, lucas_vasquez, antonio_rudiger, nacho_fernandez, ferland_mendy, toni_kroos, federico_valverde, karim_benzema, vinicius_junior, # Real Madrid
              sergio_asenjo, luis_perez, joaquin_fernandez, jawad_el_yamiq, sergio_escudero, monchu, alvaro_aguado, toni_villa, # Real Valladolid
              bono, jesus_navas, nemanja_gudelj, karim_rekik, marcos_acuna, fernando, thomas_delaney, jesus_corona, papu_gomez, lucas_ocampos, rafa_mir, # Sevilla
              fernando_martinez, chumi, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez, inigo_eguaras, samuel_costa, umar_sadiq, largie_ramazani, # Almeria
              giorgi_mamardashvili, thierry_correia, mouctar_diakhaby, jesus_vasquez, yunus_musah, hugo_guillamon, carlos_soler, samu_castillejo, samuel_lino, # Valencia
              geronimo_rulli, juan_foyth, raul_albiol, pau_torres, alfonso_pedraza, yeremy_pino, etienne_capoue, dani_parejo, francis_coquelin, gerard_moreno, nicolas_jackson] # Villareal

mins_pts_1 = [oihan_sancet, asier_villalibre, raul_garcia, oier_zarraga, gorka_guruzeta, nico_williams, malcom_ares, # Athletic Club
              yannick_carrasco, rodrigo_de_paul, angel_correa, antoine_griezmann, matheus_cunha, # Atletico Madrid
              augusto_solari, oscar_mingueza, renato_tapia, gabriel_veiga, carles_perez, # Celta
              awer_mabil, ivan_alejo, alberto_perea, tomas_alarcon, alvaro_negredo, mamady_diarra, # Cadiz
              john_donald, enzo_roco, fidel, diego_gonzalez, tete_morente, josan, alejandro_alfaro, ezequiel_ponce, # Elche
              fernando_calero, nicolas_melamed, adrian_embarba, edu_exposito, luca_koleosho, nabil_touaizi, # Espanyol
              carles_alena, portu, jaime_seoane, moi_parra, jaime_mata, # Getafe
              arnau_martinez, miguel_gutierrez, yangel_herrera, christian_stuani, oscar_urena, # Girona
              kike_barja, pablo_lumbreras, nacho_vidal, manuel_sanchez, darko_brasanac, kike_garcia, # Osasuna
              sergi_roberto, frenkie_de_jong, franck_kessie, ansu_fati, pierre_emerick_aubameyang, # FC Barcelona
              antonio_sanchez, iddrisu_baba, lago_junior, abdon_prats, # Mallorca
              oscar_valentin, salvi, jose_pozo, radamel_falcao, # Rayo Vallecano
              juan_miranda, fran_delgado, paul_akouokou, loren_moron, rober_gonzalez, # Real Betis
              asier_illaramendi, mohamed_ali_cho,ander_barrenetxea, aihen_munoz, jon_karrikaburu, # Real Sociedad
              eduardo_camavinga, aurelien_tchouameni, david_alaba, luka_modric, casemiro, dani_ceballos, eden_hazard, # Real Madrid
              sergio_leon, roque_mesa, gonzalo_plata, lucas_olaza, ivan_sanchez, oscar_plano, kike_perez, sekou_gassama, # Real Valladolid
              alex_telles, erik_lamela, ivan_rakitic, ivan_romero, youssef_ennesyri, # Sevilla
              lucas_robertone, curro, dyego_sousa, jose_carlos_lazo, francisco_portillo, arnau_puigmal, # Almeria
              hugo_duro, eray_comert, dimitri_foulquier, christian_mosquera, toni_lato, nico_gonzalez, maximiliano_gomez, # Valencia
              aissa_mandi, samuel_chukwueze, alejandro_baena, jose_luis_morales] # Villareal

goals = [chimy, aimar_oroz, rafa_mir, iago_aspas, goncalo_paciencia, edu_exposito, joselu, nicolas_jackson, alejandro_baena,
         alejandro_baena, takefusa_kubo, carlos_soler, largie_ramazani, lucas_vasquez, david_alaba, alvaro_morata, alvaro_morata,
         antoine_griezmann, borja_iglesias, juanmi, juanmi]
assists = [ruben_pena, papu_gomez, augusto_solari, javi_galan, samuel_chukwueze, mikel_merino, inigo_eguaras, karim_benzema,
           joao_felix, joao_felix, joao_felix, nabil_fekir]
clean_sheets = [geronimo_rulli, alfonso_pedraza, pau_torres, raul_albiol, juan_foyth, yeremy_pino, etienne_capoue, dani_parejo, francis_coquelin,
                jan_oblak, saul_niguez, reinildo, axel_witsel, stefan_savic, nahuel_molina, thomas_lemar, koke, marcos_llorente,
                alex_remiro, diego_rico, robin_le_normand, igor_zubeldia, aritz_elustondo, martin_zubimendi, mikel_merino, brais_mendez, david_silva, takefusa_kubo,
                rui_silva, aitor_ruibal, german_pezzella, edgar_gonzalez, alex_moreno, guido_rodriguez, william_carvalho, nabil_fekir, juanmi, rodri_sanchez,
                marc_andre_ter_stegen, ronald_araujo, andreas_christensen, eric_garcia, jordi_alba, pedri, gavi, sergio_busquets, raphinha,
                stole_dimitrievski, ivan_balliu, florian_lejeune, alejandro_catena, fran_garcia, ismaila_ciss, unai_lopez, isi_palazon, oscar_trejo, alvaro_garcia,
                giorgi_mamardashvili, thierry_correia, mouctar_diakhaby, jesus_vasquez, yunus_musah, hugo_guillamon, carlos_soler, samu_castillejo,
                predrag_rajkovic, jaume_costa, copete, antonio_raillo, martin_valjent, pablo_maffeo, dani_rodriguez, rodrigo_battaglia, clement_grenier, kang_in_lee,
                unai_simon, oscar_de_marcos, daniel_vivian, yeray_alvarez, yuri_berchiche, mikel_vesga, iker_munian, alex_berenguer]
two_GC = [agustin_marchesin, hugo_mallo, joseph_aidoo, unai_nunez, javi_galan,
          david_soria, juan_iglesias, djene, stefan_mitrovic, domingos_duarte, fabrizio_angileri,
          john_donald, enzo_roco, pedro_bigas, helibelton_palacios, johan_mojica,
          benjamin_lecomte, brian_olivan, leandro_cabrera, sergi_gomez, oscar_gil,
          sergio_asenjo, luis_perez, joaquin_fernandez, jawad_el_yamiq, lucas_olaza,
          fernando_martinez, chumi, kaiky, rodrigo_ely, srdan_babic, sergio_akieme_rodriguez,
          bono, marcos_acuna, karim_rekik, nemanja_gudelj, jesus_navas]
yellow = [david_garcia, unai_garcia, chimy, sergio_herrera, moi_gomez, papu_gomez, fernando, ivan_romero, hugo_mallo, joseph_aidoo,
          vinicius_souza, iago_aspas, oscar_gil, javi_galan, agustin_marchesin, roque_mesa, ousmane_dembele, oscar_trejo,
          alejandro_catena, florian_lejeune, radamel_falcao, ismaila_ciss, stole_dimitrievski, joseba_zaldua, lucas_perez, ivan_alejo, brais_mendez,
          fali, asier_illaramendi, yan_couto, samu_saiz, valery_fernandez, thierry_correia, jesus_vasquez, eduardo_camavinga, umar_sadiq,
          copete, rodrigo_battaglia, dani_rodriguez, antonio_sanchez, kang_in_lee, clement_grenier,
          curro, arnau_puigmal, enes_unal, carles_alena, yannick_carrasco, nabil_fekir, pere_milla, aitor_ruibal, gerard_gumbau,
          fidel, roger_marti, juanmi, josan, johan_mojica]
red = [sergio_busquets, eray_comert, john_donald]
own_goals = []
missed_pen = []
saves_pts_1 = [bono, stole_dimitrievski, thibaut_courtois, edgar_badia]
saves_pts_2 = [geronimo_rulli, jeremias_ledesma, predrag_rajkovic]
saves_pts_3 = []
saves_pts_4 = [fernando_martinez]
pen_save = []
bonus_1 = [dani_parejo, luis_hernandez, aleix_garcia, antoine_griezmann, borja_iglesias]
bonus_2 = [joselu, iago_aspas, alejandro_baena, ousmane_dembele, ismaila_ciss, santiago_bueno, lucas_vasquez, toni_kroos,
           david_alaba, martin_valjent, yuri_berchiche, joao_felix, german_pezzella]
bonus_3 = [chimy, rafa_mir, papu_gomez, edu_exposito, geronimo_rulli, stole_dimitrievski, jeremias_ledesma, mikel_merino,
           carlos_soler, fernando_martinez, predrag_rajkovic, alvaro_morata, juanmi]

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