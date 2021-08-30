# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:18:50 2021.

@author: THIVET Julien // contact : j.thivet@esff.fr
"""

import tkinter as tk
# from PIL import ImageTk ,Image

LARGE_FONT = ("Calibri", 14)


# Dictionnaire rassemblant toutes les infos sur les défauts classifié avec le livre "Recherche de la qualité de pièce en fonderie" (livre vert)
Dict = {"A": "A - Excroissances métalliques.",

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
                    "A311": ("Excroissance de forme plus ou moins sphériques sur les faces ou les arrêtes ou dans les angles rentrants.", "Resuage. Pour les fontes : goutte phosphoreuse ou diamant. Pour la fonderie de précision : bulle."),
        
        "B": "B - Cavités.",
            "B100": "B100 - Cavités à parois généralement rondes, lisses, que l'on peut distinguer et isoler à l'oeil nu ... (soufflures, piqûres, bouillonnement)",
                "B110": "...intérieures au moulage, sans communication avec l'extérieur, décelables seulement à l'aide de procédés spéciaux ou à l'usinage ou encore à la cassure de la pièce.",
                    "B111": ("Cavités rondes à parois généralement lisses, de grosseurs variées, isolées ou en groupes irréguliers dans toutes les régions du moulage.", "Piqûres, Soufflures, Bouillonnement."),
                    "B112": ("Comme ci contr, mais limitées au voisinage des pièces métalliques placées dans le moule", "Soufflures sur supports, sur pièces insérées."),
                    "B113": ("Comme B 111, mais accompagnées d'inclusions de scories (G 112).", " Soufflures de scories."),
                "B120": "...situées à la surface ou au voisinage de la surface, largement ouvertes ou au moins en communication avec l'extérieur...",
                    "B121": ("...de grosseurs diverses, isolées ou en groups, le plus souvent superficielles, avec des parois brillantes.", "Soufflures superficielles. Refus."),
                    "B122": ("...dans les angles rentrants des moulages atteignant souvent des régions profondes.", "Soufflures d'angle. Soufflures retassures. Effet Léonard."),
                    "B123": ("Petites porosités (cavités) à la surface des moulages, apparaissant dans des régions plus ou moins étendues.", "Piqûres superficielles."),
                    "B124": ("Petites cavités étroites en forme de criques apparaissant sur des faces ou le long d'arrêtes en général seulement après l'usinage.", "Défauts en virgules. Retassures dispersées."),
            "B200": "B200 - Cavités à parois généralement rugueuses. Retassures.",
                "B210": "Cavité ouverte selon B 200 pouvant pénétrer profondément dans le moulage.",
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
            "C100": "Solution de continuité par suite d'un effet mécanique (D'après la forme de la pièce t l'aspect de la cassure, celle-ci ne semble pas résulter de tensions internes).",
                "C110": "Cassure normale.",
                    "C111": ("Aspect de cassure normale avec quelquesfois des traces de matage.", "Cassure à froid."),
                "C120": "Cassure oxydée.",
                    "C121": ("Cassure oxydée entièrement ou sur les bords.", "Cassure à chaud."),
            "C200": "Solutions de continuité dues à des tensions internes et à des obstacles s'opposant au retrait (criques et tapures).",
                "C210": "Tapure à froid.",
                    "C211": ("Solution de continuité à bords écartés, dans des régions sensibles aux tensions intéressant généralement toute la section; métal non oxydé.", "Tapude à froid."),
                "C220": "Tapure à chaud et crique.",
                    "C221": ("Solution de continuité de parcours irrégulier dans les région sensibles aux tensions. Oxydation de la surface de séparation avec éventuellement structure dendritique fine.", "Crique."),
                    "C222": ("Rupture après solidification complète, en cours de refroidissement ou à l'occasion d'un traitement thermique", "Tapure à chaud, de trempe."),
            "C300": "Solutions de continuité par défaut de soudure (reprise). Les bords en général arrondis permettent de conclure à un mauvais contact entre les divers courants de métal liquiquide lors du remplissage du moule.",
                "C310": "Manque de liason ou de continuité dans les parties alimentées en dernier lieu.",
                    "C311": ("Séparation complète ou partielle souvent dans un plan vertical.", "Reprise."),
                "C320": "Manque de liaison entre deux parties du moulage.",
                    "C321": ("Séparation du moulage dans un plan horizontal", "Coulée interrompue."),
                "C330": "Manque de liason au voisinage des supports de noyau, des refroidisseurs internes, des pièces insérées.",
                    "C331": ("Solution de continuité localisée au voisinage d'une pièce insérée.", "Reprise sur support de noyau ou autre pièce insérée."),
            "C400": "Solutions de continuité par suite de défaut métallurgique.",
                "C410": "Spération le long des joints de grains.",
                    "C411": ("Séparation le long des joints de grains de cristallisation primaire", "Cassure conchoïdale ou de \"sucre candi\"."),
                    "C412": ("Criques en réseau sur tout la section (défaut du zinc coulé sous pression)", "Corrosion inter-granulaire."),

        "D": "D- Surface défectueuse.",
            "D100": "Irrégularités de la surface du moulage.",
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
                    "D142": ("Petite cavités superficielle en forme de gouttes oud e cuvettes en général colorées en g-vert (aciers au chrome carburés, coulés en fonderie de précision à modèle perdu).", "Inclusion de scorie."),
            "D200": "Irrégularités assez importantes à la surface du moulage.",
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
            "E100": "Partie manquante sans cassure.",
                "E110": "Ecarts minimes par rapport au tracé.",
                    "E111": ("La pièce est, dans l'ensemble, complète à l'exception d'arêtes plus ou moins arrondies.", "Malvenu."),
                    "E112": ("Arêtes ou contours déformés par la suite de mauvaises retouches du moule ou de passage à la couche défectueux.", "Défauts de réparation ou de passage à la couche."),
                "E120": "Ecarts importants par rapport au tracé.",
                    "E121": ("Pièce incomplète par suite de solidification prématurée.", "Manque."),
                    "E122": ("Pièce incomplète par insuffisance de métal.", "Coulé court."),
                    "E123": ("Pièce incomplète par suite de fuite de métal hors du moule.", "Moule vidé."),
                    "E124": ("Manque de matière important par suite d'un grenaillage exagéré.", "Grenaillage excessif."),
                    "E125": ("Moulage partiellement fondu ou profondément déformé au cours du recuit.", "Fusion ou effondrement au recuit."),
            "E200": "Partie manquante avec cassure.",
                "E210": "Pièce cassée.",
                    "E211": ("Pièce cassée, partie manquante importante. Cassure non oxydée.", "Cassure à froid."),
                "E220": "Pièce ébréchée.",
                    "E221": ("Cassure de dimension limitée au voisinage des attaques, évents, etc. Angle cassé ou maté.", "Jet, masselitte ou évent cassé dans la pièce. Epaufrure."),
                "E230": "Pièce cassé avec cassure oxydée.",
                    "E231": ("L'aspect de la cassure montre qu'elle a subi une oxydation à chaud.", "Cassure à chaud."),

        "F": "F - Dimensions ou forme incorrectes.",
            "F100": "Dimensions incorrectes mais forme correcte.",
                "F110": "Les cotes sont fausses dans l'ensemble.",
                    "F111": ("Toutes les cotes sont fausses dans une même proportion.", "Erreur dans la prévision du retrait."),
                "F120": "Les cotes sont fausses, mais seulement en partie.",
                    "F121": ("Trop grandes distances entre parties fortement saillantes.", "Retrait contrarié."),
                    "F122": ("Certaines cotes sont inexactes.", "Retrait irrégulier."),
                    "F123": ("Les cotes sont trop grandes dans le sens de l'ébranlage.", "Excès d'ébranlage."),
                    "F124": ("Les cotes sont trop grandes dans le sens perpandiculaire au plan de joint.", "Dilatation du moule à l'étuvage."),
                    "F125": ("Surépaisseurs irrégulières sur quelques faces externes. Identique à A211 (forçage).", "Serrage irrégulier. Serrage insuffisant."),
                    "F126": ("Parois d'épaisseur inférieure à la cote, surtout s'agissant de surfaces horizontales.", "Modèle ou plaque mmodèle déformé. Voile."),
            "F200": "Forme incorrecte dans l'ensemble ou dans certaines parties du moulage.",
                "F210": "Modèle incorrect.",
                    "F211": ("Le moulage ne correspond pas au tracé soit dans son ensemble, soit dans certaines régions. Il en est de même du modèle.", "Modèle incorrect."),
                    "F212": ("En un endroit bien déterminé le moulage ne correspond pas au tracé. Le modèle est correct.", "Erreur de montage du modèle."),
                "F220": "Variation.",
                    "F221": ("La pièce semble avoir subi un commencement de cisaillement dans le plan de joint.", "Variation de : - modèle \n - portée \n - plaque-modèle \n - moule \n - coquille \n Déformation de châssis. Déplacement de moule."),
                    "F222": ("Variation sur une face interne d'une pièce dans le plan de joint du noyau.", "Variation de noyau."),
                    "F223": ("Saillie irrégulière généralement unilatérale sur des faces verticales, en général au voisinage du plan de joint.", "Fausse variation."),
                "F230": "Déformation à partir d'une forme correcte.",
                    "F231": ("Déformation par rapport au tracé sur le moulagen le moule et le modèle.", "Modèle déformé."),
                    "F232": ("Déformation par rapport au tracé sur le moulage et le moule. Le modèle est conforme au tracé.", "Moule déformé."),
                    "F233": ("Déformation du moulage par rapport au tracé. Le moule et le modèle sont conformes au tracé.", "Déformation au retrait."),
                    "F234": ("Déformation du moulage par rapport au tracé.", "Déformation différée."),
                    
        "G": "G - Inclusions ou anomalie de structure.",
            "G100": "Inclusions.",
                "G110": "Inclusions métalliques.",
                    "G111": ("Inclusions métallique dont l'aspect, l'analyse chimique ou l'examen structural montrent qu'il s'agit d'un élément étranger à l'alliage.", "Inclusion métallique d'origine extérieure, combinaison intermétallique."),
                    "G112": ("Inclusion de même composition chimique que le métal de base, en général sphérique et souvent enveloppée d'une couche d'oxyde.", "Goutte froide."),
                    "G113": ("Inclusions métalliques sphériques dans des soufflures ou autres cavités du moulage ou dans les affaissements de la surface (voir alors défaut A 311). La composition s'apparente à celle de l'alliage coulé mais avec des différences qui la rapprochent de celle de l'eutectique.", "Ressuage interne; diamant : goutte phosphoreuse; (fonte)."),
                "G120": "Inclusions non métalliques, laitier, scories, flux.",
                    "G121": ("Inclusions non métalliques dont l'aspect ou l'analyse montrent qu'elles proviennent des laitiers d'élaboration, des produits de traitement ou des flux.", "Inclusions de laitier, de produits de traitement, de flux."),
                    "G122": ("Inclusions non métalliques en général imprégnées de gaz et accompagnées de soufflures (B 113).", "Inclusion de scorie congénitale, mousse, soufflures de scories."),
                "G130": "Inclusions non métalliques, matériau de moule ou de noyau.",
                    "G131": ("Inclusion de sable en général très près de la surface du moulage.", "Inclusion de sable."),
                    "G132": ("Inclusion de noir ou de couche en général très près de la surface du moulage.", "Inclusion de noir ou de couche."),
                "G140": "Inclusions non métalliques, oxydes et produit de réaction.",
                    "G141": ("Taches noires irrégulières, nettement délimitées dans la cassure defonte à graphite sphéroïdal.", "Taches noires."),
                    "G142": ("Inclusions en forme de peau constituées d'oxydes, le plus souvent avec interruption locale de la continuité.", "Inclusion d'oxyde. Peaux d'oxyde."),
                    "G143": ("Peaux plissées au brillant graphitique dans la paroi du moulage", "Peau de graphite brillante."),
                    "G144": ("Inclusions dures en coulée d'aluminium par gravité et sous pression.", "Points durs."),
            "G200": "Anomalie de structure (visibles par observation macrographique).",
                "G210": "Structure anormale de la fonte à graphite lamellaire.",
                    "G211": ("Structure partiellement ou totalement blanche, particulièrement dans les parois minces, les angles saillants et les arrêtes, passant progressivement à la structure normale.", "Trempe primaire. Trempe primaire partielle. Zones blanches. Arrêtes blanches. Anomalie de dureté."),
                    "G212": ("Comme G 211 mais avec passage sans transition à la structure normale.", "Trempe primaire partielle sans transition. Trempe nette."),
                    "G213": ("Zone blanche nettement délimitée dans les parties de la pièce solidifiées en dernier lieu. La structure près de la surface est grise.", "Trempe inverse."),
                "G220": "Structure anormales en malléable.",
                    "G221": ("Taches foncées dans le moulage brut; cassure gris-noir à gros grains après traitement.", "Graphite primaire."),
                    "G222": ("Malléable à coeur noir. La cassure après recuit fait apparaître une banqde claire brillante de plus de 0.5mm d'épaisseur au voisinage de la paroi, avec une région interne foncée.", "Couche superficielle dure de faible."),
                    "G223": ("Couche superficielle dure de faible profondeur dont la structure comporte des constituants de trempe.", "Ducissement superficiel localisé."),
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
    return r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/" + Xnnn + ".png"


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
    
    def bouton_selection_niv0(self, page_suivante, X, row, column, controller):
        """
        
        Patern de création pour les boutons de niveau 0: i.e ceux qui amène à un choix de type Xn00 (niveau 1).

        Parameters
        ----------
        Xnnn : float
            Exemple : "A100"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.boutons[X] = tk.Button(self, text=Dict[X], bg='red', relief="ridge", bd=10, font=LARGE_FONT, command=lambda: controller.show_frame(page_suivante))
        self.boutons[X].grid(row=row, column=column, sticky="nsew")
        
    def bouton_selection_niv1(self, page_suivante, Xnnn, row, column, controller):
        """
        
        Patern de création pour les boutons de niveau 1 : i.e ceux qui amène à un choix de type Xnn0 (niveau 2).

        Parameters
        ----------
        Xnnn : float
            Exemple : "A100"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.boutons[Xnnn] = tk.Button(self, text=Dict[Xnnn], relief="ridge", bg='orange', bd=10, font=LARGE_FONT, command=lambda: controller.show_frame(page_suivante))
        self.boutons[Xnnn].grid(row=row, column=column, sticky="nsew")
    
    def bouton_selection_niv2(self, page_suivante, Xnnn, row, column, controller):
        """
        Patern de création pour les boutons de niveau 2 : i.e ceux qui amène à un choix de type Xnnn (niv3).

        Parameters
        ----------
        Xnnn : float
            Exemple : "A100"
        row : int
            position "y" (ligne)
        column : int
            position "x" (colonne)
        """
        self.boutons[Xnnn] = tk.Button(self, text=Dict[Xnnn], relief="ridge", bg='yellow', bd=10, font=LARGE_FONT, command=lambda: controller.show_frame(page_suivante))
        self.boutons[Xnnn].grid(row=row, column=column, sticky="nsew")
    
    def bouton_selection_niv3(self, Xnnn, row, column):
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
        # self.illustrations[Xnnn] = tk.PhotoImage(master=self, file=path_photo(Xnnn))  # path_photo est défini plus haut avec le chemin d'accès aux photos
        self.boutons[Xnnn] = tk.Button(self, text=Dict[Xnnn][1], relief="raised", bd=10, font=LARGE_FONT)  #, image=self.illustrations[Xnnn], compound="right")
        self.boutons[Xnnn].grid(row=row, column=column, sticky="nsew")
        infoBulle(parent=self.boutons[Xnnn], texte=Dict[Xnnn][0])
        
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
        self.retour = tk.PhotoImage(master=self, file=r"G:/Boulot/Ferry Capitain/défauthèque/Défauthon/Back_button.png").subsample(20)
        self.butonRetour = tk.Button(self, text="Retour", font=LARGE_FONT, command=lambda: controller.show_frame(page_avant), bg='gray', relief="sunken", bd=10, image=self.retour, compound="right")
        self.butonRetour.grid(row=row, column=column, sticky="nsew")


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

        for F in (Accueil, PageA, PageA100, PageA200, PageA300, PageB, PageB100, PageB200, PageB300, PageC, PageD, PageE, PageF, PageG):

            frame = F(container, self)

            self.frames[F] = frame

            if F == Accueil:
                frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
                frame.columnconfigure(0, weight=1)
            if F == PageA or F == PageB:
                frame.rowconfigure([0, 1, 2, 3, 4], weight=1)
                frame.columnconfigure(0, weight=1)
            if F == PageB200:
                frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            if F == PageA100 or F == PageB100:
                frame.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            if F == PageA200:
                frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)
                frame.columnconfigure([0, 1], weight=1)
            if F == PageA300 or F == PageB300:
                frame.rowconfigure([0, 1, 2, 3], weight=1)
                frame.columnconfigure(0, weight=1)
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
        cont : Le nom d'une page (i.e. d'une classe définit plus bas).

        Returns
        -------
        changement de frame.
        """
        frame = self.frames[cont]
        frame.tkraise()


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

        # self.buttonA = tk.Button(self, text=Dict["A"],
        #                          command=lambda: controller.show_frame(PageA))
        # self.buttonA.grid(row=1, column=0, sticky="nsew")

        # self.buttonB = tk.Button(self, text=Dict["B"],
        #                          command=lambda: controller.show_frame(PageB))
        # self.buttonB.grid(row=2, column=0, sticky="nsew")

        # self.buttonC = tk.Button(self, text=Dict["C"],
        #                          command=lambda: controller.show_frame(PageC))
        # self.buttonC.grid(row=3, column=0, sticky="nsew")

        # self.buttonD = tk.Button(self, text=Dict["D"],
        #                          command=lambda: controller.show_frame(PageD))
        # self.buttonD.grid(row=4, column=0, sticky="nsew")

        # self.buttonE = tk.Button(self, text=Dict["E"],
        #                          command=lambda: controller.show_frame(PageE))
        # self.buttonE.grid(row=5, column=0, sticky="nsew")

        # self.buttonF = tk.Button(self, text=Dict["F"],
        #                          command=lambda: controller.show_frame(PageF))
        # self.buttonF.grid(row=6, column=0, sticky="nsew")

        # self.buttonG = tk.Button(self, text=Dict["G"], command=lambda: controller.show_frame(PageG))
        # self.buttonG.grid(row=7, column=0, sticky="nsew")


