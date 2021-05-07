# Crear una lista de 1000 valores aleatorios que sigan un distribucion normal
# Crear un histograma mediante matplotlib  con la lista de valores
# Crear un diagrama de cajas (donde se acumula el 50% de los valores mediante seaborn) )
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot  as plt

valores = np.random.randn(1000)
hist_matp = plt.hist(valores)
hist_matp

diag_box = sns.boxplot(valores)
diag_box