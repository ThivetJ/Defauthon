# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:18:50 2021.

@author: THIVET Julien // contact : j.thivet@esff.fr

version de présentation réunion brainstrorming du 08/07/2021
"""

import tkinter as tk
from tkinter import messagebox
# from PIL import ImageTk ,Image
# from tkinter import ttk
# import time
import progressbar
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime


NORMAL_FONT = ("Calibri", 12)
LARGE_FONT = ("Calibri", 14)
VERY_LARGE_FONT = ("Calibri", 21)


# Livreionnaire rassemblant toutes les infos sur les défauts classifié avec le livre "Recherche de la qualité de pièce en fonderie" (livre vert)
Livre = {"A": "A - Excroissances métalliques.",

            "A100": "A100 - Excroissances métalliques en forme de toile (ou de bavure)...",
            
                "A110": "...SANS modification des dimensions principales du moulage.",
                    
                    "A111": ("Toile (ou bavure) de faible épaisseur dans le plan de joint ou dans une portée de noyau.",
                             
                             "Bavure de joint ou Barbe.",
                             
"""Excroissance plate, de largeur irrégulière, de profil souvent dentelé, généralement normale à une des faces de la pièce.Elle se trouve le long d'un joint du moule, d'une portée de noyau ou de toute surfcae de séaration entre les éléments constituant le moule.

Les dimensions principales, en particulier l'épaisseur, ne sont pas affectées (à la différence du défaut A121, soulèvement de moule).

Les bavures peuvent accélérer le refroidissement des parties voicines et provoquer des criques (défaut C221) ou, s'agissant de fonte, des zones trempées (défaut G211).""",
                             
"""Jeu entre deux éléments du moule ou entre moule et noyau ou joint mal raccordé.""",
                             
