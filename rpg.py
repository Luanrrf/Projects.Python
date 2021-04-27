# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------- RAÇAS ------------------------------------------------------ #

racas = ('HUMANO', 'ELFO', 'ELFO_NEGRO', 'ORC', 'ANÃO', 'HALFLING', 'DRACONIANO', 'FADA', 'MEIO_DEMÔNIO', 'MEIO_ANJO',
         'GOLEM', 'REPTILIANO', 'VAMPIRO', 'LOBISOMEM', 'ULVER_ARVINGER', 'KHAJIIT', 'PRIMATA')

(HUMANO, ELFO, ELFO_NEGRO, ORC, ANAO, HALFLING, DRACONIANO, FADA, MEIO_DEMONIO, MEIO_ANJO, GOLEM, REPTILIANO,
 VAMPIRO, LOBISOMEM, ULVER_ARVINGER, KHAJIIT, PRIMATA) = racas

status = ('FORÇA', 'DESTREZA', 'CONSTITUIÇÃO', 'CARISMA', 'INTELIGÊNCIA', 'SABEDORIA')
(FORCA, DESTREZA, CONSTITUICAO, CARISMA, INTELIGENCIA, SABEDORIA) = status
HUMANO_STATUS = [0, 0, 0, 0, 0, 0]
ELFO_STATUS = [-1, 3, -1, 0, 0, 1]
ELFO_NEGRO_STATUS = [0, 1, -1, 0, 1, 1]
ORC_STATUS = [3, -1, 2, 0, -2, 0]
ANAO_STATUS = [2, -1, 2, -1, 0, 0]
HALFLING_STATUS = [-1, 2, 0, 1, 0, 0]
DRACONIANO_STATUS = [1, 0, 0, 0, 0, 1]
FADA_STATUS = [0, 0, 0, 0, 1, 1]
MEIO_DEMONIO_STATUS = [0, 0, 0, 1, 0, 1]
MEIO_ANJO_STATUS = [0, 0, 0, 1, 0, 1]
GOLEM_STATUS = [2, -2, 3, 0, -1, 0]
REPTILIANO_STATUS = [0, 1, 0, 0, 0, 1]
VAMPIRO_STATUS = [-1, 0, 0, 1, 0, 0]
LOBISOMEM_STATUS = [1, 1, 1, -1, 0, 0]
ULVER_ARVINGER_STATUS = [0, 0, 1, 2, -1, 0]
KHAJIIT_STATUS = [0, 2, 0, 0, -1, 1]
PRIMATA_STATUS = [1, 1, 0, -1, -1, 1]
# -------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------------ CLASSES ----------------------------------------------------- #

classes = ('GUERREIRO', 'CAÇADOR', 'LADINO', 'MAGO', 'SACERDOTE/SHAMAN', 'MONGE', 'BÁRBARO', 'DRUIDA', 'PIRATA',
           'SAMURAI', 'NINJA', 'NECROMANTE', 'DOBRADOR_DE_FOGO', 'DOBRADOR_DE_TERRA', 'DOBRADOR_DE_ÁGUA',
           'DOBRADOR_DE_AR', 'GLADIADOR', 'BRUXO', 'PALADINO', 'BARDO', 'ILUSIONISTA', 'TRANSMUTADOR', 'ALQUIMISTA',
           'RAIZEN', 'MESTRE_DAS_ARTES_MÍSTICAS')

(GUERREIRO, CACADOR, LADINO, MAGO, SACERDOTE, MONGE, BARBARO, DRUIDA, PIRATA, SAMURAI, NINJA, NECROMANTE,
 DOBRADOR_DE_FOGO, DOBRADOR_DE_TERRA, DOBRADOR_DE_AGUA, DOBRADOR_DE_AR, GLADIADOR, BRUXO, PALADINO, BARDO,
 ILUSIONISTA, TRANSMUTADOR, ALQUIMISTA, RAIZEN, MESTRE_DAS_ARTES_MISTICAS) = classes

# -------------------------------------------------------------------------------------------------------------------- #

# --------------------------------------------------- MODIFICADORES -------------------------------------------------- #

modificadores = ('NÍVEL', 'PORTE', 'TIPO_DE_ARMA', 'ARMA_MÃOS', 'MATERIAL_ARMA', 'ESCUDO', 'TALENTO', 'NÍVEL_TALENTO',
                 'EXTRA')
(NIVEL, PORTE, TIPO_DE_ARMA, ARMA_MAOS, MATERIAL_ARMA, ESCUDO, TALENTO, NIVEL_TALENTO, EXTRA) = modificadores

# -------------------------------------------------------------------------------------------------------------------- #


# ----------------------------------------------------- PERGUNTAS ---------------------------------------------------- #

p1 = input('Qual sua raça?')
"""
if p1 in HUMANO:
    atr1 = input("Qual será seu 1º atributo a mais?")
    atr2 = input("Qual será seu 2º atributo a mais?")
    atr3 = input("Qual será seu 3º atributo a mais?")
elif p1 in VAMPIRO:
    atr1 = input("Qual será seu 1º atributo a mais?")
    atr2 = input("Qual será seu 2º atributo a mais?")
elif p1 in PRIMATA:
    atr1 = input("Você prefere o primata com força, destreza ou constituição")

p2 = input('Qual sua classe?')
p3 = input('Qual seu nível?')
p4 = input('Seu porte é P, M OU G?')
p5 = input('Qual o tipo da sua arma?')
p6 = input('Qual o tipo da sua arma?')
p7 = input('Sua arma é de uma, duas mãos ou não se encaixa?')
p8 = input('Qual o material da sua arma?')
p9 = input('Qual o seu talento?')
p10 = input('Qual o nível do seu talento?')"""

p1 = p1 + '_STATUS'

# -------------------------------------------------------------------------------------------------------------------- #
