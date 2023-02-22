from bottle import get, run, template, static_file, response, request
import sqlite3

# This data will come from the database
# For now, we just hard code the data
# 0 False 1 True
tweets = [
    {"image_name":"1.jpg",
     "fullname":"Frederik Holm",
      "username":"fholm",
      "message":"My first tweet",
      "total_messages":"1",
      "total_retweets":"2",
      "total_likes":"3",
      "total_dislikes":"4",
      "verified":1,
      },

          {"image_name":"2.jpg",
     "fullname":"Joe Biden",
      "username":"joebiden",
      "message":"i am your daddy puarh",
      "message_image":"1.png",
      "total_messages":"1",
      "total_retweets":"2",
      "total_likes":"3",
      "total_dislikes":"4",
      "verified":1,
      },

          {"image_name":"1.jpg",
     "fullname":"Frederik Holm",
      "username":"fholm",
      "message":"My first tweet",
      "total_messages":"1",
      "total_retweets":"2",
      "total_likes":"3",
      "total_dislikes":"4",
      "verified":1,
      },

          {"image_name":"1.jpg",
     "fullname":"Frederik Holm",
      "username":"fholm",
      "message":"My first tweet",
      "message_image":"1.png",
      "total_messages":"1",
      "total_retweets":"2",
      "total_likes":"3",
      "total_dislikes":"4",
      "verified":0,
      },

          {"image_name":"1.jpg",
     "fullname":"Frederik Holm",
      "username":"fholm",
      "message":"My first tweet",
      "total_messages":"1",
      "total_retweets":"2",
      "total_likes":"3",
      "total_dislikes":"4",
      "verified":0,
      }
]

# when making dictionary, make more than one {} or else it will loop to the end


#####
# list = array
# dictionary is {}, like a json object


trends = [
    {"title":"One", "total_hash":1},
    {"title":"Two", "total_hash":2},
    {"title":"Three", "total_hash":3},
    {"title":"Four", "total_hash":4},
    {"title":"Five", "total_hash":5}
]

follows = [
    {"follow_img":"1.jpg", "title":"Elon Musk", "username":"elonmusk"},
    {"follow_img":"2.jpg", "title":"Joe Biden", "username":"joebiden"},
    {"follow_img":"3.jpg", "title":"Shakira", "username":"shakira"},
    {"follow_img":"2.jpg", "title":"Elon Musk", "username":"elonmusk"},
    {"follow_img":"1.jpg", "title":"Elon Musk", "username":"elonmusk"}
]

#####

#this is a route

@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
    return static_file(filename, root="./images")

#####

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

#####

@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

#####

@get("/thumbnails/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./thumbnails")

#####

@get("/thumbnails/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./thumbnails")

#####

@get("/app.css")
def _():
    return static_file("app.css", root=".")

#####

@get("/")
def render_index():
    return template("index", title="Twitter", tweets=tweets,
    trends=trends, follows=follows)


#####

@get("/about")
def _():
    return template("about-us", title="About us", tweets=tweets,
    trends=trends, follows=follows)

#####
@get("/contact")
def _():
    return template("contact-us", title="Contact us", tweets=tweets,
    trends=trends, follows=follows)

#####
@get("/explore")
def _():
    return template("explore", title="Explore", tweets=tweets,
    trends=trends, follows=follows)

#####
# API's do not return HTML... there are exceptions
# API returns most likely JSON
# Rule 1 - To test API you use thunderclient or Postman

@get("/api-get-name")
def _():
    try: # Best case scenario

        id = request.query.get("id")
        name = request.query.get("name")
        lastname = request.query.get("lastname")

        if id != "1": raise Exception("The ID is wrong")
        if name != "Frederik": raise Exception("The name is wrong")
        if lastname != "Holm": raise Exception("The lastname is wrong")

        # connect to the database
        db = sqlite3.connect("twitter.db")
        users = db.execute("SELECT * FROM users").fetchall()
        print(users)
        # get the name from the database

        # send the name to the client
        return {"id":id,"name":name, "lastname":lastname}
    except Exception as ex: # Something went wrong
        print(ex)
        # Send a 400 to the client
        response.status=400
        return {"error":str(ex)}
    finally: # It must be done
        # Close the database
        if "db" in locals(): db.close()
        print("I am here")

        
#####
# server="paste" is a back-up plan for web server
run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste") # 65535 amount of ports, amount of integer