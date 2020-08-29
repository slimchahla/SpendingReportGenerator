CREATE TABLE transaction_types(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);

CREATE TABLE categories(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, type INT NOT NULL,
                        FOREIGN KEY (type) REFERENCES transaction_types (id));

CREATE TABLE payment_method(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);

CREATE TABLE income(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, category INTEGER NOT NULL,
                    amount INT NOT NULL, FOREIGN KEY (category) REFERENCES categories (id));

CREATE TABLE investments(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, category TEXT NOT NULL,
                         amount INT NOT NULL, FOREIGN KEY (category) REFERENCES categories (id));

CREATE TABLE purchases(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, method INTEGER NOT NULL,
                       amount INT NOT NULL, description TEXT NOT NULL, category INT NOT NULL,
                       FOREIGN KEY (method) REFERENCES payment_method (id),
                       FOREIGN KEY (category) REFERENCES categories (id));
