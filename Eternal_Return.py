locais = ('Docas', 'Lagoa', 'Praia', 'Bairro Nobre', 'Beco', 'Hotel', 'Avenida', 'Hospital', 'Templo', 'Stand',
          'Cemitério', 'Floresta', 'Fabrica', 'Capela', 'Escola')

(docas, lagoa, praia, bairro_nobre, beco, hotel, avenida, hospital, templo, stand, cemiterio, floresta, fabrica, capela,
 escola) = locais

# ----------------------------------------------------- Caixas ------------------------------------------------------ #

caixa_verde = 'Caixa Verde'
caixa_azul = 'Caixa Azul'
caixa_roxa = 'Caixa Roxa'
caixa_lendaria = 'Caixa Lendária'

# ------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------------ Mobs ------------------------------------------------------- #

lobo = 'Lobo'
urso = 'Urso'
morcego = 'Morcego'
galinha = 'Galinha'
cachorro_selvagem = 'Cachorro Selvagem'
wickeline = 'Wickeline'

# ------------------------------------------------------------------------------------------------------------------- #

# ---------------------------------------------------- Naturais ----------------------------------------------------- #

agua = 'Água'
galho = 'Galho'
pedra = 'Pedra'
couro = (galinha, morcego, cachorro_selvagem, lobo, urso)
papel = (templo, stand, capela)
minerio_de_ferro = (hotel, cemiterio, floresta)
garrafa_de_vidro = (docas, avenida, capela)
prego = (avenida, stand, fabrica)
casco_de_tartaruga = (docas, lagoa, praia)
borracha = (docas, beco, stand)
sucata_de_metal = (docas, hotel, hospital, fabrica)
isqueiro = (docas, beco, fabrica, escola)
ponteiro_laser = (bairro_nobre, hospital, escola)
medalha_do_garanhao = (praia, beco, templo)
bateria = (docas, avenida, fabrica)
alcool = (hospital, fabrica, escola)
oleo = (bairro_nobre, avenida, stand, fabrica)
tecido = (hotel, avenida, templo)
pedra_preciosa = (lagoa, praia, templo, floresta)
cola = (beco, hospital, fabrica)
lata = (praia, avenida, escola)
polvora = (templo, stand, cemiterio)
meteorito = (caixa_verde, lobo, urso)
arvore_da_vida = (hotel, floresta, cemiterio)
po_da_vida = (arvore_da_vida, pedra)
mithril = (lobo, urso, wickeline, caixa_azul)
amostra_de_sangue_fv = (urso, wickeline, caixa_azul)
nucleo_da_forca = (po_da_vida, meteorito)

# ------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------- Itens Primários ------------------------------------------------- #

soco_ingles = [cemiterio, floresta]
agulha = [beco, hotel, hospital]
luva_de_algodao = [hotel, hospital]
bambu = [lagoa, templo, stand, cemiterio, floresta]
barra_curta = [docas, lagoa, templo]
chicote = [capela, escola]
bola_de_ferro = [stand, floresta, fabrica]
navalha = [hospital, capela, escola]
baralho = [hotel, avenida]
giz_branco = [fabrica, capela, escola]
arco = [stand, capela]
besta_curta = [floresta, fabrica]
walther_ppk = [praia, hotel, fabrica]
fedorova = [hotel, fabrica]
rifle_de_canolongo = [docas, floresta]
marreta = [lagoa, praia, beco]
picareta = [lagoa, praia, cemiterio, floresta]
machadinha = [lagoa, praia, fabrica]
tesoura = [beco, hospital, escola]
caneta_tinteiro = [bairro_nobre, avenida, escola]
faca_de_cozinha = [docas, hotel, templo]
espada_enferrujada = [docas, templo, capela]
lanca_curta = [lagoa, templo, floresta]
corrente_de_aco = [praia, beco, cemiterio]
diadema = [avenida, templo, cemiterio]
bone = [lagoa, stand, escola]
capacete_de_bicicleta = [praia, capela, escola]
jaqueta_corta_vento = [bairro_nobre, hotel, escola]
tunica_de_monge = [templo, stand]
maio = [docas, praia, beco]
armadura_de_tecido = [templo, stand, cemiterio]
relogio = [bairro_nobre, hotel, avenida]
ataduras = [docas, hospital, fabrica, escola]
bracelete = [lagoa, bairro_nobre, beco]
pantufa = [avenida, hospital, escola]
tenis_de_corrida = [bairro_nobre, beco, stand]
meia_calca = [avenida, hospital, floresta]
pena = [hospital, cemiterio, floresta]
flor = [lagoa, bairro_nobre, cemiterio, floresta]
laco = [lagoa, bairro_nobre, escola]
leque = [avenida, floresta, capela]
escrita_budista = [templo]
caixa = [docas, lagoa, capela]
calice_sagrado = [capela]
cruz = [beco, capela]
binoculos = [praia, beco, hotel, fabrica]
camera_de_seguranca = [docas, praia, bairro_nobre, avenida, hospital, stand, cemiterio, escola]
armadilha_de_laco = [docas, lagoa, praia, stand, floresta, capela]
ratoeira = [lagoa, praia, cemiterio]
corda_de_piano = [praia, bairro_nobre, hotel, capela]
laranja = [bairro_nobre, hotel, hospital]
alho = [beco, templo, cemiterio]
bandaid = [hospital]
pao = [docas, capela, escola]
ovo = [stand, cemiterio, floresta]
macarrao_instantaneo = [docas, beco, stand]
erva_oriental = [lagoa, templo, floresta]
chocolate = [bairro_nobre, avenida, stand]
po_de_curry = [bairro_nobre, fabrica]
mel = [beco, avenida, floresta]
gelo = [hotel, hospital, cemiterio]
uisque = [bairro_nobre, hotel, capela]
cafe = [docas, bairro_nobre, cemiterio]
agua_com_gas = [praia, bairro_nobre, hotel]
leite = [avenida, hospital, capela]

