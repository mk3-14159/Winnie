# Winniepot 

``` _     _  ___   __    _  __    _  ___   _______  _______  _______  _______ 
| | _ | ||   | |  |  | ||  |  | ||   | |       ||       ||       ||       |
| || || ||   | |   |_| ||   |_| ||   | |    ___||    _  ||   _   ||_     _|
|       ||   | |       ||       ||   | |   |___ |   |_| ||  | |  |  |   |  
|       ||   | |  _    ||  _    ||   | |    ___||    ___||  |_|  |  |   |  
|   _   ||   | | | |   || | |   ||   | |   |___ |   |    |       |  |   |  
|__| |__||___| |_|  |__||_|  |__||___| |_______||___|    |_______|  |___|  

NUIG FYP Honeypot Group (Coordinator: Martin Hughes) 
(c) MK Chong 2022
```

Winniepot is an open-source software in Python language which designed for creating virtual traps to secure your organisation! This project is compatible with Python 3.x and tested on Mac OS X, and [Linux](https://github.com/zdresearch/OWASP-Honeypot/actions).

### API Actions & WebUI
* We are still in development phase of the web UI
* To run API Server with default configurations visit our [website](https://deciphe.rs/)
* Deploy Winniepot at your own risk

### Usage:
* To deploy a winniepot instance

```sh
python winniepot.py
```

* To run dockerized API on host, use the command given below

```sh
docker-compose -f docker-compose-host.yml up
python winniepot.py
```
