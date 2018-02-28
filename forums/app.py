from flask import Flask, render_template
import models
import stores

app = Flask(__name__)
post_store = stores.PostStore()
post_store.add(models.Post("Life", "Life is alawys great"))
post_store.add(models.Post("Sunshine", "Sunshine is amazing"))
@app.route("/")
@app.route("/index")
def home():
	return render_template(	"index.html", posts = post_store.get_all())
		
app.run()