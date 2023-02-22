from bottle import default_app, get, post, template, run, view
import git
import sqlite3
import os

# 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

# https://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@github.com/frederikbraad/mysite.git

##############################
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./mysite')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
@get("/")
def _():
  return "Home page"

##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    db = sqlite3.connect(os.getcwd()+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE",(username,)).fetchall()[0]
    # Get the user's id
    user_id = user["id"]
    print("#"*30)
    print(f"user id:{user_id}")
    # With that id, look up/get the respectives tweets
    tweets = db.execute("SELECT * FROM tweets WHERE user_fk=?", (user_id,)).fetchall()
    print("#"*30)
    print(tweets)
    print("#"*30)
    # pass the tweets to the view. Template it
    
    print(user) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
    return template("profile", user=user)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()


##############################
#####
# Run in AWS
try:
    import production
    db = sqlite3.connect("/home/kirederfmloh/mysite/twitter.db")
    print("Server running on AWS")
    application = default_app()

# Run in local computer
except Exception as ex:
    db = sqlite3.connect("twitter.db")
    print("Server running locally")
    run(host="127.0.0.1", port=5781, debug=True, reloader=True)