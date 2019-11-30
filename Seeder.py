import asyncio
import json
import time
import random
import secrets
from datetime import datetime
import string
import uuid
from PIL import Image, ImageDraw, ImageFont
from aiofile import AIOFile, LineReader, Writer


class Seeder:


  #default password for ion_auth,laravel and django
  #ion auth:: password :: $2y$08$200Z6ZZbp3RAEXoaWcMA6uJOFicwNZaqk4oDhqTUiFXFe63MG.Daa
  #laravel:: JohnDoe :: $2y$10$jSAr/RwmjhwioDlJErOk9OQEO7huLz9O6Iuf/udyGbHPiTNuB3Iuy 
  #laravel source: https://stackoverflow.com/questions/22846897/how-to-create-a-laravel-hashed-password
  #django:: 666monkeysAndDogs777 :: pbkdf2_sha256$20000$L7uq6goI1HIl$RYqywMgPywhhku/YqIxWKbpxODBeczfLm5zthHjNSSk=
  #django: source :: https://codeday.me/en/qa/20190312/3420.html
  #validate excel file i.e sms numbers columns, empty spaces,unformatted numbers etc

    async def firstname():
        async with AIOFile("surnames.csv", 'r') as afp:
            async for line in LineReader(afp):
            #print(line[:10])
               array = line.split(',')
               first_item = array[0]
               print(first_item)

    async def lastname():
        async with AIOFile("surnames.csv", 'r') as afp:
            async for line in LineReader(afp):
            #print(line[:10])
               array = line.split(',')
               first_item = array[0]
               print(first_item)

    def salutation(self):
        salut = ['Mr', 'Mrs', 'Ms', 'Dr', 'Sir']
        return secrets.choice(salut)

    def gender(self):
        g = ['Female', 'Male']
        return secrets.choice(g)

    def coordinates(self):
        print("Hello my name is " + self.name)

    def image():
        img = Image.new('RGB', (random.randrange(211,255), random.randrange(122,255)), color = (random.randrange(0,250), random.randrange(21,76), random.randrange(160,255)))
    
        #fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
        d = ImageDraw.Draw(img)
        rn = secrets.token_urlsafe(10)
        d.text((10,10), rn, fill=(random.randrange(200,255), random.randrange(100,255), random.randrange(50,255)))
        image_name = 'username'+rn
        img.save(image_name+'.png')

    def telephone_number(self):
        return random.randrange(1234567890, 9234567890)
    #str_join('Pine', 'apple', 3)  # Returns : Pineapple3

    def country(self):
        country = ['UK', 'France', 'Ireland', 'Holland', 'Belgium','Canada']
        return secrets.choice(country)

    def unix_timestamp(self):
        print("Hello my name is " + self.name)

    def date_of_birth(self):
        print("Hello my name is " + self.name)
    #1987 to 2000
    
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
        em = random.randrange(123456789011, 923456789011)
        return str_join(em, '@', '126.com') 
    #126.com

    def django_password(self):
        return 'pbkdf2_sha256$20000$L7uq6goI1HIl$RYqywMgPywhhku/YqIxWKbpxODBeczfLm5zthHjNSSk='

    def paragraph(self):
        print("Hello my name is " + self.name)

    def credit_card_number(self):
        return random.randrange(1234567891011121, 9934567891011121)

    def cvv(self):
        return random.randrange(211, 999)

    def day(self):
        return random.randrange(1, 30) 

    def month(self):
        return random.randrange(1, 12) 

    def year(self):
        return random.randrange(1987, 2000) 

    def username(self):
        print("Hello my name is " + self.name)

    def random_string(self):
        print("Hello my name is " + self.name)

    def postal_code(self):
        return random.randrange(10001, 90001) 

    def json_object(self):
        x = {
          "name": "John",
          "age": 30,
          "married": True,
          "divorced": False,
          "children": ("Ann","Billy"),
          "pets": None,
          "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
          ]
        }
    
        print(json.dumps(x))

    def random_list_item():
        cards = ['Visa', 'Mastercard', 'Diners', 'China Union']
        return secrets.choice(cards)
               
    def laravel_password():
        return '$2y$10$jSAr/RwmjhwioDlJErOk9OQEO7huLz9O6Iuf/udyGbHPiTNuB3Iuy' 
               
    def ion_auth_password():
        return '$2y$08$200Z6ZZbp3RAEXoaWcMA6uJOFicwNZaqk4oDhqTUiFXFe63MG.Daa' 


start_time = datetime.now()
p1 = Seeder
print(p1.random_list_item())
loop = asyncio.get_event_loop()
foo = loop.run_until_complete(p1.firstname())
print(foo)
p1.image()
#check for actors in async
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))