try:
    1 / 0
except Exception as E:
    raise TypeError('Bad!!!') from E

