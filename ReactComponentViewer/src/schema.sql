CREATE TABLE users(
  id INTEGER NOT NULL PRIMARY KEY,
  username TEXT,
  password TEXT
);

CREATE TABLE components(
  id INTEGER NOT NULL PRIMARY KEY,
  owner_id INTEGER,
  component TEXT
);

INSERT INTO users (username, password) VALUES ('root', 'root');