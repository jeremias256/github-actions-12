import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!: paso 2")


if __name__ == "__main__":
    main()