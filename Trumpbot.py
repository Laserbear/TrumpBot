from responses import respond
import socket

#connection details
bot_owner = "Laserbear"
nick = "DonaldTrump"
chan = "#TrumpBot"
sock = socket.socket()
sock.connect(("irc.foonetic.net",6667))
sock.send("USER " + nick + " 0 * :" + bot_owner + "\r\n")
sock.send("NICK " + nick + "\r\n")

replied = 0
while 1:
	replied = 0
	data = sock.recv(1024)
	print data
	if data[0:4] == "PING":
		sock.send(data.replace("PING", "PONG"))
	if data[0]!=':':
		continue
	if data.split(" ")[1] == "001":
		sock.send("MODE " + nick + " +B\r\n")
		sock.send("JOIN " + chan + "\r\n")
	elif data.split(" ")[1] == "PRIVMSG" '''and data.split(":")[2].startswith(nick)''':
		if respond(data) != "NULL":
			sock.send(respond(data))
