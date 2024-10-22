# (★★★) El problema de decisión de 3-SAT dice: dadas un número de cláusulas de variables booleanas, cada cláusula consta de la operación OR entre 3 términos, decidir si existe una configuración de las variables booleanas tal que sea posible cumplir todas las cláusulas. El problema de 3-SAT es NP-Completo. Dados los problemas de decisión de Independent Set y 3-SAT, demostrar que Independent Set es NP-Completo. Luego explicar de qué manera, con el trabajo hecho en la guía hasta este ejercicio, se puede afirmar que Vertex Cover es NP-Completo.

"""
NP: Un problema está en NP sii tiene algún verificador polinómico.

NP-Completo: Un problema es NP-Completo sii todo problema dentro de NP es reducible polinómicamente a él, esto quiere decir, es de los problemas más difíciles de NP.

Problema de decisión de 3-SAT: Dado una colección de clausuras binarias de hasta 3 variables cada una, determinar si es posible lograr que todas ellas evaluen a TRUE con algúna permutación de estados en estas variables.

Problema de decisión de Independent Set: Dado un grafo y un número entero `k`, determinar si es posible obtener un subconjunto de vértices de tamaño `k` tal que ningún vértice del subconjunto sea adyacente con otro dentro de él.

Para demostrar que Independent Set es NP-Completo podemos probar que 3-SAT <=p IS y de esta forma demostrar que 3-SAT es a lo sumo tán dificil como Independent Set, como sabemos que 3-SAT es NP-Completo => a Independent Set no le queda otra que serlo también. No hace falta probar que Independent Set esta en NP, esta hecho en 1.py.

Entonces, teniendo un resolvedor de Independent Set, deberíamos ser capaces de modelar 3-SAT a partir de un grafo y resolverlo encontrando un Independent Set para algún k.

    def 3-SAT(clausuras):
        # transformacion
        return IS(grafo, k)

Creamos un vértice por cada variable de cada clausura, sabemos que hay hasta 3 variables por cada una. Por lo que obtenemos hasta 3 * k vértices, siendo k la cantidad de clausuras.

Conectamos las variables entre ellas si son la misma de forma negada, por ejemplo: x0 y x0_prima. De esta forma modelamos que dependen de la misma variable, por lo que si x0 pertenece al IS, x0_prima no.

Conectamos los vértices de cada clausura entre ellos, generando k sub-grafos 3-completos, de esta forma aseguramos distribuir los vértices que vayan a quedar en el Independent Set a uno por clausura.

Es satisfacible sii existe un Independent Set de tamaño k en el grafo generado.

3-SAT => IS:
Si la entrada es satisfacible, entonces por lo menos un vértice dentro de cada clausura está en el Independent Set. Nos quedamos con 1 por clausura de los que son TRUE, de esta forma existe un Independent Set.

IS => 3-SAT:
Si tenemos un Independent Set de k vértices, hay 1 vértice por cada clausura que está en él. Por lo que hay una de las variables que es TRUE en cada una, esto hace que todas las clausuras evaluen a TRUE, entonces se da 3-SAT.

Como 3-SAT <=p Independent Set e Independent Set <=p Vertex Cover, sabiendo que la relación <=p es transitiva, logramos demostrar que 3-SAT <=p Vertex Cover.
"""
