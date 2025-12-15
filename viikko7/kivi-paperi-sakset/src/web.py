from flask import Flask, render_template, request, redirect, url_for
import uuid

from pelilogiikka.tuomari import Tuomari
from tekoaly.tekoaly import Tekoaly
from tekoaly.tekoaly_parannettu import TekoalyParannettu

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-for-local"

# In-memory games storage: {game_id: state}
# state = {mode: 'a'|'b'|'c', tuomari: Tuomari(), tekoaly: obj, last_moves: [(eka,toka), ...]}
GAMES = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new_game():
    mode = request.form.get("mode")
    if mode not in ("a", "b", "c"):
        return redirect(url_for("index"))

    game_id = str(uuid.uuid4())
    state = {"mode": mode, "tuomari": Tuomari(), "history": []}

    if mode == "b":
        state["tekoaly"] = Tekoaly()
    elif mode == "c":
        state["tekoaly"] = TekoalyParannettu(10)

    GAMES[game_id] = state
    return redirect(url_for("play", game_id=game_id))

@app.route("/play/<game_id>", methods=["GET"]) 
def play(game_id):
    state = GAMES.get(game_id)
    if not state:
        return redirect(url_for("index"))

    return render_template(
        "play.html",
        game_id=game_id,
        history=state["history"],
        tuomari=state["tuomari"],
        mode=state["mode"],
        finished=state.get("finished", False),
        winner=state.get("winner", None),
    )

@app.route("/move/<game_id>", methods=["POST"])
def move(game_id):
    state = GAMES.get(game_id)
    if not state:
        return redirect(url_for("index"))

    eka = request.form.get("move")
    if eka not in ("k", "p", "s"):
        return redirect(url_for("play", game_id=game_id))

    mode = state["mode"]
    if mode == "a":
        # player vs player: second player's move provided in form
        toka = request.form.get("second_move")
        if toka not in ("k", "p", "s"):
            # wait for second player's move; redirect back
            return render_template("play.html", game_id=game_id, history=state["history"], tuomari=state["tuomari"], mode=mode, need_second=True, first_move=eka)
    else:
        tekoaly = state.get("tekoaly")
        if tekoaly is None:
            return redirect(url_for("index"))
        toka = tekoaly.anna_siirto()
        # if improved ai, inform it of player's move
        if hasattr(tekoaly, "aseta_siirto"):
            try:
                tekoaly.aseta_siirto(eka)
            except Exception:
                pass

    state["tuomari"].kirjaa_siirto(eka, toka)
    state["history"].append((eka, toka))

    # Check end condition: first to 3 points wins
    if state["tuomari"].onko_loppu(3):
        state["finished"] = True
        v = state["tuomari"].voittaja(3)
        if v == 1:
            state["winner"] = "Ensimmäinen pelaaja"
        elif v == 2:
            state["winner"] = "Toinen pelaaja"
        else:
            state["winner"] = "Tasapeli"

    return redirect(url_for("play", game_id=game_id))

if __name__ == "__main__":
    import socket
    from werkzeug.serving import make_server

    # choose a free port starting from 5000
    port = 5000
    s = socket.socket()
    while True:
        try:
            s.bind(("127.0.0.1", port))
            s.close()
            break
        except OSError:
            port += 1

    print(f"Starting web app on http://127.0.0.1:{port}")
    app.run(port=port)
