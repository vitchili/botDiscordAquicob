import discord
import os
import mysql.connector
import time
import datetime

client = discord.Client()
#countPropGlobal global que armazenada a ultima solicitacao de propagacao. a logica e a mesma
countSoliPropGlobal = datetime.datetime.now()
@client.event
async def on_ready():
    print('Logged on')
    con = mysql.connector.connect(host='localhost', user='phpmyadmin', password='ba67dfd4uk8aa', database='suporteaquicob')
    if con.is_connected():
        db_info = con.get_server_info()
        cursor = con.cursor(buffered=True)
        cursor.execute("select database();")
        linha = cursor.fetchone()
    if con.is_connected():
        countSoliProp = datetime.datetime.now()
        sql2 = ("SELECT csla.id, ssla.nome, csla.concluido_em FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_tela_sla tsla ON tsla.id = csla.tela WHERE csla.propagacao_solicitada = 'S' AND (aprovado_reprovado != 'S' OR aprovado_reprovado IS NULL)  AND csla.propagado = 'N' ORDER BY csla.concluido_em DESC LIMIT 1;")
        cursor.execute(sql2)
        for (count) in cursor:
            countSoliProp = count[2]
        global countSoliPropGlobal
        countSoliPropGlobal = countSoliProp
        cursor.close()
        con.close()
    channelonline = discord.utils.get(client.get_all_channels(), id=895720491199901828)
    await channelonline.send('Bot Commit - Estou Online.')
@client.event
async def on_message(message):
    # don't respond to ourselves
    while True:
        con = mysql.connector.connect(host='localhost', user='phpmyadmin', password='ba67dfd4uk8aa', database='suporteaquicob')
        if con.is_connected():  
            db_info = con.get_server_info()
            cursor = con.cursor(buffered=True)
            cursor.execute("select database();")
            linha = cursor.fetchone()
        if con.is_connected():
            sql3 = ("SELECT csla.id, ssla.nome, csla.concluido_em FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_tela_sla tsla ON tsla.id = csla.tela WHERE csla.propagacao_solicitada = 'S' AND (aprovado_reprovado != 'S' OR aprovado_reprovado IS NULL)  AND csla.propagado = 'N' ORDER BY csla.concluido_em DESC LIMIT 1;")
            cursor.execute(sql3)
            for (count2) in cursor:
                countSoliProp = count2[2]
            cursor.close()
            con.close()
            global countSoliPropGlobal
            if(countSoliProp > countSoliPropGlobal):  
                print('solicita_teste')  
                embedVar2 = discord.Embed(title="Nova Solicitação de Teste!", color=0x4caf50)
                embedVar2.set_thumbnail(url="https://cdn.discordapp.com/attachments/895720491199901828/923618934815621170/Sem_titulo.png")
                embedVar2.add_field(name="ID", value=count2[0], inline=True)
                embedVar2.add_field(name="Responsavel", value=count2[1], inline=True)
                embedVar2.add_field(name="Data conclusão", value=count2[2], inline=True)
                channel2 = discord.utils.get(client.get_all_channels(), id=921394657794064434)
                await channel2.send(embed=embedVar2)
                countSoliPropGlobal = count2[2]
        print(countSoliPropGlobal)
        time.sleep(60) 

client.run('OTIzMTk5MzUxNjE3MTIyMzY0.YcMiZQ.3BgzbzHK40Ed-qPf1mk6JLG9lMQ')