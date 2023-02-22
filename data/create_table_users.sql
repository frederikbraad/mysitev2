DROP table IF EXISTS users;

CREATE TABLE users(
  id        TEXT,
  username  TEXT,
  name      TEXT,
  last_name TEXT,
  total_following TEXT,
  total_followers TEXT,
  total_tweets  TEXT,
  avatar  Text,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;


INSERT INTO users VALUES("9b8b2400bc474c6ea66be6262b2eaccc", "elonmusk", "Elon", "Musk", "177", "128900000", "22700", "9b8b2400bc474c6ea66be6262b2eaccc.jpg");
INSERT INTO users VALUES("72d0e822cb2b4848afd83c5e0cb17108", "shakira", "Shakira", "musk", "235", "53700000", "7999", "72d0e822cb2b4848afd83c5e0cb17108.jpg");
INSERT INTO users VALUES("497434dc1eea409399404b9bc04745df", "larsloekke", "Lars", "Løkke Rasmussen", "559", "216100", "5052", "497434dc1eea409399404b9bc04745df.jpg");



