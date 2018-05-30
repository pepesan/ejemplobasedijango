from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique book instances

class Language(models.Model):
    """
    Modelo que representa un idioma por ejemplo español
    """
    name = models.CharField(max_length=200, help_text="Introduce un nombre de idioma")
    codigo = models.CharField(max_length=6, help_text="Introduce un código de idioma")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name

class Genre(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(max_length=200, help_text="Introduce un género literario")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', kwargs={'pk': self.pk})

        #return reverse('genre-list')
    #Para arreglar un warning :UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list:
    class Meta:
        ordering = ['name']


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Book(models.Model):
    """
    Modelo que representa un libro (pero no un Ejemplar específico).
    """

    title = models.CharField(max_length=200,help_text="Introduce el título del libro")

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.


    summary = models.TextField(max_length=1000, help_text="Introduce la descripción del libro")

    isbn = models.CharField('ISBN', max_length=13,
                            help_text='<a href="https://www.isbn-international.org/content/what-isbn">Número ISBN</a> de 13 caracteres')

    genre = models.ManyToManyField(Genre, help_text="Selecciona el género de este libro", blank=True)

    language = models.ManyToManyField(Language, help_text="Selecciona el idioma de este libro", blank=True)

    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.title

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('genre-detail', args=[str(self.id)])





class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Identificativo único para este libro físico")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)