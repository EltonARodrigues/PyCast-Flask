# PyCast-Flask

## Install

install requirements with pip:
```pip 3 install -r requirements.txt```

##  Configure database:

Change mysql URI in config file:

ex: ``` 'mysql://root:root@localhost/pycastdb' ```

```
flask db init
flask db migrate
flaskdb upgrade
```

# Run

``` python3 run.py ```

# Images

![Pycast home](images/pycast1.png)

![Pycast epsodes](images/pycast2.png)