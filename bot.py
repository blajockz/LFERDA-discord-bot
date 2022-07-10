import hikari
from keep_alive import keep_alive
import random

answers = ["I am cool thanks", "I am doing good, what about you?", "I am fine, thanks for asking", "The best", "I am currently fine, what about you?", "I am really fine, thanks for asking, and you, how are you doing?"]
answers2 = ["I am searching for someone to chat with!", "I am playing samp", "I am learning how to speak!", "Why asking exactly?"]
questions = ["LFERDA, ntmy", "LFERDA, nice to meet you", "LFERDA, Nice to meet you!", "LFERDA, Ntmy", "LFERDA, glad to know you", "LFERDA, nice to know you"]
questions2 = ["LFERDA, are you okay?", "LFERDA, are u ok?", "LFERDA, are u fine?", "LFERDA, are you fine?", "LFERDA, are u feeling good?", "LFERDA, how are u feeling?", "LFERDA, u good?", "LFERDA, wassup dude?", "LFERDA, how are you bro", "LFERDA, how are u bro", "LFERDA, how are you bro?", "LFERDA, how are u bro?"]

bot = hikari.GatewayBot(
    token=   "Njg1OTQ5MzM2NDExOTYzNTYw.G7XM0y.L49oKgGF7SC6QMKZneuRC2kpEfx61cTqEe4K2c")


@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return

    if event.content.startswith("!gzptp"):
        await event.message.respond(
            "come in-game LFERDA in war right now! at PTP server !! @here @here"
        )
    if event.content.startswith("!gzuif"):
        await event.message.respond(
            "come in-game LFERDA in war right now! at UIF server !! @here @here"
        )
    elif event.content.startswith("What is lferda"):
        await event.message.respond("LFERDA is a samp clan created by tochy")
    if event.content.startswith("!help"):
        await event.message.respond("Avaible commands are : !gzuif ; !gzptp")
    elif event.content.startswith("LFERDA, salam"):
        await event.message.respond("Salam!")
    if event.content.startswith("LFERDA, how are you?"):
        await event.message.respond(random.choice(answers))
    if event.content.startswith("LFERDA, i am good"):
        await event.message.respond("glad to know")
    elif event.content.startswith("LFERDA, what are you doing?"):
        await event.message.respond(random.choice(answers2))
    if event.content.startswith("LFERDA, who's oreyoo?"):
        await event.message.respond("Maybe, the management of Aurora group in UIF ?, i think")
    elif event.content.startswith("LFERDA, who's shawd?"):
        await event.message.respond("He's a deep guy, deepest as i heard, he's thinking very deep :ddd")
    if event.content.startswith("LFERDA, are you okay?"):
        await event.message.respond("Yes i am, glad to know that you care for me!")
    elif event.content.startswith("LFERDA, who is merry?"):
        await event.message.respond("She's a philo-deep girl")
    if event.content.startswith("LFERDA, who is blackjack?"):
        await event.message.respond("He's my programmer dude")
    for q in questions:
        if event.content.startswith(q):
            await event.message.respond("Nice to meet you too!")
    if event.content.startswith("LFERDA, whats your job?"):
        await event.message.respond("I am actually programmed to learn how to speak to people and be one of them, if you don't mind, help me in that!")
    for q2 in questions2:
        if event.content.startswith(q2):
            await event.message.respond(random.choice(answers))
bot.run()
keep_alive()
