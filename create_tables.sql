CREATE TABLE income(id integer primary key AUTOINCREMENT, date text not NULL, category text not null, amount INT not null);
CREATE TABLE investments(id integer primary key AUTOINCREMENT, date text not NULL, category text not null, amount INT not null);
CREATE TABLE purchases(id integer primary key AUTOINCREMENT, date text not NULL, card text not null, amount int not null, description text not null, category text not null);

