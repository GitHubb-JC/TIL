-- 테이블 만들기
CREATE TABLE healthcare (
  id PRIMARY KEY,
  sido INTEGER NOT NULL,
  gender INTEGER NOT NULL,
  age INTEGER NOT NULL,
  height INTEGER NOT NULL,
  weight INTEGER NOT NULL,
  waist REAL NOT NULL,
  va_left REAL NOT NULL,
  va_right REAL NOT NULL,
  blood_pressure INTEGER NOT NULL,
  smoking INTEGER NOT NULL,
  is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare


-- D01 ------------------------------
-- D01 ------------------------------
-- D01 ------------------------------

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);

.tables

.schema classmates

DROP TABLE classmates;

CREATE TABLE classmates(
  name TEXT,
  age INT,
  address TEXT
);

INSERT INTO classmates (name, age) VALUES ("홍길동", 23);

INSERT INTO classmates (name, age, address) VALUES ("홍길동", 23, "서울");

CREATE TABLE classmates(
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates VALUES ("홍길동", 30, "서울");

INSERT INTO classmates(name, age, address) VALUES 
("홍길동", 30, "서울"),
("김철수", 30, "제주"),
("이호영", 26, "인천"),
("박민희", 29, "대구"),
("최혜영", 28, "전주");


SELECT rowid, name FROM classmates LIMIT 1;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT rowid, name FROM classmates WHERE address="서울";

SELECT DISTINCT * FROM classmates;

SELECT COUNT(*) FROM healthcare WHERE age < 10;

SELECT COUNT(*) FROM healthcare WHERE gender=1;

SELECT COUNT(*) FROM healthcare WHERE smoking=3 AND is_drinking=1;

SELECT COUNT(*) FROM healthcare WHERE va_left>=2.0 AND va_right>=2.0;

SELECT COUNT(DISTINCT sido) FROM healthcare;

-- D02 ------------------------------
-- D02 ------------------------------
-- D02 ------------------------------

SELECT COUNT(*) FROM healthcare;

SELECT MAX(age), MIN(age) FROM healthcare;

SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;

SELECT COUNT(*) FROM healthcare WHERE 160 <=height and height<= 170;

SELECT waist FROM healthcare WHERE is_drinking=1 AND waist != '' ORDER BY waist DESC LIMIT 5;

SELECT COUNT(*) FROM healthcare WHERE (va_left>=1.5 AND va_right>=1.5) AND is_drinking=1;

SELECT COUNT(*) FROM healthcare WHERE blood_pressure<120;

SELECT AVG(waist) FROM healthcare WHERE blood_pressure>=140;

SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender=1;

SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;

SELECT COUNT(*) FROM healthcare WHERE (weight/((height * 0.01) * (height * 0.01))) > 30;

SELECT 
  id, 
  (weight/((height * 0.01) * (height * 0.01))) AS BMI
FROM healthcare WHERE smoking = 3 
ORDER BY (weight/((height * 0.01) * (height * 0.01))) DESC LIMIT 5;

-- D03 ------------------------------
-- D03 ------------------------------
-- D03 ------------------------------

SELECT smoking, count(*) FROM healthcare WHERE smoking != "" GROUP BY smoking;

SELECT is_drinking, count(*) FROM healthcare WHERE is_drinking != "" GROUP BY is_drinking;

SELECT is_drinking, count(*) AS "blood_pressure >= 200"
FROM healthcare 
WHERE blood_pressure >= 200 AND blood_pressure != "" GROUP BY is_drinking;

SELECT sido, count(*) AS "인구수" 
FROM healthcare 
WHERE
  (SELECT sido, count(*) FROM healthcare GROUP BY sido)
GROUP BY sido;