class PageA(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts A (A100/A200/A300)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["A"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.buttonA100 = tk.Button(self, text=Dict["A100"],
                                    command=lambda: controller.show_frame(PageA100))
        self.buttonA100.grid(row=1, column=0, sticky="nsew")

        self.buttonA200 = tk.Button(self, text=Dict["A200"],
                                    command=lambda: controller.show_frame(PageA200))
        self.buttonA200.grid(row=2, column=0, sticky="nsew")

        self.buttonA300 = tk.Button(self, text=Dict["A300"],
                                    command=lambda: controller.show_frame(PageA300))
        self.buttonA300.grid(row=3, column=0, sticky="nsew")
        
        self.bouton_retour(PageG, 4, 0, controller)


class PageA100(tk.Frame, Boutons_selection):
    """PageA100 (9 défauts)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text=Dict["A100"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, columnspan=2)
        
        # ------------------------------- A110 -------------------------------
        self.labelA110 = tk.Label(self, text=Dict["A110"] + "\n | \n\/", font=LARGE_FONT)
        self.labelA110.grid(row=1, column=0, sticky="nsew")
        
        for i in range(5):
            self.bouton_selection_niv3("A11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- A120 -------------------------------
        self.labelA120 = tk.Label(self, text=Dict["A120"] + "\n | \n\/", font=LARGE_FONT)
        self.labelA120.grid(row=1, column=1, sticky="nsew")
        
        for i in range(3):
            self.bouton_selection_niv3("A12" + str(i + 1), 2 + i, 1)

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT, command=lambda: controller.show_frame(PageA))
        self.buttonRetour.grid(row=6, column=1, sticky="nsew")


class PageA200(tk.Frame, Boutons_selection):
    """PageA200 (10 défauts)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["A200"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, columnspan=2)
        
        # ------------------------------- A210 -------------------------------
        self.labelA210 = tk.Label(self, text=Dict["A210"] + "\n | \n\/", font=LARGE_FONT)
        self.labelA210.grid(row=1, column=0, sticky="nsew")
        
        for i in range(3):
            self.bouton_selection_niv3("A21" + str(i + 1), 2 + i, 0)

        # ------------------------------- A220 -------------------------------
        self.labelA220 = tk.Label(self, text=Dict["A220"] + "\n | \n\/", font=LARGE_FONT)
        self.labelA220.grid(row=1, column=1, sticky="nsew")

        for i in range(6):
            self.bouton_selection_niv3("A22" + str(i + 1), 2 + i, 1)

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT,
                                      command=lambda: controller.show_frame(PageA))
        self.buttonRetour.grid(row=8, column=1, sticky="nsew")


class PageA300(tk.Frame, Boutons_selection):
    """PageA300 (1 défaut)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["A300"], font=LARGE_FONT)
        self.label.grid(row=0, column=0)

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT, command=lambda: controller.show_frame(PageA))
        self.buttonRetour.grid(row=3, column=0, sticky="nsew")
        
        # ------------------------------- A310 -------------------------------
        self.labelA310 = tk.Label(self, text=Dict["A310"] + "\n | \n\/", font=LARGE_FONT)
        self.labelA310.grid(row=1, column=0, sticky="nsew")

        self.bouton_selection_niv3("A311", 2, 0)


class PageB(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts B (B100/B200/B300)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["B"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.buttonB100 = tk.Button(self, text=Dict["B100"],
                                    command=lambda: controller.show_frame(PageB100))
        self.buttonB100.grid(row=1, column=0, sticky="nsew")

        self.buttonB200 = tk.Button(self, text=Dict["B200"],
                                    command=lambda: controller.show_frame(PageB200))
        self.buttonB200.grid(row=2, column=0, sticky="nsew")

        self.buttonB300 = tk.Button(self, text=Dict["B300"],
                                    command=lambda: controller.show_frame(PageB300))
        self.buttonB300.grid(row=3, column=0, sticky="nsew")

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT,
                                      command=lambda: controller.show_frame(Accueil))
        self.buttonRetour.grid(row=4, column=0, sticky="nsew")


class PageB100(tk.Frame, Boutons_selection):
    """PageB100 (7 défauts)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text=Dict["B100"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, columnspan=2)
        
        # ------------------------------- B110 -------------------------------
        self.labelB110 = tk.Label(self, text=Dict["B110"] + "\n | \n\/", font=LARGE_FONT)
        self.labelB110.grid(row=1, column=0, sticky="nsew")
        
        for i in range(3):
            self.bouton_selection_niv3("B11" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- B120 -------------------------------
        self.labelB120 = tk.Label(self, text=Dict["B120"] + "\n | \n\/", font=LARGE_FONT)
        self.labelB120.grid(row=1, column=1, sticky="nsew")
        
        for i in range(4):
            self.bouton_selection_niv3("B12" + str(i + 1), 2 + i, 1)

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT, command=lambda: controller.show_frame(PageB))
        self.buttonRetour.grid(row=6, column=1, sticky="nsew")


class PageB200(tk.Frame, Boutons_selection):
    """PageB200 (5 défauts)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text=Dict["B200"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, columnspan=2)
        
        # ------------------------------- B210 -------------------------------
        self.labelB210 = tk.Label(self, text=Dict["B210"] + "\n | \n\/", font=LARGE_FONT)
        self.labelB210.grid(row=1, column=0, sticky="nsew")
        
        for i in range(3):
            self.bouton_selection_niv3("B21" + str(i + 1), 2 + i, 0)  #définit un bouton pour chaque défaut à l'emplacement  row, column des deux derniers arguments sur la frame

        # ------------------------------- B220 -------------------------------
        self.labelB220 = tk.Label(self, text=Dict["B220"] + "\n | \n\/", font=LARGE_FONT)
        self.labelB220.grid(row=1, column=1, sticky="nsew")
        
        for i in range(2):
            self.bouton_selection_niv3("B22" + str(i + 1), 2 + i, 1)

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT, command=lambda: controller.show_frame(PageB))
        self.buttonRetour.grid(row=5, column=1, sticky="nsew")


class PageB300(tk.Frame, Boutons_selection):
    """PageB300 (1 défaut)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["B300"], font=LARGE_FONT)
        self.label.grid(row=0, column=0)

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT, command=lambda: controller.show_frame(PageB))
        self.buttonRetour.grid(row=3, column=0, sticky="nsew")
        
        # ------------------------------- A310 -------------------------------
        self.labelB310 = tk.Label(self, text=Dict["B310"] + "\n | \n\/", font=LARGE_FONT)
        self.labelB310.grid(row=1, column=0, sticky="nsew")

        self.bouton_selection_niv3("B311", 2, 0)


