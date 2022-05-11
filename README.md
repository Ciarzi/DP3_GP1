# Data Project 3 Modelo Predictor - Grupo 1 - BBank

# Proyecto
El objetivo de este tercer Data Project es evaluar el riesgo crediticio en una entidad bancaria a través de un modelo predictor.


# Meet the team

- [Pablo Bottero Gandía](https://github.com/aloa04)
- [Thais Casares González](https://github.com/thais1987)
- [Ramón Casans Camp](https://github.com/racasc)
- [Hermán Redondo Lázaro](https://github.com/Ciarzi)
- [José Luis Rodríguez Albert](https://github.com/joselra98)
- [Sergi Joan Sastre Antequera](https://github.com/sergijoan22)


# Proceso para calcular el riesgo crediticio
# 1.- Prerrequisitos
Los archivos necesarios para llevar a cabo el Data Project se encuentran en [esta carpeta](https://github.com/Ciarzi/DP3_GP1/tree/main/datasets/own_data), son data sets creados al transformar los del enunciado, situados en [esta carpeta](https://github.com/Ciarzi/DP3_GP1/tree/main/datasets)

Todo el código necesario para llevar a cabo el Data Project se encuentran en las carpetas [classificator](https://github.com/Ciarzi/DP3_GP1/tree/main/classificator) y [codigo](https://github.com/Ciarzi/DP3_GP1/tree/main/codigo)

# 2.- Transformación de los datos
Para ello, hemos decidido juntar todos los data sets en uno así como añadir y quitar variables.
Además, hemos decidido crear data sets propios con información como la localización y el PIB per cápita.

2.1.- Variables eliminadas:
Algunas variables han sido eliminadas porque lo que buscamos es predecir si un cliente devolverá o no un préstamo y consideramos que no aportan información útil al modelo predictivo. 
Estas variables han sido:
- “customerid”, “systemloanid”, debido a que tan solo identifican al cliente.
- “approveddate”, “creationdate”, debido a que la hora de creación, en todos los casos, es una hora después de la aprobación del préstamo.
- “bank_name_clients”, “bank_branch_clients”, debido a que aportan el nombre y la sucursal de cada banco y nada del cliente en sí.
- “level_of_education_clients”, debido a la gran cantidad de datos vacíos.

2.2.- Variables usadas
Una vez eliminadas las variables no necesarias, el siguiente paso ha sido transformar las ya existentes para poder usarlas adecuadamente. Las variables usadas han sido:
-	“historial”: lo primero para crear esta variable ha sido transformar las variables “firstduedate” y “firstrepaiddate” a un formato diferente para poder trabajar con ellas. Lo siguiente ha sido otorgar un valor negativo a aquellos préstamos que no han sido devueltos dentro de su plazo y un valor positivo a aquellos que sí lo han sido. Finalmente, aquellos usuarios que han acabado con una puntuación cero o negativa han sido asignados un “0” y quienes han acabado con una puntuación positiva un “1”.

-	“loannumber”: esta variable no ha sido modificada, representa el número de préstamos que un cliente ha pedido con anterioridad.

-	“referido”: para esta variable hemos tenido en cuenta la de “historial”. A aquellos clientes que han sido referidos por un cliente con un mal historial de pagos se les ha asignado un “0”. Quienes no han sido referidos han sido asignados un “1”. Aquel cliente que ha sido referido por otro cliente sin historial de pagos ha sido asignado con un “2” y a quienes han sido referidos por un cliente con un buen historial de pagos se les ha asignado un “3”.

-	“flag”: dado que esta es la variable que tenemos que predecir no se ha modificado

-	“age”: esta nueva variable es el resultado de cambiar de formato la variable “birthdate” para quedarnos solamente con los años de cada cliente, obviando el día y mes de nacimiento .

-	“parte_mes_pago”: esta variable surge codificar la variable “firstduedate” de manera que, los préstamos que venzan los diez últimos días del mes se marcan con un “1”, aquellos que venzan los diez primeros con un “3” y los que vencen entre medias con un “2”.

-	“due_per_day”: representa el total a pagar de cada préstamo por día. Se ha calculado diviendo la variable “totaldue” entre “termdays”.

-	“interes”: esta nueva variable representa el interés por cada día de préstamo. Ha sido calculada al restar “loanamount” a “totaldue” y dividir el resultado entre “termdays”.

-	“cuenta_corriente”, “cuenta_otra” y “cuenta_ahorro”: estas tres nuevas variables proceden de “bank_account_type”. Surgen de haber hecho one hot encoding con el objetivo de separar las respuestas dentro de la variable en lo que se conoce como “dummy variables”.

-	“employment”: esta variable es el resultado de codificar la variable “employment_status_client” de manera que aquellos clientes jubilados, desempleados o estudiantes han sido asignados un “0”. A quienes no han aportado esta información a la base de datos se les ha asignado un “1” y quienes cuentan con un empleo fijo, temporal o son autónomos se les ha asignado un “2”.

2.3.- Variables descartadas

Hemos probado a integrar datos externos que finalmente no hemos acabado usando debido a su falta de correlación.
-	“datos_localizacion”: en esta base de datos se ha asignado a cada cliente un país en base a sus coordenadas, dadas en los data sets originales.

-	“mundo_pib_capita.csv”: dado que con el anterior data set se han asignado países varios, vemos necesario comparar los distintos PIB.

-	“nigeria_pib_capita.csv”: a excepción de no llega 50 resultados, todos los clientes proceden de Nigeria, por lo que hemos decidido también comparar los PIB de cada estado de Nigeria.

# 3.- Transformación del input
**Clustering**

Ahora agruparemos los clientes en grupos, llamados clústeres. Dependiendo de las similitudes entre estos saldrán varios grupos. Para ello hemos usados el método de k-means.

El número de clústeres a usar depende del resultado que nos de el método “elbow”, en nuestro caso k=3.

<p align="center">
   <img src="https://github.com/Ciarzi/DP3_GP1/blob/main/Logo/elbow.png" alt="[YOUR_ALT]"/>
</p>


**PCA**

El objetivo ahora es simplificar la características correlacionadas para así reducir las dimensiones y comprobar si aumenta la precisión.

Al haber reducido las dimensione vemos que no hay ninguna correlación con lo que no vale para nada

<p align="center">
   <img src="https://github.com/Ciarzi/DP3_GP1/blob/main/Logo/APC.png" alt="[YOUR_ALT]"/>
</p>


# 4.- Entrenamiento del modelo

Teniendo ya todo listo pasamos a entrenar los modelos y medir el porcentaje de validación.

Para ello ejecutaremos el código que se encuentra en [esta carpeta](https://github.com/Ciarzi/DP3_GP1/tree/main/classificator), el archivo llamado "loan_prediction.ipynb"

<p align="center">
   <img src="https://github.com/Ciarzi/DP3_GP1/blob/main/Logo/predicted.png" alt="[YOUR_ALT]"/>
</p>

# 5.- Modelo final

Una vez hemos entrenado el modelo, configuraremos los hiperparámetros usando la función "scale_pos_weight" para obtener un mejor resultado.

Ya con todo obtenemos una precisión del 0.799265605875153

