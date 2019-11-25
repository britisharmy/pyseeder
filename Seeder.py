import secrets
import asyncio
import random
from aiofile import AIOFile, LineReader, Writer

class Seeder:
  #default password for ion_auth,laravel and django
  #ion auth:: password :: $2y$08$200Z6ZZbp3RAEXoaWcMA6uJOFicwNZaqk4oDhqTUiFXFe63MG.Daa
  #laravel:: JohnDoe :: $2y$10$jSAr/RwmjhwioDlJErOk9OQEO7huLz9O6Iuf/udyGbHPiTNuB3Iuy 
  #laravel source: https://stackoverflow.com/questions/22846897/how-to-create-a-laravel-hashed-password
  #django:: 666monkeysAndDogs777 :: pbkdf2_sha256$20000$L7uq6goI1HIl$RYqywMgPywhhku/YqIxWKbpxODBeczfLm5zthHjNSSk=
  #django: source :: https://codeday.me/en/qa/20190312/3420.html
  
  def __init__(self, firstname, lastname,salutation,gender,coordinates,image,telephone_number,country,unix_timestamp,date_of_birth,numbers,decimals,address,email,django_password,paragraph,credit_card_number,cvv,day,month,year,username,random_string,postal_code,json_object,post_title,random_list_item,laravel_password,ion_auth_password:

    self.firstname = firstname
    self.lastname = lastname
    self.salutation = salutation
    self.gender = gender
    self.coordinates = coordinates
    self.image = image
    self.telephone_number = telephone_number
    self.country = country
    self.unix_timestamp = unix_timestamp
    self.date_of_birth = date_of_birth
    self.numbers = numbers
    self.decimals = decimals
    #choose decimal places
    self.address = address
    #english style addresses
    self.email = email
    self.django_password = django_password
    self.paragraph = paragraph
    self.credit_card_number = credit_card_number
    self.cvv = cvv
    self.day = day
    self.month = month
    self.year = year
    self.username = username
    self.random_string = random_string
    self.postal_code = postal_code
    self.json_object = json_object
    self.post_title = post_title
    self.random_list_item = random_list_item
    self.laravel_password = laravel_password
    self.ion_auth_password = ion_auth_password

    def firstname(self):
    print("Hello my name is " + self.name)

    def lastname(self):
    print("Hello my name is " + self.name)

    def salutation(self):
    salut = ['Mr', 'Mrs', 'Ms', 'Dr', 'Sir']
    return secrets.choice(salut)

    def gender(self):
    print("Hello my name is " + self.name)

    def coordinates(self):
    print("Hello my name is " + self.name)

    def image(self):
    print("Hello my name is " + self.name)

    def telephone_number(self):
    print("Hello my name is " + self.name)

    def country(self):
    print("Hello my name is " + self.name)

    def unix_timestamp(self):
    print("Hello my name is " + self.name)

    def date_of_birth(self):
    print("Hello my name is " + self.name)
    
    #give range
    def numbers(self):
    #random from range
    print (random.randrange(20, 50, 3)) 
    #random from list
    print (random.choice([1, 4, 8, 10, 3])) 

    def decimals(self):
    return float(decimal.Decimal(random.randrange(155, 389))/100)

    def address(self):
    print("Hello my name is " + self.name)

    def email(self):
    print("Hello my name is " + self.name)

    def django_password(self):
    print("Hello my name is " + self.name)

    def paragraph(self):
    print("Hello my name is " + self.name)

    def credit_card_number(self):
    print("Hello my name is " + self.name)

    def cvv(self):
    print("Hello my name is " + self.name)

    def day(self):
    print("Hello my name is " + self.name)

    def month(self):
    print("Hello my name is " + self.name)

    def year(self):
    print("Hello my name is " + self.name)

    def username(self):
    print("Hello my name is " + self.name)

    def random_string(self):
    print("Hello my name is " + self.name)

    def postal_code(self):
    print("Hello my name is " + self.name)

    def json_object(self):
    print("Hello my name is " + self.name)

    def random_list_item(self):
    print("Hello my name is " + self.name)
               
    def laravel_password(self):
    print("Hello my name is " + self.name)
               
    def ion_auth_password(self):
    print("Hello my name is " + self.name)
