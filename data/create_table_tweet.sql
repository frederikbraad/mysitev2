DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
  id                    TEXT,
  user_fk               TEXT,
  created_at            TEXT,
  message               TEXT,
  image                 TEXT,
  updated_at            TEXT,
  total_retweets        TEXT,
  total_likes           TEXT,
  total_views           TEXT,
  total_replies         TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;

INSERT INTO tweets VALUES("9b8b2400bc474c6ea66be6262b2eaccc", "78ce72cde3d74587a52273368160b7a3", "1676283210", "Hello world", "1.jpg", "1676283211", "5959", "64300", "13000000", "7010");
