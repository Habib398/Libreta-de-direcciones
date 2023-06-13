import sys

class Menu:
    """
    Clase que representa el menú principal del programa de la libreta de direcciones.
    """

    def __init__(self, addressBook):
        """
        Inicializa una instancia del menú principal.
        Args:
            addressBook (AddressBook): La libreta de direcciones asociada al menú.
        """

        self.addressBook = addressBook

    def displayMenu(self):
        """
        Muestra el menú principal y maneja las opciones seleccionadas por el usuario.
        """

        scanner = Scanner()
        choice = ""
        while choice != 'f':
            print("\nMenú:")
            print("a) Agregar una entrada")
            print("b) Eliminar una entrada")
            print("c) Buscar entradas por apellido")
            print("d) Mostrar todas las entradas ordenadas por apellido")
            print("e) Salir")
            choice = scanner.nextLine()[0]
            if choice == 'a':
                self.addEntry()
            elif choice == 'b':
                self.deleteEntry()
            elif choice == 'c':
                self.searchEntriesByLastName()
            elif choice == 'd':
                self.showEntriesOrderedByLastName()
            elif choice == 'e':
                print("Saliendo del programa...")
            else:
                print("Opción inválida. Intente nuevamente.")


    def addEntry(self):
        """
        Agrega una nueva entrada a la libreta de direcciones.
        """

        print("Agregar una entrada:")
        scanner = Scanner()

        print("Nombre: ")
        firstName = scanner.nextLine()

        print("Apellido: ")
        lastName = scanner.nextLine()

        print("Calle: ")
        street = scanner.nextLine()

        print("Ciudad: ")
        city = scanner.nextLine()

        print("Estado: ")
        state = scanner.nextLine()

        print("Código Postal: ")
        zipCode = scanner.nextLine()

        print("Correo Electrónico: ")
        email = scanner.nextLine()

        print("Teléfono: ")
        phone = scanner.nextLine()

        address = Address(street, city, state, zipCode)
        entry = AddressEntry(firstName, lastName, address, email, phone)
        self.addressBook.addEntry(entry)

        print("La entrada ha sido agregada correctamente.")

    def deleteEntry(self):
        """
        Elimina una entrada existente de la libreta de direcciones.
        """

        print("Eliminar una entrada:")
        scanner = Scanner()

        print("Ingrese el apellido para buscar la entrada: ")
        lastName = scanner.nextLine()

        entry = self.addressBook.searchEntryByLastName(lastName)

        if entry is None:
            print("No se encontró ninguna entrada con ese apellido.")
            return

        print("Se encontró la siguiente entrada:")
        print(entry)

        print("¿Está seguro de eliminar esta entrada? (s/n): ")
        confirmation = scanner.nextLine()

        if confirmation.lower() == "s":
            self.addressBook.deleteEntry(entry)
            print("La entrada ha sido eliminada correctamente.")
        else:
            print("La entrada no ha sido eliminada.")

    def searchEntriesByLastName(self):
        """
        Busca y muestra las entradas en la libreta de direcciones por apellido.
        """

        print("Buscar entradas por apellido:")
        scanner = Scanner()

        print("Ingrese el apellido (o parte del apellido) para buscar: ")
        lastName = scanner.nextLine()

        entries = self.addressBook.searchEntriesByLastName(lastName)

        if not entries:
            print("No se encontraron entradas con ese apellido.")
        else:
            print("Se encontraron las siguientes entradas:")
            for entry in entries:
                print(entry)

    def showEntriesOrderedByLastName(self):
        """
        Muestra todas las entradas de la libreta de direcciones ordenadas por apellido.
        """

        print("Mostrar todas las entradas ordenadas por apellido:")
        entries = self.addressBook.getEntriesOrderedByLastName()

        if not entries:
            print("No hay entradas para mostrar.")
        else:
            print("Las entradas se muestran a continuación:")
            for entry in entries:
                print(entry)


class Scanner:
    """
    Clase que proporciona métodos para leer la entrada del usuario desde la consola.
    """
    def nextLine(self):
        """
        Lee la siguiente línea de entrada desde la consola y la devuelve como una cadena.
        Returns:
            str: La línea de entrada leída desde la consola.
        """
        return sys.stdin.readline().strip()

