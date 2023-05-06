from flask import Flask
app = Flask(__name__)



@app.route("/")
def home():
     return """<html>
         <head><title>Home</title></head>
          <body style="background:#FDFEFE;">
            <h1 align='center'>Welcome Home!</h1>
             </br>
              <div class="container">
                <form action="/login" method="POST">
                  Username:<input type ="text", placeholder="Username">

                   Password:<input type ="password", placeholder="Password">


                    <button type="submit">Login</button>
                 </form>
              </div>
        </body>
     </html>"""





@app.route("/login")
def login():
     username = request.args["username"]
     password = request.args["password"]

     if username != "" and password !="" :
         return "<h1>" + str("Logged in successfully!") + "</h1>"
     elif username == "":
         return "<h1>" + str("Please enter valid credentials.") + "</h1>"
     elif password == "":
         return "<h1>" + str("Please enter valid credentials.") + "</h1>"
     else:
         return "<h1>" + str("Invalid Credentials!!") + "</h1>"






if __name__ == "__main__":
	app.run()