from python:3.6.4

add requirements.txt /app/
workdir /app
run pip install -r requirements.txt

run curl -sL https://deb.nodesource.com/setup_10.x | bash -
run apt-get install -y nodejs
run npm install --save tcjs

EXPOSE 8000

add . /app
