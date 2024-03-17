## Instructions for running the project

### 1. Get the TPC-C project running
Navigate to Project-2 folder and get the repository:

`
git clone https://github.com/AgilData/tpcc.git
`

Open the project seperately in IntelliJ and run the stuff it tells you to do.
So you would eventually be able to run the following command there:

`
mvn package assembly:single
`

Note: Use SDK version 1.8 (conflicts with other stuff otherwise)

Note: the repository is mounted to docker, so the .sql files in the next step should
be already in the docker machine.

### 2. Run MySQL in docker
In this folder, run:

`
docker compose up -d
`

### 3. Logging into mySQL server
Log into the docker running the MySQL:

`
docker exec -it Mysql bash -l
`

Enter the MySQL CLI inside the docker 

`
mysql -u root -p
`

(root is required to be the user, otherwise you get something like this:  
`Access denied for user 'root'@'localhost'`)

### 4. Creating the database

Now run:

`
create database tpcc;
`

`
use tpcc;
`

`
source /storage/tpc/sql/create_tables.sql
`

`
source /storage/tpc/sql/add_fkey_idx.sql
`

### 4. Loading the data

Before running, edit the following lines in `tpcc.properties` file:

```
DRIVER=com.mysql.cj.jdbc.Driver
JDBCURL=jdbc:mysql://127.0.0.1:3307/tpcc?useSSL=false&serverTimezone=UTC&autoReconnect=true
PASSWORD=password
```

In IntellIJ, navigate to `src.main.java.TpccLoad.java` file. Run it.

### 5. Running the test

In IntellIJ, navigate to `src.main.java.Tpcc.java` file. Run it.