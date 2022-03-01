# MaisTODOS Wallet API

This is the technical challenge for join MaisTODOS company as a Dev. It consist in build a intermediate API to calculate cashback.

## EXPLICAÇÃO DAS DECISÕES

  Usei Django REST framework para desenvolver este API porque o mesmo é acoplado ao django, dessa forma as validações dos valores dos campos ficam por canto do django.
  Conta-se com grande poder do django e do django REST framework para criar apps e APIs de qualquer complexidade.

  Este par permite criar API com rapidez (não foi no meu caso, mas teria sido sim, se tivesse 100% dedicado a isso), segurança, escalabilidade e performance.

  Outro motivo é porque trata-se de tecnologias modernas amplamente utilizadas em grandes, médias e peguenase empresas ( vê-se pelas vagas no Linkedin e outros sires de emprego).

  Defini 2 produtos: DIAMANTE e OURO
  Apliquei o desconto por produto:

      DISCOUNT = {
          'DIAMANTE': 5,  # 5%
          'OURO': 3       # 3%
      }


## STEPS TO RUN THIS APP LOCALY

### 0 | Clone the remote repository to start testing

     git clone https://github.com/idelfrides/MaisTODOS_wallet_api.git

### 1 | Navegate until your project folder

    use command: cd FOLDER_NAME

### 2 | Create your virtualenv like

     virtualenv [your_venv_name]

### 3 | Virtualenv activation

     source [your_venv_name]/bin/activate

If you are using fish, write

     source [your_venv_name]/bin/activate.fish

### 4 | Install requirements

     pip install -r requirements.txt

### 5 | Migrate the models to create tables

     python manage.py migrate

### 6 | Create your superuser

     python manage.py createsuperuser

### 7 | Now you can run the application

     python manage.py runserver

### 8 | Now you gonna need to make authentication by some  client as INSOMNIA OR POSTMANT

    Use endpoint: http://127.0.0.1:8000/api-token-auth/
    Method: POST
    Body:
    {
      "username": "YOUR_USERNAME',
      "password": "YOUR_PASSWORD'
    }

    The response will be a TOKEN of your permission to make requests to this API. Copy it.

### 9 | Use the token you got in Header to performe request, like this

    HEADER

    {
      Authorization: Token YOUR_TOKEN,
      Content-Type: application/json
    }

### 10 | At this point you are able to create customers and products. You can do it via django Admin or by performing a POST reques using INSOMNIA as I Do. Also, you can use browseble API of django REST framework.

    BY REQUEST ON CUSTOMER:

     - ENDPOINT: http://127.0.0.1:8000/wallet/api/v1/customer/
     - Method: POST
     - To know fields , performe OPTIONS request on that endpoint, then you can make a POST request
     - Body:
     {
       "field": "value", ...
     }

    ---------

    BY REQUEST ON PRODUCT:

     - ENDPOINT: http://127.0.0.1:8000/wallet/api/v1/product/
     - Method: POST
     - To know fields, performe OPTIONS request on that endpoint, then you can make a POST request
     - Body:
     {
       "field": "value", ...
     }

     
     Browseble API 
     Link:  https://www.django-rest-framework.org/
     

### 11 | Now you can performe cashback request to API. See an example:

    REQUEST cashback:

     - ENDPOINT: http://127.0.0.1:8000/wallet/api/v1/redevaregista/cashback/,
     - Method: POST
     - To know fields , performe OPTIONS request on that endpoint, then you can make a POST request
     - Body:

        {
	   "name": "teste com dados deles insomnia 9",
           "sold_at": "2022-02-25 07:00:00",
           "customer": {
             "document": "027.419.227-64",
             "name": "SEMEAO"
           },
           "total": "108",
           "product": [
             {
                "productCode": "96321"
             },
             {
	        "productCode": "9874"
	     },
             {
	        "productCode": "987478"
	     }
          ]
        }

### 12 | WARNING:  
	'document' and 'productCode' values have to be one of customer/product you created at STEP 10.

### REFERENCES/TOOLS OR SITES

  1 - The Django Framework

    Link: https://www.djangoproject.com/

  2 - Django REST Framework

    Link:  https://www.django-rest-framework.org/

  3 - Draw.oi

    To create UML for this API , I used draw.io app.
    Access this app below

    Link:  https://app.diagrams.net/

  4 - Django CPF validation

    Link : https://pypi.org/project/django-cpf/
