import discord
import qrcode

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg_atts = message.attachments
    if msg_atts:
        print(f'Received url :{msg_atts[0].url}')
        qr = qrcode.QRCode(version=3, box_size=20, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
        data = msg_atts[0].url
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("to-be-sent.png")
        await message.channel.send(file=discord.File('to-be-sent.png'))
        qr.clear

client.run('TINSERT-TOKEN-HERE')
