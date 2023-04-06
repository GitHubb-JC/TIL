CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);



SELECT COUNT(*) FROM users WHERE age LIKE "2_";

SELECT * FROM users WHERE phone LIKE "02%";

SELECT * FROM users WHERE first_name LIKE "%준";

SELECT * FROM users WHERE phone LIKE "%-5114-%";

SELECT * FROM users ORDER BY age LIMIT 10;

SELECT * FROM users ORDER BY age, last_name LIMIT 10;

SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO articles(title, content) VALUES ("1번 제목", "1번 내용");

ALTER TABLE articles RENAME TO news;

ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;

SELECT COUNT(*) FROM users WHERE age LIKE "2_";

SELECT * FROM users WHERE phone LIKE "02%";

SELECT * FROM users WHERE first_name LIKE "%준";

SELECT * FROM users WHERE phone LIKE "%-5114-%";

SELECT * FROM users WHERE phone LIKE "02%";

SELECT * FROM users WHERE first_name LIKE "%준";

SELECT * FROM users WHERE phone LIKE "%-5114-%";