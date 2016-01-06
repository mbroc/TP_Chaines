# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  #1) On transforme, dans la variable pwd, la variable password en une liste
    found = False
    i=len(pwd)-1

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2) La lettre va être modifiée par la lettre suivante de l'alphabet 
           found = True
        else:
           pwd[i-1] = chr(ord(pwd[i-1])+1)
           pwd[i] = chr(ord(pwd[i])-26)
    
    return ''.join(pwd) #3) La méthode retourne la variable pwd remise sous forme de chaine de caractère



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
