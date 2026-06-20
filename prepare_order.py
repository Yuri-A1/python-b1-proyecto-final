from users import Cashier, Customer
from products import Hamburger, Soda, Drink, HappyMeal
from orders import Order
from util import CSVFileManager, CashierConverter, CustomerConverter, ProductConverter

class PrepareOrder:
    def __init__(self):
        self.cajeros = CashierConverter().convert(CSVFileManager('data/cashiers.csv').read())
        self.clientes = CustomerConverter().convert(CSVFileManager('data/customers.csv').read())
        
        self.productos = []
        self.productos.extend(ProductConverter().convert(CSVFileManager('data/hamburgers.csv').read(), Hamburger))
        self.productos.extend(ProductConverter().convert(CSVFileManager('data/sodas.csv').read(), Soda))
        self.productos.extend(ProductConverter().convert(CSVFileManager('data/drinks.csv').read(), Drink))
        self.productos.extend(ProductConverter().convert(CSVFileManager('data/happyMeal.csv').read(), HappyMeal))

    def run(self):
        dni_cajero = input("Introduce el DNI del cajero: ")
        cajero = next((c for c in self.cajeros if c.dni == dni_cajero), None)
        if not cajero:
            print("Error: Cajero no encontrado.")
            return

        dni_cliente = input("Introduce el DNI del cliente: ")
        cliente = next((c for c in self.clientes if c.dni == dni_cliente), None)
        if not cliente:
            print("Error: Cliente no encontrado.")
            return

        orden = Order(cajero, cliente)

        while True:
            print("\n--- MENÚ DE PRODUCTOS ---")
            for p in self.productos:
                print(f"ID: {p.id} | {p.name} - {p.price}€")
            
            id_prod = input("\nIntroduce ID del producto a añadir (o 'fin' para terminar): ")
            if id_prod.lower() == 'fin':
                break
            
            prod = next((p for p in self.productos if p.id == id_prod), None)
            if prod:
                orden.add(prod)
                print(f"--> Añadido: {prod.name}")
            else:
                print("Error: ID no válido.")

        print("\n" + "="*30)
        orden.show()


if __name__ == "__main__":
    app = PrepareOrder()
    app.run()