"""- Soigner l'exécution des modèles, des moules et des noyaux.
- Contrôler leurs dimensions.
- Contrôler les remmoulages.
- Tamponner s'il y a lieu."""),
                    
                    "A112": ("Excroissance en forme de veines à la surface du moulage.",
                             
                             "Gerce ou Nervure.",
                             
"""Excroissances en forme de veines, généralement perpendiculaires à la surface, isolées ou en réseau et non situées le long des joints.

En moulage à vert, elles apparaissent souvent au voisinage des angles et en même temps que le défaut D230 (gales) ou A211 (forçage).

* Ce défaut a quelquefois été appelé improprement FRIASSE.""",
                             
"""- Craquelures à la surface du moule se produisant au cours du séchage, lorsqu'il y a une trop forte tendance du sable au retrait par suite de :
    
• chauffage trop rapide,
• température trop élevée, en particulier au début de l'étuvage,
• trop forte teneur en agglomérant ou en humidité.

- Craquelures au moment de la coulée d'un sable trop compact ou trop riche en silice, début de formation de gales - voir défaut D230.
- Fissures de moule accompagnant le forçage de gravité (A211).""",
                             
"""En fonction des causes présumées :
    
- Régler la composition du sable et l'étuvage. Reboucher les craquelures du moule.
- Voir les mesures propres à empêcher les gales (défaut D230). 
- Augmenter la rigidité du moule. 
- Diminuer la pression du métal liquide.

Voir bibliographie A112 et D230."""),
                             
                    "A113": ("Excroissance en réseau à la surface de pièces coulées sous pression.",
                             
                             "Moule craquelé.",
                             
"""Formation d'un réseau de fines bavures à la surface de moulages exécutés par gravité ou sous pression.

- Le plus souvent sur les surfaces qui correspondent à des régions de la coquille ou du moule soumises à de hautes contraintes thermiques surtout avec des moules pour alliages à haut point de fusion et aussi avec des alliages d'aluminium.
- Dans la zone des attaques, car elle est soumise aux plus grands écarts de température.
- Dans les régions du moule où le métal liquide circule à la plus grande vitesse (écarts de température et érosion).
- En général après un long emploi du moule.""",

"Les alternances de température du moule provoquent des alternances de contraintes de traction et de compression qui provoquent des fissures superficielles.",
                             
"""- Choix des attaques donnant les courants de métal liquide les moins nocifs pour le moule. 
- Utilisation pour les moules d'un acier de haute qualité.
- Refroidissement rationnel du moule après mesure des températures dans les diverses régions de l'outillage.
- Avec les métaux légers en coulée sous pression : traitement thermique de détente du moule après environ 20000 injections. 
- Traitement de surface du moule (par exemple: nitruration)."""),

                    "A114": ("Excroissance mince parallèle à une surface dans les angles rentrants.",
                             
                             "Gales d'angle.",
                             
"""Excroissance métallique ayant la forme d'une lame mince de contour irrégulier située dans des angles rentrants, des coins ou au voisinage d'arêtes, à une distance de 2 à 5 mm de la surface et parallèlement à celle-ci.

Lorsqu'elle est située du côté inférieur du moulage, elle est toujours accompagnée de queues de rats (défaut D132).""",

"""Formation d'une écaille de sable non rompue due à une irrégularité de dilatation de la silice. Voir aussi gales (défauts D230).
Ce défaut est moins fréquent en sable étuvé et, dans ce cas, il peut provenir d'un étuvage insuffisant ou d'une reprise d'humidité au cours d'un trop long délai séparant l'étuvage de la coulée.""",

"""Voir D230 (gale)."""),
                    
                    "A115": ("Excroissance métallique mince située dans un angle rentrant et partageant cet angle en deux parties.",
                             
                             "Gerce d'angle.",
                             
"""Excroissance en forme de lame mince divisant en deux un angle rentrant du moulage; elle n'est donc ni parallèle, ni perpendiculaire à une face du moulage.""",

"""Fente du moule ou du noyau se produisant au cours de l'étuvage ou de la coulée et pouvant être favorisée par une trop forte proportion d'agglo mérant dans le sable.""",

"""Diminuer la teneur en agglomérant ou modifier sa nature."""),
                    
                "A120": "...AVEC modification des dimensions principales du moulage.",
                
                    "A121": ("Toile épaisse attenante au moulage dans le plan de joint.",
                             
                             "Soulèvement du moule.",
                             
"""Excroissance plate, plus ou moins épaisse, de profil dentelé et de surface lisse, en général normale à l'une des faces latérales du moulage.

Elle se trouve le long des joints du moule, des portées ou des mottes et est accompagnée d'un accroissement correspondant de l'épaisseur du moulage.""",

"""Excès de pression statique ou dynamique du métal liquide qui produit un soulèvement de la partie de dessus si la charge n'est pas suffisante ou si le crampage est défectueux.""",

"""- Proportionner la charger à la poussée ou assurer un crampage correct.
- Si c'est possible réduire la hauteur du jet de coulée."""),
                    
                    "A122": ("Toile épaisse en d'autres endroits du moulage.",
                             
                             "Défoncement du moule.",
                             
"""Excroissance en forme de voile irrégulier, plus ou moins épais, à surface rugueuse et irrégulière, partant en général des arêtes inférieures du moulage, en angle obtus, et pouvant aller jusqu'à la face inférieure du moule. Les dimensions verticales du moulage sont accrues.

Peut provoquer le défaut E123, moule vidé.""",

"""Sous l'influence de la pression statique pendant la coulée, la résistance de la couche de sable qui forme le fond du moule est dépassée, ce qui peut résulter d'une mauvaise disposition de l'empreinte dans le moule et/ou d'une trop faible charge du châssis combinées avec un serrage du sable insuffisant ou irrégulier. Le fond du moule est alors arraché.""",

"""- Accroître la résistance à vert du sable par un serrage suffisant et régulier et le choix d'un agglomérant approprié, présent à une teneur déterminée en fonction des efforts à supporter.
- Faire reposer les moules sur une aire plane et propre.
- Charger le moule, y compris le châssis, de façon suffisante.
- Si possible diminuer la hauteur de la descente de coulée."""),

                    "A123": ("Formation de toiles dans un plan déterminé par rapport à la direction de montage (coulée de précision en modèle perdu).",
                             
                             "Moule fendu.",
                             
"""MOULAGE DE PRÉCISION A MODÈLE PERDU.
Formation d'importantes toiles minces dans un plan déterminé par rapport à la direction de montage.

 Se produit à la surface et passe par une zone de moindre résistance du moule""",

"""Le moule a été fendu :
- lors des revêtements,
- au moment du décirage,
- au cours du cycle thermique que le moule subit (moule-bloc), 
- par suite d'un mauvais choix des matériaux ou d'une insuffisance de résistance des couches.""",

"""."""),
                    
            "A200": "A200 - Excroissances massives.",
            
                "A210": "Forçage.",
                
                    "A211": ("Surépaisseur sur les faces externes ou internes du moulage.",
                             
                             "Forçage extérieur ou intérieur.",
                             
"""Excroissances massives et irrégulières sur les faces intérieures et extérieures et sur les arêtes du moulage, généralement étendues et rugueuses souvent en combinaison avec les défauts D 121 (rugosité), D 122 (péné tration) et A 112 (gerces).""",

"""Forçage de gravité A 211 -1:
    
    • serrage du sable insuffisant,
    • étuvage incomplet,
    • pression statique et/ou dynamique du métal liquide trop importante. 
    
    Forçage de solidification A 211 -2:
    Seulement dans le cas de la fonte grise et de la fonte GS.
    
    • déformation du moule (de rigidité insuffisante) sous l'effet du gonflement de la pièce provoqué par la formation du graphite en cours de refroidissement,
    • le défaut s'accompagne souvent, dans ce cas, de retassure interne (B 221) ou de porosité (B 311).""",

"""- Forçage de gravité :
    
• augmenter le serrage des parties de moule sujettes au défaut ou leur
teneur en agglomérant,
• substituer au sable vert le sable séché ou durci, modifier la disposition de la pièce dans le moule ainsi que le tracé des jets de coulée afin de diminuer la pression du métal liquide.
    
- Forçage de solidification :
    
• augmenter la rigidité du moule comme ci-dessus (sable et châssis)."""),
                    
                    "A212": ("Surépaisseur au voisinage de l'attaque ou au-dessous de la coulée.",
                             
                             "Erosion.",
                             
"""Excroissance de forme irrégulière et généralement rugueuse des faces d'un moulage, en général au voisinage des attaques ou de la face inférieure, au droit d'un jet de coulée, ou se situant le long du trajet du métal liquide dans l'empreinte. On trouve souvent des inclusions de sable en d'autres régions du moulage.""",

"""- Sable de cohésion insuffisante.
- Défaut de séchage du moule ou des noyaux.
- Mauvais dispositif de coulée : le métal entre dans le moule à trop grande vitesse ou lave pendant trop longtemps une même partie de moule ou de noyau.""",

"""- Amélioration du pouvoir agglomérant du liant à haute température. Serrage plus énergique et plus régulier.
- Contrôle de l'étuvage du moule et des noyaux.
- Étude du dispositif de coulée en évitant l'entrée trop rapide ou trop localisée du métal liquide dans l'empreinte et un lavage trop prolongé d'une même région de moule ou de noyau. Éviter que le jet de métal liquide ne vienne frapper directement des arêtes de sable ou des parois verticales de l'empreinte.
- Utilisation de jets de coulée en céramique et/ou de noyaux filtres.
- Renforcer les zones menacées des parois de l'empreinte en les consti tuant de produits réfractaires ou en les protégeant par une couche résistante."""),
                    
                    "A213": ("Excroissance en forme de plages allongées dans le sens d'un remmoulage à faible jeu.",
                             
                             "Frotte.",
                             
"""Excroissance non géométrique sur les surfaces verticales ou obliques du moulage dans la direction de la fermeture du moule ou de l'introduction d'un noyau. En général, on peut en trouver en plusieurs régions d'un même moulage. Souvent combinée avec des inclusions de sable.""",

"""Lors du remmoulage, principalement lorsqu'il y a des parties en forte saillie, des arêtes ou des faces du moule ont frotté l'une contre l'autre avec arrachement de sable (voir schéma). Ce défaut peut également se produire lors de l'introduction de noyaux.""",

"""- Améliorer si possible le tracé de la pièce dans le sens d'une plus grande dépouille ou d'une plus forte épaisseur.
- Utiliser un engoujonnement correct (précision et longueur).
- Soigner et vérifier le remmoulage."""),
                    
                "A220": "Excroissances à surface rugueuse...",
                
                    "A221": ("...à la surface supérieure du moulage.",
                             
                             "Chute de sable.",
                             
"""Excroissance irrégulière, massive à apparence de cassure, sur la face supérieure du moulage. On retrouve en général sa contrepartie sous forme d'inclusion de sable ou de manque de matière.

Ce défaut, à l'inverse du défaut A 224 (cassure du moule) se produit aussi sur des faces de moulage lisses, sans qu'il y ait une gale au-dessous de lui (D 231).""",

"""Le sable de contact ou, de façon plus générale, la couche de sable voisine du modèle, n'adhère pas assez au sable de remplissage et se détache :
    
- au moment du démoulage (sable collé au modèle),
- pendant la manutention du moule,
- pendant le remmoulage.

La tenue insuffisante du sable provient d'un pouvoir agglomérant insuffisant (trop faible résistance à vert) surtout lorsque le moule est réalisé par couches séparées (sable de contact et sable de remplissage) ayant des propriétés à vert différentes. La séparation des éléments du moule peut être provoquée au moment de la coulée par la dilatation de la couche de contact. Mais, il s'agit alors du défaut D 231 (gale).""",

"""- Augmenter la proportion d'agglomérant dans le sable du moulage. 
- Éviter de fortes différences de propriétés à vert et surtout de résistance, quand plusieurs sables doivent être employés dans un même moule.
- Serrer régulièrement le sable. 
- Vérifier le moule avant le remmoulage. Réparer les points endommagés au démoulage. Employer des pointes ou des crochets."""),
                    
                    "A222": ("...à la surface inférieure du moulage (excroissance massive).",
                             
                             "Soulèvement d'un élément de moule ou du noyau.",
                             
"""Excroissance massive irrégulière qui peut boucher tout à fait l'ouverture inférieure d'un moulage en forme de cuve. Elle présente la forme d'une partie massive de moule ou de noyau détaché. On retrouve généralement sa contrepartie sous la forme d'inclusion de sable ou de manque de matière.

Elle se manifeste surtout sur des moulages d'une certaine hauteur emballés debout.""",

"""- Arrachage d'une certaine quantité de sable emballé par suite d'un démoulage maladroit.
- Résistance du sable insuffisante.
- La pression du métal liquide pénétrant dans l'empreinte est trop élevée et arrache le sable emballé.
- Manque de pointes et de crochets dans le cas d'un emballage d'une certaine hauteur.
- Une fissuration due par exemple à un étuvage trop brutal offre une possibilité de pénétration au métal dont la pression élargira la fissure jusqu'à rupture complète.""",

"""- Démouler correctement.
- Augmenter la teneur du sable en agglomérant (amélioration de la résistance à vert).
- Déplacer les attaques et diminuer la pression du métal liquide qui pénètre dans l'empreinte.
- Mettre des crochets et des pointes.
- Étuver lentement.
- Boucher les fissures.
- Caler par des supports les mottes importantes."""),
                    
                    "A223": ("...à la surface inférieure du moulage (en éléments dispersés).",
                             
                             "Soulèvement de sable.",
                             
"""Excroissance métallique, massive, irrégulière à la face inférieure du moulage, ayant l'aspect d'une cassure. Le moulage présente des inclu sions de sable dispersées surtout à la face supérieure.""",

"""Même mécanisme que A 222 mais avec désagrégation du sable détaché. Intervention éventuelle du phénomène de dilatation du sable (gale) et de serrage défectueux (deux couches de sable mal collées).""",

"""Voir A 222."""),
                    
                    "A224": ("...dans les autres parties du moulage.",
                             
                             "Casse localisée ou dèche.",
                             
"""Excroissance massive irrégulière à aspect de cassure sur les faces latérales ou dans les angles du moulage. En général, on trouve sa contrepartie dans la région supérieure du moulage sous la forme d'une inclusion de sable ou de manque de matière. Elle se situe dans une partie fragile du moule.""",

"""- Voir défaut A 221 et A 222.
- Mauvaise disposition des jets de coulée, le jet de métal liquide venant frapper les parois verticales de l'empreinte. Mauvaise disposition du modèle ou de la plaque-modèle.
- Mauvais lissage au plan de joint à la suite duquel un fragment de sable a été écrasé.""",

"""Voir défaut A 221 et A 222.

Procéder aux réparations du moule dans des conditions qui permettent d'éviter l'écrasement à la fermeture."""),
                    
                    "A225": ("...sur de larges régions du moulage.",
                             
                             "Gale d'extrémité.",
                             
"""Excroissances compactes et irrégulières sur de larges parties du moulage avec une surface à l'aspect de cassure comportant de fortes inclusions de sable.

Ce défaut apparaît dans les coins et angles rentrants du moulage ou sur des surfaces ayant une forme irrégulière, le plus souvent en même temps que les défauts D 230 (gale).""",

"""Contraintes de compression élevées dans les couches chaudes de la paroi supérieure de l'empreinte produites par la dilatation de la silice; en même temps il peut se produire, derrière ces couches, une zone humide de condensation à faible résistance. Une couche chaude peut alors se trouver arrachée.""",

"""Augmenter la résistance à vert par les moyens suivants :
    
- plus forte proportion d'argile (bentonite), meilleure qualité d'argile (bentonite), meilleure préparation du sable (broyage), serrage optimal (éviter un serrage exagéré), refroidissement du sable.
- diminution des contraintes de compression (défaut D 231), augmentation de la résistance à la traction du sable à l'état surhumi difié."""),
                    
                    "A226": ("Excroissance dans une cavité formée par un noyau.",
                             
                             "Noyau écrasé ou cassé.",
                             
"""Excroissances massives et irrégulières dont la surface a l'aspect d'une cassure et qui se situent dans les parties creuses du moulage réalisées à l'aide des noyaux. Le défaut s'accompagne généralement, dans les régions supérieures du moulage, d'inclusions compactes constituant la contre partie de l'excroissance.""",

"""- Partie faible dans le noyau : défaut de serrage ou manque de soin au noyautage ou boîte à noyau défectueuse.
- Fêlure en cours de manutention : manutentions trop brutales, outillage de manutention défectueux.
- Rupture au montage ou au remmoulage : mauvaise précision dimensionnelle, jeu insuffisant, support de noyau mal calibré, fermeture de moule mal guidée.
- Rupture à la coulée : impact du jet de métal liquide sur le noyau trop violent, pression statique du métal liquide exagérée, armaturage insuffisant, supports inexistants ou mal disposés.""",

"""."""),
                    
            "A300": "A300 - Autres excroissances métalliques.",
            
                "A310": "Petites excroissances métalliques à surface lisse.",
                
                    "A311": ("Excroissance de forme plus ou moins sphériques sur les faces ou les arrêtes ou dans les angles rentrants.",
                             
                             "Resuage. \nPour les fontes : goutte phosphoreuse ou diamant. \nPour la fonderie de précision : bulle.",
                             
"""Excroissances métalliques, à peu près sphériques à surface lisse. 

Sur les surfaces libres des moulages (coulés à découvert ou centrifugés). 

Les «perles» ont généralement une composition chimique différente de celle du métal de base.

En moulage de précision, ce défaut apparaît, surtout dans les angles rentrants, les trous borgnes et les évidements.""",

"""- Fonte

L'eutectique qui se rassemble au joint des grains en fin de solidification peut être expulsé vers les espaces libres (surfaces découvertes de la pièce ou intérieur des tuyaux centrifugés), sous l'effet des pressions qui peuvent être engendrées par la graphitisation eutectique ou par le dégagement de solidifiée. gaz dissous ou par la contraction de la partie de pièce
Dans le cas de la fonte, ces gouttes sont généralement plus riches en phosphore que la masse de la pièce d'où leur nom. Lorsque cette expulsion de liquide eutectique se produit à l'intérieur d'une soufflure ou autre défaut interne, le défaut est classé dans les inclusions à G 113.
En général il n'est pas nécessaire de remédier à ces excroissances.

- Alliages légers

Le défaut peut se produire au cours d'un traitement thermique dépassant la température du solidus. Vérifier les conditions du traitement thermique.

- Alliages cuivreux

Dans les alliages cuivreux, c'est généralement la pression due au dégagement de gaz dissous qui provoque le défaut qui de macroporosités. Le retrait de la partie solidifiée peut également jouer un rôle dans la formation du défaut. s'accompagne alors de macroporosités. Le retrait de la partie solodifiée peut également jouer un rôle dans la formation du défaut.

Le premier remède est d'éviter le gazage.

- Fonderie de précision à modèle perdu; tous métaux

En moulage de précision à modèle perdu, des bulles d'air peuvent se loger dans les couches d'enrobage ou d'enduit si ces couches ne sont pas déposées correctement ou si l'orientation des modèles sur la grappe se prête à cet emprisonnement de bulles. La couche d'enrobage est rompue à la coulée et les bulles d'air se remplissent de métal. Le remède consiste à soigner les opérations d'enrobage.""",

"""Inclus dans Cause(s)"""),
        
        "B": "B - Cavités.",
        
            "B100": "B100 - Cavités à parois généralement rondes, lisses, que l'on peut distinguer et isoler à l'oeil nu ... \n(soufflures, piqûres, bouillonnement)",
            
                "B110": "...intérieures au moulage, sans communication avec l'extérieur, \ndécelables seulement à l'aide de procédés spéciaux \nou à l'usinage ou encore à la cassure de la pièce.",
                
                    "B111": ("Cavités rondes à parois généralement lisses, de grosseurs variées, isolées ou en groupes irréguliers dans toutes les régions du moulage.",
                             
                             "Piqûres, Soufflures, Bouillonnement.",
                             
"""Cavités à parois lisses, sensiblement sphéroïdales, souvent sans communication avec l'extérieur (soufflures). Les plus grosses cavités sont le plus souvent isolées, les plus petites (piqûres) apparaissent en groupes de dimensions variées. Dans des cas particuliers, la masse peut être parsemée de soufflures ou de piqûres. La paroi intérieure des soufflures et des piqûres peut être brillante, être plus ou moins oxydée ou, lorsqu'il s'agit de fonte, être recouverte d'une fine couche de graphite. Les défauts peuvent apparaître dans toutes les régions du moulage.""",

"""Les soufflures et les piqûres se produisent du fait de gaz inclus dans le métal en cours de solidification. Toutefois les gaz peuvent être à l'origine d'autres défauts que les défauts B 111.

1/ Origine métallurgique (soufflures endogènes)

- Teneur en gaz du bain trop élevée (matières premières, mode de fusion, atmosphère, etc.); le gaz dissous se dégage lors de la solidification.
- S'agissant d'acier moulé, de fonte et de malléable formation d'oxyde de carbone, par réaction du carbone avec l'oxygène présent comme gaz ou à l'état d'oxyde. Possibilité d'un agrandissement des soufflures d'oxyde de carbone par diffusion d'hydrogène ou exceptionnellement d'azote.

2/ Gaz provenant des matériaux constituant le moule ou les noyaux (soufflures exogènes)

- trop forte humidité des moules ou noyaux; 
- agglomérants ayant une forte tendance à libérer des gaz;
- trop forte proportion d'additifs contenant des carbures d'hydrogène; 
- noirs et couches ayant une trop forte tendance à libérer des gaz.

3/ Gaz retenu mécaniquement (soufflures exogènes)

- insuffisance d'évacuation de l'air et des gaz remplissant l'empreinte;
- insuffisance de perméabilité du moule et des noyaux;
- entraînement d'air par suite de turbulence dans le jet de coulée.""",

"""- Prévoir largement l'évacuation de l'air et des gaz de l'empreinte (évents et tirage d'air); 
- augmenter la perméabilité du moule et des noyaux;
- contrôler le système de coulée;
- dans le cas du moulage étuvé, s'assurer que l'étuvage est suffisant; dans le cas du moulage à vert, contrôler l'humidité du sable;
- diminuer la proportion d'agglomérant ou d'additif ou changer d'agglomérant ou d'additif;
- employer des noirs ou des couches à réaction réductrice;
- engorger la coulée et réduire la hauteur de chute;
- augmenter la pression statique par accroissement de la hauteur des jets de coulée.

pour l'acier moulé :
    
- désoxydation suffisante;
- éviter une réoxydation;
- diminuer la teneur en hydrogène et en azote par une conduite appropriée de la fusion;
- contrôler la température et le temps de coulée.

pour la fonte et la malléable :
    
- empêcher l'introduction d'oxyde et l'oxydation du bain en évitant d'employer des charges rouillées et en surveillant la fusion;
- exceptionnellement contrôler la teneur en azote;
- surveiller la teneur en aluminium, cause possible d'introduction d'hydrogène;
- vérifier que la température de coulée n'est pas trop basse.

pour les alliages non ferreux :
    
- ne pas fondre à une température trop élevée; éventuellement dégazer le bain. Les défauts dus aux gaz dissous sont exceptionnels dans les laitons et les alliages de magnésium.

Éléments de diagnostic

Le diagnostic, souvent difficile, peut s'appuyer sur les éléments suivants :
- Les cavités de grandes dimensions (bouillonnement) sont le plus souvent d'origine exogène.
- Les soufflures exogènes ont souvent des dimensions variables. Elles sont isolées ou en groupes irréguliers. 
- Les soufflures endogènes sont généralement de petite dimension régu lières et réparties d'une façon homogène dans la pièce ou dans une partie de la pièce.
- Dans les alliages ferreux, les soufflures d'hydrogène ont des parois brillantes non oxydées, les soufflures d'oxyde de carbone des parois bleutées, les soufflures d'air entraîné des parois légèrement oxydées, grises.

Le diagnostic n'est pas toujours possible par le seul examen du défaut. Il requiert généralement une enquête et des essais puis un ajustement de certains des facteurs tenant à la métallurgie ou au moulage."""),
                    
                    "B112": ("Comme ci contre, mais limitées au voisinage des pièces métalliques placées dans le moule",
                             
                             "Soufflures sur supports, sur pièces insérées.",
                             
"""Soufflures de diverses dimensions à l'intérieur d'un moulage, isolées ou groupées, au voisinage immédiat de supports de noyaux, refroidisseurs ou pièces insérées.""",

"""- Pièces métalliques humides ou oxydées.
- Absence de protection métallique telle que zingage ou cuivrage. 
- Condensation sur les pièces métalliques par suite de la différence de température entre ces pièces d'une part, le moule et les part. noyaux d'autre
- Pièces insérées ou refroidisseurs souillés, huileux ou recouverts de poteyage susceptible de libérer des gaz.""",

"""- N'employer que des pièces insérées galvanisées ou cuivrées.
- Bien nettoyer, sécher (éventuellement réchauffer) toutes les pièces métalliques avant de les placer dans le moule.
- Éviter que le moule ou les noyaux aient une température supérieure à celle des pièces métalliques destinées à être insérées dans le moule.
- Enduire les refroidisseurs d'huile de lin et les sécher dans une étuve à noyaux; dans le cas de moulage étuvé, mettre une couche de noir sur les surfaces ainsi préparées.
- Utiliser des refroidisseurs dont la surface de contact est cannelée."""),
                    
                    "B113": ("Comme B 111, mais accompagnées d'inclusions de scories (G 112).",
                             
                             " Soufflures de scories.",
                             
"""Même aspect que le défaut B 111 (soufflures) mais toujours accompagné d'inclusion de scorie (défaut G 122) généralement localisé à la partie supérieure des moulages.""",

"""- Réactions d'oxydation au sein du métal liquide donnant naissance à des oxydes liquides ou solides, puis à des gaz (soufflures). 
- Réactions du métal liquide et de ses oxydes avec le réfractaire des appareils de fusion, des poches ou avec les matériaux constituant le moule.""",

"""Voir B 111, remèdes aux phénomènes d'origine métallurgique.

Voir bibliographie G 122."""),
                    
                "B120": "...situées à la surface ou au voisinage de la surface, \nlargement ouvertes \nou au moins en communication avec l'extérieur.",
                
                    "B121": ("...de grosseurs diverses, isolées ou en groupes, le plus souvent superficielles, avec des parois brillantes.",
                             
                             "Soufflures superficielles. Refus.",
                             
"""Cavités à parois le plus souvent arrondies et en général lisses, souvent sous forme de bulles aplaties avec des coins arrondis ou anguleux, à la surface du moulage, isolées ou en groupe.

Les cavités sont parfois ouvertes (refus ouvert) mais le plus souvent situées sous une mince couche de métal (refus fermé) et ne sont visibles qu'après grenaillage ou usinage ou bien apparaissent au décochage comme des régions brillantes.""",

"""- Insuffisance de perméabilité du moule ou des noyaux.
- Coulée trop lente ou trop froide.
- Insuffisance de hauteur des jets et masselottes. 
- Toutes les causes de B 111 (soufflures).
- En coulée sous pression; entraînement d'air, trop haute température du moule, éventuellement en conjonction avec une température du métal trop élevée; vaporisation du produit lubrifiant.
- L'air ou les gaz ont pu encore s'élever dans le sein du métal liquide, mais non quitter l'empreinte, faute d'issue, par manque de perméabi lité du moule ou à cause d'une couche de métal déjà solidifiée.""",

"""- Parer aux causes possibles 
- En fonderie sous pression:
    
• ajuster la température du moule et du métal, 
• lubrifier modérément,
• introduire une régulation de température du moule, employer le vide."""),
                    
                    "B122": ("...dans les angles rentrants des moulages atteignant souvent des régions profondes.",
                             
                             "Soufflures d'angle. Soufflures retassures. \nEffet Léonard.",
                             
"""Cavités dans les angles rentrants d'un moulage se développant vers l'in térieur. Les arêtes sont en général arrondies à la différence du défaut B 212 (retassure de coin ou d'angle rentrant).""",

"""L'échauffement du sable donne lieu à des phénomènes de dilatation, vaporisation, déshydratation, distillation, etc., générateurs de gaz dont la pression, qui s'ajoute à la pression atmosphérique peut être suffisante pour permettre leur pénétration dans la pièce en cours de solidification par les points singuliers de la surface qui se solidifient en dernier lieu, particulièrement les angles rentrants.

Le défaut peut être favorisé par la contraction de solidification ou, dans le cas des fontes grises et G.S., par l'expansion de la croûte solidifiée due à la graphitisation.

Lorsque ces derniers facteurs sont prépondérants, le défaut doit être de préférence classé à B 212 (retassure d'angle) et les remèdes recherchés à cette rubrique.""",

"""Lorsque l'effet de gaz est prépondérant (défaut B 122) la cavité et les arêtes sont arrondies alors qu'elles sont rugueuses et généralement dendritiques pour les retassures d'angles B 212.

- Prévoir des congés aux angles rentrants.
- Diminuer l'emploi des produits susceptibles de dégager des gaz à chaud. Améliorer la perméabilité du sable et le système de tirage d'air.
- Disposer un refroidisseur ou un noyau externe dans les parties sujettes au défaut.
- Augmenter la pression du métal liquide, nourrir."""),
                    
                    "B123": ("Petites porosités (cavités) à la surface des moulages, apparaissant dans des régions plus ou moins étendues.",
                             
                             "Piqûres superficielles.",
                             
"""Petites cavités quelquefois de la dimension d'une tête d'épingle situées à la surface d'un moulage, en colonies plus ou moins étendues, apparaissant sous deux formes:

- Cavités généralement sphériques qui disparaissent à l'usinage après une passe de 1 à 2 mm (piqûres superficielles).
- Dans une section, ou une cassure il apparaît au voisinage de la surface, des cavités en forme de flamme, de massue ou de gouttes, dont la paroi, lorsqu'il s'agit de fonte, est généralement recouverte d'une fine couche de graphite. Si ces cavités n'apparaissent qu'après usinage d'une surface qui était apparemment saine, ou après traitement thermique, ou encore si les trous qui apparaissent déjà sur la surface brute voient leur diamètre augmenter à l'usinage, il s'agit de piqûres sous-cutanées. Le grand axe de ces soufflures allongées et à parois lisses est toujours perpendiculaire à la surface du moulage et se situe entre les grains de cristallisation décelables à l'attaque macrogra phique. La couche où sont situées ces piqûres ne dépasse pas en général 4 mm d'épaisseur, le reste de la section étant sain.

Se produit

dans l'acier moulé :
    
- surtout dans les régions des moulages ayant des épaisseurs de l'ordre de 15 à 30 mm,

dans la fonte et la malléable : 
    
- surtout dans les régions minces,

en coulée à vert:
    
- au voisinage des surfaces formées par des noyaux exécutés à l'aide d'agglomérants organiques.


Formation

- Piqûres superficielles
Réactions avec le carbone de scories riches en oxyde de fer et non saturées en silice, d'où production d'oxyde de carbone, qui se dégage en piqûres superficielles. Celles-ci pouvant être agrandies par un dégagement d'hydrogène diffusé.

- Piqûres sous-cutanées
Oxydation superficielle du jet de métal pénétrant dans l'empreinte par réaction avec l'oxygène de l'atmosphère du moule ou avec les constituants du matériau de moulage.
Réaction des oxydes formés avec le carbone du métal liquide et dégage ment d'oxyde de carbone. Ces réactions, dans les zones voisines de la surface provoquent des cavités pouvant se développer sous l'effet du dégagement d'hydrogène.

Lorsque la pression gazeuse atteint une valeur suffisante il se produit entre les cellules en cours de formation au voisinage de la surface, dans le liquide intercristallin, de minces canaux qui partent du voisinage de la surface sur laquelle ils débouchent dans certains cas.
""",

"""- Métallurgiques :
    
• teneur excessive du bain en oxygène et éventuellement en hydrogène (du fait de la charge ou du processus de l'élaboration);
• teneur élevée en éléments ayant une forte affinité pour l'oxygène, par exemple le titane et l'aluminium éventuellement contenus dans les produits inoculants; 
• température excessive. 
• rapport manganèse/silicium défavorable et/ou haute teneur en soufre, fonte grise et malléable.

- Relatives au matériau de moulage :
    
• trop forte humidité du moule et/ou des noyaux,
• s'agissant d'agglomérants organiques : trop forte teneur en urée.""",

"""Moulage :
    
• Diminuer l'humidité des mélanges pour moules et noyaux; 
• Employer des agglomérants pour moules et noyaux comportant une teneur aussi faible que possible en urée.

Métallurgie :
    
- Acier moulé

• Maintenir la teneur du bain en hydrogène aussi basse que possible, ce qui peut être réalisé en faisant travailler le bain de façon intensive pendant l'affinage. 
• Désoxyder soigneusement le bain à l'aide de manganèse et de silicium et, à la coulée, à l'aide d'aluminium.
• Éviter de trop longs canaux de coulée.
• Faire les jets de coulée et les canaux de coulée en chamotte réfractaire.
• Couler rapidement mais sans turbulence.

- Fonte

• Améliorer la fonte en veillant à sa composition et à son élaboration (éviter des charges rouillées ou sales, augmenter la teneur en sili cium, diminuer la teneur en manganèse).
• Éviter l'introduction d'éléments avides d'oxygène, surtout le titane et l'aluminium dans le ferro-silicium et dans les produits d'inoculation.
• Abaisser la température de coulée. Utiliser des attaques en pression avec des canaux aussi courts que possible."""),
                    
                    "B124": ("Petites cavités étroites en forme de criques apparaissant sur des faces ou le long d'arrêtes en général seulement après l'usinage.",
                             
                             "Défauts en virgules. Retassures dispersées.",
                             
"""INTÉRESSE ESSENTIELLEMENT LES FONTES.

Cavités étroites ayant la forme de déchirures généralement perpendicu laires à la surface du moulage. Leur profondeur peut aller jusqu'à 2 cm. La surface intérieure des cavités est dendritique.

Elles sont souvent accompagnées d'un grossissement des lamelles de graphite.""",

"""- Trop basse teneur en carbone.

- Trop forte teneur en azote (en général au-dessus de 100 ppm).
Ce facteur a d'autant plus d'influence que les pièces sont plus épaisses. C'est souvent la conséquence d'une proportion élevée d'acier dans la charge, particulièrement d'acier Thomas, ou d'une élaboration au four à arc.

- Moule insuffisamment rigide.

Le dégagement d'azote a lieu pendant la solidification ce qui provoque la dispersion de la retassure.""",

"""- Diminuer la teneur en azote.
- Diminuer la proportion d'acier de la charge.
- Élaborer le métal dans un autre appareil que le four à arc (four induction - cubilot, etc.). 
- Fixer l'azote sous forme de nitrure à l'aide de titane ou d'aluminium. 
- Étuver les moules."""),
                    
            "B200": "B200 - Cavités à parois généralement rugueuses. Retassures.",
            
                "B210": "Cavité ouverte selon B 200 \npouvant pénétrer profondément dans le moulage.",
                
                    "B211": ("Cavité en forme d'entonnoir. Parois en général garnies de dendrites.",
                             
                             "Retassure ouverte. Retassure externe.",
                             
"""Cavité ouverte ou fermée, à parois généralement rugueuses, souvent dendritiques (mais lisses pour certains alliages eutectiques), unique ou plus ou moins dispersée, localisée dans les zones se solidifiant en dernier lieu ou encore au contact des angles rentrants de la pièce, des noyaux ou à proximité des attaques.""",

"""La cause principale est la contraction de volume subie par le métal: 
    
- a l'état liquide, dans le moule, jusqu'au début de la solidification, 
- en passant de l'état liquide à l'état solide.

Des causes accessoires peuvent éventuellement agir sur l'importance, l'aspect et la localisation du défaut. Ce sont :

- Les gaz dégagés par le moule et la pression atmosphérique (effet Léonard). 
- L'effet, sur les parties en cours de solidification, du retrait solide de parties déjà solidifiées (crique de retassure). 
- Des dégagements gazeux au sein du métal liquide (soufflures endogènes, retassures dispersées).
- Les déformations du moule sous l'effet de la dilatation due à son élévation de température ou de la pression du métal (pression statique ou gonflement de solidification).

Cas particulier des fontes grises et G.S.

La contraction de solidification se manifeste dans tous les alliages de fonderie.

Toutefois, dans le cas des fontes grises et G.S., le gonflement dû à la formation du graphite eutectique compense l'effet des contractions pour donner en fin de compte suivant les teneurs croissantes en graphite eutectique :

- une contraction réduite, 
- une absence de contraction,
- un gonflement.

Dans ce dernier cas, le plus fréquent, l'expansion subie par les zones périphériques de la pièce, solidifiées en premier lieu, crée dans les zones centrales un vide, avec déplacement de liquide. Ce vide ne sera pas comblé au moment de la solidification du liquide résiduel car l'édifice cristallin très développé s'opposera alors au cheminement de ce liquide.

Il résulte de ces phénomènes des cavités qui ont l'apparence de retassures mais dont les causes sont différentes; ce qui implique des remèdes en partie différents.

Diagnostic

Un indice sûr est le gonflement de la pièce avec forçage du moule. Les dimensions sont augmentées d'une façon sensible, le poids des pièces défectueuses est généralement supérieur à celui des pièces bonnes en dépit des cavités.

Terminologie

Le mot retassure quoique très généralement utilisé est impropre dans ce cas et ne s'applique qu'aux retassures authentiques des fontes blanches, truitées ou à bas carbone.

Nous recommandons le terme « fausse retassure >>.""",

"""Remèdes aux retassures. Cas général

- Tracé 

• S'astreindre à constituer les pièces de régions dont les modules soient sensiblement égaux, ou aillent en croissant vers les masselottes (solidification dirigée). Il s'agit bien entendu de modules corrigés suivant les formules en usage. 
• Modifier éventuellement le tracé par addition de surépaisseurs qui seront, si c'est nécessaire, enlevées à l'usinage. 

- Métal

Utiliser un alliage ne présentant qu'une contraction de solidification faible ou nulle. La fonte grise ou la fonte G.S. sont les seuls alliages de fonderie susceptibles de se prêter, dans une certaine mesure à un tel réglage par variation de la teneur en graphite eutectique.

- Coulée

Limiter, dans la mesure du possible, la température de coulée afin de réduire la contraction à l'état liquide.

- Alimentation

• Masselottes disposées de façon à alimenter les zones de haut module, comportant une réserve de métal liquide en quantité suffisante et pourvues d'un tracé ou de dispositifs permettant un libre passage du métal liquide jusqu'à la fin de la solidification.
• Emploi de produits exothermiques.
• Nombre de masselottes suffisant, compte tenu des zones d'action propres au métal à alimenter et du degré de compacité exigé. 
• Utilisation éventuelle de refroidisseurs externes ou internes, pour créer des effets d'extrémité ou pour modifier les modules.
• Addition éventuelle de nervures de refroidissement.

Remèdes particuliers à la «fausse retassure» des fontes grises et des fontes G.S.

- Réaliser une fonte voisine du point où il n'y a ni contraction ni retrait, soit en augmentant la vitesse de refroidissement, soit en supprimant, si c'est possible, l'inoculation (diminution du nombre de cellules eutec tiques). Intérêt du contrôle par l'analyse thermique.
- Si la fonte est élaborée au four électrique, contrôler avec précision les températures, la durée des opérations et le processus des additions (nature, poids, instant). 
- Augmenter la rigidité du moule soit par serrage plus intense des moules à vert, soit par passage au sable étuvé ou au sable durci ou à la coulée en coquille. 
- Éventuellement masselotter, en choisissant un rapport de modules réduit (par exemple 0,6)."""),
                    
                    "B212": ("Cavité à arêtes aiguës dans les angles des pièces épaisses ou aux attaques de coulées.",
                             
                             "Retassure d'angle.",
                             
"""Cavité débouchant dans des angles rentrants du moulage, aux attaques de coulées ou d'une façon plus générale aux points singuliers de la surface se caractérisant par une solidification tardive. Elle peut se prolonger vers l'intérieur par des cavités isolées ou par des zones poreuses.

Les parois de ces cavités sont rugueuses, le plus souvent dendritiques sauf dans certains alliages eutectiques.""",

"""Mêmes causes que la retassure ouverte (voir B 200) mais avec intervention possible de la pression atmosphérique et de la pression des gaz dégagés par le moule. 

Le simple examen du défaut n'est généralement pas suffisant pour formuler un diagnostic. L'influence respective des principaux facteurs : contraction de solidification, expansion (pour les fontes), gaz et atmosphère ne peut être précisée dans chaque cas particulier que par des observations en cours de fabrication et par des essais.""",

"""Voir B 200.

Plus particulièrement :
    
- Améliorer le tracé de la pièce par des changements de section progres sifs, des congés dans les angles, des nervures de refroidissement.
- Placer un refroidisseur dans l'angle sujet au défaut ou au contraire, l'alimenter si la forme de la pièce s'y prête.
- Utiliser une <<masselotte atmosphérique » pour rétablir la pression atmosphérique dans la cavité de retassure en voie de formation et permettre son alimentation.
- Améliorer la perméabilité du sable et les tirages d'air dans les angles (effet Léonard).
- Prendre des dispositions permettant le libre retrait des parties de la pièce solidifiées en premier lieu et susceptible de ««<tirer» sur les angles des parties massives."""),
                    
                    "B213": ("Cavité en communication avec un noyau",
                             
                             "Retassure de noyau.",
                             
"""Cavité comportant tous les caractères d'une retassure (voir B 200) mais communiquant avec un noyau, généralement dans une partie massive de la pièce.""",

"""Même mécanisme que B 212 (retassure d'angle). C'est le noyau, dans ce cas, qui sert de passage aux gaz ou à l'air (pression de l'atmosphère) jus qu'à la cavité de retassure en cours de formation.""",

"""Voir B 200 et B 212."""),
                    
                "B220": "... située entièrement à l'intérieur du moulage.",
                
                    "B221": ("Cavité de forme irrégulière. Parfois souvent garnies de dendrites.",
                             
                             "Retassure interne.",
                             
"""Caractères généraux de la retassure (B 200) mais sans communication avec l'extérieur. Généralement vers le haut des parties massives de la pièce ou dans les raccordements de parois.""",

"""Voir B 200.

- Contractions de solidification et alimentation insuffisante des régions épaisses.
- Dans le cas des fontes grises riches en graphite eutectique et coulées en moule de rigidité insuffisante: gonflement à la solidification avec formation de «fausses retassures» dans les parties épaisses (voir B 200 - fontes).""",

"""Voir les groupes de défauts B 200 et B 300.

- Lors du tracé, éviter les accumulations de matière. Veiller à l'alimentation des parties massives.
- S'il s'agit de fonte à haute teneur en graphite eutectique, veiller à la stabilité dimensionnelle du moule (peu de bentonite et d'eau, soigner le serrage).
- Utiliser des refroidisseurs internes ou externes.
- Dans le cas de coulée sous pression, ajuster la température du métal et celle du moule. Veiller à l'évacuation d'air."""),
                    
                    "B222": ("Cavité ou région poreuse dans le plan médian du moulage.",
                             
                             "Retassure axiale.",
                             
"""Cavité ou région poreuse dans le plan médian du moulage ou des parties de moulages ayant la forme de plaques.""",

"""Une couche de métal se solidifie rapidement au contact du moule, surtout s'il s'agit de sable vert ou d'un moule métallique, mais la partie située dans le plan médian ne se solidifie qu'avec un certain retard et subit l'effet du retrait liquide et de la contraction de solidification.

Cet effet est surtout marqué si l'alliage a été coulé à une température un peu trop élevée pour l'épaisseur considérée.""",

"""- Abaisser la température de coulée.
- Ne pas couler dans une coquille insuffisamment chaude.
- Incliner le moule et couler lentement ou couler par basculement. Respecter les règles relatives à la position et aux dimensions des masselottes.
- Employer un alliage peu chargé en impuretés."""),
                    
            "B300": "B300 - Régions poreuses, aspect spongieux, juxtaposition de nombreuses petites cavités.",
            
                "B310": "Région poreuse non visible ou à peine visible à l'oeil nu.",
                
                    "B311": ("Régions poreuses visibles à l'oeil nu.",
                             
                             "Porosités, Micro-retassures.",
                             
"""Ce défaut peut être révélé soit par un essai d'étanchéité négatif, soit examen à l'oeil nu ou à l'aide d'appareil grossissant des parties internes de la pièce découvertes par l'usinage ou mis à nu par essai destructif. Il peut également correspondre à l'extérieur de la pièce à des défauts secondaires dans les revêtements (émaillage, galvanisation, etc.) ou à des dépressions superficielles (poquettes). 

Il se présente sous un aspect spongieux, parfois dendritique ou sous forme de petites cavités juxtaposées.

Le défaut est généralement localisé dans les parties se solidifiant en dernier lieu (masses, raccords de parois, angles rentrants, noyaux, attaches des jets et masselottes). Il accompagne parfois et prolonge les défauts B 200 (retassure).

Il affecte de préférence les alliages à grand intervalle de solidification (voir B 200-retassures).""",

"""- Changement de volume à la solidification.

• Contraction de solidification et défaut d'alimentation des parties défectueuses (microretassures). 
• Dans le cas des fontes riches en graphite eutectique, expansion à la solidification avec déplacement de liquide eutectique entre les cristaux solidifiés (fausse retassure).
• Dans le cas des fontes phosphoreuses, contraction à la solidification du liquide eutectique, riche en phosphore, dans les parties épaisses des pièces. Particulièrement sensible si la fonte phosphoreuse contient du chrome et du molybdène.

- Gaz (voir B 100 - soufflures).

• Dégagements gazeux en cours de solidification : gaz dissous dans le métal ou produits de réactions internes. 
• Dégagements gazeux des matériaux de moulage sous l'effet thermique ou chimique du métal liquide. 
• En coulée, sous pression, entraînement d'air.""",

"""Le diagnostic est généralement difficile en raison du grand nombre de facteurs, de leurs origines très diverses et souvent de leur interdépendance. De plus, certains de ces facteurs sont parfois intangibles, la composition du métal par exemple.

Un examen attentif des pièces (aspect, dimensions, position des défauts) des observations de la fabrication, des contrôles en laboratoire et des essais en usine sont alors nécessaires.

1/ Microretassures

- Améliorer le tracé : variations d'épaisseur progressives, éviter les angles rentrants et les masses difficiles à alimenter.
- Modifier la composition du métal dans le sens donnant une diminution de l'intervalle de solidification.
- Établir le système de coulée, de masselottage et de refroidisseurs de façon à réaliser une solidification correctement dirigée. Respecter les règles relatives aux zones d'action, aux modules, à la bonne commu nication et aux réserves de métal liquide dans les masselottes. Aug menter le nombre d'attaques.

Dans le cas de la fonte grise ou de la fonte G.S.: 
- Chercher à réaliser une fonte dans laquelle les phénomènes de contraction et de gonflement se compensent soit :

• S'il y a contraction (retassure) augmenter les teneurs en carbone et silicium dans la mesure où les caractéristiques mécaniques requises le permettent, avec rapport C/Si aussi élevé que possible.
• S'il s'agit de gonflement (fausse retassure) diminuer la teneur en graphite eutectique par abaissement du taux des éléments graphi tisants (carbone, silicium), addition d'éléments gammagènes ou augmentation de leur taux (manganèse, nickel, cuivre, étain, azote) et augmentation de la vitesse de solidification.

- Diminuer le nombre de cellules eutectiques par la surchauffe, la sup pression de l'inoculation, ou l'emploi d'un inoculant n'agissant pas sur le nombre de cellules.
- Diminuer la teneur en phosphore.
- Abaisser la température de coulée.
- Augmenter la rigidité du moule soit : moule à vert serré plus énergi quement, moule séché ou durci, coquille. Ce dernier facteur (la rigidité du moule) est l'un des plus efficaces lorsqu'il s'agit de porosité du type «fausse retassure » affectant des fontes grises.

Dans le cas des alliages non ferreux :
- Choisir si possible des alliages à faible intervalle de solidification moins sensibles à la porosité.
- Affiner le grain s'il s'agit d'alliages Al-Mg ou Al-Cu-Ti ou d'alliages de Mg.
- Éviter les inclusions non métalliques en suspension dans le bain.

2/ Porosités gazeuses

- Porosités endogènes : 
    
• Désoxydation poussée du bain dans le cas de l'acier.
• Dans le cas du bronze à l'étain ou du bronze-étain-zinc, éviter les teneurs élevées en S (produits de réaction gazeux).
• Dégazage du bain.

- Porosités exogènes :
    
• Diminuer dans les sables de moulage et de noyautage les proportions d'eau, d'agglomérants et d'additifs divers ou utiliser des produits donnant des dégagements gazeux moins importants ou plus tardifs.
• Même observation pour les couches et produits contre le collage. . Améliorer la perméabilité des sables et les tirages d'air.
• Introduire dans les sables de moulage ou de noyautage des inhibiteurs par exemple pour les alliages de magnésium: soufre et acide borique.

- Dans tous les cas l'augmentation de la pression statique du métal liquide, par élévation du niveau des coulées, joue dans un sens favorable à l'élimination des défauts.

- Inclusions d'air en coulée sous pression : 
    
• Ajuster le volume de la chambre à la quantité de métal à couler.
• Prévoir l'évacuation d'air de la chambre."""),

        "C": "C -  Solutions de continuité.",
        
            "C100": "C100 - Solution de continuité par suite d'un effet mécanique \n(D'après la forme de la pièce t l'aspect de la cassure, celle-ci ne semble pas résulter de tensions internes).",
            
                "C110": "Cassure normale.",
                
                    "C111": ("Aspect de cassure normale avec quelquesfois des traces de matage.",
                             
                             "Cassure à froid.",
                             
"""Solution de continuité, souvent à peine visible, car en général la pièce n'est pas séparée en plusieurs fragments. Le tracé de la pièce ne permet pas de supposer qu'il y ait eu effet de contrainte lors du refroidissement""",

"""Détérioration du moulage par suite de maladresse au décochage, à l'ébarbage ou lors de manutentions.

Contrainte exagérée exercée à l'ébarbage ou à l'usinage vitesse de coupe, profondeur de passe ou avance exagérées, excès de serrage.""",

"""Soins apportés aux opérations énumérées ci-dessus."""),
                    
                "C120": "Cassure oxydée.",
                
                    "C121": ("Cassure oxydée entièrement ou sur les bords.",
                             
                             "Cassure à chaud.",
                             
"""Solution de continuité souvent à peine visible, car la pièce ne se sépare généralement pas en plusieurs parties. Les parois de la cassure peuvent être colorées par suite de l'oxydation en surface. Le tracé de la pièce ne permet pas de supposer qu'il y ait eu effet de contrainte.""",

"""Détérioration à chaud, par suite d'un décochage prématuré ou trop brutal.""",

"""- Soins au décochage et à la manipulation du moulage encore chaud. 
- Refroidissement suffisant de la pièce dans le moule. 
- En moule métallique : démoulage non prématuré et bien rectiligne, utilisation éventuelle d'éjecteurs."""),
                    
            "C200": "C200 - Solutions de continuité dues à des tensions internes et à des obstacles s'opposant au retrait \n(criques et tapures).",
            
                "C210": "Tapure à froid.",
                
                    "C211": ("Solution de continuité à bords écartés, dans des régions sensibles aux tensions intéressant généralement toute la section; métal non oxydé.",
                             
                             "Tapure à froid.",
                             
"""Solution de continuité sous forme d'une fissure visible. Les bords à angle vif délimitent une cassure de largeur constante qui en général s'étend sur toute la section. Le grain de la cassure présente l'aspect habituel de celui d'une pièce cassée à froid. S'il est oxydé (alliages ferreux et cui vreux), il s'agit d'une tapure à chaud C 222.

S'agissant de malléable, la tapure est souvent apparente avant le traitement de malléabilisation. 

Ce défaut se produit aux endroits sujets à des tensions, c'est-à-dire dans les parties de la pièce solidifiées en dernier lieu, les parties solidifiées en premier étant au contraire soumises à des compressions.""",

"""- En tout premier lieu le tracé qui crée de grandes différences de refroi dissement.
- Le système de coulée et de masselottage créant ou accentuant l'aniso thermie au refroidissement.
- Effort ou choc extérieur, s'ajoutant à l'effet des tensions, au cours du décochage, des manutentions, de l'ébarbage, de l'usinage ou en service. 
- Insuffisance de la résistance à la traction ou de la capacité de déformation de l'alliage.""",

"""- Tracé correct.
- Attaques, masselottes et refroidisseurs favorisant un refroidissement isotherme.
- Refroidissement lent dans le moule accompagné éventuellement d'un dégagement rapide des parties massives, par exemple gros moyeux et leurs noyaux d'alésage.
- Soin au décochage. 
- Utilisation de marteaux « amortis» en alliage léger, cuivre, caoutchouc dur, bois dur. 
- Limitation du cheminement des tapures admissibles par un trou percé à leur extrémité.
- Pour les pièces sujettes aux tapures à froid, traitement de stabilisation comportant une mise à température et un refroidissement lent par exemple pour la fonte grise, chauffage et refroidissement à 50°C : heure et maintien à 550°C pendant 2 heures + 1 heure par centimètre d'épaisseur."""),
                    
                "C220": "Tapure à chaud et crique.",
                
                    "C221": ("Solution de continuité de parcours irrégulier dans les région sensibles aux tensions. \nOxydation de la surface de séparation avec éventuellement structure dendritique fine.",
                             
                             "Crique.",
                             
"""Fissures intercristallines plus ou moins profondes dont le parcours est irrégulier. La cassure présente parfois une structure dendritique fine et un aspect oxydé.

Ce défaut apparaît le plus souvent dans les régions se solidifiant en dernier lieu et dans lesquelles des contraintes se produisent (par exemple changements de section, angles rentrants).""",

"""- En principe:
L'alliage en cours de solidification, à une température voisine de celle
du solidus, a subi une contrainte ou une déformation.

-En général :

    Retrait contrarié par suite d'un tracé défectueux : 
        
• De fortes différences d'épaisseur.
• Passages trop rapides d'une épaisseur à une autre.
• Moulage trop ramifié.

    
    Retrait contrarié pour des raisons tenant au moule :
        
• Matériaux de moulage et de noyautage trop rigides.
• Surfaces de moule rugueuses.
• Vitrification de sable.

    Allongement ou déformation du moule : 
        
• Sable ou parties métalliques échauffées.

- S'agissant de moulage par gravité ou sous pression: 
• Maintien trop prolongé de la pièce dans le moule.
• Retrait contrarié par suite d'une dépouille insuffisante. 
• Moule ouvert trop tôt, pièce endommagée à l'extraction. 
• Criques à l'extraction des noyaux du fait d'un manque de précision d'ajustage.
• Mauvaise disposition des éjecteurs provoquant des contraintes de
flexion. 
• Création de points chauds par suite d'une température de coulée
trop élevée ou par effet d'arête de sable. 
• Alimentation en métal liquide insuffisante.

- Causes métallurgiques :
    
    Certains alliages peuvent être sensibles à la crique du fait d'une composition incorrecte.
• Acier moulé : 
Teneur en soufre ou en aluminium trop élevée.

• Malléable :
Retrait trop important par suite de teneurs insuffisantes en silicium et surtout en carbone, combinées avec une trop haute temperature de coulée.

• Fonte et surtout fonte coulée en coquille (cylindres de laminoir):
Teneur en phosphore insuffisante.

• Bronze à l'étain : Ségrégation de plomb.""",

"""- Remédier aux causes générales indiquées ci-dessus.
- Disposer des nervures de refroidissement ou des refroidisseurs externes aux régions menacées de tensions et où un retard de solidification est à prévoir.

- Métallurgie:
    
• En acier moulé : désulfuration (moins de 0,02% S) et désoxydation suffisante. Diminuer la durée de la coulée.
• En alliage léger : affinage du grain."""),
                    
                    "C222": ("Rupture après solidification complète, en cours de refroidissement ou à l'occasion d'un traitement thermique",
                             
                             "Tapure à chaud, de trempe.",
                             
"""Solution de continuité sous la forme d'une crevasse visible à l'œil nu. Les bords aigus délimitent une cassure nettement visible et de largeur régulière superficielle ou intéressant toute la section. Les parois de la cassure. par suite d'oxydation à chaud, sont colorées dans le cas des alliages ferreux.""",

"""- Traitement thermique mal conduit. 
- Pièce comportant des tensions préalables.""",

"""- Modification des conditions de trempe: température et nature du bain adoucissement de ces conditions lorsqu'il s'agit de pièces compliquées.
- Emploi d'alliages qui ont une faible vitesse critique de trempe, modi fication du tracé (régularisation des épaisseurs)."""),
                    
            "C300": "C300 - Solutions de continuité par défaut de soudure (reprise). \nLes bords en général arrondis permettent de conclure à un mauvais contact entre \nles divers courants de métal liquiquide lors du remplissage du moule.",
            
                "C310": "Manque de liason ou de continuité dans les parties alimentées en dernier lieu.",
                
                    "C311": ("Séparation complète ou partielle souvent dans un plan vertical.",
                             
                             "Reprise.",
                             
"""Solution de continuité à bords arrondis. Ce défaut, nettement caractérisé, intéresse une partie ou la totalité de la section de la pièce et peut à la limite se réduire à un léger sillon à bords arrondis. Il peut être accompagné d'arêtes mal venues (voir défaut E 111, mal venu ou défaut E 121, manque). Il se produit sur les grandes surfaces ou dans les régions des pièces d'accès difficile pour le métal liquide ou dans la zone de rencontre de deux nappes de métal liquide.""",

"""- Coulabilité insuffisante.
- Coulée trop lente.
- Dégagement d'air insuffisant.
- En coulée sous pression : mauvaise soudure de courants de métal fortement refroidis, qui ont une histoire thermique différente (ce qui se manifeste aussi par une différence de structure).""",

"""- Couler plus chaud.
- Améliorer la coulabilité de l'alliage.
- Accroître la régularité ou la vitesse de remplissage de l'empreinte par une meilleure conception des attaques.
- Ménager des dégagements d'air suffisants. 

En moule métallique :
    
• Ajuster la température du moule et celle du métal (en général les élever). 
• Réchauffer certaines parois du moule, ou mieux régler leur température. 
• Mettre au point le système d'attaque. 
• Vérifier le poteyage (conductibilité)."""),
                    
                "C320": "Manque de liaison entre deux parties du moulage.",
                
                    "C321": ("Séparation du moulage dans un plan horizontal",
                             
                             "Coulée interrompue.",
                             
"""Solution de continuité qui se présente comme un joint visible dans un plan horizontal. Les deux parties du moulage sont séparées ou soudées seu lement par endroits. La partie inférieure présente des arêtes arrondies.""",

"""- Irrégularités de coulée pouvant conduire à une interruption du remplissage de l'empreinte.
- Quantité de métal insuffisante et complément tardif de métal liquide avec solidification prématurée de la surface du métal qui est dans l'empreinte au moment de l'interruption de la coulée.""",

"""- Éviter toute irrégularité de coulée.
- Prévoir une quantité suffisante de métal liquide. 
- Surveiller la dimension des poches."""),
                    
                "C330": "Manque de liason au voisinage des supports de noyau, des refroidisseurs internes, des pièces insérées.",
                
                    "C331": ("Solution de continuité localisée au voisinage d'une pièce insérée.",
                             
                             "Reprise sur support de noyau ou autre pièce insérée.",
                             
"""Solution de continuité localisée au voisinage de la pièce insérée : support de noyau, tube inséré, refroidisseur interne, etc.""",

"""Mauvaise soudure entre la pièce insérée et le métal par suite de solidifi cation prématurée ou de refroidissement excessif du métal liquide au contact de cette pièce.""",

"""- Plus haute température de coulée. 
- Amélioration de la coulabilité.
- Modification des attaques en vue d'accélérer le remplissage de l'empreinte.
- Dimensionnement et disposition corrects des pièces à insérer. 

Dans l'application de ces mesures, il faut évidemment veiller à éviter la fusion des pièces insérées."""),
                    
            "C400": "C400 - Solutions de continuité par suite de défaut métallurgique.",
            
                "C410": "Spération le long des joints de grains.",
                
                    "C411": ("Séparation le long des joints de grains de cristallisation primaire",
                             
                             "Cassure conchoïdale ou de \"sucre candi\".",
                             
"""La cassure présente des facettes lisses légèrement incurvées comme celles du sucre candi.""",

"""Ce défaut se produit lorsque les teneurs en aluminium et en azote sont trop élevées et que le nitrure d'aluminium précipite aux joints de grains.""",

"""Limiter le taux d'addition d'aluminium à la valeur juste nécessaire pour assurer le calmage. Éventuellement fixer l'azote par le titane ou le zirconium (veiller aux inconvénients en ce qui concerne les caractéristiques mécaniques)."""),
                    
                    "C412": ("Criques en réseau sur tout la section (défaut du zinc coulé sous pression)",
                             
                             "Corrosion inter-granulaire.",
                             
"""Détérioration des caractéristiques mécaniques par suite de fissures en réseau qui occupent toute la section du moulage. Gonflement, voile des moulages et fissuration de la surface. Ce défaut peut n'apparaître qu'à long terme.""",

"""Emploi d'un alliage de zinc non conforme à la norme et contenant des impuretés telles que l'étain, le plomb, le cadmium. Décohésion de l'alliage le long des joints de grains.""",

"""Emploi exclusif d'alliages de zinc affinés, purs et contrôlés. La teneur en magnésium doit rester à l'intérieur des limites fixées par la norme (de préférence près de la limite supérieure)."""),

        "D": "D- Surface défectueuse.",
        
            "D100": "D100 - Irrégularités de la surface du moulage.",
            
                "D110": "Plissement de la peau du moulage.",
                
                    "D111": ("Plissement sur des régions assez importantes de la surface.",
                             
                             "Peau de crapaud. Friasses.",
                             
"""Plissements irréguliers répartis sur la surface du moulage. Avec l'acier moulé le plus souvent sur les faces peu épaisses et horizontales.""",

"""- Trop grande viscosité du métal liquide.
- Température de coulée trop basse et coulée trop lente. Gaz résultant de la réaction entre la couche et le métal.
- Formation de peau à la coulée.
- En coulée en coquille : coquille trop froide.""",

"""."""),
                    
                    "D112": ("Surface plissée ou sillonée par des anfractuosités en réseaux (fonte G.S.).",
                             
                             "Peau d'éléphant.",
                             
"""Surface irrégulièrement grenue ou plissée souvent avec des sillons un peu plus profonds disposés en réseau. 

Aspect parcheminé.

Se rencontre principalement à la surface supérieure horizontale de moulages épais.""",

"""Les composés résultant du traitement au magnésium, par exemple oxyde de magnésium, sulfure de magnésium, etc., apparaissent en général sous forme de pellicules plus ou moins dispersées qui, dans la poche, ne montent que lentement à la surface. Elles se rassemblent partiellement à la surface supérieure du moulage ou à la face intérieure des moulages centrifugés.""",

"""- Emploi de matières premières de bonne qualité contenant peu d'oxygène et de soufre ou désulfuration poussée.
- Emploi d'une poche théière.
- Réglage corrélatif, au plus bas, de l'addition de magnésium. Éventuellement prolongation du temps de maintien au repos après traitement au magnésium.
- Régler la teneur en carbone en fonction de la température de coulée."""),
                    
                    "D113": ("Plis serpentant sans solution de continuité. Les bords du pli sont au même niveau. La surface de moulage est lisse.",
                             
                             "Rides.",
                             
"""Sillons en forme de plis dans la surface du moulage se propageant en serpentant, sans solution de continuité profonde. La surface du moulage peut être lisse et brillante.

Contrairement au défaut D 132 (queue de rat) les deux bords de ces sillons sont au même niveau.

Se rencontre sur les surfaces horizontales ou bombées des pièces minces.

Avec la fonte à graphite lamellaire hypereutectique il peut apparaître simultanément de l'écume de graphite surtout dans les régions épaisses. Les rides peuvent être un point de départ pour des reprises (C 311).""",

"""- Par suite de la solidification superficielle d'un métal trop visqueux ou trop froid les plissements formés par les peaux d'oxyde, au voisinage de la surface ne sont pas aplanis par la pression du métal liquide.
- Lors de l'emploi d'argiles (bentonites) de faible réfractairité comme agglomérants pour la coulée d'acier (ou plus rarement de fonte) la surface du sable peut subir un ramollissement et une déformation sous la poussée du métal liquide.

La dilatation du sable n'est pas en cause dans ce cas qu'il ne faut pas confondre avec le défaut D 132 (queue de rat) caractérisé par des bords dissymétriques.""",

"""- Employer des matières premières à faible teneur en oxygène et en soufre.
- Élever la température de coulée, éventuellement réduire le temps remplissage en augmentant la section d'attaque. de
- Éviter la coulée dans des coquilles trop froides.
- Pour l'acier moulé, choisir un liant plus réfractaire.
- Voir aussi défaut D 132."""),
                    
                    "D114": ("Lignes marquant, sur la surface du moulage, l'écoulement du métal liquide (alliage légers).",
                             
                             "Fleurs. Traces d'écoulement.",
                             
"""Sur la surface qui par ailleurs est saine, il apparaît des lignes, marquant éventuellement le parcours des filets de métal liquide.""",

"""Peaux d'oxyde, marquant en partie le parcours des filets de métal liquide.

Nota: Ce défaut peut conduire à des reprises (C 311).""",

"""- Élever la température du moule.
- Abaisser s'il y a lieu la température de coulée.
- Modifier la disposition et la taille des attaques (en coulée par gravité ou sous basse pression).
- Incliner le moule pendant la coulée.
- En coulée sous pression soumettre les surfaces du moule perpendicu laires ou à peu près perpendiculaires au plan de joint à un dépolissage par projection de liquide ou de sable."""),
                    
                "D120": "Surface rugueuse.",
                
                    "D121": ("Rugosités dont la profondeur est de l'ordre de frandeur des dimensions des grains de sable.",
                             
                             "Rugosité.",
                             
"""La surface de la pièce est rugueuse. La profondeur des rugosités est de l'ordre de grandeur des dimensions des grains de sable avec éventuellement des inclusions de sable.

Dans le cas du moulage à vert, la rugosité apparaît souvent en même temps que d'autres défauts provenant de la dilatation du sable D 132 (queue de rat), D 230 (gale), ce qui la distingue des défauts D 122 (pénétration), D 221 (grippure) et D 222 (vitrification).

Se produit surtout en moulage à vert aux endroits qui correspondent au «plafond» de l'empreinte, en moulage étuvé aux endroits qui n'ont pas ou pas suffisamment été passés à la couche ou au noir.""",

"""A la surface de séparation métal-sable, il y a un équilibre entre les forces capillaires du sable (perméabilité aux gaz), la tension superficielle du métal et la pression métallostatique. Si la pression métallostatique dépasse les forces qui lui sont opposées, le métal liquide pénètre entre les grains de sable de la paroi du moule, ce qui provoque la rugosité de la surface du moulage, et peut même après dépassement d'une valeur critique (pression de pénétration) conduire au défaut D 122 (pénétration).

En outre par suite de la dilatation de la silice, des grains de sable peuvent être désagrégés, donnant ce qu'on appelle une «pluie de sable». Après remplissage de l'empreinte les endroits où s'est produit cette pluie de sable présentent le défaut D 121 (rugosité).""",

"""- Emploi de sable à granulométrie plus fine. 
- Addition d'une quantité de sable fin au sable de moulage.
- S'agissant de fonte, addition de noir minéral, ou de granulés de brai au sable de moulage.
- Diminution de la contrainte de compression du sable (voir défauts D 230).
- Passage d'une couche ou augmentation de son épaisseur. 
- Serrage plus fort et plus régulier.
- Abaissement de la température de coulée.
- Diminution de la pression métallostatique."""),
                    
                    "D122": ("Rugosités dont la profondeur est supérieure aux dimensions des grains de sable.",
                             
                             "Forte rugosité. Pénétration. Coup de feu.",
                             
"""Surface très rugueuse. La rugosité est d'un ordre de grandeur supérieur à celui de la dimension des grains de sable. A l'ébarbage, ce défaut ne peut être éliminé que très difficilement.""",

"""- Comme pour le défaut D 121 (rugosité) mais plus accentuées.
- Une réaction chimique métal-moule peut, par la formation d'un laitier visqueux à basse température, renforcer la pénétration.
- Excès de pression pouvant être créé ou renforcé par des explosions à la coulée (coup de feu).""",

"""Les mesures recommandées pour éviter le défaut D 121 (rugosité) doivent être non seulement prises, mais renforcées.

- Éviter les réactions moule-métal.
- Adopter des attaques qui évitent les coups de feu.
- Éviter la formation de couches de condensation. 
- Employer un sable de plus grande finesse.
- Régler convenablement la proportion de poussier dans le sable. N'employer que du poussier de houille ou de brai de qualité appropriée.
- Diminuer le taux d'humidité du sable.
- Serrer plus fort et surtout plus régulièrement.
- Dans le cas de moulage à haute pression, contrairement au cas du moulage normal, une augmentation de l'addition de bentonite agit dans un sens favorable."""),
                    
                "D130": "Sillons dans la surface du moulage.",
                
                    "D131": ("Sillons de diverses longueurs, souvent ramifiés, avec fond d'entaille et bords adoucis.",
                             
                             "Stries.",
                             
"""Sillons à bords adoucis dans la surface du moulage, le plus souvent ramifiés. Profondeur de l'ordre de 2 mm. 

Se produit sur toutes les surfaces mais en général sur les surfaces horizontales supérieures et inférieures.""",

"""Ce défaut est un début de gale, la dilatation de la silice produit un commencement de soulèvement qui ne s'est pas poursuivi jusqu'à l'éclatement de la croûte de sable avec pénétration du métal dans la partie sous-jacente (gale).

Les causes et les remèdes se confondent avec ceux de la gale (voir D 231, article et exemples).
""",

"""."""),
                    
                    "D132": ("Sillons pouvant atteindre 5mm de profondeur, l'un des deux bords formant un pli qui recouvre plus ou moins complètement le sillon.",
                             
                             "Queue de rat.",
                             
"""Défaut superficiel n'apparaissant en général que sur les faces du moulage en contact avec la paroi horizontale inférieure de l'empreinte. Il consiste en un sillon pouvant avoir jusqu'à 5 mm de profondeur, avec un bord à angle vif qui emprisonne souvent des grains de sable.

Les queues de rat partent le plus souvent des attaques de coulée et sont assez rarement reliées les unes aux autres par des ramifications (figure 145a). Dans les cas où le sable a une forte tendance à l'apparition de ce genre de défaut les queues de rat peuvent être accompagnées de stries (D 131) et de gales (D 230).

Des «<rides» (défaut D 113) peuvent s'étendre parallèlement à de légères << queues de rat» ou les recouvrir. Leur différence de niveau avec la surface saine avoisinante est à peine perceptible (figure 145b).""",

"""Comme pour les gales (D 230).

Formation sous l'effet de la chaleur d'une zone de condensation et décollement de la croûte du sable par dilatation de la silice. La croûte ainsi formée dépasse les dimensions de son ancien emplacement.

Lorsque cette écaille ne s'aplatit pas elle forme des queues de rat à la surface.

Nota: Ce n'est pas toujours la longueur, mais plutôt la profondeur des queues de rat qui caractérise la tendance d'un sable à produire ce défaut.""",

"""Voir défaut D 230. Il est surtout important d'ajouter du noir au sable."""),
                    
                    "D133": ("Dépressions irréglièrement réparties de dimensions variées courant à la surface du moulafe, le plus souvent en suivant le chemin d'écoulement du métal liquide(acier moulé).",
                             
                             "Cicatrices.",
                             
"""Dépressions irrégulièrement réparties allongées ou en forme de calotte, suivant en règle générale le chemin que parcourt le métal liquide et se situant dans les angles morts et dans les régions éloignées des attaques. Apparaissant souvent en même temps que des porosités superficielles. Avant l'ébarbage il y a de la calamine dans les cicatrices.""",

"""- Teneur en gaz trop élevée dans le métal liquide par suite d'une désoxydation insuffisante.
- Couches produisant beaucoup de gaz.""",

"""- Désoxyder soigneusement l'acier liquide.
- Raccourcir le trajet du métal liquide dans le moule.
- Augmenter le nombre des attaques, incliner le moule.
- S'agissant de moules importants diminuer fortement la durée de la coulée. 
- Étuver suffisamment le moule et employer des couches pauvres en gaz.
- Prévoir une évacuation d'air largement suffisante à travers le moule et les noyaux."""),
                    
                    "D134": ("Surface grêlée comme marquée de petite vérole sur toute la pièce.",
                             
                             "Peau d'orange.",
                             
"""Toute la surface de la pièce est recouverte de pustules, en creux, présentant un aspect de petite vérole. Les dimensions des pustules sont variables selon l'importance du défaut. Elles sont plus importantes sur les pièces ou parties de pièces les plus épaisses.""",

"""Emploi d'un sable synthétique insuffisamment régénéré et pollué par des déchets acides provenant des noyaux et des additifs (huiles, dextrines, résines furanniques, acide phosphorique, mogul, poussières d'oxyde ferrique, cendres de farine de bois, etc.).

Réaction à haute température entre ce sable et le métal liquide.""",

"""- En dépannage : ajouter au sable du carbonate de soude en solution dans l'eau de malaxage.
- Solution définitive : utiliser un sable synthétique calcique correctement régénéré ou sodique.

La mesure du pH est un moyen de surveillance de la dégradation du sable."""),
                    
                    "D135": ("Sillons et rugosités au voisinage des angles rentrants de la pièce en coulée sous pression.",
                             
                             "Etamage. Erosion.",
                             
"""Sillons et rugosités sur de petites sections de la surface, en général dans les angles rentrants des pièces coulées sous pression.
""",

"""Action du métal liquide sur le moule. S'il s'agit d'alliage d'aluminium, il peut former un alliage avec le métal du moule surtout dans les endroits où le courant de métal liquide est rapide. Cet alliage constitue une couche qui peut être arrachée lors de l'extraction du moulage.
""",

"""- Éviter l'effet d'érosion du courant de métal liquide en améliorant le dispositif d'attaque.
- Soigner le poteyage.
- Ajuster la température de coulée.
- Augmenter les dépouilles prévues pour l'extraction.
- Nettoyer plus souvent le moule."""),
                    
                "D140": "Affaissements de la surface du moulage.",
                
                    "D141": ("Dépression à la surface du moulgae dans un région d'accumulation de chaleur.",
                             
                             "Poquette.",
                             
"""Affaissement de surface du moulage dans les régions d'accumulation de matière. La surface de cet affaissement ne se distingue en général pas du reste de la surface du moulage.

Ce défaut apparaît le plus souvent aux épaississements de section et souvent à l'aplomb d'une retassure interne ou d'une porosité.""",

"""Contraction à la solidification aux noeuds qui constituent une accumulation de matière. 

En coulée sous pression, éventuellement en corrélation avec une température trop basse du métal et/ou du moule et une pression insuffisante.

Nota: En cas d'insuffisance locale d'évacuation de gaz, il peut aussi se produire à cet endroit des défauts B 121 (refus). Il n'est pas toujours facile de caractériser le défaut et les deux causes doivent être prises en considération (voir aussi défaut B 311 porosités).""",

"""- Modifier le tracé, supprimer les changements brusques de section. 
- Agrandir les sections de liaison avec les accumulations de matière. 
- Si possible, ajouter des masselottes ou des attaques supplémentaires. 
- En coulée sous pression, vérifier la température du métal et du moule ainsi que la vitesse et la pression de la coulée."""),
                    
                    "D142": ("Petite cavités superficielle en forme de gouttes oud e cuvettes en général colorées en g-vert \n(aciers au chrome carburés, coulés en fonderie de précision à modèle perdu).",
                             
                             "Inclusion de scorie.",
                             
"""Petites cavités superficielles ayant la forme de gouttes ou de cuvettes en général colorées en gris-vert.""",

"""Il se produit vraisemblablement par réaction entre le moule et le métal des crasses facilement fusibles qui adhèrent au moulage mais qui sont arrachées lors du sablage et laissent une cavité en forme de goutte. Ce phénomène s'observe avant tout avec les aciers alliés à forte teneur en chrome. Il est favorisé par un refroidissement relativement lent.""",

"""- Diminution de la température de coulée.
- Refroidissement sous atmosphère réductrice."""),
                    
            "D200": "D200 - Irrégularités assez importantes à la surface du moulage.",
            
                "D210": "Irrégularité par approfondissement.",
                
                    "D211": ("Approfondissement souvent étendu  sans contrepartie.",
                             
                             "Enfoncement (de moule).",
                             
"""Dépression ou cavité souvent de grande étendue qui a le même aspect de peau que la pièce. Ce défaut correspond à une déformation ou à un déplacement d'une partie de la surface de la pièce. Il n'y a pas saillante. de contrepartie""",

"""Une partie du moule a été enfoncée en bloc. Une région de l'empreinte a donc été déplacée vers l'intérieur du moule en diminuant d'autant l'épaisseur de la pièce. Cette déformation du moule peut être due:
- à un remmoulage sur une couche de sable irrégulière et dure;
- à un chargement ou un crampage exagéré;
- à un manque de planéité du support du moule;
- au déplacement d'un crochet ou d'une armature.""",

"""Non renseigné"""),
                    
                "D220": "Adhérence de sable plus ou moins vitrifié.",
                
                    "D221": ("Sable adhérent fortement à la pièce et formant surépaisseur.",
                             
                             "Sable brûlé, grippure.",
                             
"""Croûte de sable adhérant fortement à la pièce qui ne peut être éliminée par un grenaillage de durée normale mais exige un meulage. Ce défaut est localisé dans les parties les plus chaudes du moulage.
""",

"""- Réaction chimique moule-métal (formation de fayalite). 
- Réfractairité insuffisante du sable.
- Serrage insuffisant.
- Mouillabilité du sable.
- Température de coulée exagérée.""",

"""- Améliorer le dépoussiérage et le taux de régénération du sable. 
- Augmenter, s'il y a lieu, le taux des additifs contenant des hydro-carbures.
- Utiliser un enduit ou renforcer son épaisseur.
- Serrer plus énergiquement.
- Contrôler la température de coulée."""),
                    
                    "D222": ("Sable très adhérent et en partie fondu.",
                             
                             "Vitrification.",
                             
"""Croûte mince de sable fondu, solidement adhérente au moulage. La surface a un aspect vitreux, éventuellement pustuleux. 

Se produit de préférence sur les surfaces ayant été portées aux températures les plus élevées. """,

"""- Température de frittage du sable trop basse.
- Haute température de coulée.
- Forte accumulation locale de chaleur.
- Scorification du sable par les oxydes ou les sulfures contenus dans le métal liquide.""",

"""- Sable plus réfractaire.
- Dispositif de coulée évitant les accumulations de chaleur.
- Température de coulée plus basse.
- Voir D 221."""),
                    
                    "D223": ("Conglomérat de sable et de métal hérant fortement au moulage dans les régions les plus chaudes (angles rentrants et noyaux).",
                             
                             "Abreuvage..",
                             
"""Excroissance de forme non géométrique, constituée par un mélange intime de sable et de métal, d'aspect spongieux, fortement adhérent à la pièce généralement localisé dans les parties de sable les plus chaudes (noyaux, parties concaves) et les moins denses.

Particularité : Le défaut D 223 ne se rencontre pas sur les moulages en alliages de magnésium ou d'aluminium.""",

"""Les facteurs ci-dessous tendent à favoriser l'abreuvage :
- Faible tension superficielle du métal liquide : . 

• teneur élevée en phosphore, en silicium, en manganèse, pour les alliages ferreux, 
• teneur élevée en phosphore ou en plomb pour les alliages cuivreux.

- Pressions statique et dynamique élevées.
- Température du métal et du sable élevée.
- Sable trop gros ou insuffisamment serré.
- Réfractairité du sable insuffisante (quantité trop élevée d'argile ou d'éléments fondants).
- Sable trop chargé en agglomérant.
- Conductibilité thermique du sable trop faible. Qualité insuffisante de l'enduit ou du noir minéral.
- Dans le cas de l'acier, réaction physico-chimique d'inclusions ou d'oxydes basiques sur le sable généralement acide.""",

"""Agir sur les facteurs énumérés ci-dessus (voir également D 122 et D 222)."""),
                    
                    "D224": ("Ecaille de moule emprisonnée dans le métal (fonderie de précision à modèle perdu).",
                             
                             "Décollement de la première couche. Gale.",
                             
"""Écaille de moule emprisonnée dans le métal.
""",

"""- Décollement de couche total ou partiel.
- Manque de liaison entre les couches : une cloque ou une écaille se soulève pendant la fabrication du moule et peut se rompre lors de la coulée.""",

"""Réajustement des cycles de trempe et de séchage."""),
                    
                "D230": "Excroissance métalliques en forme de lames à parois rugueuses en général parallèles à la surface du moulage.",
                
                    "D231": ("Excroissance métallique en forme de lame à parois rugueuses parallèles à la surface, susceptible d'être éliminée par burinage.",
                             
                             "Gale franche.",
                             
"""Excroissance métallique irrégulière d'une épaisseur de quelques millimètres, en général à bords aigus, parallèle à la surface du moulage, à sur face très rugueuse, qui d'habitude ne tient au moulage que par endroits. Pour le reste elle s'en éloigne. La surface du moulage sous ce défaut présente une dépression qui épouse la forme et la grandeur de la gale. Les gales franches peuvent être détachées au burin, mais l'attache à la pièce reste apparente et la dépression subsiste.

La gale franche (D 231) se produit sur tous les moulages principalement sur : 
- la surface horizontale supérieure de l'empreinte (gale de plafond), 
- la surface inférieure horizontale de l'empreinte (gale de plancher).

Elles se forment moins souvent sur les parois latérales.""",

"""1/ Gale de plafond:
    
1.1. - Apparition d'une zone de condensation de faible résistance puis formation d'une croûte dont la dilatation est contrariée par la contrainte de compression dans la paroi de l'empreinte. Compression de cette croûte contre le sable de remplissage par l'arrivée du métal liquide et éclatement de la croûte. Le métal liquide vient s'infiltrer dans l'espace qui peut rester entr la croûte et le reste du moule et forme une languette qui consti tue la gale. Si cette pénétration ne se produit pas, c'est le défaut D 131 (stries).

1.2. - Apparition d'une zone de condensation de faible résistanc - Formation d'une croûte non contrariée par la contrainte de compression. La croûte ne se rompt pas et pénètre dans l'empreinte où elle se dilate (sillon). Le métal remplit la cavité qui s'est formée derrière la croûte en donnant des excroissances plates partant de l'angle : défaut A 114 (gale d'angle).

2/ Gale de plancher : 
    
La nappe de métal entrant dans l'empreinte provoque rapidement une zone de condensation d'humidité de faible résistance. Ensuite une avec d'assez fortes contraintes de compression dans la paroi de l'empreinte il se produit une croûte dont la formation est contrariée le long de cette zone. 

2.1.- La croûte ne se sépare pas complètement du sable de remplissage et glisse par suite de la dilatation de la silice sur la région avoisinante de la paroi de l'empreinte. Les bords de cette croûte s'élèvent ce qui produit des queues de rat (R) ou bien, s'ils s'élèvent au point que du métal peut pénétrer sous la croûte, des gales (S).

2.2. - La croûte se soulève entre deux flux de métal liquide puis est comprimée par la continuation de l'arrivée de métal liquide. Si elle ne se rompt pas il se produit seulement un enfoncement de la surface du moulage (défaut D 211). Si elle se rompt et si le métal liquide pénètre dans la cavité qu'elle a laissée, il y a formation d'une gale.""",

"""1/Augmentation de la résistance à vert par :
- plus forte proportion d'agglomérant (argile, bentonite);
- emploi d'une meilleure qualité d'argile (bentonite);
- activation de la bentonite par la soude;
- bon refroidissement du sable en circuit; meilleure préparation du sable (malaxage);
- choix d'un sable plus gros.

2/ Diminution des contraintes de compression : 
    
- remplissage de l'empreinte plus rapide et plus régulier;
- éviter une trop forte humidité du sable; 
- emploi d'additifs qui par ramollissement ou combustion compensent la dilatation de la silice: poussier de charbon, brai, bitume. N'utiliser néanmoins qu'avec précaution les additifs qui ont une forte action ramollissante tels que la farine de tourbe et la farine de bois car leur emploi entraîne une diminution de la résistance à vert du sable; 
- remplacement total ou partiel du sable siliceux par des sables réfrac taires à faible dilatation et ne comportant pas, comme la silice, des transformations allotropiques accompagnées au chauffage de fortes expansions. Le sable de zircon remplit ces conditions.

3/Tirer l'air. Augmenter la perméabilité.

4/ Remèdes généralement à déconseiller : Pointer; incliner le moule; couvrir les parties menacées avec des tôles."""),
                    
                    "D232": ("Comme ci-dessus, mais l'élimination n'est possible que par usinage ou meulage.",
                             
                             "Gale volante.",
                             
"""Surépaisseurs massives irrégulières, de faible ou de forte surface en général de plusieurs mm d'épaisseur à bords irrégulièrement formés ayant un aspect de cassure, avec formation de croûtes multiples, se superposant les unes sur les autres, plus ou moins parallèles à la surface du moulage avec une surface rugueuse. Les surépaisseurs paraissent souvent crevassées par suite d'inclusions de croûtes de sable. Les moulages présentant ce défaut comportent des inclusions de croûtes de sable en général près de la surface supérieure du moulage. Ces surépaisseurs ne peuvent être éliminées que par usinage ou par meulage, en admettant que les inclusions de sable correspondantes puissent être tolérées.

Se produit surtout sur les faces qui correspondent au plancher et au plafond de l'empreinte.""",

"""Le mécanisme de la formation des gales volantes est le suivant : 

1/ Au plafond de l'empreinte ou le long de parois verticales ou inclinées de l'empreinte :

1.1.- Formation d'une zone de condensation d'humidité de faible résistance. Rupture en plusieurs morceaux de cette croûte séchée lorsque sa dilatation est contrariée. Lors du remplissage de l'empreinte ces morceaux de croûte surnagent et vont jusqu'au plafond de l'empreinte. Outre les gales crevassées on trouve aussi des gerces (A 112) ou des queues de rat (D 132).
Voir aussi défaut A 112 (gerces)

2/ Au plancher de l'empreinte.

Le métal liquide provoque rapidement une zone de condensation de faible résistance; par suite des fortes contraintes de compression et de la faible résistance à vert du sable, la croûte se sépare du sable sous jacent et, surtout si le sable a une forte mouillabilité, elle est entraînée par le métal liquide et monte en flottant jusqu'au plafond. Le métal liquide vient remplir la cavité qui s'est formée dans le plancher, d'où une gale volante (S). En outre la croûte vient former des inclusions (E) près du plafond de l'empreinte et il y a souvent des porosites dans la région supérieure de l'empreinte.""",

"""Les mêmes que pour D 231 (gale franche)."""),
                    
                    "D233": ("Excroissances métalliques plates sur des moulages obtenus en moules étuvés passés à la couche ou au noir ou en moules à vert avec des noyaux passés à la couche ou au noir.",
                             
                             "Dartres.",
                             
"""Surépaisseur à la surface du moulage, sous forme aplatie, à surface rugueuse d'un côté et à bords en général aigus. Si elle ne tient au moulage que par une petite surface on peut en général l'éliminer au burin (dartre de noir ou de couche). Sous la dartre la surface du moulage présente une légère dépression. Si la surépaisseur fait corps avec le moulage (dartre déplacée par le courant de métal) on trouve plus ou moins loin une ou des inclusions de sable. Cette surépaisseur ne peut être éliminée que par le meulage à condition que les inclusions correspondantes puissent, par ailleurs, être tolérées.
""",

"""La couche, souvent riche en argile, subit une contraction à chaud alors que le sable siliceux sous jacent se dilate. Si l'adhérence de la couche est insuffisante, ces deux mouvements contraires peuvent provoquer son décollement avec maintien sur place de la pellicule (dartre franche) ou déplacement de celle-ci par le mouvement du métal ou par la gravité (dartre volante).
""",

"""- Couche présentant une faible contraction à chaud.
- Couche d'épaisseur modérée et régulière.
- Couche à pouvoir mouillant élevé, pénétrant dans le sable. Sable présentant une moindre dilatation à chaud (voir D 231 et D 232).
- Séchage correct."""),
                    
                "D240": "Adhérence d'oxydes à la suite de traitement thermique (recuit, revenu, malléabilisation pr décarburation).",
                
                    "D241": ("Adhérence d'oxyde après recuit.",
                             
                             "Calamine.",
                             
"""Couche d'oxyde adhérente qui en général ne s'effrite que sous l'effet de chocs ou de flexions répétés. Dans certains cas cette couche est si adhérente qu'elle ne se révèle qu'après rupture de la pièce. La coloration due à ce défaut n'est pas reconnaissable après grenaillage.
""",

"""- Atmosphère oxydante lors du recuit.
- Le four n'est pas étanche.""",

"""- Contrôler l'atmosphère du four et son étanchéité.com
- Éviter le chargement de pièces ou de matériel humide D 243)."""),
                    
                    "D242": ("Adhérence de minerai après recuit de malléable à coeur blanc.",
                             
                             "Collage de minerai.",
                             
"""Présence de minerai en moulages en partie fondu fortement adhérent à la surface des malléable à coeur blanc, traités au minerai.""",

"""- Température de recuit Minerai trop fusible. trop élevée.
- Minerai en morceaux trop fins.""",

"""- Contrôler soigneusement la température lors du recuit. 
- Employer du minerai présentant une température de ramollissement élevée.
- Éviter l'emploi de minerai comportant une forte proportion de fines.
- La grosseur optimale des grains va de 5 à 15 mm."""),
                    
                    "D243": ("Ecaillage après recuit de malléable à coeur blanc.",
                             
                             "Ecaillage.",
                             
"""Séparation de couches parallèles à la surface à la suite du recuit en atmosphère oxydante.
""",

"""Sulfuration de la région superficielle du moulage par une atmosphère contenant de l'anhydride sulfureux ou de l'hydrogène sulfuré. L'anhydride sulfureux peut aussi provenir de l'oxydation des sulfures contenus dans la fonte au début du traitement de malléabilisation. La phase riche en sulfure de fer qui peut en résulter est liquide aux températures habituelles de malléabilisation. Avec la progression de la décarburation elle peut pénétrer dans le moulage principalement par les joints de grains et former en fonction de la teneur en silicium un réseau plus ou moins serré de sulfures.

Dans la région extérieure au réseau de sulfure, zone fortement décarbu rée, il se forme des oxydes contenant du manganèse et du silicium dont la formation est accompagnée d'une augmentation de volume. La structure devient lâche, jusqu'à la formation de cavités.

La couche extérieure jusqu'à la zone de cavités peut éclater au refroidissement du moulage. Une deuxième écaille, dans la région du réseau de sulfure se forme, seulement quand la pièce subit une déformation. La résistance du réseau de sulfures est très faible (couche intermédiaire fine non métallique très fragile).

Il est possible également que, par suite d'une atmosphère de recuit très oxydante dans le domaine de la formation de FeO des inclusions de sulfures soient immédiatement oxydées d'où libération de SO₂ qui provoque un nouveau réseau de sulfures. Le silicium et le manganèse de la couche extérieure sont aussi scorifiés à l'état de silicate de manganèse.

Ces conditions conduisent à une large zone superficielle à structure lâche, plutôt qu'à un alignement de trous""",

"""- Diminuer la teneur en silicium de l'alliage.
- Diminuer la teneur en soufre de l'alliage ou augmenter la teneur en manganèse. 
- Veiller à ce que le minerai soit pauvre en soufre, éventuellement diminuer la proportion de minerai neuf. 
- Diminuer la teneur en soufre de l'atmosphère du four.
- Contrôler l'étanchéité des pots."""),
                    
        "E": "E - Pièce incomplète.",
        
            "E100": "E100 - Partie manquante sans cassure.",
            
                "E110": "Ecarts minimes par rapport au tracé.",
                
                    "E111": ("La pièce est, dans l'ensemble, complète à l'exception d'arêtes plus ou moins arrondies.",
                             
                             "Malvenu.",
                             
"""La pièce est complète à l'exception des angles saillants qui sont plus ou moins arrondis. S'agissant de fonte, la surface est généralement brillante et se laisse bien décaper.""",

"""- Manque de fluidité et de coulabilité du métal liquide dû à une température de coulée trop basse eu égard à la composition. 
- Remplissage trop lent de l'empreinte par suite d'une trop faible section des jets et des attaques.
- Dégagements d'air insuffisant (perméabilité, évents, tirages d'air). - En coulée en coquille : température trop basse de la coquille.""",

"""- Régler la température de coulée assez haut, eu égard à la composition chimique de l'alliage et aux épaisseurs du moulage.
- Vérifier le système d'attaque et augmenter les sections s'il y a lieu. 
- En coulée en coquille : élever la température de la coquille.
- Améliorer la perméabilité et les dispositifs de dégagement des gaz."""),
                    
                    "E112": ("Arêtes ou contours déformés par la suite de mauvaises retouches du moule ou de passage à la couche défectueux.",
                             
                             "Défauts de réparation ou de passage à la couche.",
                             
"""En certains endroits, les angles saillants ou rentrants sont irrégulièrement arrondis, ou manquent complètement alors que les formes avoisinantes correspondent bien à celles du modèle.
""",

"""Réparations mal exécutées, enduit irrégulièrement appliqué sur les moules et noyaux, formant des protubérances dans l'empreinte et laissant des traces dans le moulage, souvent sous forme de gouttes.
""",

"""Soins dans les réparations des moules et dans le passage de la couche.
"""),
                    
                "E120": "Ecarts importants par rapport au tracé.",
                
                    "E121": ("Pièce incomplète par suite de solidification prématurée.",
                             
                             "Manque.",
                             
"""Une partie de la pièce manque, généralement à la partie supérieure du moule ou dans une région éloignée des coulées. Les arêtes à l'endroit du défaut sont arrondies. Les surfaces avoisinant le défaut en général sont brillantes. Les jets de coulée, chenaux, attaques sont bien remplis (différence avec le défaut E 122).""",

"""- Température de coulée trop basse. Fluidité et coulabilité du métal insuffisantes.
- Système d'attaque de section insuffisante ou mal conçu eu égard à la forme du moulage.
- En moulage en coquille : température trop basse de la coquille, départs d'air insuffisants.

Nota: Ne pas confondre avec les défauts E 122 et E 123.""",

"""- Élever la température de coulée.
- Modifier la conception ou les dimensions du système de coulée.
- Prévoir des tirages d'air plus efficaces. 
- Élever la température de la coquille.
- Si les conditions le permettent, s'entendre avec le client pour augmenter les épaisseurs de la pièce."""),
                    
                    "E122": ("Pièce incomplète par insuffisance de métal.",
                             
                             "Coulé court.",
                             
"""La partie supérieure du moulage manque. voisinage de la partie manquante sont légèrement arrondies, tous les autres contours sont conformes au modèle. Le jet de coulée, Les arêtes au les masselottes et évents situés latéralement ne sont remplis que jusqu'au niveau limite de remplissage de la pièce (principe des vases communiquants) (contrairement à ce qui se passe pour le défaut E 121).""",

"""- Quantité insuffisante de métal liquide dans la poche.
- Interruption prématurée de la coulée par suite d'une erreur de l'ouvrier qui croit que le moule est rempli du fait d'une section d'attaque insuffisante par rapport à celle du jet et du chenal.

Nota: Ne pas confondre avec les défauts E 121 et E 123.""",

"""- Préparer une quantité suffisante de métal.
- Vérifier le système d'attaque.
- Instructions au couleur et surveillance."""),
                    
                    "E123": ("Pièce incomplète par suite de fuite de métal hors du moule.",
                             
                             "Moule vidé.",
                             
"""Une partie de la pièce manque. La surface supérieure est en général concave et se prolonge souvent en bavure tapissant plus ou moins les parois du moule.

La partie manquante peut d'autre part, surtout pour des moulages épais, être localisée à l'intérieur de la pièce qui semble s'être vidée. Ne pas confondre avec E 121 (manque) ou E 122 (coulé court).""",

"""- Étanchéité insuffisante du moule ou résistance insuffisante des parois du moule et des noyaux (surtout pour les moulages épais) ces parois venant à se rompre sous l'effet d'une forte pression métallostatique.
- Des ouvertures de montage du moule ou du noyau n'ont pas été fermées par suite d'une négligence.
- Les évents pour départ d'air des noyaux ont été mal tamponnés. 
- Les surfaces des plaques modèles de la partie de dessus et de la partie de dessous ne se correspondent pas. Dans le moulage à main raccord de joint mal fait; dans le moulage à la machine plaque-modèle mal-propre.
- Le moule a été mal crampé ou insuffisamment chargé (voir aussi défaut A 121).
- Le décochage a été effectué prématurément.

Nota: Dans le cas d'un moule mal crampé ou insuffisamment chargé, ce défaut se produit en même temps que le défaut A 121 (soulèvement de moule).""",

"""Remédier aux causes possibles indiquées ci-dessus."""),
                    
                    "E124": ("Manque de matière important par suite d'un grenaillage exagéré.",
                             
                             "Grenaillage excessif.",
                             
"""Manque de matière sur les surfaces plates de certaines pièces d'arêtes observés seulement après grenaillage, dans n'importe quelle région du moulage. ou manque
""",

"""- Fort enlèvement de métal par suite d'un grenaillage trop intense dû à un défaut du matériel ou à une négligence du personnel.""",

"""Limiter le grenaillage dans l'ensemble ou localement. Veiller au bon fonctionnement du matériel."""),
                    
                    "E125": ("Moulage partiellement fondu ou profondément déformé au cours du recuit.",
                             
                             "Fusion ou effondrement au recuit.",
                             
"""Après le recuit, il manque une partie en général saillante, de la pièce qui semble avoir été partiellement fondue ou bien toute la pièce s'est effondrée et a perdu ses contours. On trouve le métal manquant sous forme de gouttes ou de masse informe contre le moulage ou à proximité de celui-ci""",

"""- Trop haute température de recuit.""",

"""- Régler la température de recuit de façon à atteindre mais à ne pas dépasser celle qui est nécessaire pour obtenir la modification de struc ture désirée, compte tenu de la composition de l'alliage.
- Contrôler constamment la température effective de recuit."""),
                    
            "E200": "E200 - Partie manquante avec cassure.",
            
                "E210": "Pièce cassée.",
                
                    "E211": ("Pièce cassée, partie manquante importante. Cassure non oxydée.",
                             
                             "Cassure à froid.",
                             
"""Une partie du moulage manque. A l'endroit du défaut la pièce présente un aspect de cassure(voir aussi défaut C 111).

Se produit dans toutes les régions de la pièce, de préférence aux parties saillantes : nervures, bossages, angles saillants.""",

"""- Décochage brutal.
- Manutention défectueuse, choc.
- Souvent aussi suite d'une fêlure à froid (défaut C 111).""",

"""Soin dans le décochage et les manutentions.
"""),
                    
                "E220": "Pièce ébréchée.",
                
                    "E221": ("Cassure de dimension limitée au voisinage des attaques, évents, etc. Angle cassé ou maté.",
                             
                             "Jet, masselitte ou évent cassé dans la pièce. Epaufrure.",
                             
"""Dans la région de l'attache des jets, évents, masselottes sur la pièce, il y a une cassure de forme irrégulière dont la surface pénètre à l'intérieur de la pièce. La surface de la cassure peut être oxydée.""",

"""- Les attaques, évents et masselottes ont été prévus trop grands, ou ne sont pas entaillés au col, ou le sont, mais insuffisamment. 
- L'ébarbage a été effectué trop brutalement eu égard aux dimensions du moulage, ou maladroitement.""",

"""- Dimensionner de façon correcte l'attache ou le col des attaques, évents et masselottes, en tenant compte de l'épaisseur du moulage. 
- Éventuellement, prévoir un étranglement, un noyau d'étranglement.
- Procéder correctement au décochage, à la manutention et à l'ébarbage
- Avant de casser les jets, évents et masselottes, exécuter une entaille à l'aide d'une meule tronçonneuse."""),
                    
                "E230": "Pièce cassé avec cassure oxydée.",
                
                    "E231": ("L'aspect de la cassure montre qu'elle a subi une oxydation à chaud.",
                             
                             "Cassure à chaud.",
                             
"""Le moulage est cassé en plusieurs morceaux; la cassure est fortement oxydée dans le cas des alliages ferreux.""",

"""La pièce a été décochée trop tôt, les régions épaisses de la pièce, ou même toute la pièce, n'étant pas encore complètement solidifiées ou se trouvant à l'état pâteux.""",

"""Prolonger le refroidissement dans le moule."""),

        "F": "F - Dimensions ou forme incorrectes.",
        
            "F100": "F100 - Dimensions incorrectes mais forme correcte.",
            
                "F110": "Les cotes sont fausses dans l'ensemble.",
                
                    "F111": ("Toutes les cotes sont fausses dans une même proportion.",
                             
                             "Erreur dans la prévision du retrait.",
                             
"""Toutes les dimensions du moulage sont inexactes, mais dans une même proportion par rapport aux dimensions désirées.
""",

"""Le retrait prévu lors de l'exécution du modèle diffère du retrait réel de l'alliage employé.
""",

"""Établir ou modifier le modèle en se basant sur le retrait réel de la pièce,
retrait établi par des mesures directes préalables."""),
                    
                "F120": "Les cotes sont fausses, mais seulement en partie.",
                
                    "F121": ("Trop grandes distances entre parties fortement saillantes.",
                             
                             "Retrait contrarié.",
                             
"""Les dimensions sont exagérées dans un sens où le moule, les noyaux ou les armatures offrent une résistance au retrait anormalement élevée.""",

"""- Serrage exagéré du moule ou des noyaux. 
- Sable trop chargé en argile.
- Noyaux contenant une proportion d'agglomérant trop forte. 
- Armatures surabondantes ou mal disposées.

Dans les pièces minces, sable rugueux offrant à la pièce une possibilité d'accrochage qui s'oppose au retrait.
Une pièce présentant ce défaut risque en outre d'être le siège de tensions internes et d'être sujette à crique ou à tapure (C 221-C 222).""",

"""- Ne pas trop serrer le moule dans le cas du moulage à vert ou diminuer la proportion de liant ou d'agglomérant dans les autres cas. 
- Améliorer la possibilité de désagrégation des moules ou noyaux étuvés ou durcis, par exemple à l'aide d'additifs appropriés.
- Intercaler dans la masse du sable des produits susceptibles de s'écraser sous l'effet du retrait : coke, paille, polystyrène, ou simplement espace vide.
- Contrôler la position des armatures, crochets ou autres renforcements. 
- Si les conditions le permettent, obtenir du client une modification du tracé."""),
                    
                    "F122": ("Certaines cotes sont inexactes.",
                             
                             "Retrait irrégulier.",
                             
"""Le taux de retrait est plus élevé dans les parties épaisses de la pièce.
""",

"""Pour un même alliage, le retrait peut varier en fonction des structures qui peuvent elles-mêmes dépendre d'un refroidissement plus ou moins rapide.

D'où la possibilité de taux de retrait variés entre des pièces d'épaisseur différentes, entre les diverses parties d'une même pièce thermiquement hétérogène, ou encore entre des pièces coulées dans des moules de conductibilités différentes.""",

"""- Série :
Modifier le modèle en se basant sur le retrait réel des diverses parties de la pièce type coulée dans les conditions de la fabrication de série.

- Pièce unitaire :
Expérience préalable effectuée une fois pour toutes sur éprouvettes d'épaisseurs diverses dans les conditions de moulage de coulée et avec l'alliage envisagés."""),
                    
                    "F123": ("Les cotes sont trop grandes dans le sens de l'ébranlage.",
                             
                             "Excès d'ébranlage.",
                             
"""Les dimensions sont exagérées dans le sens de l'ébranlage.
""",

"""Non renseigné""",

"""-Ébranler avec précaution.
- Mettre une dépouille suffisante.
- Disposer correctement les plaques d'ébranlage."""),
                    
                    "F124": ("Les cotes sont trop grandes dans le sens perpandiculaire au plan de joint.",
                             
                             "Dilatation du moule à l'étuvage.",
                             
"""Les dimensions de la pièce perpendiculairement au plan de joint sont trop fortes.
""",

"""Sable trop gras ou trop humide qui, à l'étuvage, gonfle et déborde du châssis.

Nota: Ne pas confondre avec le défaut A 121 (soulèvement de moule).""",

"""- Amaigrir le sable par addition de sable siliceux.
- Éviter de mouiller exagérément le moule après démoulage."""),
                    
                    "F125": ("Surépaisseurs irrégulières sur quelques faces externes. Identique à A211 (forçage).",
                             
                             "Serrage irrégulier. Serrage insuffisant.",
                             
"""Identique à A211""",

"""Identique à A211""",

"""Identique à A211"""),
                    
                    "F126": ("Parois d'épaisseur inférieure à la cote, surtout s'agissant de surfaces horizontales.",
                             
                             "Modèle ou plaque mmodèle déformé. Voile.",
                             
"""Épaisseurs insuffisantes dans les grandes surfaces, horizontales au moment du serrage.
""",

"""La rigidité du modèle ou de la plaque modèle n'est pas suffisante eu égard à la pression de serrage du sable. Il en résulte une déformation élastique du modèle avec une déformation permanente correspondante de l'empreinte.

En vue du diagnostic, comparer les surfaces du modèle au repos avec les surfaces du moule.""",

"""Contrôler la rigidité des plaques modèles et modèles, notamment lorsqu'on augmente les pressions de serrage."""),
                    
            "F200": "F200 - Forme incorrecte dans l'ensemble ou dans certaines parties du moulage.",
            
                "F210": "Modèle incorrect.",
                
                    "F211": ("Le moulage ne correspond pas au tracé soit dans son ensemble, soit dans certaines régions. Il en est de même du modèle.",
                             
                             "Modèle incorrect.",
                             
"""Le moulage ne correspond pas au dessin, localement ou dans l'ensemble. Le contrôle montre que le modèle ne correspondait pas au dessin.
""",

"""- Manque de précision du dessin.
- Malfaçon lors de l'exécution du modèle.
- Manque de contrôle du modèle avant livraison.""",

"""Contrôler le dessin et le modèle au modelage.
"""),
                    
                    "F212": ("En un endroit bien déterminé le moulage ne correspond pas au tracé. Le modèle est correct.",
                             
                             "Erreur de montage du modèle.",
                             
"""Le moulage ne correspond pas au dessin dans une ou plusieurs régions. L'enquête montre qu'il y a eu confusion dans la mise en place des parties démontables.""",

"""Des parties démontables de modèle n'ont pas été munies de repères ou ne l'ont pas été de façon indiscutable.""",

"""- Repérer les parties de modèle avec des traits de montage ou des couleurs ou des numéros.
- Prévoir des modes d'assemblage non susceptibles de confusion.
- Montage du modèle avec le dessin en main."""),
                    
                "F220": "Variation.",
                
                    "F221": ("La pièce semble avoir subi un commencement de cisaillement dans le plan de joint.",
                             
                             "Variation de :\n - modèle \n - portée \n - plaque-modèle \n - moule \n - coquille \n Déformation de châssis. Déplacement de moule.",
                             
"""La pièce semble avoir subi un commencement de cisaillement. Les saillies opposées sont égales et de sens contraire; de part et d'autre du plan de cisaillement la forme de la pièce est correcte.""",

"""- Mauvais repérage jeu dans les ou assemblages du modèle
- Mauvais repérage ou jeu dans les portées
- Mauvais repérage ou jeu dans une plaque-modèle
- Jeu exagéré dans les châssis, non compensé par des artifices de repérage («soleil », repères, etc.). Mauvais repérage ou jeu dans une coquille 
- Précision des outillages correcte mais châssis faiblement dimen sionnés par rapport à la pression de serrage
- Défaut non systématique sem blant se rattacher à un accident survenu au moule remmoulé
- Mauvais repérage ou jeu dans les assemblages d'une boîte à noyau.""",

"""Non renseigné"""),
                    
                    "F222": ("Variation sur une face interne d'une pièce dans le plan de joint du noyau.",
                             
                             "Variation de noyau.",
                             
"""Les deux parties des cavités du moulage formées par un noyau présentent dans le plan de joint du noyau (plan correspondant au plan de joint de la boîte) une translation relative; mais, prises séparément, elles correspondent bien au dessin en ce qui concerne la forme et les dimensions.""",

"""Non renseigné""",

""" Munir la boîte à noyau de repères corrects.
- Limiter le jeu des assemblages de la boîte à noyau.
- Ajuster exactement les éléments dans le cas de noyaux collés."""),
                    
                    "F223": ("Saillie irrégulière généralement unilatérale sur des faces verticales, en général au voisinage du plan de joint.",
                             
                             "Fausse variation.",
                             
"""Épaississement de la pièce au voisinage du joint (a) ou d'une surface parallèle au joint (b). Ressemble au défaut F 221 (variation) dont il diffère par le fait que les déformations ne sont pas nécessairement égales et de sens contraire de part et d'autre du joint. Le défaut peut encore être appelé du nom plus général de «fausse serre ».""",

"""Un mauvais serrage du moule a écarté le sable de certaines faces verticales du modèle.
""",

"""Examiner en détail les conditions de serrage.
"""),
                    
                "F230": "Déformation à partir d'une forme correcte.",
                
                    "F231": ("Déformation par rapport au tracé sur le moulagen le moule et le modèle.",
                             
                             "Modèle déformé.",
                             
"""Le moulage présente des déformations localisées ou générales par rapport au dessin, mais pas par rapport au modèle qui est lui-même déformé de la même façon. Ces déformations sont systématiques.""",

"""Non renseigné""",

"""- Vérifier la construction du modèle.
- Utiliser un bois de qualité et d'essence appropriées à cet usage. 
- Choisir une classe de modèle appropriée au genre de pièces et au mode de fabrication. -
- Entreposer les modèles dans un local dont la température et l'humidité sont constantes. 
- Gerber les modèles avec soin en utilisant des cales convenables.
- Ne pas voiler le modèle ou la plaque modèle au moment du montage dans la machine à mouler ou sur le chantier. 
- Éviter que le modèle prenne l'humidité du moule grâce à un vernissage correct avec un vernis adéquat et en limitant le temps de séjour du modèle dans le moule."""),
                    
                    "F232": ("Déformation par rapport au tracé sur le moulage et le moule. Le modèle est conforme au tracé.",
                             
                             "Moule déformé.",
                             
"""Le moulage présente par rapport au dessin et au modèle des déformations générales ou locales non systématiques.
""",

"""- Le modèle ou la plaque-modèle est l'objet d'une contrainte locale exagérée lors du serrage et subit une déformation élastique. 
- Le modèle ou la plaque-modèle est placé sur un support ou un chantier gauche ou insuffisamment rigide.
- Le moule a été déformé avant coulée par suite d'une déformation du châssis (par exemple au cours du transport). 
- Pose du moule sur une surface non plane.
- Déformation pendant le transport, rigidité insuffisante du châssis. 
- Chargement exagéré ou irrégulier du moule.
- Crampage défectueux.
- Serrage insuffisant dans l'ensemble ou en certains endroits.""",

"""- Placer le modèle sur un sol bien plan. Dans le cas d'une surface de joint non plane préparer une fausse partie précise. S'agissant de plaques modeles montées sur un support, veiller à ce que ce support soit plan, que ele serrage soit bien régulier.
- Couler des pièces d'essai et les vérifier.
- Renforcer les modèles légers par des « barres à boucher»
- Exécuter les portées de noyau de telle façon qu'ils contribuent à la rigidité. Monter les modèles sur plaque. Renforcer les plaques-modèles par des nervures.
- Placer le moule sur un lit bien plan et également résistant. 
- Choisir des châssis suffisamment rigides.
- Les poids de charge doivent être supportés par les parois latérales des châssis et intéresser des surfaces de joint suffisamment importantes.
- Prévoir l'importance de la cambrure par le calcul et par l'expérience.
- Serrer le moule autant qu'il est nécessaire, éventuellement changer de matériau de moulage.
- Disposer correctement les ancrages."""),
                    
                    "F233": ("Déformation du moulage par rapport au tracé. Le moule et le modèle sont conformes au tracé.",
                             
                             "Déformation au retrait.",
                             
"""La pièce présente dans l'ensemble ou localement des déformations par rapport au dessin, au modèle et au moule, déformations qui peuvent se répéter plus ou moins régulièrement surtout dans les régions comportant des différences d'épaisseur.""",

"""- Retrait contrarié :
    
• par le tracé de la pièce,
• par les masselottes et attaques, 
• par des parties de moule et noyaux.

- Mauvaise technique d'attaque et de coulée. 
- Retrait irrégulier causé par un décochage prématuré.""",

"""- Modifier le tracé pour tenir compte des impératifs techniques.
- Choisir la technique de coulée et d'attaque de façon que la répartition de la température dans la pièce soit aussi régulière que possible. Déterminer le temps de coulée et la température de coulée corrects. Prévoir des dégorgeoirs.
- Dégager les masselottes et attaques après la coulée.
- Disposer des noyaux d'écrasement.
- Laisser le moulage se refroidir dans le moule.
"""),
                    
                    "F234": ("Déformation du moulage par rapport au tracé.",
                             
                             "Déformation différée.",
                             
"""Déformation de la pièce par rapport à sa forme initiale après stockage, recuit, usinage.
""",

"""- Après stockage prolongé ou usinage : il s'agit de libération plus ou moins complète de contraintes résiduelles.
- Après traitement thermique général ou localisé : il s'agit soit de libération de contraintes, soit de l'un des facteurs suivants :

• température excessive ou hétérogène, 
• calage défectueux,
• alliage de rigidité insuffisante à chaud, 
• conception de pièce rendant leur empilage et leur calage difficile,
• trempe trop intense, 
• trempe dissymétrique,
• évolution de l'état structural de l'alliage à la température ordinaire.""",

"""Concernant les contraintes, il convient en premier lieu de les éliminer ou de les réduire par un tracé convenable de la pièce et par un système d'alimentation permettant un refroidissement aussi homogène et aussi lent que possible.

Concernant les autres causes, les remèdes sont évidents."""),
                    
        "G": "G - Inclusions ou anomalie de structure.",
        
            "G100": "G100 - Inclusions.",
            
                "G110": "Inclusions métalliques.",
                
                    "G111": ("Inclusions métallique dont l'aspect, l'analyse chimique ou l'examen structural montrent qu'il s'agit d'un élément étranger à l'alliage.",
                             
                             "Inclusion métallique d'origine extérieure, \ncombinaison intermétallique.",
                             
"""Inclusions métalliques ou intermétalliques de diverses grandeurs qui différent nettement du matériau de base par la structure et la couleur, mais surtout par les propriétés. Ces défauts apparaissent le plus souvent lors de l'usinage.""",

"""- Combinaisons intermétalliques avec des métaux étrangers (impuretés étrangères).
- En coulée par gravité ou sous pression d'alliages d'aluminium, surtout d'alliage Al-Si (Cu) contenant du fer composés intermétalliques (Fe, Al, Mn, Si) sous forme de grains ou d'aiguilles provenant d'une tempé rature trop basse du bain dans le creuset de maintien, en moyenne ou localement. Enrichissement en fer provenant du creuset.
- Éléments d'alliage ou de préalliage (par ex. ferro-alliages) qui ne se sont pas complètement dissous dans le bain.
- Supports de noyaux.
- Lors de la solidification, il se produit une ségrégation de composés intermétalliques insolubles qui se concentrent dans le liquide résiduel.
- Éléments d'alliage incomplètement dissous, alliages-mères ou métaux étrangers introduits accidentellement et inclus lors de la solidification.""",

"""- Veiller à la propreté des charges, éliminer les métaux étrangers.
- Employer des éléments d'alliage ou des alliages-mères en morceaux de petite dimension. Veiller à ce que le bain soit assez chaud lorsqu'on procède à l'addition. Un brassage énergique accélère la dissolution. Ne pas faire ces additions à un moment trop proche de la coulée.
- S'agissant d'alliages non ferreux, protéger les creusets en fonte à l'aide d'un enduit approprié. 
- En coulée d'alliages d'aluminium par gravité et sous pression,veiller à ce que la température de maintien soit assez élevée. 
- Décanter soigneusement à la coulée pour éviter d'entraîner le dépôt du fond du creuset."""),
                    
                    "G112": ("Inclusion de même composition chimique que le métal de base, en général sphérique et souvent enveloppée d'une couche d'oxyde.",
                             
                             "Goutte froide.",
                             
"""Inclusion métallique généralement sphéroïdale située à la partie inférieure des moulages. Sa composition chimique est identique à celle de la pièce. La surface est généralement oxydée.
""",

"""Des gouttes de métal tombées prématurément dans le moule se sont solidifiées et ne se sont pas soudées au métal coulé ultérieurement. Ne pas confondre avec le défaut G 113 (ressuage interne).""",

"""- Protéger les orifices du moule contre les projections.
- Disposer correctement jets et masselottes (espacement et niveaux respectifs).
- Couler avec précaution."""),
                    
                    "G113": ("Inclusions métalliques sphériques dans des soufflures ou autres cavités du moulage ou dans les affaissements de la surface (voir alors défaut A 311). La composition s'apparente à celle de l'alliage coulé mais avec des différences qui la rapprochent de celle de l'eutectique.",
                             
                             "Ressuage interne; diamant : goutte phosphoreuse; (fonte).",
                             
"""Inclusion métallique, généralement sphérique à surfaces lisses, souvent brillantes. On la rencontre à l'intérieur des soufflures ou autres défauts internes qu'elle remplit totalement ou partiellement. Cette inclusion a généralement une composition chimique différente de celle du métal de base et se rapprochant de la composition de l'eutectique. C'est ce qui permet de la distinguer du défaut G 112 (goutte froide).
""",

"""L'eutectique qui se rassemble aux joints des grains en fin de solidification peut être expulsé vers les espaces libres; soit vers les surfaces extérieures où il donne lieu au défaut A 311 (ressuage externe), soit vers les soufflures ou autres défauts internes pour donner le défaut G 113 (ressuage interne). Cette expulsion est provoquée par la pression due à la graphiti sation eutectique dans le cas de la fonte ou au dégagement de ou encore à la contraction de la partie de pièce solidifiée qui commence son retrait. Dans le cas de la fonte ces gouttes sont souvent plus riches en gaz dissous phosphore que la masse de la pièce, d'où leur nom. Elles présentent une grande dureté et peuvent susciter des incidents à l'usinage.
""",

"""Le meilleur remède consiste à éliminer les défauts primaires : soufflures ou autres cavités sans lesquelles le défaut G 113 ne peut se produire.
"""),
                    
                "G120": "Inclusions non métalliques, laitier, scories, flux.",
                
                    "G121": ("Inclusions non métalliques dont l'aspect ou l'analyse montrent qu'elles proviennent des laitiers d'élaboration, \ndes produits de traitement ou des flux.",
                             
                             "Inclusions de laitier, de produits de traitement, de flux.",
                             
"""Inclusions non métalliques de forme irrégulière ayant l'aspect et la composition des laitiers des fours de fusion ou de traitement (par exemple carbure, produit d'affinage dans le cas de métaux légers) situées à la surface du moulage (laissant à l'ébarbage une cavité irrégulière) ou dans la paroi (et alors visibles à l'usinage). S'il y a des soufflures voir défaut G 122.

Elles apparaissent le plus souvent sur les surfaces supérieures des moulages, près des noyaux ou dans les saillies du moule.""",

"""Laitier de l'appareil de fusion ou laitier de traitement par exemple laitier au carbure ayant servi à la désulfuration ou flux de traitement d'alliage non ferreux entraîné lors de la coulée.

La scorie s'accumule à la partie supérieure de l'empreinte ou reste accrochée, pendant sa montée, dans les angles ou contre les noyaux où elle est emprisonnée à la solidification.""",

"""- Lors du remplissage de la poche, éviter les entraînements de scories venant de l'appareil de fusion. 
- Décrasser la poche et éventuellement épaissir le laitier avec du sable siliceux propre et sec ou mieux, avec de la chaux. 
- Pendant la coulée retenir le laitier dans la poche, de préférence en employant une poche-siphon ou une poche à quenouille.
- Maintenir pleins pendant toute la coulée les entonnoirs ou bassins de coulée.
- Employer des noyaux-filtres.
- Prévoir des pièges à crasses, par exemple des pièges à circuit tangentiel.
- Disposer les faces destinées à être usinées à la partie inférieure moule."""),
                    
                    "G122": ("Inclusions non métalliques en général imprégnées de gaz \net accompagnées de soufflures (B 113).",
                             
                             "Inclusion de scorie congénitale, mousse, soufflures de scories.",
                             
"""Inclusions non métalliques souvent associées à des soufflures dans les inclusions et dans la masse de la pièce.

Réparties dans la pièce mais le plus souvent dans la partie supérieure du moule ou accrochées aux angles rentrants ou aux noyaux.

L'analyse chimique révèle de fortes teneurs en soufre ainsi qu'en oxydes de silicium, fer et manganèse avec des teneurs en chaux voisines de zéro. 

L'examen micrographique ou même visuel laisse parfois apparaître une phase de silice pure en grains blancs qui ne doit pas être confondue avec une inclusion de sable""",

"""Réactions complexes au sein de l'alliage liquide entre ses divers consti tuants (carbone, silicium, manganèse, soufre, aluminium, titane, etc.) leurs oxydes, l'atmosphère, les éléments constituant la poche, le moule ou leurs revêtements.

Ces réactions remontent souvent à l'élaboration du métal voire à la qualité ou au mode d'élaboration des matières premières.""",

"""- Utiliser des matières premières peu chargées en oxydes métalliques internes (inclusion) ou externes (rouille). 
- Éviter les basses teneurs en silicium et les hautes teneurs en manganèse avec, si possible, Si Mn + 0,5%.
- Limiter les teneurs en aluminium et en titane.
- Teneur en soufre inférieure à 0,1%.
- Élaborer et piquer le métal à haute température.
- Attendre la température correcte pour couler le moule. 
- Couler rapidement avec un système d'alimentation évitant la turbulence."""),
                    
                "G130": "Inclusions non métalliques, matériau de moule ou de noyau.",
                
                    "G131": ("Inclusion de sable en général très près de la surface du moulage.",
                             
                             "Inclusion de sable.",
                             
"""Inclusions de sable de forme irrégulière, le plus souvent compactes au voisinage de la surface supérieure du moulage. Souvent visibles sur le moulage brut de coulée, mais pouvant n'apparaître qu'à l'usinage. En général, il y a en d'autres endroits de la pièce, des excroissances métalliques massives (sous-groupe de défauts A 220).

Comme ci-dessus, mais il y a des cavités de 2 à 6 mm d'épaisseur, plus ou moins développées, avec en général des inclusions de sable attenantes. Ce défaut apparaît toujours en même temps que les défauts du sous-groupe D 230 (gales).""",

"""- Morceaux détachés du moule ou des noyaux (sous-groupe A 220). 
- Manque de soin au moulage (sous-groupe F 230). -
- Érosion ou frottes (défauts A 212, A 213). 
- Croûtage du sable dû à la dilatation de la silice (défaut D 230-gale).""",

"""Voir sous-groupe A 220, sous-groupe D 230 et défauts A 212-A 213."""),
                    
                    "G132": ("Inclusion de noir ou de couche en général très près de la surface du moulage.",
                             
                             "Inclusion de noir ou de couche.",
                             
"""Inclusion de peau en génér au-dessous de la surface du moulage dans les régions supérieures du moule. En d'autres endroits du moulage, il y a des excroissances peu saillantes correspondant à l'épaisseur de la couche décollée.""",

"""Parcelles de couche de noir ou d'enduit exfoliée, détachée et surnageant à la surface du métal liquide lors de sa montée dans le moule.""",

"""- Employer une couche ou un enduit dont le coefficient de dilatation thermique est voisin de celui du matériau constituant le moule.
- Ne pas employer de noir liquide sur les moules ou noyaux chauds.
- Limiter l'épaisseur du noir. 
- Réduire la teneur en argile du noir."""),
                    
                "G140": "Inclusions non métalliques, oxydes et produit de réaction.",
                
                    "G141": ("Taches noires irrégulières, nettement délimitées dans la cassure defonte à graphite sphéroïdal.",
                             
                             "Taches noires.",
                             
"""La cassure présente des taches noires nettement délimitées de forme irrégulière ayant quelques millimètres à quelques centimètres dans leur plus grande dimension; surtout dans les épaisseurs supérieures à 25 mm et dans les régions hautes du moulage.

Les caractéristiques mécaniques sont très mauvaises.""",

"""Très haute teneur du bain en oxydes et sulfures.
""",

"""- Éviter les fontes neuves à très basses teneurs en silicium. 
- Limitation sévère de la teneur en soufre du bain avant le traitement au magnésium (moins de 0,01%). 
- Emploi de teneur en magnésium aussi faible que possible.
- Limitation de la teneur en aluminium.
- Température de coulée aussi élevée que possible.
- Addition de cryolithe ou d'autre produit favorisant la coagulation des crasses.
- Emploi de poche-siphon.
- Réduction de la turbulence lors du transfert et de la coulée du métal liquide traité au magnésium."""),
                    
                    "G142": ("Inclusions en forme de peau constituées d'oxydes, le plus souvent avec interruption locale de la continuité.",
                             
                             "Inclusion d'oxyde. Peaux d'oxyde.",
                             
"""Inclusions non métalliques ayant la forme de peaux qui constituent une solution de continuité localisée. La couleur correspond à celle du genre d'oxyde qui constitue ces inclusions.
""",

"""Formation de peaux d'oxyde lors du remplissage de la poche ou de la coulée dans le moule, ces peaux restant emprisonnées dans le métal liquide sous l'effet d'un écoulement turbulent.
""",

"""- Éviter l'oxydation du jet de métal.
- Couler autant que possible sans pression et en source.
- Employer des canaux et attaques plans et longs. Pour les non ferreux, coulée sans turbulence avec moule à inclinaison variable.
- S'agissant de fonte G.S., tenir la teneur en magnésium aussi basse que possible.
- En outre, prendre les mêmes précautions que contre le défaut G 121 (inclusion de scories)."""),
                    
                    "G143": ("Peaux plissées au brillant graphitique dans la paroi du moulage",
                             
                             "Peau de graphite brillante.",
                             
"""Minces peaux graphitiques brillantes, bien délimitées, généralement plissées, situées dans une paroi de la pièce et constituant une solution de continuité du matériau. Ne se voient en général que sur la cassure. Ce défaut est souvent accompagné de gerces plus ou moins plissées à la surface du moulage.""",

"""Les carbures d'hydrogène présents dans les produits d'addition ou dans les liants ou agglomérants de moules et de noyaux se gazéifient et subissent un cracking produisant des peaux de carbone brillant dans l'empreinte. Ces peaux sont entraînées et à la solidification sont emprisonnées dans les parois du moulage, surtout lorsque l'écoulement du métal liquide a été turbulent.""",

"""Diminuer dans les matériaux de moulage et de noyautage, la proportion de produits d'addition susceptibles de former du carbone brillant."""),
                    
                    "G144": ("Inclusions dures en coulée d'aluminium par gravité et sous pression.",
                             
                             "Points durs.",
                             
"""Inclusions dures plus ou moins finement dispersées, quelquefois grossières, situées dans toute la pièce, dans le cas de moulage sous pression d'alliage léger. Elles se manifestent surtout à l'usinage ou au traitement de surface.""",

"""Inclusions de corindon, spinelle, carbure de silicium, de constituants intermétalliques riches en fer.""",

"""- Conduite soignée de la fusion.
- Dans certains cas assez long maintien du métal liquide permettant la décantation des inclusions non métalliques. 
- Ne pas employer de creusets en fonte garnis d'un poteyage non approprié.
- N'employer que des alliages purs."""),
                    
            "G200": "G200 - Anomalie de structure (visibles par observation macrographique).",
            
                "G210": "Structure anormale de la fonte à graphite lamellaire.",
                
                    "G211": ("Structure partiellement ou totalement blanche, particulièrement dans les parois minces, les angles saillants et les arrêtes, passant progressivement à la structure normale.",
                             
                             "Trempe primaire. Trempe primaire partielle. Zones blanches. \nArrêtes blanches. Anomalie de dureté.",
                             
"""Structure de fonte blanche, au moins partiellement, surtout dans les parties minces et aux arêtes, passant progressivement à la structure normale. La transition entre partie grise et partie blanche peut être très progressive (trempe primaire normale) ou discontinue avec taches blanches dans le gris et taches grises dans le blanc (trempe primaire à transition truitée).""",

"""Le carbone équivalent et/ou le rapport carbone/silicium ne sont pas appropriés à l'épaisseur des pièces.""",

"""- Inoculer suffisamment.
- Ralentir la vitesse de refroidissement (par exemple, supprimer les bavures qui créent un refroidissement local).
- Limiter et contrôler les teneurs en éléments trempants (chrome par exemple).
- Éviter la surchauffe ou le maintien prolongé à l'état liquide (trempe pri maire à transition truitée)."""),
                    
                    "G212": ("Comme G 211 mais avec passage sans transition à la structure normale.",
                             
                             "Trempe primaire partielle sans transition. Trempe nette.",
                             
"""Zones ayant la structure de fonte blanche, surtout dans les parties minces, aux arêtes ou au voisinage des bavures, mais contrairement au défaut G 211, le passage de la zone blanche à la zone grise a lieu sans transition.
""",

"""Lorsque les causes données pour le défaut G 211 ne sont pas à incriminer: rapport soufre/manganèse trop élevé.
""",

"""La trempe nette n'est pas toujours un défaut. Elle est recherchée au contraire dans certaines applications (cylindres de laminoirs). Elle est favorisée entre autres par un rapport S/Mn élevé.

Pour l'élimination de la partie trempée, avec ou sans transition, voir les remèdes à G 211."""),
                    
                    "G213": ("Zone blanche nettement délimitée dans les parties de la pièce solidifiées en dernier lieu. La structure près de la surface est grise.",
                             
                             "Trempe inverse.",
                             
"""La cassure présente des bords de structure grise normale; le centre ou bien est solidifié sous forme de fonte blanche sans zone de transition ou présente des taches blanches ou encore est grossièrement truité.
""",

"""- Rapport S/Mn trop élevé.
- Haute teneur en hydrogène.
- Haute teneur en titane avec faible teneur ou soufre.""",

"""- Diminution de la teneur en soufre, éventuellement par un traitement désulfurant. Neutralisation du soufre Mn supérieur à 1,75 S + 0,3. par le manganèse :
- Surchauffe et inoculation efficace.
- Diminution de la teneur en hydrogène par l'emploi de poches bien séchées. Étuvage des moules."""),
                    
                "G220": "Structure anormales en malléable.",
                
                    "G221": ("Taches foncées dans le moulage brut; cassure gris-noir à gros grains après traitement.",
                             
                             "Graphite primaire.",
                             
"""Les pièces coulées, avant recuit, ne sont pas intégralement blanches, et elles comportent du graphite primaire. Le défaut est visible sur les cassures qui présentent, avant le traitement, des taches gris foncé dans les parties massives, après traitement, des taches noires à grain grossier.""",

"""- Teneur trop élevée en carbone et silicium eu égard à l'épaisseur des parois. 
- Effet d'inoculation des additions.""",

"""- Éviter de fortes différences d'épaisseur (d'un point à un autre du moulage) ainsi que les accumulations de chaleur qui peuvent résulter d'une technique d'attaque ou de masselottage incorrecte.
- Employer des refroidisseurs. 
- Ajuster la composition aux épaisseurs de parois, en jouant de préférence sur le carbone pour les malléables à cœur noir et sur le silicium pour les malléables à coeur blanc. Veiller à la propreté des constituants des charges et à une conduite correcte de la fusion.
- Ajouter du bismuth (70 g par tonne environ)."""),
                    
                    "G222": ("Malléable à coeur noir. La cassure après recuit fait apparaître une banqde claire brillante de plus \nde 0.5mm d'épaisseur au voisinage de la paroi, avec une région interne foncée.",
                             
                             "Couche superficielle dure de faible.",
                             
"""La cassure présente après recuit une bordure claire et brillante contrastant avec l'intérieur sombre. 

La structure comporte une bordure perlitique pouvant contenir du graphite de recuit qui peut d'ailleurs être précédée d'une lisière ferritique. 
A cœur : ferrite et graphite de recuit.

Un cordon perlitique de 0,5 mm d'épaisseur ne constitue pas un défaut.""",

"""Humidité dans l'atmosphère du four de traitement, provoquée par un séchage incomplet de la maçonnerie du four ou par des charges de moulages bruts humides.

L'oxygène et l'hydrogène d'une atmosphère humide réagissent à haute température avec la charge du four de traitement.
Par suite de l'action décarburante de l'oxygène, il se forme une lisière ferritique étroite. 

L'hydrogène diffuse vers l'intérieur du moulage, stabilise la perlite et empêche sa décomposition dans le deuxième stade du traitement."
Si la bordure de perlite provient de l'effet d'une atmosphère carburante dans le four de traitement, il n'y a pas de lisière ferritique.""",

"""- Veiller à ce que l'atmosphère du four de traitement soit absolument neutre.
- Veiller à un séchage complet de la maçonnerie du four.
- Ne pas charger dans le four de traitement des pièces humides ou rouillées."""),
                    
                    "G223": ("Couche superficielle dure de faible profondeur \ndont la structure comporte des constituants de trempe.",
                             
                             "Ducissement superficiel localisé.",
                             
"""Zones martensitiques très dures de faible épaisseur à la surface de la pièce.""",

"""Fort échauffement superficiel localisé suivi d'un refroidissement rapide par transmission de la chaleur à la masse froide de la pièce et à l'air ambiant.

Provoqué par :

- échauffement lors du meulage,
- production d'arc par suite d'un mauvais contact entre l'électrode et la pièce lors de l'essai magnétoscopique de contrôle de l'absence de fissure.""",

"""- Réduire la pression lors du meulage. 
- Effectuer le meulage de la malléable avant le recuit.
- Disposer les parties à meuler (attaques et attaches de masselottes) en des points qui n'auront pas à être usinés. Veiller au bon contact des électrodes avec la pièce dans l'essai magnétoscopique.
- Ne mettre le courant que lorsque la pièce à essayer est déjà aspergée du liquide contenant la poudre de fer. 
- Les trempes locales peuvent être facilement éliminées par un traitement de revenu (1 à 2 h à 450-650 °C)."""),
                    
                "G260": "Formation anormale de graphite.",
                
                    "G261": ("Graphite très grossier régulièrement réparti.",
                             
                             "Piqûres de graphite.",
                             
"""Lors de l'usinage de moulages épais en fonte à graphite lamellaire, surtout dans les régions correspondant à la partie supérieure du moule, apparaissent des porosités plus ou moins grandes à bords déchiquetés, dans lesquelles on observe la présence de poussière de graphite. Le matériau a en général une faible dureté et n'est souvent pas étanche.""",

"""- Équivalent en carbone trop élevé, surtout du fait du carbone, eu égard à l'épaisseur des pièces. 
- Refroidissement trop lent favorisant la formation de graphite du type A en lamelles très grossières. 
- Trop fortes différences d'épaisseur (défaut de tracé).""",

"""- Améliorer si possible le tracé dans le sens d'une diminution des plus fortes épaisseurs. 
- Ajuster l'équivalent en carbone et plus particulièrement la teneur en
carbone en fonction des épaisseurs. 
- Éviter une mise au mille de coke exagérée.
- Utiliser des fontes neuves à graphite fin (fontes affinées à bas carbone) de préférence aux fontes neuves à graphite développé. 
- Homogénéiser la vitesse de refroidissement par l'emploi de refroidisseurs intéressant les parties épaisses.
- Utiliser une poche à quenouille ou une poche théière, laisser reposer la fonte liquide avant de couler et ne pas vider la poche complètement dans le moule.
- Couler à la température minimale compatible avec la bonne venue de la pièce."""),
                    
                    "G262": ("Accumulation locale de graphite grossier dans la structure. Précipitation de graphite dans les cavités (resttasures).",
                             
                             "Nids de graphite.",
                             
"""A l'usinage apparaissent des porosités grossières remplies de graphite. Il l y a également du graphite libre dans les retassures. La structure est irrégulière, grossière et sans étanchéité.""",

"""Les mêmes que pour G 261 mais à un degré plus poussé permettant le rassemblement en amas des inclusions de graphite.""",

"""Les mêmes que pour G 261 en veillant tout particulièrement à la constitution des charges (coke et fontes neuves)."""),
                    
                    "G263": ("Amas de sphérules dans les régions supérieures du moulage (fonte G.S).",
                             
                             "Décantation de sphérolithes.",
                             
"""Le matériau a de mauvaises caractéristiques mécaniques. La cassure de moulages ayant des épaisseurs supérieures à 25 mm présente des bordures noires profondes plus ou moins larges situées dans la partie supérieure de la pièce. Dans la zone de décantation l'examen micrographique fait apparaître des sphérolithes éclatés, ainsi qu'un enrichissement en sulfures et oxydes de magnésium.""",

"""- L'équivalent en carbone (CE) est trop élevé, eu égard à l'épaisseur des parois.
- Le traitement au magnésium et l'inoculation sont faits à une température trop basse (inférieure à 1450 °C).
- Le maintien entre traitement et coulée est trop long. 
- Le refroidissement dans le moule est trop lent.""",

"""- Limiter l'équivalent en carbone en fonction de l'épaisseur des parois du moulage. Par exemple:
Épaisseur: 10 mm........CE maximum : 4,5
Épaisseur: 30 mm........CE maximum : 4,3
- Effectuer le traitement au magnésium et l'inoculation dans le domaine des températures optimales c'est-à-dire entre 1480 et 1510°C. - Couler au plus tard 10 minutes après le traitement.
- Respecter une température de coulée comprise entre 1400 et 1 360 °C. 
- Veiller à ce que le refroidissement et la solidification dans le moule soient aussi rapides que possible. """),
                    
                    "G264": ("Cassure présentant des facettes planes diversement orientées (fonte G.S., alliage eutectique Al-Si).0",
                             
                             "Alignement de sphéroïdes. Cassure à facettes.",
                             
"""La cassure présente une anomalie d'aspect : facettes planes diversement orientées.

L'examen micrographique révèle la présence de dendrites, soulignées par des alignements de graphite dans le cas de la fonte GS.""",

"""Formation de grandes dendrites lors de la solidification.""",

"""Cette anomalie n'est pas un défaut : les caractéristiques mécaniques sta tiques et dynamiques ne sont pas affectées. 

Nota: La même anomalie de structure se rencontre avec certains alliages eutectiques Al-Si."""),
        }


