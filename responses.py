# -*- coding: utf-8 -*-
import random
import socket

chan = "#TrumpBot "
def respond(data):
    for word in keywords1:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages1)) + "\r\n"
            break;
    for word in keywords2:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages2))+ "\r\n"
            break;
    for word in keywords3:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages3))+ "\r\n"
            break;
    for word in keywords4:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages4))+ "\r\n"
            break;
    for word in keywords5:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages5))+ "\r\n"
            break;
    for word in keywords6:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages6))+ "\r\n"
            break;
    for word in keywords7:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages7))+ "\r\n"
            break;
    for word in keywords9:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages9))+ "\r\n"
            break;
    for word in keywords10:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages10))+ "\r\n"
            break;
    for word in keywords11:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages11))+ "\r\n"
            break;
    for word in keywords12:
        if word in data:
            return "PRIVMSG " + chan + str(random.choice(messages12))+ "\r\n"
            break;
    return "NULL"

keywords1 = ["america", "usa", "united states", "the us", "jobs", "economy"]
messages1 = ["When was the last time anybody saw us beating, let’s say, China in a trade deal? They kill us. I beat China all the time.",
            "The U.S. has become a dumping ground for everybody else’s problems.",
            "And our real unemployment is anywhere from 18 to 20 percent. Don't believe the 5.6. Don't believe it.",
            "I will be the greatest jobs president that God ever created.",
            "Hillary Clinton was the worst Secretary of State in the history of the United States. There's never been a Secretary of State so bad as Hillary. The world blew up around us. We lost everything, including all relationships. There wasn't one good thing that came out of that administration or her being Secretary of State."]

keywords2 = ["mexico", "mexican", "latino", "border"]
messages2 = ["When Mexico sends its people, they’re not sending their best. ", 
            "When Mexico sends its people, they’re not sending their best. "
            + "They’re sending people that have lots of problems.",
            "I will build a great wall — and nobody builds walls better than me, "
            + "believe me —and I’ll build them very inexpensively. I will build, "
            + "a great, great wall on our southern border, and I will make Mexico "
            + "pay for that wall. Mark my words.",
            "They’re bringing drugs. They’re bringing crime. They’re rapists. "
            + "And some, I assume, are good people.",
            "Mexico is becoming the new China!",
            "Mexico’s totally corrupt government looks horrible with El Chapo’s"
            + " escape—totally corrupt. U.S. paid them $3 billion."]

keywords3 = ["jeb", "wall", "borders", "immigra", "illegal"]
messages3 = [
            "Jeb Bush has to like the Mexican illegals because of his wife.",
            "A nation WITHOUT BORDERS is not a nation at all. We must have a wall. "
            + "The rule of law matters. Jeb just doesn’t get it."
        ]

keywords4 = ["china", "asia", "japan", "korea"]
messages4 = [
            "When did we beat Japan at anything? They send their cars over "
            + "here by the millions, and what do we do? When was the last time "
            + "you saw a Chevrolet in Tokyo? It doesn't exist, folks.",
            "I know the Chinese. I've made a lot of money with the Chinese. I understand "
            + " the Chinese mind."
        ]

keywords5 = ["trump", "donald", "president"]
messages5 =["Do you mind if I sit back a little? Because your breath is very bad.",
            "Sorry losers and haters, but my I.Q. is one of the highest—and you all "
            + "know it! Please don’t feel so stupid or insecure. It’s not your fault.",
            "As everybody knows, but the haters & losers refuse to acknowledge, I do not "
            + "wear a “wig.” My hair may not be perfect, but it’s mine."
        ]
keywords6 =  ["isis", "middle east", "iran", "iraq", "israel", "terror"]
messages6 = [
            "I would bomb the hell out of those oilfields. I wouldn't send many "
            + "troops because you won't need 'em by the time I'm finished.",
            "They just built a hotel in Syria. Can you believe this? They built a hotel. "
            + "When I have to build a hotel, I pay interest. They don't have to pay interest, "
            + "because they took the oil that, when we left Iraq, I said we should've taken.",
            "If Iran was a stock you should go out and buy it, cause you'll quadruple."
        ]

keywords7 = ["mccain", "john", "veterans", "army", "war", "hero"]
messages7 =[
            "I'm very disappointed in John McCain because the vets are horribly treated "
            + "in this country. I'm fighting for the vets. I've done a lot for the vets.",
            "He's not a war hero. He's a war hero because he was captured. I like people that "
            + "weren't captured, OK, I hate to tell you."
        ]

keywords9 = ["obama"]
messages9 = [
            "He may have a birth certificate but there's something on that, maybe religion, maybe it says he is a Muslim. "
            + "I don't know. Maybe he doesn't want that. Or he may not have one. I will tell you this: "
            + "if he wasn't born in this country, it's one of the great scams of all time.",
            "An 'extremely credible source' has called my office and told me that Barack Obama's birth "
            + "certificate is a fraud."
        ]

keywords10 = ["oil", "price"]
messages10 = [
            "We have nobody in Washington that sits back and said, you're not going to raise that fucking oil price."
        ]

keywords11 = ["republican", "republican party", "nominee", "candidate"]
messages11 =[
            "I’m talking about a lot of leverage. I want to win and we will win.",
            "I can't say that I have to respect that person who wins. If I'm"
            + "the nominee, I pledge I will not run as an independent.",
            "The other candidates — they went in, they didn’t know the air conditioning didn’t work. They sweated"
            + "like dogs. They didn’t know the room was too big because they didn’t have anybody there. How are they"
            + "gonna beat ISIS? I don’t think it’s gonna happen."]

keywords12 = ["free trade", "trade"]
messages12 = ["Free trade is terrible. Free trade can be wonderful if you have smart people. But we have stupid people."]

