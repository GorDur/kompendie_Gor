import ui   # importerar ui och web 
import web
# använder funktioner från ui
ui.line()
ui.header("ARTIST DATABASE")
ui.line()
ui.echo("Welcome to a world of")
ui.echo("Musice!")
ui.line()
ui.echo(" L | List artists")
ui.echo(" V | View artist profile")
ui.echo(" E | Exit application")
ui.line()
s = ui.prompt("Selection")
s
# urlen går genom get funktionen från web
url= "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" 
r = web.get(url)
# om man skriver in L
if s == "L" or s == "l":
    ui.clear()
    ui.line()
    ui.header("ARTIST DATABASE")
    ui.line()
    ui.echo("Ariana Grande")
    ui.echo("Avicii")
    ui.echo("Blink -182")
    ui.echo("Brad Paisley")
    ui.echo("Ed Sheeran")
    ui.echo("Imagine Dragons")
    ui.echo("Maroon 5")
    ui.echo("Scorpions")
    ui.line(True)
    ui.echo("L | List artists")
    ui.echo("V | View artist profile")
    ui.echo("E | Exit application")
    ui.line()
    s = ui.prompt("Selection")
    s
# om man skriver in V
if s == "V" or s == "v":
    ui.clear()
    ui.line()
    ui.header("ARTIST DATABASE")
    ui.line()
    q = ui.prompt("Artist name")
    q
    ui.line(True)
    ui.header(q)
    ui.line(True)
    c = ""
    # den kolar id för artisten vems namn var skriven in
    for S in r["artists"]:
        if (q == S["name"]):
            c = S["id"]
    # använder samma url igen på samma sätt men med artistens id
    url1= "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + c
    r1 =web.get(url1)
    # variabler för genre, aktiva år och medlemar
    e = r1["artist"]["genres"]
    f = r1["artist"]["years_active"]
    h = r1["artist"]["members"]
    # toma variabler
    i=""
    i1=""
    i2=""
    # varje tom variabel får alla värden fårn genre, aktiva år eller medlemar
    for k in e:
        i += k +", "

    for k1 in f:
        i1 += k1 +", "

    for k2 in h:
        i2 += k2 +", "
    # skriver ut resten med genre,aktiva år och medlemar som vi fick nyss
    ui.echo("Genres: " + i) 
    ui.echo("Active: "+ i1)
    ui.echo("Members: " + i2)
    ui.echo("L | List artists")
    ui.echo("V | View artist profile")
    ui.echo("E | Exit application")
    ui.line()
    s
# om man skriver in E
if s == "e" or s == "E":
    ui.clear()
    ui.clear()
    s # tar bort och frågar igen