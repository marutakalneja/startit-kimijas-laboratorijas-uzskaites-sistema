from flask import Flask, jsonify
import dati

app = Flask(__name__)

app.config["JSON_AS_ASCII"]=False #džeisonu nevajag apstrādāt ar šo kodu tabulu

@app.route('/')
def index():
  return "Labrīt!"

#izveidot route /api/v1/vielas, kas atgriež visus piemēra datus, kas atrodami datnē dati.py mainīgajā vielas. Ievērot, ka jāatgriež ir string datu tips

@app.route("/api/v1/vielas")
def vielas():
  return jsonify(dati.vielas) # ja jāatgriež džeison dati, tad izmanto jsonify

#izveidot route /api/v1/viela/<vielasID>, kas atgriež datus par vielu ar ID <vielasID>, kas atrodami datnē dati.py mainīgajā vielas. Ievērot, ka jāatgriež ir string datu tips

@app.route("/api/v1/viela/<vielasID>")
def viela(vielasID):

  viela=f"Viela ar doto id {vielasID} nav atrasta"

  for v in dati.vielas:
    if str(v["id"])==vielasID:
      viela=v
  
  return jsonify(viela)

#izveidot route /api/v1/inventars, kas atgriež visus piemēra datus, kas atrodami datnē dati.py mainīgajā inventars

@app.route("/api/v1/inventars")
def inventars():
  return jsonify(dati.inventars)
