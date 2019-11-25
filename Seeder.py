import asyncio
import json
import time
import random
import string
import uuid
from PIL import Image, ImageDraw, ImageFont
import secrets
from aiofile import AIOFile, LineReader, Writer


class Seeder:
  #default password for ion_auth,laravel and django
  #ion auth:: password :: $2y$08$200Z6ZZbp3RAEXoaWcMA6uJOFicwNZaqk4oDhqTUiFXFe63MG.Daa
  #laravel:: JohnDoe :: $2y$10$jSAr/RwmjhwioDlJErOk9OQEO7huLz9O6Iuf/udyGbHPiTNuB3Iuy 
  #laravel source: https://stackoverflow.com/questions/22846897/how-to-create-a-laravel-hashed-password
  #django:: 666monkeysAndDogs777 :: pbkdf2_sha256$20000$L7uq6goI1HIl$RYqywMgPywhhku/YqIxWKbpxODBeczfLm5zthHjNSSk=
  #django: source :: https://codeday.me/en/qa/20190312/3420.html
  #validate excel file i.e sms numbers columns, empty spaces,unformatted numbers etc

    def firstname(self):
    async with AIOFile("file.csv", 'r') as afp:
        async for line in LineReader(afp):
            #print(line[:10])
            array = line.split(',')
            first_item = array[0]
            print(first_item)

    def lastname(self):
    async with AIOFile("file.csv", 'r') as afp:
        async for line in LineReader(afp):
            #print(line[:10])
            array = line.split(',')
            first_item = array[0]
            print(first_item)

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
