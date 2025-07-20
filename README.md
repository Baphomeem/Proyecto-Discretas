# Expansor de Expresiones Algebraicas en LaTeX

Este proyecto es un programa en Python que **expande productos de factores algebraicos** escritos en sintaxis **LaTeX**, y devuelve la expresión resultante como un **polinomio también en formato LaTeX**.

Fue desarrollado sin el uso de bibliotecas externas, empleando únicamente funciones básicas de Python y una estructura clara y modular. Además, ahora soporta **factores elevados a potencias**, como:

```
(x+1)^2(x-2)
```

---

## ✨ Características

- Entrada y salida en formato **LaTeX**.
- Soporta términos como `x`, `x^2`, `-3x`, constantes, etc.
- Admite expresiones con potencias, como `(x+2)^3`.
- Suma automáticamente los términos semejantes.
- Ordena los términos de mayor a menor grado.
- No depende de bibliotecas externas.

---

## 🛠️ Requisitos

- Python 3.x

---

## 🚀 Uso

1. Guarda el archivo Python (por ejemplo, `expandir.py`).
2. Ejecuta el script desde la terminal:

```bash
python expandir.py
```

3. Ingresa una expresión en formato LaTeX cuando se te solicite:

```
Ingresa la expresión en LaTeX: (x+1)^2(x-2)
```

4. El programa mostrará el resultado expandido, también en LaTeX:

```
$x^{3}-3x^{2}+2$
```

---

## 📚 Ejemplos de entrada/salida

| Entrada                   | Salida                   |
|---------------------------|---------------------------|
| `(x+1)(x-2)`             | `$x^{2}-x-2$`             |
| `(x+2)^2(x-1)`           | `$x^{3}+3x^{2}-2x-4$`     |
| `(x-3)^2(x+3)^2`         | `$x^{4}-18x^{2}+81$`      |
| `(2x+1)(x-4)`            | `$2x^{2}-7x-4$`           |

> Puedes usar o no usar `\left` y `\right`, y puedes envolver la expresión con `$...$` (se ignora automáticamente).

---

## 👨‍💻 Estructura del Código

- Funciones pequeñas y claras para:
  - Limpieza y preprocesamiento de la entrada.
  - Expansión de potencias.
  - Extracción de factores y términos.
  - Multiplicación de factores.
  - Suma de términos semejantes.
  - Conversión a LaTeX.

---

## 👥 Créditos

Desarrollado por Juan Esteban Ocampo Vidal, Sara Isabel Sepulveda Perez, Nicolas Caucali Junco, Daniel Felipe Pardo Castillo.
Inspirado en prácticas de álgebra computacional y enseñanza.

---

## 🪪 Licencia

Este proyecto se puede usar libremente con fines educativos o personales.  
Si deseas modificarlo o publicarlo, incluye referencia al autor original.