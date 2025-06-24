### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Important Note
You must have [MySQL](https://dev.mysql.com/downloads/) downloaded and a database setup before using the server.
### Configuration
In api/dependencies/config.py their contains information you need to edit to connect to your local MySQL instance

You can use what I have there and set up a local enviroment password on your respective machine through the command line (MAC users I am sorry idk how to do that on MAC) or just use a plaintext password either is fine.
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)