class infoBulle(tk.Toplevel):
    """Gestion des infobulles."""
    
    def __init__(self, parent=None, texte='', temps=500):
        tk.Toplevel.__init__(self, parent, bd=1, bg='black')
        self.tps = temps
        self.parent = parent
        self.withdraw()
        self.overrideredirect(1)
        self.transient()
        label = tk.Label(self, text=texte, bg="yellow", justify='left', font=LARGE_FONT)
        label.update_idletasks()
        label.pack()
        label.update_idletasks()
        self.tipwidth = label.winfo_width()
        self.tipheight = label.winfo_height()
        self.parent.bind('<Enter>', self.delai)
        self.parent.bind('<Button-1>', self.efface)
        self.parent.bind('<Leave>', self.efface)

    def delai(self, event):
        """Retarde l'affichage du défli de tems rentré dans l'__init__."""
        self.action = self.parent.after(self.tps, self.affiche)

    def affiche(self):
        """Gère l'affichage de l'infobulle."""
        self.update_idletasks()
        posX = self.parent.winfo_rootx()  #+self.parent.winfo_width()
        posY = self.parent.winfo_rooty()  #+self.parent.winfo_height()
        if posX + self.tipwidth > self.winfo_screenwidth():
            posX = posX - self.winfo_width() - self.tipwidth
        if posY + self.tipheight > self.winfo_screenheight():
            posY = posY - self.winfo_height() - self.tipheight
        # ~ print posX,print posY
        self.geometry('+%d+%d' % (posX, posY))
        self.deiconify()

    def efface(self, event):
        """Clean l'infobulle."""
        self.withdraw()
        self.parent.after_cancel(self.action)


