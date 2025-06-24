import os
class conf:
    db_host = "localhost"
    db_name = "sandwich_maker_api"
    db_port = 3306
    db_user = "root"
    """To set enviroment variables on . . .
        BASH - export SQL_DB_PASSWORD="your_secret_password"
        Windows (CMD) - set SQL_DB_PASSWORD=your_secret_password
        Windows (Powershell) - $env:SQL_DB_PASSWORD = "your_secret_password"

        This prevents hardcoding your SQL password.
    """
    db_password = os.getenv("SQL_DB_PASSWORD")
    app_host = "localhost"
    app_port = 8000