# ------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------ Itens Secundários ------------------------------------------------ #

foice_com_corrente = (picareta, corrente_de_aco)
machado_de_batalha = (machadinha, bambu)
canivete = (faca_de_cozinha, galho)
shamshir = (espada_enferrujada, isqueiro)
espadas_duplas = (faca_de_cozinha, espada_enferrujada)
mascara = (diadema, pena)
diadema2 = (diadema, galho)
boina = (bone, tesoura)
capuz_de_cota_de_malha = (bone, corrente_de_aco)
capacete_de_seguranca = (capacete_de_bicicleta, pedra)
armadura_de_couro = (armadura_de_tecido, couro)
jaqueta_de_couro = (jaqueta_corta_vento, couro)
dobok_de_tartaruga = (tunica_de_monge, casco_de_tartaruga)
traje_militar = (jaqueta_corta_vento, galho)
manto_remendado = (tunica_de_monge, ataduras)
vestido = (tecido, tesoura)
biquini = (maio, tesoura)
traje_de_mergulho = (maio, borracha)
escudo_de_couro = (casco_de_tartaruga, couro)
bracadeira_de_lider_do_esquadrao = (ataduras, agulha)
protetor_de_braco = (ataduras, couro)
joelheiras = (meia_calca, couro)
perneiras_de_cotademalha = (meia_calca, corrente_de_aco)
salto_alto = (pantufa, sucata_de_metal)
tenis_de_rodinha = (tenis_de_corrida, bola_de_ferro)
pantufas_reforcadas = (pantufa, tecido)
relicario_de_santo = (cruz, calice_sagrado)
flor_do_destino = (flor, baralho)
pedacos_de_vidro = (garrafa_de_vidro, pedra)
boneca = (laco, tecido)
mira_telescopica = (ponteiro_laser, binoculos)
sarira_de_buda = (escrita_budista, tunica_de_monge)
aljava = (couro, bambu)
espanador_de_po = (barra_curta, pena)
leque_de_pena_dourada = (leque, prego)
tabua_com_pregos = (ratoeira, prego)
ratoeira_aprimorada = (ratoeira, minerio_de_ferro)
dinamite = (corda_de_piano, polvora)
armadilha_de_bambu = (armadilha_de_laco, bambu)
armadilha = (armadilha_de_laco, cola)
ruido_metalico = (lata, bola_de_ferro)
camera_fotografica = (camera_de_seguranca, binoculos)
gilhotina_da_selva = (ratoeira, faca_de_cozinha)
armadilha_explosiva = (ratoeira, polvora)
aco = (sucata_de_metal, minerio_de_ferro)
tecido_impermeavel = (oleo, ataduras)
oleo_quente = (oleo, isqueiro)
rubi = (marreta, pedra_preciosa)
bateria_descarregada = (bateria, agua)
po_branco = (giz_branco, pedra)
cinzas = (papel, isqueiro)
componentes_eletronicos = (bateria, corda_de_piano)
diagrama = (caneta_tinteiro, papel)
placa_de_metal = (sucata_de_metal, marreta)
ouro = (picareta, pedra_preciosa)
pedra_aquecida = (pedra, isqueiro)














# ------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------ Itens Terciários ------------------------------------------------- #

machadinha_leve = (machadinha, bambu, pena)
foice_da_morte = (picareta, corrente_de_aco, barra_curta)
machado_gigante = (machado_de_batalha, aco)


# ------------------------------------------------------------------------------------------------------------------- #

# ----------------------------------------------- Itens Quaternários ------------------------------------------------ #




# ------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------- Itens Lendários ------------------------------------------------- #




# ------------------------------------------------------------------------------------------------------------------- #
# print confirmando os locais print(locais)

print(nucleo_da_forca)
