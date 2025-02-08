class Steen:
    def __init__(self, number, coller):
        self.nummer = number
        self.kleur = coller


class GrotereSteen(Steen):
    def __init__(self, number, coller):
        self.verticla = 0
        self.horizontol = 0
        self.verticlalist = []
        self.horizontollsit = []
        Steen.__init__(self, number, coller)


class Combi:
    def __init__(self):
        self.lijst_van_stenen = []

    def voeg_toe_aan_combi(self, steen):
        if self.lijst_van_stenen[0].number == self.lijst_van_stenen[1].number:
            if steen.number == self.lijst_van_stenen[0].number:
                colerlist = [nuwsteen.classcoller for nuwsteen in self.lijst_van_stenen]
                if steen.classcoller not in colerlist:
                    self.lijst_van_stenen.append(steen)

        elif self.lijst_van_stenen[0].number != self.lijst_van_stenen[1].number:
            if steen.classcoller == self.lijst_van_stenen[0].classcoller:
                colerlist = [
                    nuwsteen
                    for nuwsteen in self.lijst_van_stenen
                    if (steen.number + 1) == nuwsteen.number
                    or (steen.number - 1) == nuwsteen.number
                ]
                if len(colerlist) != 0:
                    self.lijst_van_stenen.append(steen)

    def print(self):
        print("combie")
        for i in self.lijst_van_stenen:
            print(i.number, i.classcoller)


class hand:
    def __init__(self):
        self.hand = []

    def voeg_toe_aan_hand(self, steen):
        self.hand.append(steen)

    def speelbare_hand(self):
        nieuwe_lijst: list[GrotereSteen] = []
        for i in self.hand:
            nieuwe_lijst.append(GrotereSteen(i.number, i.classcoller))
        for i in nieuwe_lijst:
            for a in nieuwe_lijst:
                if a == i:
                    continue
                if i.classcoller != a.classcoller and i.number == a.number:
                    i.horizontol += 1
                    i.horizontollsit.append(a)
                if i.classcoller == a.classcoller and i.number == (a.number - 1):
                    i.verticla += 1
                    i.verticlalist.append(a)
                if i.classcoller == a.classcoller and i.number == (a.number + 1):
                    i.verticla += 1
                    i.verticlalist.append(a)
        # nuwlist.sort(key=lambda x: x.verticla, reverse=True)
        combielist1, playedsteen1 = self.hor4ver(nieuwe_lijst)
        combielist2, playedsteen2 = self.ver4hor(nieuwe_lijst)
        combielist = combielist1
        usersteen = playedsteen1
        if len(playedsteen1) < len(playedsteen2):
            combielist = combielist2
            usersteen = playedsteen2

        for i in combielist:
            i.pritcombo()

        for i in self.hand[
            :
        ]:  # Use a copy of self.hand to safely remove items while iterating
            for a in usersteen[
                :
            ]:  # Use a copy of usersteen to safely remove items while iterating
                if a.number == i.number and a.classcoller == i.classcoller:
                    self.hand.remove(i)  # Remove from self.hand
                    usersteen.remove(a)  # Remove from usersteen
                    break  # Exit the inner loop once a match is found and removed

        print("hand")
        for i in self.hand:
            print(i.number, i.classcoller)

    def hor4ver(self, nuwlist):
        number = 2
        playedsteen = []
        combielist = []
        while number < len(self.hand):
            filter_listhand = [steen for steen in nuwlist if steen.horizontol == number]
            for i in filter_listhand:
                if i not in playedsteen:
                    steenlsit = self.horizontol_maker(i, playedsteen)
                    if len(steenlsit) >= 3:
                        playedsteen += steenlsit
                        newcombie = Combi()
                        newcombie.lijst_van_stenen = steenlsit
                        combielist.append(newcombie)
            number += 1
        number = 2

        while number < len(self.hand):
            filter_listhand = [steen for steen in nuwlist if steen.verticla == number]
            for i in filter_listhand:
                if i not in playedsteen:
                    steenlsit = self.vertical_maker(i, playedsteen)
                    if len(steenlsit) >= 3:
                        playedsteen += steenlsit
                        newcombie = Combi()
                        newcombie.lijst_van_stenen = steenlsit
                        combielist.append(newcombie)
            number += 1
        return combielist, playedsteen

    def ver4hor(self, nuwlist):
        number = 2
        playedsteen = []
        combielist = []

        while number < len(self.hand):
            filter_listhand = [steen for steen in nuwlist if steen.verticla == number]
            for i in filter_listhand:
                if i not in playedsteen:
                    steenlsit = self.vertical_maker(i, playedsteen)
                    if len(steenlsit) >= 3:
                        playedsteen += steenlsit
                        newcombie = Combi()
                        newcombie.lijst_van_stenen = steenlsit
                        combielist.append(newcombie)
            number += 1

        number = 2

        while number < len(self.hand):
            filter_listhand = [steen for steen in nuwlist if steen.horizontol == number]
            for i in filter_listhand:
                if i not in playedsteen:
                    steenlsit = self.horizontol_maker(i, playedsteen)
                    if len(steenlsit) >= 3:
                        playedsteen += steenlsit
                        newcombie = Combi()
                        newcombie.lijst_van_stenen = steenlsit
                        combielist.append(newcombie)
            number += 1
        return combielist, playedsteen

    def horizontol_maker(self, horizontollsit, playseen):
        rollerchekken = []
        steenlsit = []
        self.horizontol_maker_afstand(
            horizontollsit, rollerchekken, steenlsit, playseen
        )
        return steenlsit

    def horizontol_maker_afstand(self, horizontollsit, listcoller, steenlist, playseen):
        if (
            horizontollsit.classcoller not in listcoller
            and horizontollsit not in playseen
        ):
            listcoller.append(horizontollsit.classcoller)
            steenlist.append(horizontollsit)
        for i in horizontollsit.horizontollsit:
            if i not in steenlist and i not in playseen:
                self.horizontol_maker_afstand(i, listcoller, steenlist, playseen)

    def vertical_maker(self, horizontollsit, playseen):
        rollerchekken = []
        steenlsit = []
        self.vertical_maker_afstand(horizontollsit, rollerchekken, steenlsit, playseen)
        return steenlsit

    def vertical_maker_afstand(self, horizontollsit, listcoller, steenlist, playseen):
        if horizontollsit.number not in listcoller and horizontollsit not in playseen:
            listcoller.append(horizontollsit.number)
            steenlist.append(horizontollsit)

        for i in horizontollsit.verticlalist:
            if i not in steenlist and i not in playseen:
                self.vertical_maker_afstand(i, listcoller, steenlist, playseen)
