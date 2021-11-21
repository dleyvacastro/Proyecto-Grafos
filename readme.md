<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">ANIME SUGGESTOR</h3>
</p>

<!-- TABLE OF CONTENTS -->- [Tabla de contenidos:]
- [Descripcion:](#descripcion)
- [Modelo:](#modelo)
  - [Vertices:](#vertices)
  - [Aristas:](#aristas)
  - [Relación:](#relación)
- [Implementación:](#implementacion)
  - [Recolección de datos:](#recoleccion-de-datos)
  - [Procesamiento de datos:](#procesamiento-de-datos)
  - [Muestra de datos:](#muestra-de-datos)
- [Resultado final:](#resultado-final)


## Descripcion
Se desarrollo una aplicación que con el uso de grafos ponderados es capaz de generar recomendaciones de series anime con base en los gustos del usuario, especificamente, en los interpretes de voz y generos de obras vistas previamente.

## Modelo
Se modeló un grafo ponderado, definido de la siguiente manera:
### Vertices
$V = {v_1,v_2,...,v_3}$ donde $n$ es el número de animes en el grafo y $v_i$ es la representación del anime $i$.
### Aristas
$E = {e_1,e_2,...,e_k}$ donde $k$ es el numero de aristas del grafo y la arista $e_i$ conecta 2 animes que guarden una relación por géneros o por interpretes de voz en comun.
### Relación
$W = \{w_{0}, w_{2}, ..., w_{k}\}$ donde $w_{i}$ representa el peso de la arista $e_{i}$ dada por la relación $f$ existente entre los vértices $a$ y $b$, lo calculamos de la siguiente manera:
        
        $f = 1 - (0.7 \cdot{**g**} +0.3 \cdot{\textbf{**s**}})$
        
        Donde: \\

            \item $**g**$ es la proporción dada por la cantidad de géneros que coinciden sobre la cantidad de géneros totales entre 2 animes:    
                $$\dfrac{|GE_{a} \cap GE_{b}|}{|GE_{a} \cup GE_{b}|}$$
            \item $**s**$ es la proporción dada por la cantidad de seiyuu's que coinciden sobre la cantidad de seiyuu's totales entre 2 animes:    
                $$\dfrac{|SL_{a} \cap SL_{b}|}{|SL_{a} \cup SL_{b}|}$$

        Note que $\textbf{g,s} \leq 1$.