class Boutons_selection:
    """Créer les façons de créer les boutons utilisés sur toutes les pages (héritage)."""
    
    illustrations = {}
    boutons = {}
    Labels = {}
    
    def path_photo(Xnnn):
        """
        Renvoie l'image de l'arborescence associé à un défaut.
    
        Parameters
        ----------
        Xnnn : float
            Exemples : "A111".
    
        Returns
        -------
        .png
            Image de description shéma explicatif.
        """
        return "E:/Boulot/Ferry_Capitain/Defautheque/Defauthon/Donnees/" + Xnnn + "/" + Xnnn + ".png"
    
    def bouton_selection_niv0(self, page_suivante, X, row, column, controller):
        """
        
        Patern de création pour les boutons de niveau 0: i.e ceux qui amène à un choix de type Xn00 (niveau 1).

        Parameters
        ----------
        X : float
            Exemple : "A"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.boutons[X] = tk.Button(self, text=Livre[X], bg='#8B0000', relief="ridge", bd=10, font=VERY_LARGE_FONT, command=lambda: controller.show_frame(page_suivante))
        self.boutons[X].grid(row=row, column=column, sticky="nsew")
        
    def bouton_selection_niv1(self, page_suivante, Xn, row, column, controller):
        """
        
        Patern de création pour les boutons de niveau 1 : i.e ceux qui amène à un choix de type Xnn0 (niveau 2).

        Parameters
        ----------
        Xn : float
            Exemple : "A100"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.boutons[Xn] = tk.Button(self, text=Livre[Xn], relief="ridge", bg='orange', bd=10, font=LARGE_FONT, command=lambda: controller.show_frame(page_suivante))
        self.boutons[Xn].grid(row=row, column=column, sticky="nsew")
    
    def bouton_selection_niv2(self, page_suivante, Xnn, row, column, controller):
        """
        Patern de création pour les boutons de niveau 2 : i.e ceux qui amène à un choix de type Xnnn (niv3).

        Parameters
        ----------
        Xnn : float
            Exemple : "A110"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.boutons[Xnn] = tk.Button(self, text=Livre[Xnn] + "\n | \n\/", relief="ridge", bg='yellow', bd=10, font=LARGE_FONT, command=lambda: controller.show_frame(page_suivante))
        self.boutons[Xnn].grid(row=row, column=column, sticky="nsew")
    
    def lance_affichage(self, Xnnn, controller):
        """Définit l'action suivit la pression d'un bouton de niv 3."""
        defautX = Info_defaut()
        img = tk.PhotoImage(file=Boutons_selection.path_photo(Xnnn))
        defautX.img = img
        defautX.nom = Xnnn
        defautX.affiche_info(Xnnn, controller)
    
    def bouton_selection_niv3(self, Xnnn, row, column, controller):
        """
        Patern de création pour les boutons de niveau 3: i.e. ceux qui amène à la page résumé d'un défaut.
        
        Construit le boutton du défaut "Xnnn" avec son image  et son placement dans la grille de la page.
        
        Uniquement les boutons de choix final des défauts.

        Parameters
        ----------
        Xnnn : float
            Exemple : "A111"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        try:
            # Avec image: -----------------------------
            self.illustrations[Xnnn] = tk.PhotoImage(master=self, file=Boutons_selection.path_photo(Xnnn))
            r = self.illustrations[Xnnn].height() / 100  # Coefficient de "dezoom" à donner pour avoir au ax 125 pixel de haut
            self.illustrations[Xnnn] = self.illustrations[Xnnn].subsample(int(r + 0.5))
            
            # Cas particuliers
            if Xnnn == "B112":
                self.illustrations[Xnnn] = self.illustrations[Xnnn].subsample(2)
            if Xnnn == "G221" or Xnnn == "G222":
                self.illustrations[Xnnn] = self.illustrations[Xnnn].zoom(2)
            
            self.boutons[Xnnn] = tk.Button(self, text=Livre[Xnnn][1], relief="raised", bd=10, font=LARGE_FONT,
                                           image=self.illustrations[Xnnn], compound="right",
                                           command=lambda: self.lance_affichage(Xnnn, controller))
        except Exception:
            # Sans image: -----------------------------
            self.boutons[Xnnn] = tk.Button(self, text=Livre[Xnnn][1], relief="raised", bd=10, font=LARGE_FONT)
        self.boutons[Xnnn].grid(row=row, column=column, sticky="nsew")
        infoBulle(parent=self.boutons[Xnnn], texte=Livre[Xnnn][0])
        
    def bouton_retour(self, page_avant, row, column, controller):
        """
        Construit le bouton de retour.

        Parameters
        ----------
        page_avant : class
            La classe de la page où on souhaite aller
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        controller : TYPE ??
        """
        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Back_button.png").subsample(20)
        if str(page_avant)[17:-2] == "Accueil":
            text = "Retour à la page d'accueil"
        else:
            text = "Retour à la page " + str(page_avant)[21:-2]
        self.butonRetour = tk.Button(self, text=text, font=LARGE_FONT, command=lambda: controller.show_frame(page_avant), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.butonRetour.grid(row=row, column=column, sticky="nsew")

    def label_niv0(self, X, row, column):
        """
        Créer des labels pour le niv2.

        Parameters
        ----------
        Xn : float
            Exemple : "A"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.label = tk.Label(self, text=Livre[X], bg='#8B0000', font=VERY_LARGE_FONT)
        self.label.grid(row=row, column=column, sticky="nsew")

    def label_niv1(self, Xn, row, column, *args, **kwargs):
        """
        Créer des labels pour le niv2.

        Parameters
        ----------
        Xn : float
            Exemple : "A100"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.label = tk.Label(self, text=Livre[Xn] + str(args)[2:-3], bg='orange', font=LARGE_FONT)
        self.label.grid(row=row, column=column, columnspan=2, sticky="nsew")
        
    def label_niv2(self, Xnn, row, column):
        """
        Créer des labels pour le niv2.

        Parameters
        ----------
        Xn : float
            Exemple : "A110"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.label = tk.Label(self, text=Livre[Xnn], bg='yellow', font=LARGE_FONT)
        self.label.grid(row=row, column=column, sticky="nsew")


class Defauthon(tk.Tk):
    """Fenetre pirncipale (seul l'intérieur de container change)."""
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        # création d'une entité contenante, elle sert de support aux frames
        container = tk.Frame(self)

        # Plus simplement on peux assimiler container à la surface entre les bords de la fenêtre
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)  # Structure du container, permet de remplir tout l'espace de la frame
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [Accueil,
                                          PageA, PageA100, PageA200, PageA300,
                                          PageB, PageB100, PageB200, PageB300,
                                          PageC, PageC100, PageC200, PageC300, PageC400,
                                          PageD, PageD100, PageD100bis, PageD200, PageD200bis,
                                          PageE, PageE100, PageE200,
                                          PageF, PageF100, PageF200, PageF200bis,
                                          PageG, PageG100, PageG100bis, PageG200, PageG200bis,
                                          ]:
            frame = F(container, self)

            self.frames[F] = frame

            if F == Accueil:
                frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
                frame.columnconfigure(0, weight=1)
            if F == PageD or F == PageE or F == PageF or F == PageG or F == PageA300 or F == PageB300:
                frame.rowconfigure([0, 1, 2, 3], weight=1)
                frame.columnconfigure(0, weight=1)
            if F == PageA or F == PageB or F == PageC400:
                frame.rowconfigure([0, 1, 2, 3, 4], weight=1)
                frame.columnconfigure(0, weight=1)
            if F == PageC or F == PageD200bis:
                frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
                frame.columnconfigure(0, weight=1)
            if F == PageF200bis or F == PageG200bis:
                frame.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
                frame.columnconfigure(0, weight=1)
            
            if F == PageC200 or F == PageC100:
                frame.rowconfigure([0, 1, 2, 3], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            if F == PageB200 or F == PageC300 or F == PageE200 or F == PageG100:
                frame.rowconfigure([0, 1, 2, 3, 4], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            if F == PageB100 or F == PageD100 or F == PageD200 or F == PageF200 or F == PageG100bis or F == PageG200:
                frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            if F == PageA100 or F == PageD100bis or F == PageE100:
                frame.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            if F == PageA200 or F == PageF100:
                frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            else:
                frame.rowconfigure(0, weight=1)
                frame.columnconfigure(0, weight=1)
            # placement de la frame dans le container
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Accueil)

    def show_frame(self, cont):
        """
        Permet de changer de page.

        Parameters
        ----------
        cont : "Controller !!" Le nom d'une page (i.e. d'une classe définit plus bas).

        Returns
        -------
        changement de frame.
        """
        frame = self.frames[cont]
        frame.tkraise()


class Info_defaut(tk.Toplevel):
    """Page résume d'un défaut qui vient s'adapter à chaque défaut en fonction de ce qu'il y a en données dans le dossier correspondant."""
    
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("1200x900")
        # self.resizable(width=False, height=False)
        self.grid_rowconfigure([0, 1, 2, 3], weight=2, uniform=True)
        self.grid_rowconfigure([0, 3], weight=1)
        self.grid_columnconfigure([0, 1, 2, 3], weight=1)
        
        # print("dans l'init self :", self)
    
    def confirmation(self, nom, intitulé, texte, methode_si_oui, controller):
        """Message de confirmation pour l'annulation de la modification."""
        reponse = tk.messagebox.askokcancel(intitulé, texte)
        self.tkraise()
        if reponse == 1:
            methode_si_oui(nom, controller)
    
    def text_recap_modif_info(self, nom):
        """Prepare le texte récapitulatif des moficiations proposées afin de les envoyer par mail."""
        
        Texte = {}
        Texte["Sujet"] = "Proposition de modification des informations du défaut {0}".format(nom)
        Texte["Main_text"] = '''Bonjour,
                                \nCeci est un message automatiquement généré suite à la modification du défaut indentifié {0} le {1}
                                \n\nLes modifications proposées sont les suivantes :
                                \n -----------------------------------------
                                \n AVANT : Information(s) générale(s)
                                \n {2}
                                \n APRES : Information(s) générale(s) - MODE EDITION
                                \n {5}
                                
                                \n -----------------------------------------
                                \n AVANT : Cause(s)
                                \n {3}
                                \n APRES : Cause(s) - MODE EDITION
                                \n {6}
                                
                                \n -----------------------------------------
                                \n AVANT : Remède(s)
                                \n {4}
                                \n APRES : Remède(s) - MODE EDITION
                                \n {7}
                                
                                '''.format(nom, datetime.date.today(), 
                                            Livre[self.nom][2], Livre[self.nom][3], Livre[self.nom][4],
                                            self.texte_descriptif.get(1.0, 'end'), self.texte_cause.get(1.0, 'end'), self.texte_remede.get(1.0, 'end'))
        
        return Texte
    
    def envoie_mail(self, email_receiver, texte_recap):
        """Envoie un mail au destinataire pour l'informer d'une modification d'un défaut."""
        
        reponse = tk.messagebox.askokcancel('Valider la proposition de modification', "êtes vous certain de vouloir valider la proposition de modification en l'état ?\n\nRemarque : - cliquer sur oui va générer un envoi d'email\n                     - L'envoi prends quelques dizaines de secondes")
        self.tkraise()
        if reponse == 0:
            return None
        
        # on rentre les renseignements pris sur le site du fournisseur
        smtp_address = 'smtp.laposte.net'
        smtp_port = 465
        
        # on rentre les informations sur notre adresse e-mail
        email_address = 'julien.thivet@laposte.net'
        email_password = 'F$z@-ti!GiXT5er'
        
        # on rentre les informations sur le destinataire
        # email_receiver = 'jjulien.thivet@gmail.com'
        
        # on crée un e-mail
        message = MIMEMultipart("???")
        # on ajoute un sujet
        message["Subject"] = texte_recap["Sujet"]
        # un émetteur
        message["From"] = email_address
        # un destinataire
        message["To"] = email_receiver
        
        # on crée un texte et sa version HTML
        texte = texte_recap["Main_text"]
        
        # on crée deux éléments MIMEText 
        texte_mime = MIMEText(texte, 'plain')
        
        # on attache ces deux éléments 
        message.attach(texte_mime)
        
        # on crée la connexion
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            # connexion au compte
            server.login(email_address, email_password)
            # envoi du mail
            server.sendmail(email_address, email_receiver, message.as_string())
            tk.messagebox.showinfo("Réussi", "Proposition de modification bien envoyé")
            # print("Email bien envoyé de {0} à {1}".format(email_address, email_receiver))
    
    def helper(self, nom, controller):
        """Pour résoudre le soucis avec lambda et la création des tags."""
        return lambda a: Boutons_selection.lance_affichage(self, nom, controller)
    
    def creer_tag(self, text_widget, controller):
        """Creer les tags associés à chaque nom de défaut dans les textes de Info_defaut, ils sont clicable et viennent ouvrir la fenetres correspondante au défaut en question."""
        texte = text_widget.get(1.0, 'end')
        
        for i in range(len(texte)):
            if (texte[i] == "A" or texte[i] == "B" or texte[i] == "C" or texte[i] == "D" or texte[i] == "E" or texte[i] == "F" or texte[i] == "G"):
                #  sans espace "A300"
                if (texte[i + 1] == '0' or texte[i + 1] == '1' or texte[i + 1] == '2' or texte[i + 1] == '3' or texte[i + 1] == '4'):
                    index = text_widget.search(texte[i:i + 4], 1.0)
                    tag_nom = str(texte[i:i + 4])
                    print(tag_nom)
                    if texte[i + 2] == '0':
                        tag_nom = str(texte[i: i + 2]) + '1' + texte[i + 3]
                    if texte[i + 3] == '0':
                        tag_nom = str(texte[i: i + 3]) + '1'
                    if texte[i + 2] == '0' and texte[i + 3] == '0':
                        tag_nom = texte[i:i + 2] + '11'
                        
                    text_widget.tag_add(tag_nom, index, index + '+ 4 chars')
                
                # tag avec un espace "A 300"
                if texte[i + 1] == ' ':
                    # print("y'a un espace, num : ", str(texte[i]) + str(texte[i + 2:i + 5]))
                    if (texte[i + 2] == '0' or texte[i + 2] == '1' or texte[i + 2] == '2' or texte[i + 2] == '3' or texte[i + 2] == '4'):
                        index = text_widget.search(texte[i:i + 5], 1.0)
                        tag_nom = str(texte[i]) + str(texte[i + 2:i + 5])
                        if texte[i + 3] == '0':
                            tag_nom = str(texte[i]) + texte[i + 2] + '1' + texte[i + 4]
                        if texte[i + 4] == '0':
                            tag_nom = str(texte[i]) + texte[i + 2:i + 4] + '1'
                        if texte[i + 3] == '0' and texte[i + 4] == '0':
                            tag_nom = texte[i] + texte[i + 2] + '11'  
                        
                        text_widget.tag_add(tag_nom, index, index + '+ 5 chars')
                    
        for i in range(len(text_widget.tag_names()) - 1):
            nom = text_widget.tag_names()[i + 1]
            # print(nom)
            text_widget.tag_configure(nom, font=('Calibri', 12, 'italic', 'underline'), foreground='blue')
            # text_widget.tag_bind(nom, '<Button-1>', lambda a: Boutons_selection.lance_affichage(self, nom, controller))
            text_widget.tag_bind(nom, '<Button-1>', self.helper(nom, controller))
         
    def modif_info(self, nom, controller):
        """Affiche et permet la modification des informations sur le défaut."""
        
        for widget in self.winfo_children():
            widget.destroy()
        
        self.frame_nom = tk.Frame(master=self, padx=20, pady=20,
                                  highlightbackground="black", highlightcolor="black", highlightthickness=3) 
    
        
        self.label_nom = tk.Label(self.frame_nom, text=self.nom + " - " + Livre[self.nom][1] + "\n------ MODE EDITION ------", font=VERY_LARGE_FONT)
        self.label_nom.pack()
        
        
        self.frame_nom.grid(row=0, column=0, columnspan=4)
        
        
        
        self.frame_info = tk.LabelFrame(master=self, padx=10, pady=10,
                                   # highlightbackground="saddle brown", highlightcolor="saddle brown", highlightthickness=4,
                                   text="Information(s) générale(s) - MODE EDITION", fg="saddle brown", font=("Calibri", 18))
        
        self.label_img = tk.Label(self.frame_info, image=self.img)
        self.label_img.pack()
        
        self.texte_descriptif = tk.Text(self.frame_info, wrap="word", font=LARGE_FONT)
        self.texte_descriptif.insert(tk.INSERT, Livre[self.nom][2])
        # self.texte_descriptif.config(height=len(self.texte_descriptif.get(1.0, "end")) / 50 + 2)
        self.texte_descriptif.pack()
        
        
        self.frame_info.grid(row=1, column=0, rowspan=2, columnspan=2)
        
        
        self.frame_cause = tk.LabelFrame(master=self, padx=10, pady=10,
                                   # highlightbackground="OrangeRed2", highlightcolor="OrangeRed2", highlightthickness=4,
                                   text="Cause(s) - MODE EDITION", fg="OrangeRed2", font=("Calibri", 18))
        
        
        self.texte_cause = tk.Text(self.frame_cause, wrap="word", font=LARGE_FONT)
        self.texte_cause.insert(tk.INSERT, Livre[self.nom][3])
        # self.texte_cause.config(height=len(self.texte_cause.get(1.0, "end")) / 70 + 2)
        self.texte_cause.pack()
         
        
        self.frame_cause.grid(row=1, column=2, columnspan=2)
        
        
        self.frame_remede = tk.LabelFrame(master=self, padx=10, pady=10,
                                   # highlightbackground="green4", highlightcolor="green4", highlightthickness=4,
                                   text="Remède(s) - MODE EDITION", fg="green4", font=("Calibri", 18))
        
        
        self.texte_remede = tk.Text(self.frame_remede, wrap="word", font=LARGE_FONT)
        self.texte_remede.insert(tk.INSERT, Livre[self.nom][4])
        # self.texte_remede.config(height=len(self.texte_remede.get(1.0, "end")) / 70 + 3)
        self.texte_remede.pack()
         
        
        self.frame_remede.grid(row=2, column=2, columnspan=2)
        
        
        self.bouton_annulation_modif = tk.Button(self, text="Annuler toutes les modifications en cours", 
                                                 font=LARGE_FONT, relief="raised", bg="red", bd=10,
                                                 command=lambda: self.confirmation(nom, "Annuler les modifications en cours", "êtes vous sûr de vouloir annuler les modifications en cours sans valider ?", self.affiche_info, controller))
        self.bouton_annulation_modif.grid(row=3, column=0, columnspan=2, sticky="nsew")
        
        self.bouton_validation_modif = tk.Button(self, text="Valider les modifications", 
                                                 font=LARGE_FONT, relief="raised", bg="green", bd=10,
                                                 command=lambda: [self.envoie_mail('jjulien.thivet@gmail.com', self.text_recap_modif_info(nom)),
                                                                  self.affiche_info(nom, controller),
                                                                  self.tkraise()])

        self.bouton_validation_modif.grid(row=3, column=2, columnspan=2, sticky="nsew")
    
    def affiche_info(self, nom, controller):
        """Met à jour les infos et build les composants."""
        
        for widget in self.winfo_children():
            widget.destroy()
        
        self.frame_nom = tk.Frame(master=self, padx=20, pady=20,
                                  highlightbackground="black", highlightcolor="black", highlightthickness=3) 
    
        
        self.label_nom = tk.Label(self.frame_nom, text=self.nom + " - " + Livre[self.nom][1], font=VERY_LARGE_FONT)
        self.label_nom.pack()
        
        
        self.frame_nom.grid(row=0, column=0, columnspan=4)
        
        
        
        self.frame_info = tk.LabelFrame(master=self, padx=10, pady=10,
                                   # highlightbackground="saddle brown", highlightcolor="saddle brown", highlightthickness=4,
                                   text="Information(s) générale(s)", fg="saddle brown", font=("Calibri", 18))
        
        if nom == 'A211' or nom == 'A212' or nom == 'A311':
            self.img = self.img.subsample(2)
            
        self.label_img = tk.Label(self.frame_info, image=self.img)
        self.label_img.pack()
        
        self.texte_descriptif = tk.Text(self.frame_info, wrap="word", font=LARGE_FONT)
        self.texte_descriptif.insert(tk.INSERT, Livre[self.nom][2])
        self.texte_descriptif.configure(state='disabled')
        # self.texte_descriptif.config(height=len(self.texte_descriptif.get(1.0, "end")) / 50 + 2)
        # self.texte_descriptif.config(height=24)
        self.creer_tag(self.texte_descriptif, controller)
        self.texte_descriptif.pack()
         
        
        self.frame_info.grid(row=1, column=0, rowspan=2, columnspan=2)
        
        
        self.frame_cause = tk.LabelFrame(master=self, padx=10, pady=10,
                                   # highlightbackground="OrangeRed2", highlightcolor="OrangeRed2", highlightthickness=4,
                                   text="Cause(s)", fg="OrangeRed2", font=("Calibri", 18))
        
        
        self.texte_cause = tk.Text(self.frame_cause, wrap="word", font=LARGE_FONT)
        self.texte_cause.insert(tk.INSERT, Livre[self.nom][3])
        self.texte_cause.configure(state='disabled')
        # self.texte_cause.config(height=len(self.texte_cause.get(1.0, "end")) / 70 + 2)
        # self.texte_cause.config(height=2)
        self.creer_tag(self.texte_cause, controller)
        self.texte_cause.pack()
         
        
        self.frame_cause.grid(row=1, column=2, columnspan=2)
        
        
        self.frame_remede = tk.LabelFrame(master=self, padx=10, pady=10,
                                   # highlightbackground="green4", highlightcolor="green4", highlightthickness=4,
                                   text="Remède(s)", fg="green4", font=("Calibri", 18))
        
        
        self.texte_remede = tk.Text(self.frame_remede, wrap="word", font=LARGE_FONT)
        self.texte_remede.insert(tk.INSERT, Livre[self.nom][4])
        self.texte_remede.configure(state='disabled')
        # self.texte_remede.config(height=len(self.texte_remede.get(1.0, "end")) / 70 + 3)
        # self.texte_cause.config(height=2)
        self.creer_tag(self.texte_remede, controller)
        self.texte_remede.pack()
         
        
        self.frame_remede.grid(row=2, column=2, columnspan=2)
        
        
        self.bouton_consulter_experience = tk.Button(self, text="Consulter les expériences passées", font=LARGE_FONT, relief="raised", bg="turquoise3", bd=10)
        self.bouton_consulter_experience.grid(row=3, column=3, sticky="nsew")
        
        self.bouton_ajouter_experience = tk.Button(self, text="Soumettre une nouvelle expérience", font=LARGE_FONT, relief="ridge", bg="DarkOliveGreen3")
        self.bouton_ajouter_experience.grid(row=3, column=1, columnspan=2, sticky="nsew")
        
        self.bouton_modif_info = tk.Button(self, text="Proposer une modification des informations", 
                                           font=LARGE_FONT, relief="raised", bg="NavajoWhite4",
                                           command=lambda: self.modif_info(nom, controller))

        self.bouton_modif_info.grid(row=3, column=0, sticky="nsew")
        
        
        print("------\nnom : ", self.nom)
        

class Accueil(tk.Frame, Boutons_selection):
    """Page de garde de l'arborescence des défauts."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Accueil", font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.bouton_selection_niv0(PageA, "A", 1, 0, controller)
        self.bouton_selection_niv0(PageB, "B", 2, 0, controller)
        self.bouton_selection_niv0(PageC, "C", 3, 0, controller)
        self.bouton_selection_niv0(PageD, "D", 4, 0, controller)
        self.bouton_selection_niv0(PageE, "E", 5, 0, controller)
        self.bouton_selection_niv0(PageF, "F", 6, 0, controller)
        self.bouton_selection_niv0(PageG, "G", 7, 0, controller)


class PageA(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts A (A100/A200/A300)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("A", 0, 0)
        # self.label = tk.Label(self, text=Livre["A"], bg='red', font=LARGE_FONT)
        # self.label.grid(row=0, column=0, sticky="nsew")
        
        self.bouton_selection_niv1(PageA100, "A100", 1, 0, controller)
        self.bouton_selection_niv1(PageA200, "A200", 2, 0, controller)
        self.bouton_selection_niv1(PageA300, "A300", 3, 0, controller)
        self.bouton_retour(Accueil, 4, 0, controller)


class PageA100(tk.Frame, Boutons_selection):
    """PageA100 (9 défauts)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label_niv1("A100", 0, 0)
        
        # ------------------------------- A110 -------------------------------
        self.label_niv2("A110", 1, 0)
        
        for i in range(5):
            self.bouton_selection_niv3("A11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- A120 -------------------------------
        self.label_niv2("A120", 1, 1)
        
        for i in range(3):
            self.bouton_selection_niv3("A12" + str(i + 1), 2 + i, 1, controller)

        self.bouton_retour(PageA, 6, 1, controller)


class PageA200(tk.Frame, Boutons_selection):
    """PageA200 (10 défauts)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("A200", 0, 0)
        
        # ------------------------------- A210 -------------------------------
        self.label_niv2("A210", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("A21" + str(i + 1), 2 + i, 0, controller)

        # ------------------------------- A220 -------------------------------
        self.label_niv2("A220", 1, 1)

        for i in range(6):
            self.bouton_selection_niv3("A22" + str(i + 1), 2 + i, 1, controller)

        self.bouton_retour(PageA, 7, 0, controller)


class PageA300(tk.Frame, Boutons_selection):
    """PageA300 (1 défaut)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("A300", 0, 0)
        
        # ------------------------------- A310 -------------------------------
        self.label_niv2("A310", 1, 0)

        self.bouton_selection_niv3("A311", 2, 0, controller)
        
        self.bouton_retour(PageA, 3, 0, controller)


class PageB(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts B (B100/B200/B300)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("B", 0, 0)

        self.bouton_selection_niv1(PageB100, "B100", 1, 0, controller)
        self.bouton_selection_niv1(PageB200, "B200", 2, 0, controller)
        self.bouton_selection_niv1(PageB300, "B300", 3, 0, controller)
        self.bouton_retour(Accueil, 4, 0, controller)


class PageB100(tk.Frame, Boutons_selection):
    """PageB100 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("B100", 0, 0)
        
        # ------------------------------- B110 -------------------------------
        self.label_niv2("B110", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("B11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- B120 -------------------------------
        self.label_niv2("B120", 1, 1)
        
        for i in range(4):
            self.bouton_selection_niv3("B12" + str(i + 1), 2 + i, 1, controller)

        self.bouton_retour(PageB, 5, 0, controller)


class PageB200(tk.Frame, Boutons_selection):
    """PageB200 (5 défauts)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("B200", 0, 0)
        
        # ------------------------------- B210 -------------------------------
        self.label_niv2("B210", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("B21" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- B220 -------------------------------
        self.label_niv2("B220", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("B22" + str(i + 1), 2 + i, 1, controller)

        self.bouton_retour(PageB, 4, 1, controller)


class PageB300(tk.Frame, Boutons_selection):
    """PageB300 (1 défaut)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("B300", 0, 0)
        
        # ------------------------------- B310 -------------------------------
        self.label_niv2("B310", 1, 0)

        self.bouton_selection_niv3("B311", 2, 0, controller)
        
        self.bouton_retour(PageB, 3, 0, controller)


class PageC(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts C (C100/C200/C300/C400)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("C", 0, 0)

        self.bouton_selection_niv1(PageC100, "C100", 1, 0, controller)
        self.bouton_selection_niv1(PageC200, "C200", 2, 0, controller)
        self.bouton_selection_niv1(PageC300, "C300", 3, 0, controller)
        self.bouton_selection_niv1(PageC400, "C400", 4, 0, controller)
        self.bouton_retour(Accueil, 5, 0, controller)


class PageC100(tk.Frame, Boutons_selection):
    """PageC100 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C100", 0, 0)
        
        # ------------------------------- C110 -------------------------------
        self.label_niv2("C110", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("C11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- C120 -------------------------------
        self.label_niv2("C120", 1, 1)
        
        for i in range(1):
            self.bouton_selection_niv3("C12" + str(i + 1), 2 + i, 1, controller)

        self.bouton_retour(PageC, 3, 1, controller)


class PageC200(tk.Frame, Boutons_selection):
    """PageC200 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C200", 0, 0)
        
        # ------------------------------- C210 -------------------------------
        self.label_niv2("C210", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("C21" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- C220 -------------------------------
        self.label_niv2("C220", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("C22" + str(i + 1), 2 + i, 1, controller)

        self.bouton_retour(PageC, 3, 0, controller)
    

class PageC300(tk.Frame, Boutons_selection):
    """PageC300 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C300", 0, 0)
        
        # ------------------------------- C310 -------------------------------
        self.label_niv2("C310", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("C31" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- C320 -------------------------------
        self.label_niv2("C320", 1, 1)
        
        for i in range(1):
            self.bouton_selection_niv3("C32" + str(i + 1), 2 + i, 1, controller)
            
        # ------------------------------- C330 -------------------------------
        self.label_niv2("C330", 3, 0)
        
        self.bouton_selection_niv3("C331", 4, 0, controller)

        self.bouton_retour(PageC, 4, 1, controller)


class PageC400(tk.Frame, Boutons_selection):
    """PageC400 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C400", 0, 0)
        
        # ------------------------------- C410 -------------------------------
        self.label_niv2("C410", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("C41" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageC, 4, 0, controller)


class PageD(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts D (D100/D200)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("D", 0, 0)

        self.bouton_selection_niv1(PageD100, "D100", 1, 0, controller)
        self.bouton_selection_niv1(PageD200, "D200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageD100(tk.Frame, Boutons_selection):
    """PageD100 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D100", 0, 0, " Page 1/2")
        
        # ------------------------------- D110 -------------------------------
        self.label_niv2("D110", 1, 0)
        
        for i in range(4):
            self.bouton_selection_niv3("D11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- D120 -------------------------------
        self.label_niv2("D120", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("D12" + str(i + 1), 2 + i, 1, controller)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageD100bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=4, column=1, sticky="nsew")
        
        self.bouton_retour(PageD, 5, 1, controller)


class PageD100bis(tk.Frame, Boutons_selection):
    """PageD100bis ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D100", 0, 0, " Page 2/2")
        
        # ------------------------------- D130 -------------------------------
        self.label_niv2("D130", 1, 0)
        
        for i in range(5):
            self.bouton_selection_niv3("D13" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- D140 -------------------------------
        self.label_niv2("D140", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("D14" + str(i + 1), 2 + i, 1, controller)
        
        self.bouton_retour(PageD100, 6, 1, controller)


class PageD200(tk.Frame, Boutons_selection):
    """PageD200 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D200", 0, 0, " Page 1/2")
        
        # ------------------------------- D210 -------------------------------
        self.label_niv2("D210", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("D21" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- D220 -------------------------------
        self.label_niv2("D220", 1, 1)
        
        for i in range(4):
            self.bouton_selection_niv3("D22" + str(i + 1), 2 + i, 1, controller)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageD200bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=4, column=0, sticky="nsew")
        
        self.bouton_retour(PageD, 5, 0, controller)


class PageD200bis(tk.Frame, Boutons_selection):
    """PageD200bis ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D200", 0, 0, " Page 2/2")
        
        # ------------------------------- D230 -------------------------------
        self.label_niv2("D230", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("D23" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageD200, 5, 0, controller)


class PageE(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts E (E100/E200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("E", 0, 0)

        self.bouton_selection_niv1(PageE100, "E100", 1, 0, controller)
        self.bouton_selection_niv1(PageE200, "E200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageE100(tk.Frame, Boutons_selection):
    """PageE100 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("E100", 0, 0)
        
        # ------------------------------- E110 -------------------------------
        self.label_niv2("E110", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("E11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- E120 -------------------------------
        self.label_niv2("E120", 1, 1)
        
        for i in range(5):
            self.bouton_selection_niv3("E12" + str(i + 1), 2 + i, 1, controller)
        
        self.bouton_retour(PageE, 6, 0, controller)


class PageE200(tk.Frame, Boutons_selection):
    """PageD200 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("E200", 0, 0)
        
        # ------------------------------- E210 -------------------------------
        self.label_niv2("E210", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("E21" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- E220 -------------------------------
        self.label_niv2("E220", 1, 1)
        
        for i in range(1):
            self.bouton_selection_niv3("E22" + str(i + 1), 2 + i, 1, controller)
            
        # ------------------------------- E230 -------------------------------
        self.label_niv2("E230", 3, 0)
        
        self.bouton_selection_niv3("E231", 4, 0, controller)

        self.bouton_retour(PageE, 4, 1, controller)
    

class PageF(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts F (F100/F200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("F", 0, 0)

        self.bouton_selection_niv1(PageF100, "F100", 1, 0, controller)
        self.bouton_selection_niv1(PageF200, "F200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageF100(tk.Frame, Boutons_selection):
    """PageF100 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("F100", 0, 0)
        
        # ------------------------------- F110 -------------------------------
        self.label_niv2("F110", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("F11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- F120 -------------------------------
        self.label_niv2("F120", 1, 1)
        
        for i in range(6):
            self.bouton_selection_niv3("F12" + str(i + 1), 2 + i, 1, controller)
        
        self.bouton_retour(PageF, 7, 0, controller)


class PageF200(tk.Frame, Boutons_selection):
    """PageF200 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("F200", 0, 0, " Page 1/2")
        
        # ------------------------------- F210 -------------------------------
        self.label_niv2("F210", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("F21" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- F220 -------------------------------
        self.label_niv2("F220", 1, 1)
        
        for i in range(3):
            self.bouton_selection_niv3("F22" + str(i + 1), 2 + i, 1, controller)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageF200bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=5, column=1, sticky="nsew")
        
        self.bouton_retour(PageF, 5, 0, controller)


class PageF200bis(tk.Frame, Boutons_selection):
    """PageF200bis ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("F200", 0, 0, " Page 2/2")
        
        # ------------------------------- F230 -------------------------------
        self.label_niv2("F230", 1, 0)
        
        for i in range(4):
            self.bouton_selection_niv3("F23" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageF200, 6, 0, controller)


class PageG(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts G (G100/G200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("G", 0, 0)

        self.bouton_selection_niv1(PageG100, "G100", 1, 0, controller)
        self.bouton_selection_niv1(PageG200, "G200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageG100(tk.Frame, Boutons_selection):
    """PageG100 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G100", 0, 0, " Page 1/2")
        
        # ------------------------------- G110 -------------------------------
        self.label_niv2("G110", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("G11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- G120 -------------------------------
        self.label_niv2("G120", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("G12" + str(i + 1), 2 + i, 1, controller)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageG100bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=4, column=1, sticky="nsew")
        
        self.bouton_retour(PageG, 4, 0, controller)


class PageG100bis(tk.Frame, Boutons_selection):
    """PageG100bis ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G100", 0, 0, " Page 2/2")
        
        # ------------------------------- G130 -------------------------------
        self.label_niv2("G130", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("G13" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- G140 -------------------------------
        self.label_niv2("G140", 1, 1)
        
        for i in range(4):
            self.bouton_selection_niv3("G14" + str(i + 1), 2 + i, 1, controller)
        
        self.bouton_retour(PageG100, 5, 0, controller)


class PageG200(tk.Frame, Boutons_selection):
    """PageG200 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G200", 0, 0, " Page 1/2")
        
        # ------------------------------- G210 -------------------------------
        self.label_niv2("G210", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("G21" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- G220 -------------------------------
        self.label_niv2("G220", 1, 1)
        
        for i in range(3):
            self.bouton_selection_niv3("G22" + str(i + 1), 2 + i, 1, controller)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageG200bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=5, column=1, sticky="nsew")
        
        self.bouton_retour(PageG, 5, 0, controller)


class PageG200bis(tk.Frame, Boutons_selection):
    """PageD200 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G200", 0, 0, " Page 2/2")
        
        # ------------------------------- G260 -------------------------------
        self.label_niv2("G260", 1, 0)  # oui 260 et pas 230, je pense qu'il manque une page dans le livre... à voir
        
        for i in range(4):
            self.bouton_selection_niv3("G26" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageG200, 6, 0, controller)


if __name__ == "__main__":
    app = Defauthon()
    app.state("zoomed")
    app.title("Defauthon v4.0")
    # app.geometry("1294x800")
    app.mainloop()
    