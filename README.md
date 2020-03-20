# Funny Internet Portal
Repo for CUBigDataClass Project Team 16

### Group Members:
- [Jay Patel](https://github.com/jaykpatel1996)
- [Pradyoth Srinivasan](https://github.com/Pradyoth)
- [Vandana Sridhar](https://github.com/vandana28)
- [Ray Shash](https://github.com/Blackbird002)

# Installation Steps

## Ubuntu 18.04:

Install Node.js
```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Update npm (Node package manager)
```
sudo npm install npm@latest -g
```

Install Create-React-App Tool
```
sudo npm install -g create-react-app
```

Install Pip package management system 
```
sudo apt update

sudo apt install python3-pip

```

Pip Usage Reference (don't type this in):
```
python3 -m pip install <packageName>
```

Install **MongoDB Community Edition** & Driver (pymongo):
- [Ubuntu MongoDB Install](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

- [MongoDB Python Driver Reference](https://api.mongodb.com/python/current/tutorial.html)

```
python3 -m pip install pymongo
```

Install python3-venv
```
sudo apt-get install python3-venv
```

Create a Python virtual enviroment called "venv" (in api folder - where Flask source will be)
```
cd api
python3 -m venv venv
```

Activate to enviroment (called venv):
```
. venv/bin/activate
```

Install Flask & [python-dotenv](https://pypi.org/project/python-dotenv/):
```
python3 -m pip install flask
python3 -m pip install python-dotenv
```

Required Python packages for [**twitterscraper**](https://github.com/taspinar/twitterscraper)
```
python3 -m pip install twitterscraper
```

Install [yarn](https://classic.yarnpkg.com/en/docs/install/#debian-stable):
```
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -

echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt update && sudo apt install yarn

```

# Run project

Activate to enviroment (called venv):
```
cd api
. venv/bin/activate
```

Start MongoDB:
```
sudo systemctl start mongod
```

**In react-flask-app directory:**

Start Flask (back-end):
```
yarn start-api
```

Start React (front-end):
```
yearn start
```