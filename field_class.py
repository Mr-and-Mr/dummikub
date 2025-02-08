from class_holder import Combi, Steen


class veld:
    def __init__(self):
        self.veld_combie: Combi = []

    def voeg_combi_toe(self, combie):
        self.veld_combie.append(combie)

    def vind_missend_steentje(self, steen):
        steen_lijst = []
        for i in self.veld_combie:
            for a in i.listofsteen:
                steen_lijst.append(nieuwe_steen(a, steen, i))

        steen_lijst = sorted(steen_lijst, key=lambda x: x.horizontol)
        for i in steen_lijst:
            print(i.horizontol)


class nieuwe_steen(Steen):
    def __init__(self, oude_steen: Steen, nieuwe_steen: Steen, combie):
        self.verticla = False
        if oude_steen.kleur == nieuwe_steen.kleur:
            self.verticla = True
        self.horizontol = abs(nieuwe_steen.nummer - oude_steen.nummer)
        self.combie = combie
        Steen.__init__(self, oude_steen.nummer, oude_steen.kleur)
