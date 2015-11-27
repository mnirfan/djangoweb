from django.contrib import admin
from books.models import Publisher, Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')  # menampilkan search untuk fields first_name dan last_name

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'book_publisher', 'publication_date') # untuk menentukan urutan kolom di halaman admin
    list_filter = ('publication_date',) #> menampilkan panel filter tanggal
    date_hierarchy = 'publication_date' #> menampilkan hierarki tanggal diatas tabel list data buku
    ordering = ('publication_date',)    #> mengatur pengurutan data di tabel
                                        #> ordering bisa menggunakan descending dengan menggunakan '-publication_date'
    fields = ('title', 'author', 'publisher',)      #> fields berguna untuk mengatur urutan form yang tampil
                                                    #  dihalaman admin change book
    filter_horizontal = ('author',)                 #> bisa searching dan select dengan mudah dengan 2 panel

    def book_publisher(self, obj):
        return "\n".join([p.name for p in obj.publisher.all()])

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)