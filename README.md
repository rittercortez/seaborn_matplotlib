#############  Modulo SEABORN y Modulo MATPLOTLIB  ###########
__________________________________________________________________________

############# INSTALACIÓN ###########

- pip install seaborn
- conda install seaborn

__________________________________________________________________________

############# HISTOGRAMAS ###########

ex:
    import pandas as pd
    import numpy as np
    # Importamos el modulo gráfico "matplotlib" y lo convertimos en "mpl"
    # Importamos el modulo gráfico "seaborn"y lo convertimos en "sns"
    import matplotlib as mpl
    import seaborn as sns
    # Para poder visualizar cualquier tipo de gráfico debemos escribir "%matplotlib inline"
    %matplotlib inline
    valor1 = np.random.randint(0,1000,100)
    valor2 = np.random.randint(0,1000,90)
    # "mpl" llamamos al modulo, ".pyplot" es el tipo de gráfico, ".hist" mostramos el histograma
    # "color = " podemos insertar el color que queramos
    # "alpha = " sirve para poner la intensidad del color opciones del [0.0 al 1.0]
    # "bins = " sirve para introducir las barras que queremos visualizar
    # "density = " nos permite unir distintas capacidades de valores en un solo gráfico
    grafico1 = mpl.pyplot.hist(valor1, color = "blue", alpha = 0.4, bins=50, density = True )
    # "sns" llamamos al modulo de "searborn"
    # ".distplot " el tipo de gráfico que mostraremos
    grafico2 = sns.distplot(valor2, color = "green")
    grafico2
    valor3 = np.random.randint(0,10000,1000)
    valor4 = np.random.randint(0,10000,1000)
    # ".joinplot" es un tipo de gráfico del modulo SEABORN
    # "kind = " sirve para mostrar valores hexadecimales
    sns.jointplot(valor3,valor4, kind = 'hex')


__________________________________________________________________________

############# DISTRIBUCIONES ###########

ex:
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import seaborn as sns
    %matplotlib inline
    datos = np.random.randint(0,10000, 100)
    # "rug = " y "hist =" nos permite borrar el grafico de barras  para
    # solo mostrar la linea de datos
    vsta_sns1 = sns.distplot(datos, rug = False, hist= False)
    vsta_sns1


    arg_curva = {'color':'blue','label':'curva'}
    arg_histograma = {'color':'red','label':'histograma'}
    # "kde_kws" nos permite editar nuestra linea de datos
    # "hist_kws" nos permite editar nuestro histograma
    sns.distplot(datos, kde_kws = arg_curva, hist_kws = arg_histograma)

    # Aqui podemos ver lo sencillo que es trabalar con datos de una Serie en Seaborn
    datos_serie = pd.Series(datos)
    vsta_sns_Series = sns.distplot(datos_serie, color= "green")
    vsta_sns_Series

__________________________________________________________________________

############# GRAFICOS DE CAJAS ###########

ex:
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import seaborn as sns
    %matplotlib inline
    datos = np.random.randint(-100,1000,100)
    # Con este tipo de grafico podemos visualizar en la caja donde se encuentra el 50% de los valores
    # el resto de los 25% lo visualizamos en la linea alrededor
    grafico_caja = sns.boxplot(datos)
    grafico_caja

__________________________________________________________________________

############# REGRESIÓN LINEAL ###########

La regresión lineal aplicada en fabricación es una técnica estadística para modelar e investigar la relación entre dos o más variables. 

ex: 
    import pandas as pd
    import numpy as np
    import seaborn as sns

    %matplotlib inline
    # '.load_dataset()' nos permite cargar el dataset 
    propinas = sns.load_dataset('tips')
    # Aqui primero describimos los dos angulos que queremos visualizar y al final cargamos el 'dataset'
    grafico1 = sns.lmplot('total_bill','tip',propinas)
    grafico1

    # 'scatter_kws' permite ponerle color a los puntos de  datos
    # 'line_kws '  permite cambiar el color a la linea de regresión
    grafico2 = sns.lmplot('total_bill','tip',propinas, scatter_kws = {'color': 'green'}, line_kws = {'color': 'red'})

    # 'fit_reg ' permite borrar la linea
    grafico3 = sns.lmplot('total_bill','tip',propinas, fit_reg = False)
    grafico3

    # Filtamos por sex de personas que da mas propinas, y cambiamos los puntos de datos por 'x'para hombres y 'o'para mujeres
    grafico4 = sns.lmplot('total_bill','tip',propinas, hue = "sex" , markers = ["x","o"])
    grafico4


__________________________________________________________________________

############# MAPA DE CALOR (heatmap) ###########

Un mapa de calor es una técnica de visualización de datos que mide la magnitud de un fenómeno en colores en dos dimensiones

ex: 
    import pandas as pd
    import numpy as np
    import seaborn as sns

    %matplotlib inline
    vuelos = sns.load_dataset('flights')
    vuelos.head()
    # Ordenar datos para luego introducirlos al mapa del calor
    pivot_calor = vuelos.pivot('month','year', 'passengers')
    pivot_calor

    # '.heatmap' permite crear el mapa de calor
    map_calor1 = sns.heatmap(pivot_calor)
    map_calor1

    # 'annot' nos permite visualizar datos en el mapa de calor
    # 'fmt' nos permite introducir cualquier tipo de formato  digito, caracteres entre otros.
    # 'cbar_kws' permite mover la barra indicativa en la posición horizontal o vertical
    map_calor2 = sns.heatmap(pivot_calor, annot = True, fmt = 'd', cbar_kws = {'orientation':'horizontal'})
    map_calor2