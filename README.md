# Virtualización: Promedio en Python con Docker y VirtualBox

Este proyecto es parte de un trabajo integrador para la materia **Arquitectura y Sistemas Operativos**, donde se compara el uso de **Docker** y **Oracle VirtualBox** para ejecutar un mismo programa en Python.

## 🧪 Descripción del script

El archivo `promedio.py` solicita tres notas al usuario y calcula el promedio.

```python
notas = []

for i in range(3):
    nota = float(input(f"Ingresá la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"El promedio es: {promedio}")
```

## 🐳 Uso con Docker

1. Crear los archivos `promedio.py` y `Dockerfile` en una misma carpeta.

### Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY promedio.py .
CMD ["python", "promedio.py"]
```

2. Construir la imagen:

```bash
docker build -t promedio-python .
```

3. Ejecutar el contenedor:

```bash
docker run -it --rm promedio-python
```

## 💻 Uso en VirtualBox

1. Crear una máquina virtual con Ubuntu.
2. Abrir terminal y crear el archivo `promedio.py` (usando `nano` o un editor).
3. Ejecutar:

```bash
python3 promedio.py
```

## 📊 Comparativa

| Característica | Docker | VirtualBox |
|----------------|--------|------------|
| Tiempo de arranque | Rápido (segundos) | Lento (minutos) |
| Recursos utilizados | Bajos | Altos |
| Nivel de aislamiento | Medio | Completo |
| Facilidad para tareas simples | Alta | Baja |
| Ideal para... | Apps y scripts | Sistemas completos |

---

## 👨‍🎓 Autores

- Stefan Dios Mayarin
- Mathias Flor