#!/bin/bash

. .env

export MYSQL_ROOT_PASSWORD
export MYSQL_DATABASE
export MYSQL_USER
export MYSQL_PASSWORD

# Database name
DB_NAME="counter"

# MySQL root user credentials
MYSQL_ROOT_USER="root"
MYSQL_PASSWORD="your_password"

# Create the database
mysql -u ${MYSQL_ROOT_USER} -p -e "CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};"

# Grant privileges to the user
mysql -u ${MYSQL_ROOT_USER} -p -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${MYSQL_USER}'@'%';"
