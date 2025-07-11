# tienda Pybooks

produtos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
 }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
         'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],}

def stock_marca(marca):
    marca = marca.lower()
    total_stock = 0
    for modelo, datos in produtos.items():
        marca_modelo = datos[0].lower()
        if marca_modelo == marca:
            if modelo in stock:
                total_stock += stock[modelo][1]
    print(f"stock total de la marca {marca.capitalize()}: {total_stock}")

def buscar_por_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except:
        print("Debe ingresar valores enteros!!")
        return
    
    modelos_en_rango = []
    for modelo, datos_stock in stock.items():
        precio, cantidad = datos_stock
        if cantidad > 0 and p_min <= precio <= p_max:
            marca = produtos.get(modelo, ["Desconocida"])[0]
            modelos_en_rango.append(f"{marca}--{modelo}")
    
    if modelos_en_rango:
        modelos_en_rango.sort()
        print("Modelos disponibles e n el rango de precios:")
        for m in modelos_en_rango:
            print(m)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False

def menu():
    while True:
        print("============================")
        print("Bienvenido a la tienda Pybooks")
        print("============================")
        print("\n---| MENU PRINCIPAL |---")
        print("1. Stock por marca")
        print("2. Buscar por rango de precios")
        print("3. Actualizar precio de modelo")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == '1':
            marca = input("Ingrese la marca: ")
            stock_marca(marca)
            
        elif opcion == '2':
            p_min = input("Ingrese precio minimo: ")
            p_max = input("Ingrese precio maximo: ")
            buscar_por_precio(p_min, p_max)
            
        elif opcion == '3':
            while True:
                modelo = input("Ingrese el modelo a actualizar: ").strip()
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: ").strip())
                except:
                    print("Debe ingresar un valor numerico para el precio.")
                    continue
                
                if actualizar_precio(modelo, nuevo_precio):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                
                continuar = input("Desea actualizar otro precio? (s/n): ").strip().lower()
                if continuar != 's':
                    break
                
        elif opcion == '4':
            print("Programa finalizado.")
            break
            
        else:
            print("Debe seleccionar una opcion valida!!")


menu()
