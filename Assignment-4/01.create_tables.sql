CREATE SCHEMA sales_info;


set search_path = "sales_info";
-- Create Invoice table
CREATE TABLE Invoice (
                         IdInv SERIAL PRIMARY KEY,
                         DateInv DATE NOT NULL,
                         DatePay DATE,
                         ModePay VARCHAR(50) DEFAULT 'Card' CHECK (ModePay IN ('Check', 'Card', 'Cash')),
                         Status VARCHAR(50) DEFAULT 'Not Paid' CHECK (Status IN ('Paid', 'Not Paid'))
);

-- Create Product table
CREATE TABLE Product (
                         BareCode VARCHAR(50) PRIMARY KEY,
                         Label VARCHAR(100) NOT NULL,
                         Category VARCHAR(50),
                         Stock INT CHECK (Stock > 0)
);

-- Create Customer table
CREATE TABLE Customer (
                          IdCust SERIAL PRIMARY KEY,
                          Name VARCHAR(100) NOT NULL,
                          Phone VARCHAR(20) NOT NULL CHECK (Phone LIKE '00%')
);

-- Create OrderC table
CREATE TABLE OrderC (
                        IdOrd SERIAL PRIMARY KEY,
                        DateOrd DATE NOT NULL,
                        StatusOrd VARCHAR(50) DEFAULT 'Pending' CHECK (StatusOrd IN ('validate', 'Pending', 'Partial')),
                        IdCust INT REFERENCES Customer(IdCust),
                        IdInv INT REFERENCES Invoice(IdInv)
);

-- Create Delivery table
CREATE TABLE Delivery (
                          IdDel SERIAL PRIMARY KEY,
                          DateExp DATE,
                          DateDel DATE
);

-- Create OrderLigne table
CREATE TABLE OrderLigne (
                            IdOrLi SERIAL PRIMARY KEY,
                            Quantity INT NOT NULL CHECK (Quantity > 0),
                            StatusOrLig VARCHAR(50) DEFAULT 'Preparation' CHECK (StatusOrLig IN ('Preparation', 'prepared', 'Supply')),
                            IdOrd INT REFERENCES OrderC(IdOrd),
                            IdDel INT REFERENCES Delivery(IdDel) NULL,
                            BareCode VARCHAR(50) REFERENCES Product(BareCode)
);
