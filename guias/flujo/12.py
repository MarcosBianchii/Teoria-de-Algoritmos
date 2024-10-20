# (★★★) Suponer que queremos schedulear cómo los aviones van de un aeropuerto a otro para cumplir sus horarios. Podemos decir que podemos usar un avión para un segmento/vuelo i y luego para otro j si se cumple alguna de las siguientes condiciones: a. El destino de i y el origen de j son el mismo. o b. Podemos agregar un vuelo desde el destino de i al origen de j con tiempo suficiente.

# Decimos que el vuelo j es alcanzable desde el vuelo i si es posible usar el avión del vuelo i y después para el vuelo j. Dados todos los vuelos con origen y destino, y el tiempo que tarda un avión entre cada par de ciudades queremos decidir: ¿Podemos cumplir con los m vuelos usando a lo sumo k aviones? Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se decide si es posible cumplir con la premisa. ¿Cuál es el orden temporal de la solución implementada?

"""
Crear una red de flujo siguiendo los siguentes criterios:

    - Si el vuelo debe hacerse, entonces crear un arco entre los aeropuertos tal que tengan capacidad uno y demanda uno.
    - Si el vuelo no es obligatorio pero es posible llevar un avion de un aeropuerto a otro en tiempo, entonces creamos un arco de capacidad 1 sin cota minima tal que pueda o no pasar que un avion sea utilizado de esta manera.

Para acotar inferiormente la capacidad de un arco (v, w):

    Creamos super-fuente tal que con la fuente tenga capacidad igual a la suma de sus pesos adyacentes menos uno por cada arco que querramos marcar como obligatorio. En este caso es asi porque queremos por cada uno tener capacidad uno. Analogo con el super-sumidero, con la salvedad de que ahora el arco entre ellos tiene capacidad igual a la suma de los pesos incidentes en el menos esta cantidad de arcos obligatorios.

    Restamos uno de capacidad al arco que queremos marcar como obligatorio, en este caso al llevar la capacidad a 0, lo borramos.

    De esta forma "ya gastamos" este flujo, pues creamos un nuevo camino mas corto hasta `w` y otro camino mas corto de `v` hasta el sumidero, entonces las otras mitades de los caminos al llegar a `v` gastaran 1 de capacidad por todo el camino y aseguramos que salga por este camino nuevo. Para `w` pasa lo mismo, probablemente sea el primer camino que el algoritmo de Ford Fulkeron tome y de esta forma gaste el flujo saliente de `w` de esta manera.

Una vez se tiene armado el grafo residual corremos Ford-Fulkerson, si el flujo maximo hasta el sumidero original es menor o igual a `k` entonces podemos asegurar que podemos tomar los `m` vuelos con a lo sumo `k` aviones.

Algoritmo:

1. Crear un grafo residual con los vertices siendo los extremos de cada vuelo (los aeropuertos en un cierto horario) O(n).

2. Agregar super-fuente y conectarla con capacidad 1 a todos los vertices con grado de incidencia 0, agregar super-sumidero y conectar todos los vertices con grado de adyacencia 0 O(n).

3. Insertar los arcos entre los vuelos (estos son los de demanda 1) O(n).

4. Por cada aeropuerto en un cierto horario agregar un arco de capacidad 1 entre el y todos los vertices tal que sea posible ir desde este aeropuerto al otro si llega a tiempo O(n^2).

5. Correr Ford-Fulkerson O(?).

6. Devovler si el flujo maximo es menor o igual al `k` pasado por parametro O(1).
"""
