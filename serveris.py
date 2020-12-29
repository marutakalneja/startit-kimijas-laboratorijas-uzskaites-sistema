from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Labrīt!!!"

#izveidot route "/sveiki", kas atgriež tekstu "Nav vairs nekāds rīts!"
@app.route("/sveiki")
def sveiki():
  return "Nav vairs nekāds rīts!"

#izveidot route "/sveiki/<vards>", kas izmanto mainīgo vards, lai atgrieztu personalizētu sveicienu, piemēram, ja vards ir Māris, tad atgriež tekstu "Sveiki, Māris!"

@app.route("/sveiki/<vards>") #tiek ielikts iekavās parametrs vai f"Sveiki {vards}"
def sveikiPersona(vards):
  return "Sveiki {}".format(vards)

#izveidot route "/cik2/<reizinamais>", kas izmanto mainīgo reizinamais un aprēķina un atgriež dotā skaitļa reizinājumu ar 2. Ievērot, ka jāatgriež ir string datu tips
@app.route("/cik/<sk1>/<sk2>")
def reizinajums(sk1, sk2):
  sk1=int(sk1)
  sk2=int(sk2)
  reizinajums=sk1*sk2
  return str(reizinajums)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
