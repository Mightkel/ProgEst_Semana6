def create_product(products):
    print("--- CREAR PRODUCTO ---")

    try:
        product_id = int(input("ID del producto: "))

        # Verificar que el ID no exista
        for product in products:
            if product["id"] == product_id:
                print("Error: ese ID ya existe.")
                return

        name = input("Nombre del producto: ")

        if name.strip() == "":
            print("Error: el nombre no puede estar vacío.")
            return

        price = float(input("Precio: "))
        quantity = int(input("Cantidad: "))

        if price < 0 or quantity < 0:
            print("Error: precio y cantidad no pueden ser negativos.")
            return

        product = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)

        print("Producto creado correctamente.")

    except ValueError:
        print("Error: ingrese valores numéricos válidos.")