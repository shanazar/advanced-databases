set search_path = "sales_info";
-- 2.a
INSERT INTO customer(Name, Phone) values ('Alice','002736014251');

insert into product(BareCode, Label, Category, Stock) values
                    ('AAA001', 'Wood Chair', 'House', 10),
                    ('AAA002', 'Iron bed', 'House', 5),
                    ('AAA003', 'Mathematics Book', 'Education', 2),
                    ('AAA004', 'Couch', 'House', 2);

-- 2.b
-- Insert into Invoice table
INSERT INTO Invoice (DateInv, ModePay, Status) VALUES
    (CURRENT_DATE, 'Card', 'Not Paid');

-- Assuming IdCust = 1 and IdInv = 1
-- Insert into OrderC table
INSERT INTO OrderC (DateOrd, StatusOrd, IdCust, IdInv) VALUES
    (CURRENT_DATE, 'Pending', 1, 1);

-- Assuming IdOrd = 1
-- Insert into OrderLigne table
INSERT INTO OrderLigne (Quantity, StatusOrLig, IdOrd, BareCode) VALUES
                                                                    (5, 'Preparation', 1, 'AAA001'),  -- Wood Chair
                                                                    (4, 'Preparation', 1, 'AAA003'),  -- Mathematics Book
                                                                    (1, 'Preparation', 1, 'AAA004');  -- Couch

-- Update the Invoice for payment by cash
UPDATE Invoice
SET ModePay = 'Cash'
WHERE IdInv = 1;


