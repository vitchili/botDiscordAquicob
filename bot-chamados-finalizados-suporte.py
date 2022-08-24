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
        print("Conectado ao servidor MySQL versao ",db_info)
        cursor = con.cursor(buffered=True)
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ",linha)
    if con.is_connected():
        countPropagado = datetime.datetime.now()

        sql4 = ("SELECT csla.id, ssla.nome, csla.modificacao, csla.concluido_em, tsla.nome AS tela, csla.direcionamento FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_tela_sla tsla ON tsla.id = csla.tela JOIN tb_modulo modu ON tsla.modulo = modu.id WHERE csla.propagado = 'N' AND csla.concluido_em IS NOT NULL AND csla.propagacao_solicitada = 'N' AND csla.aprovacao_tester is NULL AND ultima_aprovacao IS NULL ORDER BY csla.concluido_em DESC LIMIT 1;")
        cursor.execute(sql4)
        for (count3) in cursor:
            countPropagado = count3[3]   
        global countPropagadoGlobal
        countPropagadoGlobal = count3[3]

        cursor.close()
        con.close()
    channelonline = discord.utils.get(client.get_all_channels(), id=895720491199901828)
    await channelonline.send('-')
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
            sql4 = ("SELECT csla.id, ssla.nome, csla.modificacao, csla.concluido_em, tsla.nome AS tela, csla.direcionamento FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_tela_sla tsla ON tsla.id = csla.tela JOIN tb_modulo modu ON tsla.modulo = modu.id WHERE csla.propagado = 'N' AND csla.concluido_em IS NOT NULL AND csla.propagacao_solicitada = 'N' AND csla.aprovacao_tester is NULL AND ultima_aprovacao IS NULL ORDER BY csla.concluido_em DESC LIMIT 1;")
            cursor.execute(sql4)
            for (count3) in cursor:
                countPropagado = count3[4]
            global countPropagadoGlobal
            
            cursor.close()
            con.close()
            
            if(count3[3] > countPropagadoGlobal):
                print(count3[3])
                embedVar3 = discord.Embed(title="Chamado finalizado pelo Suporte!", color=0xd7cc23)
                embedVar3.set_thumbnail(url="https://cdn.discordapp.com/attachments/895720491199901828/923618934815621170/Sem_titulo.png")
                embedVar3.add_field(name="ID", value=count3[0], inline=True)
                embedVar3.add_field(name="Responsável", value=count3[1], inline=True)
                embedVar3.add_field(name="Tela", value=count3[1], inline=True)
                embedVar3.add_field(name="Modificação", value=count3[2], inline=True)
                embedVar3.add_field(name="Data conclusão", value=count3[3], inline=True)
                embedVar3.add_field(name="Link", value='http://sla.aquicob.com.br/suporte-aquicob/resources/views/controle-sla/propagacoes.php?pagProp=1', inline=True)
                channel3 = discord.utils.get(client.get_all_channels(), id=921394759426252810)
                await channel3.send(embed=embedVar3)
                countPropagadoGlobal = count3[3]
        time.sleep(60)

client.run('OTIzMTk5MzUxNjE3MTIyMzY0.YcMiZQ.3BgzbzHK40Ed-qPf1mk6JLG9lMQ')