import sqlite3 as sql


def addEvent(id, event_name, date, ticket_cnt):
    con = sql.connect("database.db", timeout=10)
    cur = con.cursor()
    cur.execute("INSERT INTO events (id, event_name, evedate, ticket_cnt) VALUES (?,?,?,?)", \
               (id, event_name, date, ticket_cnt))
    con.commit()
    con.close()

def getEvent(id):
	eveData = ""
	con = sql.connect("database.db", timeout=10)
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM events where id = ?", (id,))
	eveData = cur.fetchall()
	con.close()
	return eveData
	
def updateEvent(id, cnt):
	con = sql.connect("database.db", timeout=10)
	cur = con.cursor()
	cur.execute("UPDATE events SET ticket_cnt = ? WHERE id = ?", (cnt, id,))
	con.commit()
	con.close()
	return "Success"