class PageC(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts C (C100/C200/C300/C400)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["C"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.buttonC100 = tk.Button(self, text=Dict["C100"],
                                    command=lambda: controller.show_frame(PageA100))
        self.buttonC100.grid(row=1, column=0, sticky="nsew")

        self.buttonC200 = tk.Button(self, text=Dict["C200"],
                                    command=lambda: controller.show_frame(PageA200))
        self.buttonC200.grid(row=2, column=0, sticky="nsew")

        self.buttonC300 = tk.Button(self, text=Dict["C300"],
                                    command=lambda: controller.show_frame(PageA300))
        self.buttonC300.grid(row=3, column=0, sticky="nsew")
        
        self.buttonC400 = tk.Button(self, text=Dict["C400"],
                                    command=lambda: controller.show_frame(PageA100))
        self.buttonC400.grid(row=4, column=0, sticky="nsew")

        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT,
                                      command=lambda: controller.show_frame(Accueil))
        self.buttonRetour.grid(row=5, column=0, sticky="nsew")


class PageD(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts D (D100/D200)."""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["D"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.buttonD100 = tk.Button(self, text=Dict["D100"],
                                    command=lambda: controller.show_frame(PageA100))
        self.buttonD100.grid(row=1, column=0, sticky="nsew")

        self.buttonD200 = tk.Button(self, text=Dict["D200"],
                                    command=lambda: controller.show_frame(PageA200))
        self.buttonD200.grid(row=2, column=0, sticky="nsew")
        
        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT,
                                      command=lambda: controller.show_frame(Accueil))
        self.buttonRetour.grid(row=3, column=0, sticky="nsew")


class PageE(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts E (E100/E200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["E"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.buttonE100 = tk.Button(self, text=Dict["E100"],
                                    command=lambda: controller.show_frame(PageA100))
        self.buttonE100.grid(row=1, column=0, sticky="nsew")

        self.buttonE200 = tk.Button(self, text=Dict["E200"],
                                    command=lambda: controller.show_frame(PageA200))
        self.buttonE200.grid(row=2, column=0, sticky="nsew")
        
        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT,
                                      command=lambda: controller.show_frame(Accueil))
        self.buttonRetour.grid(row=3, column=0, sticky="nsew")


class PageF(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts F (F100/F200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["F"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.buttonF100 = tk.Button(self, text=Dict["F100"],
                                    command=lambda: controller.show_frame(PageA100))
        self.buttonF100.grid(row=1, column=0, sticky="nsew")

        self.buttonF200 = tk.Button(self, text=Dict["F200"],
                                    command=lambda: controller.show_frame(PageA200))
        self.buttonF200.grid(row=2, column=0, sticky="nsew")
        
        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT,
                                      command=lambda: controller.show_frame(Accueil))
        self.buttonRetour.grid(row=3, column=0, sticky="nsew")


class PageG(tk.Frame, Boutons_selection):
    """Page de sélections des sous défauts G (G100/G200)."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=Dict["G"], font=LARGE_FONT)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.buttonG100 = tk.Button(self, text=Dict["G100"],
                                    command=lambda: controller.show_frame(PageA100))
        self.buttonG100.grid(row=1, column=0, sticky="nsew")

        self.buttonG200 = tk.Button(self, text=Dict["G200"],
                                    command=lambda: controller.show_frame(PageA200))
        self.buttonG200.grid(row=2, column=0, sticky="nsew")
        
        self.buttonRetour = tk.Button(self, text="Retour", font=LARGE_FONT,
                                      command=lambda: controller.show_frame(Accueil))
        self.buttonRetour.grid(row=3, column=0, sticky="nsew")


if __name__ == "__main__":
    app = Defauthon()
    app.title("Defauthon v0")
    app.geometry("1294x800")
    app.mainloop()