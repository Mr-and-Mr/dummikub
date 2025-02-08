from class_holder import Steen, Combi, hand
from field_class import veld

gamefiel = veld()
newcombie = Combi()
newcombie.lijst_van_stenen = [
    Steen(1, "Rood"),
    Steen(2, "Rood"),
    Steen(3, "Rood"),
    Steen(4, "Rood"),
    Steen(5, "Rood"),
]
gamefiel.veld_combie = [newcombie]
gamefiel.vind_missend_steentje(Steen(3, "Rood"))
exit()
playerhand = hand()
playerhand.hand = [
    Steen(1, "Rood"),
    Steen(2, "Rood"),
    Steen(3, "Rood"),
    Steen(4, "Rood"),
    Steen(4, "Rood"),
    Steen(5, "Rood"),
    Steen(6, "Rood"),
]
playerhand.speelbare_hand()
