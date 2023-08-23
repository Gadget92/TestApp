Создайте django проект. 
Стек - django4, django REST framework, docker-compose, postgresql, nginx, gunicorn.
Приложение должно разворачиватся командами - docker-compose build, docker-compose up.

-----------------------------------------------

Структура.
...
- apps
   - Accounts
   - Catalog
- settings
- manage.py
...

Приложение Accounts.
Создайте модель пользователя, основным индефикатором пользователя должна быть почта а не username.
Авторизация в приложении должна быть по полям - email, password. 

Приложение Catalog.
 - class Product
    - name (str)
   
 - class Filial
    - name (str)
    - region (int)
   
- class Characterictic
    - self (ForeignKey -> Characterictic) 
    - name (str)
  - product_id (ManyToManyField <- Product)
   
 - class FilialPrice
    - product_id (ForeignKey -> Product)
  - filial_id (ForeignKey -> Filial)
  - price (int)

-------------------------------------------------------

Реализуйте роуты и предоставления для них, желательно с помощью rest_framework.decorators.action в одном классе.
catalog/?filial=<id> список объектов Product + стоимость
catalog/<product_id>/?filial=<id> данные объекта Product + стоимость
catalog/<product_id>/price/?filial=<id> данные объекта FilialPrice
catalog/<product_id>/characterictic/  все связанные с этим товаром характеристики

Все модели должны иметь сериализаторы.
Сериализаторы должны поддерживать создание и обновление объектов.

Предоставление может получать параметры - id филиала и характеристики catalog/?filial=<id>&characteristic=<id>
Возвращать - товары с стоимостью в этом филиале, фильтровать список по характеристике