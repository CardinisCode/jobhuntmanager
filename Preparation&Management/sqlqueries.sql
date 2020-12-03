CREATE TABLE IF NOT EXISTS 'users' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'username' TEXT NOT NULL, 'hash' TEXT NOT NULL, 'email' TEXT NOT NULL);
CREATE UNIQUE INDEX 'user_id' ON "users" ("id");


INSERT INTO users (username, hash, email)
VALUES ('marypoppins1', 'pbkdf2:sha256:150000$USxcihqi$866e1852c8cc6936a41405ebe2825160f2950b8516fdf18c2eaa603b2d54c134', 'marypoppins@gmail.com');

"INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", (username, hashed_password, email))

ALTER TABLE users ADD date datetime;


