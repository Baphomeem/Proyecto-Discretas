# Manual de Usuario — Expansor de Expresiones Algebraicas en LaTeX

Este manual explica cómo usar el programa de expansión algebraica, paso a paso, desde su ejecución hasta la interpretación de los resultados.

---

## 🧩 ¿Qué hace el programa?

Este programa toma una **expresión escrita como producto de factores en LaTeX** y devuelve el **polinomio expandido equivalente**, también en LaTeX.

### 🧪 Ejemplo

**Entrada:** `(x+1)^2(x-2)`  
**Salida:** `$x^{3} - 3x^{2} + 2$`

---

## 🖥️ Requisitos del sistema

- Tener instalado **Python 3.x**
- Un editor de texto o consola para ejecutar el script

---

## ▶️ Cómo ejecutar el programa

1. Abre una terminal (o consola de comandos).
2. Ejecuta el archivo `.py` con Python:

```bash
python expandir.py
```

---

## ⌨️ Instrucciones de uso

Una vez ejecutado el programa:

1. Se mostrará el mensaje:

```
Ingresa la expresión en LaTeX:
```

2. Escribe una expresión algebraica en formato LaTeX, por ejemplo:

```
(x+1)^2(x-2)
```

3. Presiona `Enter`.

4. El programa mostrará la **expansión del producto** en formato LaTeX, como:

```
$x^{3} - 3x^{2} + 2$
```

---

## 🎯 Reglas de entrada

- Puedes usar expresiones como `(x+2)(x-3)` o con potencias como `(x+1)^3`.
- Los paréntesis deben estar correctamente balanceados.
- No necesitas incluir símbolos LaTeX como `\left`, `\right` o `$...$` (el programa los ignora o limpia).

---

## 🚫 Qué no soporta (aún)

- Expresiones con varias variables (como `x` y `y`).
- Fracciones, radicales u operaciones racionales.
- Entrada de expresiones mal escritas (con paréntesis mal cerrados, por ejemplo).

---

## ✅ Ejemplos válidos

| Entrada                   | Salida                    |
|---------------------------|----------------------------|
| `(x+1)(x+2)`             | `$x^{2}+3x+2$`             |
| `(x+1)^2(x-2)`           | `$x^{3}-3x^{2}+2$`         |
| `(x-3)^2(x+3)^2`         | `$x^{4}-18x^{2}+81$`       |
| `(2x+1)(x-4)`            | `$2x^{2}-7x-4$`            |

---

## ℹ️ Notas adicionales

- Si ingresas un término como `-x`, el programa lo interpreta como `-1x`.
- Si el resultado tiene un coeficiente `1`, se omite por convención (por ejemplo, `1x^2` se muestra como `x^2`).
- Si un término queda con coeficiente `0`, se elimina automáticamente.

---

## 🆘 Problemas comunes

| Problema | Solución |
|---------|----------|
| Escribí `((x+1)^2` y no funcionó | Revisa que todos los paréntesis estén cerrados |
| Puse `$` y me da error raro | El programa limpia `$`, pero si hay errores de sintaxis dentro, fallará |
| Pongo `x+1)^2` y da error | El paréntesis inicial es obligatorio: pon `(x+1)^2` |

---

## 📬 Contacto

Si tienes dudas, errores o mejoras, puedes contactar al desarrollador o modificar el código por tu cuenta.