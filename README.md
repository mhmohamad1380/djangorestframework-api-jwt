<div  align="center">
<h1  align="center">Dockerized Django Rest Framework with JWT and Sending Email Whenever a new Post Create Using Celery</h1>
</div>

## Installation

1. first, You should clone this Repository.<br/>
2. delete the txt file exists in db folder
3. at the third step, go to the Cloned Directory, then Open Terminal(CMD). <br/>
4. then, type ```docker-compose up --build ``` and Press Enter. (tip: make sure that Docker and Docker-Compose is Installed on Your Machine)
5. tip: username is ``` admin ``` and password is ``` admin ```

## Routes

1. ```api/shop/list``` Provides a List of Shop Items <br/>
2. ```api/shop/retrieve-destroy/<pk>``` for getting an Item and Destoy it or Not <br/>
3. ```api/token/``` send a POST method (You Can Use PostMan) to this page and send username and password to get a Token <br/>
4. ```api/token/refresh/``` send a POST method (You Can Use PostMan) to this page and send refresh token to get a New Token <br/>


### Good Luck
