import sqlite3

def getbalance(msid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select balance from users WHERE id = {msid}")
	balancenow = cur.fetchone()[0]
	con.commit()

	return balancenow

def deleteoplata(msid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"DELETE FROM oplata WHERE id = {msid}")
	con.commit()

def getstatus(msid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select status from users WHERE id = {msid}")
	statusgame = cur.fetchone()[0]
	con.commit()

	return statusgame




