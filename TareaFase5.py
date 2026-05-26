def calcular_precio_final(datos):
    for i in range(len(datos)):
        if datos[i][2] > 15000 and datos[i][1] == "Especial":
            datos[i][2] = datos[i][2] - (datos[i][2] * 0.15)
    for i in range(len(datos)):
        if datos[i][2] > 8000 and datos[i][1] == "Malteadas":
            datos[i][2] = datos[i][2] - (datos[i][2] * 0.15)

    return datos


def principal():
    datos = [
        ["Carne asada", "Ejecutivo", 13000],
        ["Pollo BBQ", "Especial", 16000],
        ["Pechuga de pollo", "Plato del día", 12000],
        ["Postre de chocolate", "postres", 5000],
        ["Jugos en agua", "Jugos", 7900],
        ["Malteada de chocolate", "Malteadas", 8900],
    ]
    n = 3
    print("""
        El producto Pollo BBQ tiene un precio base de 16000, pero al ser un producto especial y tener un precio"
        " mayor a 15000, se le aplica un descuento del 15%, quedando con un precio final de 13600.
        """)
    print("""
╔═════════════════════════╦═════════════════╦═══════════════╦══════════════╗
║         Producto        ║    Categoría    ║  Precio Base  ║ Precio final ║
╠═════════════════════════╬═════════════════╬═══════════════╬══════════════╣""")
    for i in range(len(datos)):

        print(
            f"║  {datos[i][0]:22} ║  {datos[i][1]:14} ║  {datos[i][2]:12} ║ {calcular_precio_final([datos[i]])[0][2]:12} ║"
        )
    print(
        """╚═════════════════════════╩═════════════════╩══════════════════════════════╝"""
    )


principal()
