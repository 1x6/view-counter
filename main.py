import os
from flask import Flask, send_file, redirect
from PIL import Image, ImageFont, ImageDraw 
import pymongo

app = Flask(__name__)
myclient = pymongo.MongoClient("mongo_db_link")
mydb = myclient["counter"]
mycol = mydb["counter"]

@app.route('/')
def index():
    return redirect("https://github.com/1x6/view-counter, 302)

@app.route("/counter.png", methods=["GET"])
def view():

    for x in mycol.find():
        amnt = x['amount']

    myquery = {"amount": amnt}
    amount = amnt + 1
    newvalues = { "$set": { "amount": amount } }

    mycol.update_one(myquery, newvalues)

    for x in mycol.find():
        amnt = x['amount']

    W, H = (100,18)
    my_image = Image.open("Untitled.png")
    
    title_font = ImageFont.truetype('SpaceMono-Regular.ttf', 15)
    
    title_text = str(amnt) + " views"
    
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(title_text, font=title_font)
    image_editable.text(((W-w)/2,(H-h)/2), title_text, (0,0,0), font=title_font, )
    
    my_image.save("result.png")

    return send_file("result.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
