# (★★★) Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar juntos para ir a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus hermanos! Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la escuela quedan en esquinas, pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela. No se puede asumir que la ciudad tenga alguna forma en específico, por ejemplo, no hay que asumir que todas las calles sean cuadradas. Utilizando lo visto en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo.

"""
Los hijos de Carlos estan representados por el flujo de la red.

La red residual tiene como fuente a la esquina donde esta la casa y sumidero a la esquina de la escuela, agregamos los vertices que componen los caminos posibles entre ellas y agregamos arcos de capacidad 1, de esta forma representamos los caminos que tomo cada uno de los hermanos como ya tomado o no a la hora de llenar la red con flujo.

Corremos Ford-Fulkerson sobre esta red, si el flujo maximo es mayor o igual a 5, entonces los hijos de Carlos pueden ir de casa a la escuela sin encontrarse.

La complejidad del algoritmo es O(V * A^2)
"""
