import discord
import os
import mysql.connector
import time
import datetime

client = discord.Client()
#countPropagadoGlobal segue a mesma logica para chamados propagados
countPropagadoGlobal = datetime.datetime.now()
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
        countPropagado = datetime.datetime.now()
        sql4 = ("SELECT csla.id, ssla2.nome, csla.ultima_aprovacao FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_solicitante_sla ssla2 ON csla.aprovacao_tester = ssla2.id JOIN tb_tela_sla tsla ON tsla.id = csla.tela WHERE csla.propagacao_solicitada = 'S' AND csla.aprovacao_tester IS NOT NULL AND aprovado_reprovado = 'A' AND csla.propagado = 'N' ORDER BY csla.ultima_aprovacao DESC LIMIT 1;")
        cursor.execute(sql4)
        for (count3) in cursor:
            countPropagado = count3[2]   
        global countPropagadoGlobal
        countPropagadoGlobal = count3[2]

        cursor.close()
        con.close()
    channelonline = discord.utils.get(client.get_all_channels(), id=895720491199901828)
    await channelonline.send('Bot Aprovacao Tester - Estou Online.')
@client.event
async def on_message(message):
    # don't respond to ourselves
    while True:
        con = mysql.connector.connect(host='localhost', user='phpmyadmin', password='ba67dfd4uk8aa', database='suporteaquicob')
        if con.is_connected():
            print('ok')
            db_info = con.get_server_info()
            cursor = con.cursor(buffered=True)
            cursor.execute("select database();")
            linha = cursor.fetchone()
        if con.is_connected():
            sql4 = ("SELECT csla.id, ssla2.nome, csla.ultima_aprovacao FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_solicitante_sla ssla2 ON csla.aprovacao_tester = ssla2.id JOIN tb_tela_sla tsla ON tsla.id = csla.tela WHERE csla.propagacao_solicitada = 'S' AND csla.aprovacao_tester IS NOT NULL AND aprovado_reprovado = 'A' AND csla.propagado = 'N' ORDER BY csla.ultima_aprovacao DESC LIMIT 1;")
            cursor.execute(sql4)
            for (count3) in cursor:
                countPropagado = count3[2]
            global countPropagadoGlobal
            
            cursor.close()
            con.close()
            
            if(count3[2] > countPropagadoGlobal):
                print('aprovado_teste')
                embedVar3 = discord.Embed(title="Teste Aprovado!", color=0x53a9db)
                embedVar3.set_thumbnail(url="https://cdn.discordapp.com/attachments/895720491199901828/923618934815621170/Sem_titulo.png")
                embedVar3.add_field(name="ID", value=count3[0], inline=True)
                embedVar3.add_field(name="Responsavel teste", value=count3[1], inline=True)
                embedVar3.add_field(name="Link", value='http://sla.aquicob.com.br/suporte-aquicob/resources/views/controle-sla/propagacoes.php?pagProp=1', inline=True)
                channel3 = discord.utils.get(client.get_all_channels(), id=921394657794064434)
                await channel3.send(embed=embedVar3)
                countPropagadoGlobal = count3[2]
        time.sleep(60)

client.run('OTIzMTk5MzUxNjE3MTIyMzY0.YcMiZQ.3BgzbzHK40Ed-qPf1mk6JLG9lMQ')