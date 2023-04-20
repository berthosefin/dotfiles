

# Generateur de phrases
# demander en console une chaine de la forme "mot1/mot2/mot3/..."
user_input = input("Entrer une chaine de la forme 'mot1/mot3/mot3/...': ")

# transformer cette chaine en une liste
# la melanger
lst = user_input.split("/")

# si le nombre d'éléments de cette liste est inférieur à 10
# -> afficher les deux premiers mots
if len(lst) < 10:
    print(f"Les deux premiers mots de cette liste sont: {lst[0:1]}")

# si le nombre d'éléments est supérieur ou égal à 10
# -> afficher les 3 derniers
if len(lst) >= 10:
    print(f"Les trois derniers mots de cette liste sont: {lst[-2:-1]}")