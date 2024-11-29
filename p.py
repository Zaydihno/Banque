class Produit:
    def __init__(self, id, nom, prix, stock):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def vendre(self):
        """Vendre le produit si le stock est suffisant."""
        if self.stock > 0:
            self.stock -= 1
            print(f"{self.nom} vendu !")
            return True
        else:
            print(f"Désolé, {self.nom} est en rupture de stock.")
            return False
    
    def reapprovisionner(self, quantite):
        """Réapprovisionner le produit."""
        self.stock += quantite
        print(f"{quantite} unités de {self.nom} ont été ajoutées au stock.")
    
    def __str__(self):
        """Retourner une description lisible du produit."""
        return f"{self.nom} - {self.prix}$ - Stock disponible: {self.stock}"


class Panier:
    def __init__(self):
        self.produits = []  # Liste de produits dans le panier
        self.total = 0       # Montant total de la commande

    def ajouter_produit(self, produit):
        """Ajouter un produit au panier si le stock est suffisant."""
        if produit.vendre():
            self.produits.append(produit)
            self.total += produit.prix
            print(f"Produit {produit.nom} ajouté au panier.")
        else:
            print(f"Impossible d'ajouter {produit.nom} au panier.")

    def afficher_panier(self):
        """Afficher le contenu du panier."""
        print("Panier :")
        for produit in self.produits:
            print(produit)
        print(f"Total à payer : {self.total}$")

    def vider_panier(self):
        """Vider le panier."""
        self.produits.clear()
        self.total = 0
        print("Panier vidé.")


class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.historique_achats = []  # Liste des paniers d'achats passés

    def ajouter_achat(self, panier):
        """Ajouter un panier à l'historique d'achats."""
        self.historique_achats.append(panier)
        print(f"Votre achat de {panier.total}$ a été ajouté à l'historique.")

    def afficher_historique(self):
        """Afficher l'historique des achats de l'utilisateur."""
        print(f"Historique des achats de {self.nom} ({self.email}):")
        for panier in self.historique_achats:
            panier.afficher_panier()


class Paiement:
    def __init__(self, montant, moyen):
        self.montant = montant
        self.moyen = moyen  # "carte" ou "especes"

    def effectuer_paiement(self):
        """Effectuer le paiement."""
        if self.moyen == "carte":
            print(f"Paiement de {self.montant}$ effectué par carte.")
        elif self.moyen == "especes":
            print(f"Paiement de {self.montant}$ effectué en espèces.")
        else:
            print("Méthode de paiement inconnue.")
            return False
        return True


class Vente:
    def __init__(self, utilisateur):
        self.utilisateur = utilisateur
        self.panier = Panier()

    def ajouter_au_panier(self, produit):
        """Ajouter un produit au panier."""
        self.panier.ajouter_produit(produit)
    
    def payer(self, moyen_paiement):
        """Effectuer le paiement et ajouter l'achat à l'historique de l'utilisateur."""
        if self.panier.total == 0:
            print("Le panier est vide. Aucun produit à acheter.")
            return

        paiement = Paiement(self.panier.total, moyen_paiement)
        if paiement.effectuer_paiement():
            self.utilisateur.ajouter_achat(self.panier)
            self.panier.vider_panier()


# Simulation de la gestion des produits et des ventes

# Création des produits
pepsi = Produit(1, "Pepsi", 3.5, 10)
coca = Produit(2, "Coca", 2.5, 5)
snickers = Produit(3, "Snickers", 4.0, 2)
mars = Produit(4, "Mars", 2.5, 7)

# Création d'un utilisateur
utilisateur1 = Utilisateur("Alice", "alice@example.com")

# Démarrer une vente pour l'utilisateur
vente1 = Vente(utilisateur1)

# Ajouter des produits au panier
vente1.ajouter_au_panier(pepsi)
vente1.ajouter_au_panier(coca)
vente1.ajouter_au_panier(snickers)

# Afficher le panier de l'utilisateur
vente1.panier.afficher_panier()

# Effectuer le paiement
vente1.payer("carte")

# Afficher l'historique des achats de l'utilisateur
utilisateur1.afficher_historique()

# Réapprovisionner les produits (par exemple, réapprovisionner Snickers)
snickers.reapprovisionner(5)

# Ajouter un autre produit au panier après réapprovisionnement
vente1.ajouter_au_panier(snickers)
vente1.panier.afficher_panier()

# Payer en espèces cette fois
vente1.payer("especes")

# Afficher à nouveau l'historique des achats de l'utilisateur
utilisateur1.afficher_historique()
