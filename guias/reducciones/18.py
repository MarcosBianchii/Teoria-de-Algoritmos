# (★★) Definir la relación entre la dificultad entre el problema de obtener el flujo máximo, con el problema de obtener el corte mínimo en una red de transporte. ¿Se puede concluir si alguno de estos problemas es NP-Completo, o que no lo sea? ¿Estos problemas pertenecen a PSPACE? Justificar adecuadamente cada respuesta.

"""
La dificultad de obtener el flujo máximo y el de obtener el corte mínimo de una red de transporte, es igual de dificil. Pues, determinar cualquiera de estos dos da la respuesta al otro, podríamos decir que son el mísmo problema. No lo digo yo, existe el siguiente teorema:

Teorema Max-Flow Min-Cut:
En una red de flujo, el máximo flujo que pasa de la fuente al sumidero es igual al peso máximo de los arcos en el corte mínimo.

Entonces si alguno de ellos es NP-Completo, entonces ambos lo son.

Como ya sabemos que el cálculo del flujo máximo toma tiempo polinomial (mediante el algoritmo de Ford-Fulkerson) bastaría con reducirlo polinomialmente a corte mínimo para concluir que ambos problemas viven en P. Ahora, no podemos concluir que no son NP-Completos, puesto que no sabemos si P = NP o no.

Podría intentar reducir un problema NP-Completo a él, pero, no ser capaz de hacer esto quiere decir una de las siguientes cuestiones, estas son:

i)  El problema no es reducible, por lo que es un problema más sencillo.
ii) No tengo la capacidad de crear un modelo que lo permita porque no soy lo suficientemente inteligente para reducir un problema al otro.

Como no puedo determinar por cual de las dos estoy fallando, entonces (mientras que no se pruebe que P != NP) no puedo concluir de que sean o no NP-Completos.

Ambos problemas pertenecen a PSPACE, puesto que el algoritmo de Ford-Fulkerson tiene una complejidad espacial de O(V + A) que no es exponencial. Por el teorema antes mencionado, calcular el corte mínimo es igual de difícil que calcular el flujo máximo de una red de flujo.
"""
