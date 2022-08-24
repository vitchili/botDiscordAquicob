import discord
import os
import mysql.connector
import time

client = discord.Client()
#countGlobal e a global de contador de chamados. Toda vez que a iteracao do on_message repete, ele compara o contador atual de chamados com o anterior. essa var representa o valor anterior, antes da comparacao
countGlobal = 0
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
        contador = 0
        sql = ("SELECT csla.id AS COUNT, cliente.cliente AS cliente, psla.nome AS prioridade, tsla.nome AS tela, csla.prazo, csla.descricao, modu.modulo AS modulo, IF(csla.`direcionamento` = 'S', 'SUPORTE', 'DESENVOLVIMENTO') AS direcionamento FROM tb_chamados_sla csla JOIN tb_prioridade_sla psla ON csla.prioridade = psla.id JOIN tb_tela_sla tsla ON tsla.id = csla.tela JOIN tb_cliente cliente ON cliente.id = csla.cliente JOIN tb_modulo modu ON tsla.modulo = modu.id WHERE direcionamento = 'D' AND csla.status = '1' ORDER BY csla.id DESC LIMIT 1;")
        cursor.execute(sql)
        for (count) in cursor:
            contador = count[0]
        global countGlobal
        countGlobal = contador

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
            sql = ("SELECT csla.id AS COUNT, cliente.cliente AS cliente, psla.nome AS prioridade, tsla.nome AS tela, csla.prazo, csla.descricao, modu.modulo AS modulo, IF(csla.`direcionamento` = 'S', 'SUPORTE', 'DESENVOLVIMENTO') AS direcionamento FROM tb_chamados_sla csla JOIN tb_prioridade_sla psla ON csla.prioridade = psla.id JOIN tb_tela_sla tsla ON tsla.id = csla.tela JOIN tb_cliente cliente ON cliente.id = csla.cliente JOIN tb_modulo modu ON tsla.modulo = modu.id WHERE direcionamento = 'D' AND csla.status = '1' ORDER BY csla.id DESC LIMIT 1;")
            cursor.execute(sql)
            for (count) in cursor:
              contador = count[0]
            
            cursor.close()
            con.close()
            print('newError')
            channelOnline = discord.utils.get(client.get_all_channels(), id=895720491199901828)
            global countGlobal
            await channelOnline.send('-') 
            if(int(contador) > int(countGlobal)):
                print('dev')
                embedVar = discord.Embed(title="Novo Erro/Bug/Informativo!", color=0xff0000)
                embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/895720491199901828/923618934815621170/Sem_titulo.png")
                embedVar.add_field(name="ID", value=count[0], inline=True)
                embedVar.add_field(name="Cliente", value=count[1], inline=True)
                embedVar.add_field(name="Prioridade", value=count[2], inline=True)
                embedVar.add_field(name="Tela", value=count[3], inline=True)
                embedVar.add_field(name="Prazo", value=str(count[4]) + ' horas', inline=True)
                embedVar.add_field(name="Direcionamento", value=str(count[7]), inline=True)
                embedVar.add_field(name="Descrição", value=count[5], inline=False)
                embedVar.add_field(name="Link", value='http://sla.aquicob.com.br/suporte-aquicob/resources/views/controle-sla/controle-sla.php', inline=False)
                channel = discord.utils.get(client.get_all_channels(), id=921394628664643624)
                countGlobal = contador
                await channel.send(embed=embedVar)
                continue
        print(countGlobal)
        time.sleep(60) 

client.run('OTIzMTk5MzUxNjE3MTIyMzY0.YcMiZQ.3BgzbzHK40Ed-qPf1mk6JLG9lMQ')