class Address:

    """
    Clase que representa una dirección en la libreta de direcciones.

    """
    def __init__(self, street, city, state, zipCode):

        """
        Inicializa una instancia de la clase Address.

        Args:
        street (str): El nombre de la calle.
        city (str): El nombre de la ciudad.
        state (str): El nombre del estado.
        zipCode (str): El código postal.
        """
        self.street = street
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def __str__(self):

        """
        Devuelve una representación de cadena de la dirección en el formato "calle, ciudad, estado código_postal".
        Returns:
        str: La representación de cadena de la dirección.
        """

        return self.street + ", " + self.city + ", " + self.state + " " + self.zipCode


class AddressEntry:

    """
    Clase que representa una entrada en la libreta de direcciones.
    """

    def __init__(self, firstName, lastName, address, email, phone):

        """
        Inicializa una instancia de la clase AddressEntry.

        Args:
        firstName (str): El nombre del contacto.
        lastName (str): El apellido del contacto.
        address (Address): La dirección del contacto.
        email (str): El correo electrónico del contacto.
        phone (str): El número de teléfono del contacto.
        """

        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.email = email
        self.phone = phone

    def getFirstName(self):

        """
        Devuelve el nombre del contacto.
        Returns:
        str: El nombre del contacto.
        """

        return self.firstName

    def getLastName(self):

        """
        Devuelve el apellido del contacto.
        Returns:
        str: El apellido del contacto.
        """

        return self.lastName

    def getAddress(self):

        """
        Devuelve la dirección del contacto.
        Returns:
        Address: La dirección del contacto.
        """

        return self.address

    def getEmail(self):

        """
        Devuelve el correo electrónico del contacto.
        Returns:
        str: El correo electrónico del contacto.
        """

        return self.email

    def getPhone(self):

        """
        Devuelve el número de teléfono del contacto.
        Returns:
        str: El número de teléfono del contacto.
        """

        return self.phone

    def __str__(self):

        """
        Devuelve una representación de cadena de la entrada en formato legible.
        Returns:
        str: La representación de cadena de la entrada.
        """

        return "Nombre: " + self.firstName + " " + self.lastName + "\n" + \
               "Dirección: " + str(self.address) + "\n" + \
               "Correo electrónico: " + self.email + "\n" + \
               "Teléfono: " + self.phone


class AddressBook:

    """
    Clase que representa una libreta de direcciones.
    """

    def __init__(self):

        """
        Inicializa una instancia de la clase AddressBook con una lista vacía de entradas.
        """

        self.entries = []

    def addEntry(self, entry):

        """
        Agrega una entrada a la libreta de direcciones.
        Args:
        entry (AddressEntry): La entrada a agregar.
        """

        self.entries.append(entry)

    def deleteEntry(self, entry):

        """
        Elimina una entrada de la libreta de direcciones.
        Args:
        entry (AddressEntry): La entrada a eliminar.
        """

        self.entries.remove(entry)

    def searchEntryByLastName(self, lastName):

        """
        Busca una entrada en la libreta de direcciones por apellido.
        Args:
        lastName (str): El apellido para buscar.
        Returns:
        AddressEntry or None: La entrada encontrada o None si no se encuentra ninguna entrada con ese apellido.
        """

        for entry in self.entries:
            if entry.getLastName().lower() == lastName.lower():
                return entry
        return None

    def searchEntriesByLastName(self, lastName):

        """
        Busca y devuelve una lista de entradas en la libreta de direcciones que coinciden con un apellido dado.
        Args:
        lastName (str): El apellido (o parte del apellido) para buscar.
        Returns:
        list: Una lista de AddressEntry que coinciden con el apellido buscado.
        """

        matchingEntries = []
        for entry in self.entries:
            if entry.getLastName().lower().startswith(lastName.lower()):
                matchingEntries.append(entry)
        return matchingEntries

    def getEntriesOrderedByLastName(self):

        """
        Devuelve una lista de todas las entradas de la libreta de direcciones ordenadas por apellido.
        Returns:
        list: Una lista de AddressEntry ordenadas por apellido.
        """

        sortedEntries = sorted(self.entries, key=lambda entry: entry.getLastName().lower())
        return sortedEntries


if __name__ == "__main__":
    # Crea una instancia de AddressBook y Menu, luego muestra el menú principal.
    addressBook = AddressBook()
    menu = Menu(addressBook)
    menu.displayMenu()
