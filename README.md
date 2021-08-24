# mcart-test
## FASTAPI CRUD application.
REST API application for exchange rate.<br>

### Stack of technologies:<br>
-Python >= 3.9<br>
-FastApi<br>
-linter: Black<br>

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
The key features are: fast to code, based on the open standards for APIs,
very high performance, minimize code duplication.

### Basic functionality:<br>
1.Web REST API<br>
2.Getting list of currencies of the world.<br>
3.Getting the difference in the exchange rate (ruble) between two dates.<br>

### APIs endpoints:<br>
| requests | url | description  |
| ------- | --- | --- |
| GET | /currency/all | list of currencies of the world |
| GET | /currency/difference| difference in the exchange rate |





## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/MCART-test<br>
$ cd mcart-test<br>

### Build your FastAPI image:
$ docker build -t myimage . <br>

### Run a container based on your image:
$ docker run -d --name mycontainer -p 80:80 myimage <br>





### API from the browser:
You can work on the API directly in your browser.<br>
You will see the automatic interactive API documentation (provided by Swagger UI).
http://127.0.0.1:8000/docs <br>
![Screenshot](https://github.com/SparklingAcidity/MCART-test/blob/in_process/img_for_readme/1.png) <br>
![Screenshot](https://github.com/SparklingAcidity/MCART-test/blob/in_process/img_for_readme/2.png) <br>
or http://127.0.0.1:8000/redoc
![Screenshot](https://github.com/SparklingAcidity/MCART-test/blob/in_process/img_for_readme/3.png)
