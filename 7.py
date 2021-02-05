import pandas as pd 
import constantes

ranking = pd.read_csv(constantes.RANKING, sep=',')
print(ranking.dtypes)
ranking = ranking.sort_values(['Puntaje'], ascending=False)
print(ranking)
ranking = ranking.to_csv(constantes.RANKING, index = False)

#ranking = pd.read_csv(constantes.RANKING, nrows=3)

#ranking = ranking.to_csv(constantes.RANKING)

