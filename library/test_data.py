from authentication.models import CustomUser
from author.models import Author
from django.utils.timezone import datetime
from book.models import Book
from order.models import Order
from django.http import HttpResponse
import pytz
import datetime



def add_test_data():

    TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
    TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)

    CustomUser.objects.all().delete()

    user1=CustomUser(id=111,
            email='email@mail.com',
            password='1234',
            first_name='fname',
            middle_name='mname',
            created_at=TEST_DATE,
            last_name='lname')
    user1.save()
        
    user2=CustomUser(id=112,
            email='email1@mail.com',
            password='12345',
            first_name='firstname',
            middle_name='middlename',
            created_at=TEST_DATE,
            last_name='lname')
    user2.save()

    user3=CustomUser(id=113,
            email='artem@mail.com',
            password='1234567',
            first_name='Artem',
            middle_name='',
            last_name='Deineko',
            created_at=TEST_DATE,
            role=1,
            is_active=True)
    user3.save()
        
    user4=CustomUser(id=114,
            email='arthur@mail.com',
            password='1234567',
            first_name='Arthur',
            middle_name='',
            last_name='Sobolevsky',
            created_at=TEST_DATE,
            role=1,
            is_active=True)
    user4.save()


    Author.objects.all().delete()
    author1 = Author(id=101, name="author1", surname="s1", patronymic="p1")
    author1.save()
    author2=Author(id=102, name="author2", surname="s2", patronymic="p2")
    author2.save()
    author3=Author(id=103, name="author3", surname="s3", patronymic="p3")
    author3.save()
    author4=Author(id=104, name="author4", surname="s4", patronymic="p4")
    author4.save()
    author5=Author(id=105, name="author5", surname="s5", patronymic="p5")
    author5.save()
    author6=Author(id=106, name="Andrzej ", surname="Sapkowski", patronymic="Batkovich")
    author6.save()
    author7=Author(id=107, name="George", surname="Raymond", patronymic="Martin")
    author7.save()

    Book.objects.all().delete()
    book1=Book(id=121, name="book1", description="description1", count=1)
    book1.save()
    book1.authors.add(author2)
    book1.save()
    book2 = Book(id=122, name="book2", description="description2", count=2)
    book2.save()
    book2.authors.add(author2)
    book2.save()
    book3 = Book(id=123, name="book3", description="description3", count=3)
    book3.save()
    book3.authors.add(author3)
    book3.save()
    book4 = Book(id=124, name="book4", description="description4", count=4)
    book4.save()
    book4.authors.add(author4)
    book4.save()
    book5 = Book(id=125, name="book5", description="description5", count=5)
    book5.save()
    book5.authors.add(author4)
    book5.save()
    book6 = Book(id=126, name="book6", description="description6", count=6)
    book6.save()
    book6.authors.add(author2)
    book6.save()
    book7 = Book(id=127, name="book7", description="description7", count=7)
    book7.save()
    book7.authors.add(author5)
    book7.save()
    book8 = Book(id=128, name="book8", description="description8", count=8)
    book8.save()
    book8.authors.add(author5)
    book8.save()
    book9 = Book(id=129, name="book9", description="description9", count=9)
    book9.save()
    book9.authors.add(author5)
    book9.save()
    book10 = Book(id=130, name="book10", description="description10", count=10)
    book10.save()
    book10.authors.add(author5)
    book10.save()
    book11 = Book(id=131, name="The Witcher : The Last Wish", description="description11", count=7)
    book11.save()
    book11.authors.add(author6)
    book12 = Book(id=132, name="The Witcher : Sword of Destiny", description="description12", count=4)
    book12.save()
    book12.authors.add(author6)
    book13 = Book(id=133, name="The Witcher : Blood of Elves", description="description13", count=9)
    book13.save()
    book13.authors.add(author6)
    book14 = Book(id=134, name="A Song of Ice and Fire", description="description14", count=2)
    book14.save()
    book14.authors.add(author7)


    Order.objects.all().delete()
    Order(id=151, user=user1, book=book1, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=152, user=user2, book=book2, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=153, user=user3, book=book3, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=154, user=user4, book=book3, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=155, user=user3, book=book4, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=156, user=user3, book=book5, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=157, user=user4, book=book4, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=158, user=user4, book=book6, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=159, user=user1, book=book7, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=160, user=user3, book=book8, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=161, user=user4, book=book9, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()
    Order(id=162, user=user2, book=book10, end_at=TEST_DATE_END, plated_end_at=TEST_DATE).save()

