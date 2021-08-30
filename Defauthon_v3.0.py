# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:18:50 2021.

@author: THIVET Julien // contact : j.thivet@esff.fr
"""

import tkinter as tk
# from PIL import ImageTk ,Image
# from tkinter import ttk
import progressbar


LARGE_FONT = ("Calibri", 14)
VERY_LARGE_FONT = ("Calibri", 21)


# Livreionnaire rassemblant toutes les infos sur les défauts classifié avec le livre "Recherche de la qualité de pièce en fonderie" (livre vert)
Livre = {"A": "A - Excroissances métalliques.",

            "A100": "A100 - Excroissances métalliques en forme de toile (ou de bavure)...",
                "A110": "...SANS modification des dimensions principales du moulage.",
                    "A111": ("Toile (ou bavure) de faible épaisseur dans le plan de joint ou dans une portée de noyau.", "Bavure de joint ou Barbe."),
                    "A112": ("Excroissance en forme de veines à la surface du moulage.", "Gerce ou Nervure."),
                    "A113": ("Excroissance en réseau à la surface de pièces coulées sous pression.", "Moule craquelé."),
                    "A114": ("Excroissance mince parallèle à une surface dans les angles rentrants.", "Gales d'angle."),
                    "A115": ("Excroissance métallique mince située dans un angle rentrant et partageant cet angle en deux parties.", "Gerce d'angle."),
                "A120": "...AVEC modification des dimensions principales du moulage.",
                    "A121": ("Toile épaisse attenante au moulage dans le plan de joint.", "Soulèvement du moule."),
                    "A122": ("Toile épaisse en d'autres endroits du moulage.", "Défoncement du moule."),
                    "A123": ("Formation de toiles dans un plan déterminé par rapport à la direction de montage (coulée de précision en modèle perdu).", "Moule fendu."),
            "A200": "A200 - Excroissances massives.",
                "A210": "Forçage.",
                    "A211": ("Surépaisseur sur les faces externes ou internes du moulage.", "Forçage extérieur ou intérieur."),
                    "A212": ("Surépaisseur au voisinage de l'attaque ou au-dessous de la coulée.", "Erosion."),
                    "A213": ("Excroissance en forme de plages allongées dans le sens d'un remmoulage à faible jeu.", "Frotte."),
                "A220": "Excroissances à surface rugueuse...",
                    "A221": ("...à la surface supérieure du moulage.", "Chute de sable."),
                    "A222": ("...à la surface inférieure du moulage (excroissance massive).", "Soulèvement d'un élément de moule ou du noyau."),
                    "A223": ("...à la surface inférieure du moulage (en éléments dispersés).", "Soulèvement de sable."),
                    "A224": ("...dans les autres parties du moulage.", "Casse localisée ou dèche."),
                    "A225": ("...sur de larges régions du moulage.", "Gale d'extrémité."),
                    "A226": ("Excroissance dans une cavité formée par un noyau.", "Noyau écrasé ou cassé."),
            "A300": "A300 - Autres excroissances métalliques.",
                "A310": "Petites excroissances métalliques à surface lisse.",
                    "A311": ("Excroissance de forme plus ou moins sphériques sur les faces ou les arrêtes ou dans les angles rentrants.", "Resuage. \nPour les fontes : goutte phosphoreuse ou diamant. \nPour la fonderie de précision : bulle."),
        
        "B": "B - Cavités.",
            "B100": "B100 - Cavités à parois généralement rondes, lisses, que l'on peut distinguer et isoler à l'oeil nu ... (soufflures, piqûres, bouillonnement)",
                "B110": "...intérieures au moulage, sans communication avec l'extérieur, \ndécelables seulement à l'aide de procédés spéciaux \nou à l'usinage ou encore à la cassure de la pièce.",
                    "B111": ("Cavités rondes à parois généralement lisses, de grosseurs variées, isolées ou en groupes irréguliers dans toutes les régions du moulage.", "Piqûres, Soufflures, Bouillonnement."),
                    "B112": ("Comme ci contre, mais limitées au voisinage des pièces métalliques placées dans le moule", "Soufflures sur supports, sur pièces insérées."),
                    "B113": ("Comme B 111, mais accompagnées d'inclusions de scories (G 112).", " Soufflures de scories."),
                "B120": "...situées à la surface ou au voisinage de la surface, \nlargement ouvertes \nou au moins en communication avec l'extérieur...",
                    "B121": ("...de grosseurs diverses, isolées ou en groups, le plus souvent superficielles, avec des parois brillantes.", "Soufflures superficielles. Refus."),
                    "B122": ("...dans les angles rentrants des moulages atteignant souvent des régions profondes.", "Soufflures d'angle. Soufflures retassures. Effet Léonard."),
                    "B123": ("Petites porosités (cavités) à la surface des moulages, apparaissant dans des régions plus ou moins étendues.", "Piqûres superficielles."),
                    "B124": ("Petites cavités étroites en forme de criques apparaissant sur des faces ou le long d'arrêtes en général seulement après l'usinage.", "Défauts en virgules. Retassures dispersées."),
            "B200": "B200 - Cavités à parois généralement rugueuses. Retassures.",
                "B210": "Cavité ouverte selon B 200 \npouvant pénétrer profondément dans le moulage.",
                    "B211": ("Cavité en forme d'entonnoir. Parois en général garnies de dendrites.", "Retassure ouverte. Retassure externe."),
                    "B212": ("Cavité à arêtes aiguës dans les angles des pièces épaisses ou aux attaques de coulées.", "Retassure d'angle."),
                    "B213": ("Cavité en communication avec un noyau", "Retassure de noyau."),
                "B220": "... située entièrement à l'intérieur du moulage.",
                    "B221": ("Cavité de forme irrégulière. Parfois souvent garnies de dendrites.", "Retassure interne."),
                    "B222": ("Cavité ou région poreuse dans le plan médian du moulage.", "Retassure axiale."),
            "B300": "B300 - Régions poreuses, aspect spongieux, juxtaposition de nombreuses petites cavités.",
                "B310": "Région poreuse non visible ou à peine visible à l'oeil nu.",
                    "B311": ("Régions poreuses visibles à l'oeil nu.", "Porosités, Micro-retassures)."),

        "C": "C -  Solutions de continuité.",
            "C100": "C100 - Solution de continuité par suite d'un effet mécanique \n(D'après la forme de la pièce t l'aspect de la cassure, celle-ci ne semble pas résulter de tensions internes).",
                "C110": "Cassure normale.",
                    "C111": ("Aspect de cassure normale avec quelquesfois des traces de matage.", "Cassure à froid."),
                "C120": "Cassure oxydée.",
                    "C121": ("Cassure oxydée entièrement ou sur les bords.", "Cassure à chaud."),
            "C200": "C200 - Solutions de continuité dues à des tensions internes et à des obstacles s'opposant au retrait \n(criques et tapures).",
                "C210": "Tapure à froid.",
                    "C211": ("Solution de continuité à bords écartés, dans des régions sensibles aux tensions intéressant généralement toute la section; métal non oxydé.", "Tapude à froid."),
                "C220": "Tapure à chaud et crique.",
                    "C221": ("Solution de continuité de parcours irrégulier dans les région sensibles aux tensions. \nOxydation de la surface de séparation avec éventuellement structure dendritique fine.", "Crique."),
                    "C222": ("Rupture après solidification complète, en cours de refroidissement ou à l'occasion d'un traitement thermique", "Tapure à chaud, de trempe."),
            "C300": "C300 - Solutions de continuité par défaut de soudure (reprise). \nLes bords en général arrondis permettent de conclure à un mauvais contact entre \nles divers courants de métal liquiquide lors du remplissage du moule.",
                "C310": "Manque de liason ou de continuité dans les parties alimentées en dernier lieu.",
                    "C311": ("Séparation complète ou partielle souvent dans un plan vertical.", "Reprise."),
                "C320": "Manque de liaison entre deux parties du moulage.",
                    "C321": ("Séparation du moulage dans un plan horizontal", "Coulée interrompue."),
                "C330": "Manque de liason au voisinage des supports de noyau, des refroidisseurs internes, des pièces insérées.",
                    "C331": ("Solution de continuité localisée au voisinage d'une pièce insérée.", "Reprise sur support de noyau ou autre pièce insérée."),
            "C400": "C400 - Solutions de continuité par suite de défaut métallurgique.",
                "C410": "Spération le long des joints de grains.",
                    "C411": ("Séparation le long des joints de grains de cristallisation primaire", "Cassure conchoïdale ou de \"sucre candi\"."),
                    "C412": ("Criques en réseau sur tout la section (défaut du zinc coulé sous pression)", "Corrosion inter-granulaire."),

        "D": "D- Surface défectueuse.",
            "D100": "D100 - Irrégularités de la surface du moulage.",
                "D110": "Plissement de la peau du moulage.",
                    "D111": ("Plissement sur des régions assez importantes de la surface.", "Peau de crapaud. Friasses."),
                    "D112": ("Surface plissée ou sillonée par des anfractuosités en réseaux (fonte G.S.).", "Peau d'éléphant."),
                    "D113": ("Plis serpentant sans solution de continuité. Les bords du pli sont au même niveau. La surface de moulage est lisse.", "Rides."),
                    "D114": ("Lignes marquant, sur la surface du moulage, l'écoulement du métal liquide (alliage légers).", "Fleurs. Traces d'écoulement."),
                "D120": "Surface rugueuse.",
                    "D121": ("Rugosités dont la profondeur est de l'ordre de frandeur des dimensions des grains de sable.", "Rugosité."),
                    "D122": ("Rugosités dont la profondeur est supérieure aux dimensions des grains de sable.", "Forte rugosité. Pénétration. Coup de feu."),
                "D130": "Sillons dans la surface du moulage.",
                    "D131": ("Sillons de diverses longueurs, souvent ramifiés, avec fond d'entaille et bords adoucis.", "Stries."),
                    "D132": ("Sillons pouvant atteindre 5mm de profondeur, l'un des deux bords formant un pli qui recouvre plus ou moins complètement le sillon.", "Queue de rat."),
                    "D133": ("Dépressions irréglièrement réparties de dimensions variées courant à la surface du moulafe, le plus souvent en suivant le chemin d'écoulement du métal liquide(acier moulé).", "Cicatrices."),
                    "D134": ("Surface grêlée comme marquée de petite vérole sur toute la pièce.", "Peau d'orange."),
                    "D135": ("Sillons et rugosités au voisinage des angles rentrants de la pièce en coulée sous pression.", "Etamage. Erosion."),
                "D140": "Affaissements de la surface du moulage.",
                    "D141": ("Dépression à la surface du moulgae dans un région d'accumulation de chaleur.", "Poquette."),
                    "D142": ("Petite cavités superficielle en forme de gouttes oud e cuvettes en général colorées en g-vert \n(aciers au chrome carburés, coulés en fonderie de précision à modèle perdu).", "Inclusion de scorie."),
            "D200": "D200 - Irrégularités assez importantes à la surface du moulage.",
                "D210": "Irrégularité par approfondissement.",
                    "D211": ("Approfondissement souvent étendu  sans contrepartie.", "Enfoncement (de moule)."),
                "D220": "Adhérence de sable plus ou moins vitrifié.",
                    "D221": ("Sable adhérent fortement à la pièce et formant surépaisseur.", "Sable brûlé, grippure."),
                    "D222": ("Sable très adhérent et en partie fondu.", "Vitrification."),
                    "D223": ("Conglomérat de sable et de métal hérant fortement au moulage dans les régions les plus chaudes (angles rentrants et noyaux).", "Abreuvage.."),
                    "D224": ("Ecaille de moule emprisonnée dans le métal (fonderie de précision à modèle perdu).", "Décollement de la première couche. Gale."),
                "D230": "Excroissance métalliques en forme de lames à parois rugueuses en général parallèles à la surface du moulage.",
                    "D231": ("Excroissance métallique en forme de lame à parois rugueuses parallèles à la surface, susceptible d'être éliminée par burinage.", "Gale franche."),
                    "D232": ("Comme ci-dessus, mais l'élimination n'est possible que par usinage ou meulage.", "Gale volante."),
                    "D233": ("Excroissances métalliques plates sur des moulages obtenus en moules étuvés passés à la couche ou au noir ou en moules à vert avec des noyaux passés à la couche ou au noir.", "Dartres."),
                "D240": "Adhérence d'oxydes à la suite de traitement thermique (recuit, revenu, malléabilisation pr décarburation).",
                    "D241": ("Adhérence d'oxyde après recuit.", "Calamine."),
                    "D242": ("Adhérence de minerai après recuit de malléable à coeur blanc.", "Collage de minerai."),
                    "D243": ("Ecaillage après recuit de malléable à coeur blanc.", "Ecaillage."),
                    
        "E": "E - Pièce incomplète.",
            "E100": "E100 - Partie manquante sans cassure.",
                "E110": "Ecarts minimes par rapport au tracé.",
                    "E111": ("La pièce est, dans l'ensemble, complète à l'exception d'arêtes plus ou moins arrondies.", "Malvenu."),
                    "E112": ("Arêtes ou contours déformés par la suite de mauvaises retouches du moule ou de passage à la couche défectueux.", "Défauts de réparation ou de passage à la couche."),
                "E120": "Ecarts importants par rapport au tracé.",
                    "E121": ("Pièce incomplète par suite de solidification prématurée.", "Manque."),
                    "E122": ("Pièce incomplète par insuffisance de métal.", "Coulé court."),
                    "E123": ("Pièce incomplète par suite de fuite de métal hors du moule.", "Moule vidé."),
                    "E124": ("Manque de matière important par suite d'un grenaillage exagéré.", "Grenaillage excessif."),
                    "E125": ("Moulage partiellement fondu ou profondément déformé au cours du recuit.", "Fusion ou effondrement au recuit."),
            "E200": "E200 - Partie manquante avec cassure.",
                "E210": "Pièce cassée.",
                    "E211": ("Pièce cassée, partie manquante importante. Cassure non oxydée.", "Cassure à froid."),
                "E220": "Pièce ébréchée.",
                    "E221": ("Cassure de dimension limitée au voisinage des attaques, évents, etc. Angle cassé ou maté.", "Jet, masselitte ou évent cassé dans la pièce. Epaufrure."),
                "E230": "Pièce cassé avec cassure oxydée.",
                    "E231": ("L'aspect de la cassure montre qu'elle a subi une oxydation à chaud.", "Cassure à chaud."),

        "F": "F - Dimensions ou forme incorrectes.",
            "F100": "F100 - Dimensions incorrectes mais forme correcte.",
                "F110": "Les cotes sont fausses dans l'ensemble.",
                    "F111": ("Toutes les cotes sont fausses dans une même proportion.", "Erreur dans la prévision du retrait."),
                "F120": "Les cotes sont fausses, mais seulement en partie.",
                    "F121": ("Trop grandes distances entre parties fortement saillantes.", "Retrait contrarié."),
                    "F122": ("Certaines cotes sont inexactes.", "Retrait irrégulier."),
                    "F123": ("Les cotes sont trop grandes dans le sens de l'ébranlage.", "Excès d'ébranlage."),
                    "F124": ("Les cotes sont trop grandes dans le sens perpandiculaire au plan de joint.", "Dilatation du moule à l'étuvage."),
                    "F125": ("Surépaisseurs irrégulières sur quelques faces externes. Identique à A211 (forçage).", "Serrage irrégulier. Serrage insuffisant."),
                    "F126": ("Parois d'épaisseur inférieure à la cote, surtout s'agissant de surfaces horizontales.", "Modèle ou plaque mmodèle déformé. Voile."),
            "F200": "F200 - Forme incorrecte dans l'ensemble ou dans certaines parties du moulage.",
                "F210": "Modèle incorrect.",
                    "F211": ("Le moulage ne correspond pas au tracé soit dans son ensemble, soit dans certaines régions. Il en est de même du modèle.", "Modèle incorrect."),
                    "F212": ("En un endroit bien déterminé le moulage ne correspond pas au tracé. Le modèle est correct.", "Erreur de montage du modèle."),
                "F220": "Variation.",
                    "F221": ("La pièce semble avoir subi un commencement de cisaillement dans le plan de joint.", "Variation de :\n - modèle \n - portée \n - plaque-modèle \n - moule \n - coquille \n Déformation de châssis. Déplacement de moule."),
                    "F222": ("Variation sur une face interne d'une pièce dans le plan de joint du noyau.", "Variation de noyau."),
                    "F223": ("Saillie irrégulière généralement unilatérale sur des faces verticales, en général au voisinage du plan de joint.", "Fausse variation."),
                "F230": "Déformation à partir d'une forme correcte.",
                    "F231": ("Déformation par rapport au tracé sur le moulagen le moule et le modèle.", "Modèle déformé."),
                    "F232": ("Déformation par rapport au tracé sur le moulage et le moule. Le modèle est conforme au tracé.", "Moule déformé."),
                    "F233": ("Déformation du moulage par rapport au tracé. Le moule et le modèle sont conformes au tracé.", "Déformation au retrait."),
                    "F234": ("Déformation du moulage par rapport au tracé.", "Déformation différée."),
                    
        "G": "G - Inclusions ou anomalie de structure.",
            "G100": "G100 - Inclusions.",
                "G110": "Inclusions métalliques.",
                    "G111": ("Inclusions métallique dont l'aspect, l'analyse chimique ou l'examen structural montrent qu'il s'agit d'un élément étranger à l'alliage.", "Inclusion métallique d'origine extérieure, combinaison intermétallique."),
                    "G112": ("Inclusion de même composition chimique que le métal de base, en général sphérique et souvent enveloppée d'une couche d'oxyde.", "Goutte froide."),
                    "G113": ("Inclusions métalliques sphériques dans des soufflures ou autres cavités du moulage ou dans les affaissements de la surface (voir alors défaut A 311). La composition s'apparente à celle de l'alliage coulé mais avec des différences qui la rapprochent de celle de l'eutectique.", "Ressuage interne; diamant : goutte phosphoreuse; (fonte)."),
                "G120": "Inclusions non métalliques, laitier, scories, flux.",
                    "G121": ("Inclusions non métalliques dont l'aspect ou l'analyse montrent qu'elles proviennent des laitiers d'élaboration, \ndes produits de traitement ou des flux.", "Inclusions de laitier, de produits de traitement, de flux."),
                    "G122": ("Inclusions non métalliques en général imprégnées de gaz \net accompagnées de soufflures (B 113).", "Inclusion de scorie congénitale, mousse, soufflures de scories."),
                "G130": "Inclusions non métalliques, matériau de moule ou de noyau.",
                    "G131": ("Inclusion de sable en général très près de la surface du moulage.", "Inclusion de sable."),
                    "G132": ("Inclusion de noir ou de couche en général très près de la surface du moulage.", "Inclusion de noir ou de couche."),
                "G140": "Inclusions non métalliques, oxydes et produit de réaction.",
                    "G141": ("Taches noires irrégulières, nettement délimitées dans la cassure defonte à graphite sphéroïdal.", "Taches noires."),
                    "G142": ("Inclusions en forme de peau constituées d'oxydes, le plus souvent avec interruption locale de la continuité.", "Inclusion d'oxyde. Peaux d'oxyde."),
                    "G143": ("Peaux plissées au brillant graphitique dans la paroi du moulage", "Peau de graphite brillante."),
                    "G144": ("Inclusions dures en coulée d'aluminium par gravité et sous pression.", "Points durs."),
            "G200": "G200 - Anomalie de structure (visibles par observation macrographique).",
                "G210": "Structure anormale de la fonte à graphite lamellaire.",
                    "G211": ("Structure partiellement ou totalement blanche, particulièrement dans les parois minces, les angles saillants et les arrêtes, passant progressivement à la structure normale.", "Trempe primaire. Trempe primaire partielle. Zones blanches. \nArrêtes blanches. Anomalie de dureté."),
                    "G212": ("Comme G 211 mais avec passage sans transition à la structure normale.", "Trempe primaire partielle sans transition. Trempe nette."),
                    "G213": ("Zone blanche nettement délimitée dans les parties de la pièce solidifiées en dernier lieu. La structure près de la surface est grise.", "Trempe inverse."),
                "G220": "Structure anormales en malléable.",
                    "G221": ("Taches foncées dans le moulage brut; cassure gris-noir à gros grains après traitement.", "Graphite primaire."),
                    "G222": ("Malléable à coeur noir. La cassure après recuit fait apparaître une banqde claire brillante de plus \nde 0.5mm d'épaisseur au voisinage de la paroi, avec une région interne foncée.", "Couche superficielle dure de faible."),
                    "G223": ("Couche superficielle dure de faible profondeur \ndont la structure comporte des constituants de trempe.", "Ducissement superficiel localisé."),
                "G260": "Formation anormale de graphite.",
                    "G261": ("Graphite très grossier régulièrement réparti.", "Piqûres de graphite."),
                    "G262": ("Accumulation locale de graphite grossier dans la structure. Précipitation de graphite dans les cavités (resttasures).", "Nids de graphite."),
                    "G263": ("Amas de sphérules dans les régions supérieures du moulage (fonte G.S).", "Décantation de sphérolithes."),
                    "G264": ("Cassure présentant des facettes planes diversement orientées (fonte G.S., alliage eutectique Al-Si).0", "Alignement de sphéroïdes. Cassure à facettes."),
        }


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
    return r"G:/Boulot/Ferry_Capitain/Defautheque/Defauthon/Donnees/" + Xnnn + "/" + Xnnn + ".png"


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


illustrations = {}


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
    tk.Button(self, text=Livre[X], bg='#8B0000', relief="ridge", bd=10, font=VERY_LARGE_FONT,
              command=lambda: controller.show_frame(page_suivante)).grid(row=row, column=column, sticky="nsew")
    
    
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
    tk.Button(self, text=Livre[Xn], relief="ridge", bg='orange', bd=10, font=LARGE_FONT,
              command=lambda: controller.show_frame(page_suivante)).grid(row=row, column=column, sticky="nsew")


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
    tk.Button(self, text=Livre[Xnn] + "\n | \n\/", relief="ridge", bg='yellow', bd=10, font=LARGE_FONT,
              command=lambda: controller.show_frame(page_suivante)).grid(row=row, column=column, sticky="nsew")


def affiche_info_defaut(self, text, controller):
    print("zorg")
    Info_defaut.modify_text(self, text)
    controller.show_frame(Info_defaut)
    print("antizorg")


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
    # try:
    # Avec image: -----------------------------
    self.illustrations[Xnnn] = tk.PhotoImage(master=self, file=path_photo(Xnnn))
    r = self.illustrations[Xnnn].height() / 100  # Coefficient de "dezoom" à donner pour avoir au ax 125 pixel de haut
    self.illustrations[Xnnn] = self.illustrations[Xnnn].subsample(int(r + 0.5))
    
    # Cas particuliers
    if Xnnn == "B112":
        self.illustrations[Xnnn] = self.illustrations[Xnnn].subsample(2)
    if Xnnn == "G221" or Xnnn == "G222":
        self.illustrations[Xnnn] = self.illustrations[Xnnn].zoom(2)
    
    print("1")
    tk.Button(self, text=Livre[Xnnn][1], relief="raised", bd=10, font=LARGE_FONT,
              image=self.illustrations[Xnnn], compound="right",
              command=self.affiche_info_defaut(Xnnn, controller())).grid(row=row, column=column, sticky="nsew").grid(row=row, column=column, sticky="nsew")
    print('2')
    
    # except Exception:
    #     # Sans image: -----------------------------
    #     self.boutons[Xnnn] = tk.Button(self, text=Livre[Xnnn][1], relief="raised", bd=10, font=LARGE_FONT)
    # infoBulle(parent=self.boutons[Xnnn], texte=Livre[Xnnn][0])
    
    
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
    tk.Button(self, text=text, font=LARGE_FONT, bg='gray', relief="sunken", bd=10,
              command=lambda: controller.show_frame(page_avant)).grid(row=row, column=column, sticky="nsew")  #, image=self.retour, compound="right")
    

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
    tk.Label(self, text=Livre[X], bg='#8B0000', font=VERY_LARGE_FONT).grid(row=row, column=column, sticky="nsew")


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
    tk.Label(self, text=Livre[Xn] + str(args)[2:-3], bg='orange', font=LARGE_FONT).grid(row=row, column=column, columnspan=2, sticky="nsew")
    
    
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
    tk.Label(self, text=Livre[Xnn], bg='yellow', font=LARGE_FONT).grid(row=row, column=column, sticky="nsew")


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

        for F in progressbar.progressbar([Accueil, Info_defaut,
                                          PageA, PageA100,  #PageA200, PageA300,
                                          # PageB, PageB100, PageB200, PageB300,
                                          # PageC, PageC100, PageC200, PageC300, PageC400,
                                          # PageD, PageD100, PageD100bis, PageD200, PageD200bis,
                                          # PageE, PageE100, PageE200,
                                          # PageF, PageF100, PageF200, PageF200bis,
                                          # PageG, PageG100, PageG100bis, PageG200, PageG200bis,
                                          ]):

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
            
            # print("Ok pour", F)

        self.show_frame(Accueil)

    def show_frame(self, cont):
        """
        Permet de changer de page.

        Parameters
        ----------
        cont : Le nom d'une page (i.e. d'une classe définit plus bas).

        Returns
        -------
        changement de frame.
        """
        frame = self.frames[cont]
        frame.tkraise()


class Info_defaut(tk.Frame):
    """Page résume d'un défaut qui vient s'adapter à chaque défaut en fonction de ce qu'il y a en données dans le dossier correspondant."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.labeltext = "toto"
        self.label = tk.Label(self, text=self.labeltext, font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")
        
    def modify_text(self, new_text):
        """
        Modify le texte du label.

        Parameters
        ----------
        new_text : string

        """
        self.labeltext = new_text
    print("ok")


class Accueil(tk.Frame):
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


class PageA(tk.Frame):
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


class PageA100(tk.Frame):
    """PageA100 (9 défauts)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label_niv1("A100", 0, 0)
        
        # ------------------------------- A110 -------------------------------
        self.label_niv2("A110", 1, 0)
        
        self.button = tk.Button(self, text=Livre["A111"][1], command=lambda: self.affiche_defaut())
        self.button.grid(row=0, column=0)
        
        for i in range(5):
            self.bouton_selection_niv3("A11" + str(i + 1), 2 + i, 0, controller)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- A120 -------------------------------
        self.label_niv2("A120", 1, 1)
        
        for i in range(3):
            self.bouton_selection_niv3("A12" + str(i + 1), 2 + i, 1, controller)

        self.bouton_retour(PageA, 6, 1, controller)


class PageA200(tk.Frame):
    """PageA200 (10 défauts)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("A200", 0, 0)
        
        # ------------------------------- A210 -------------------------------
        self.label_niv2("A210", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("A21" + str(i + 1), 2 + i, 0)

        # ------------------------------- A220 -------------------------------
        self.label_niv2("A220", 1, 1)

        for i in range(6):
            self.bouton_selection_niv3("A22" + str(i + 1), 2 + i, 1)

        self.bouton_retour(PageA, 7, 0, controller)


class PageA300(tk.Frame):
    """PageA300 (1 défaut)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("A300", 0, 0)
        
        # ------------------------------- A310 -------------------------------
        self.label_niv2("A310", 1, 0)

        self.bouton_selection_niv3("A311", 2, 0)
        
        self.bouton_retour(PageA, 3, 0, controller)


class PageB(tk.Frame):
    """Page de sélections des sous défauts B (B100/B200/B300)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("B", 0, 0)

        self.bouton_selection_niv1(PageB100, "B100", 1, 0, controller)
        self.bouton_selection_niv1(PageB200, "B200", 2, 0, controller)
        self.bouton_selection_niv1(PageB300, "B300", 3, 0, controller)
        self.bouton_retour(Accueil, 4, 0, controller)


class PageB100(tk.Frame):
    """PageB100 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("B100", 0, 0)
        
        # ------------------------------- B110 -------------------------------
        self.label_niv2("B110", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("B11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- B120 -------------------------------
        self.label_niv2("B120", 1, 1)
        
        for i in range(4):
            self.bouton_selection_niv3("B12" + str(i + 1), 2 + i, 1)

        self.bouton_retour(PageB, 5, 0, controller)


class PageB200(tk.Frame):
    """PageB200 (5 défauts)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("B200", 0, 0)
        
        # ------------------------------- B210 -------------------------------
        self.label_niv2("B210", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("B21" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- B220 -------------------------------
        self.label_niv2("B220", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("B22" + str(i + 1), 2 + i, 1)

        self.bouton_retour(PageB, 4, 1, controller)


class PageB300(tk.Frame):
    """PageB300 (1 défaut)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("B300", 0, 0)
        
        # ------------------------------- B310 -------------------------------
        self.label_niv2("B310", 1, 0)

        self.bouton_selection_niv3("B311", 2, 0)
        
        self.bouton_retour(PageB, 3, 0, controller)


class PageC(tk.Frame):
    """Page de sélections des sous défauts C (C100/C200/C300/C400)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("C", 0, 0)

        self.bouton_selection_niv1(PageC100, "C100", 1, 0, controller)
        self.bouton_selection_niv1(PageC200, "C200", 2, 0, controller)
        self.bouton_selection_niv1(PageC300, "C300", 3, 0, controller)
        self.bouton_selection_niv1(PageC400, "C400", 4, 0, controller)
        self.bouton_retour(Accueil, 5, 0, controller)


class PageC100(tk.Frame):
    """PageC100 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C100", 0, 0)
        
        # ------------------------------- C110 -------------------------------
        self.label_niv2("C110", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("C11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- C120 -------------------------------
        self.label_niv2("C120", 1, 1)
        
        for i in range(1):
            self.bouton_selection_niv3("C12" + str(i + 1), 2 + i, 1)

        self.bouton_retour(PageC, 3, 1, controller)


class PageC200(tk.Frame):
    """PageC200 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C200", 0, 0)
        
        # ------------------------------- C210 -------------------------------
        self.label_niv2("C210", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("C21" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- C220 -------------------------------
        self.label_niv2("C220", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("C22" + str(i + 1), 2 + i, 1)

        self.bouton_retour(PageC, 3, 0, controller)
    

class PageC300(tk.Frame):
    """PageC300 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C300", 0, 0)
        
        # ------------------------------- C310 -------------------------------
        self.label_niv2("C310", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("C31" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- C320 -------------------------------
        self.label_niv2("C320", 1, 1)
        
        for i in range(1):
            self.bouton_selection_niv3("C32" + str(i + 1), 2 + i, 1)
            
        # ------------------------------- C330 -------------------------------
        self.label_niv2("C330", 3, 0)
        
        self.bouton_selection_niv3("C331", 4, 0)

        self.bouton_retour(PageC, 4, 1, controller)


class PageC400(tk.Frame):
    """PageC400 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("C400", 0, 0)
        
        # ------------------------------- C410 -------------------------------
        self.label_niv2("C410", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("C41" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageC, 4, 0, controller)


class PageD(tk.Frame):
    """Page de sélections des sous défauts D (D100/D200)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("D", 0, 0)

        self.bouton_selection_niv1(PageD100, "D100", 1, 0, controller)
        self.bouton_selection_niv1(PageD200, "D200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageD100(tk.Frame):
    """PageD100 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D100", 0, 0, " Page 1/2")
        
        # ------------------------------- D110 -------------------------------
        self.label_niv2("D110", 1, 0)
        
        for i in range(4):
            self.bouton_selection_niv3("D11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- D120 -------------------------------
        self.label_niv2("D120", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("D12" + str(i + 1), 2 + i, 1)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageD100bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=4, column=1, sticky="nsew")
        
        self.bouton_retour(PageD, 5, 1, controller)


class PageD100bis(tk.Frame):
    """PageD100bis ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D100", 0, 0, " Page 2/2")
        
        # ------------------------------- D130 -------------------------------
        self.label_niv2("D130", 1, 0)
        
        for i in range(5):
            self.bouton_selection_niv3("D13" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- D140 -------------------------------
        self.label_niv2("D140", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("D14" + str(i + 1), 2 + i, 1)
        
        self.bouton_retour(PageD100, 6, 1, controller)


class PageD200(tk.Frame):
    """PageD200 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D200", 0, 0, " Page 1/2")
        
        # ------------------------------- D210 -------------------------------
        self.label_niv2("D210", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("D21" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- D220 -------------------------------
        self.label_niv2("D220", 1, 1)
        
        for i in range(4):
            self.bouton_selection_niv3("D22" + str(i + 1), 2 + i, 1)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageD200bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=4, column=0, sticky="nsew")
        
        self.bouton_retour(PageD, 5, 0, controller)


class PageD200bis(tk.Frame):
    """PageD200bis ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("D200", 0, 0, " Page 2/2")
        
        # ------------------------------- D230 -------------------------------
        self.label_niv2("D230", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("D23" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageD200, 5, 0, controller)


class PageE(tk.Frame):
    """Page de sélections des sous défauts E (E100/E200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("E", 0, 0)

        self.bouton_selection_niv1(PageE100, "E100", 1, 0, controller)
        self.bouton_selection_niv1(PageE200, "E200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageE100(tk.Frame):
    """PageE100 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("E100", 0, 0)
        
        # ------------------------------- E110 -------------------------------
        self.label_niv2("E110", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("E11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- E120 -------------------------------
        self.label_niv2("E120", 1, 1)
        
        for i in range(5):
            self.bouton_selection_niv3("E12" + str(i + 1), 2 + i, 1)
        
        self.bouton_retour(PageE, 6, 0, controller)


class PageE200(tk.Frame):
    """PageD200 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("E200", 0, 0)
        
        # ------------------------------- E210 -------------------------------
        self.label_niv2("E210", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("E21" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- E220 -------------------------------
        self.label_niv2("E220", 1, 1)
        
        for i in range(1):
            self.bouton_selection_niv3("E22" + str(i + 1), 2 + i, 1)
            
        # ------------------------------- E230 -------------------------------
        self.label_niv2("E230", 3, 0)
        
        self.bouton_selection_niv3("E231", 4, 0)

        self.bouton_retour(PageE, 4, 1, controller)
    

class PageF(tk.Frame):
    """Page de sélections des sous défauts F (F100/F200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("F", 0, 0)

        self.bouton_selection_niv1(PageF100, "F100", 1, 0, controller)
        self.bouton_selection_niv1(PageF200, "F200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageF100(tk.Frame):
    """PageF100 ."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("F100", 0, 0)
        
        # ------------------------------- F110 -------------------------------
        self.label_niv2("F110", 1, 0)
        
        for i in range(1):
            self.bouton_selection_niv3("F11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- F120 -------------------------------
        self.label_niv2("F120", 1, 1)
        
        for i in range(6):
            self.bouton_selection_niv3("F12" + str(i + 1), 2 + i, 1)
        
        self.bouton_retour(PageF, 7, 0, controller)


class PageF200(tk.Frame):
    """PageF200 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("F200", 0, 0, " Page 1/2")
        
        # ------------------------------- F210 -------------------------------
        self.label_niv2("F210", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("F21" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- F220 -------------------------------
        self.label_niv2("F220", 1, 1)
        
        for i in range(3):
            self.bouton_selection_niv3("F22" + str(i + 1), 2 + i, 1)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageF200bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=5, column=1, sticky="nsew")
        
        self.bouton_retour(PageF, 5, 0, controller)


class PageF200bis(tk.Frame):
    """PageF200bis ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("F200", 0, 0, " Page 2/2")
        
        # ------------------------------- F230 -------------------------------
        self.label_niv2("F230", 1, 0)
        
        for i in range(4):
            self.bouton_selection_niv3("F23" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageF200, 6, 0, controller)


class PageG(tk.Frame):
    """Page de sélections des sous défauts G (G100/G200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv0("G", 0, 0)

        self.bouton_selection_niv1(PageG100, "G100", 1, 0, controller)
        self.bouton_selection_niv1(PageG200, "G200", 2, 0, controller)
        self.bouton_retour(Accueil, 3, 0, controller)


class PageG100(tk.Frame):
    """PageG100 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G100", 0, 0, " Page 1/2")
        
        # ------------------------------- G110 -------------------------------
        self.label_niv2("G110", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("G11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- G120 -------------------------------
        self.label_niv2("G120", 1, 1)
        
        for i in range(2):
            self.bouton_selection_niv3("G12" + str(i + 1), 2 + i, 1)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageG100bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=4, column=1, sticky="nsew")
        
        self.bouton_retour(PageG, 4, 0, controller)


class PageG100bis(tk.Frame):
    """PageG100bis ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G100", 0, 0, " Page 2/2")
        
        # ------------------------------- G130 -------------------------------
        self.label_niv2("G130", 1, 0)
        
        for i in range(2):
            self.bouton_selection_niv3("G13" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- G140 -------------------------------
        self.label_niv2("G140", 1, 1)
        
        for i in range(4):
            self.bouton_selection_niv3("G14" + str(i + 1), 2 + i, 1)
        
        self.bouton_retour(PageG100, 5, 0, controller)


class PageG200(tk.Frame):
    """PageG200 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G200", 0, 0, " Page 1/2")
        
        # ------------------------------- G210 -------------------------------
        self.label_niv2("G210", 1, 0)
        
        for i in range(3):
            self.bouton_selection_niv3("G21" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- G220 -------------------------------
        self.label_niv2("G220", 1, 1)
        
        for i in range(3):
            self.bouton_selection_niv3("G22" + str(i + 1), 2 + i, 1)

        # self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Next_button.png").subsample(20)
        self.buton_next = tk.Button(self, text="Next", font=LARGE_FONT, command=lambda: controller.show_frame(PageG200bis), bg='gray', relief="sunken", bd=10)  #, image=self.retour, compound="right")
        self.buton_next.grid(row=5, column=1, sticky="nsew")
        
        self.bouton_retour(PageG, 5, 0, controller)


class PageG200bis(tk.Frame):
    """PageD200 ."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_niv1("G200", 0, 0, " Page 2/2")
        
        # ------------------------------- G260 -------------------------------
        self.label_niv2("G260", 1, 0)  # oui 260 et pas 230, je pense qu'il manque une page dans le livre... à voir
        
        for i in range(4):
            self.bouton_selection_niv3("G26" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame
        
        self.bouton_retour(PageG200, 6, 0, controller)


if __name__ == "__main__":
    app = Defauthon()
    app.title("Defauthon v0")
    app.geometry("1294x800")
    app.mainloop()