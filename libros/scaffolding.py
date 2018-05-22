from generic_scaffold import CrudManager
import libros.models as models

class LibroCrudManager(CrudManager):
    model = models.Libro
