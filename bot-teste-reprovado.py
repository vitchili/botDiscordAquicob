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
    con = mysql.connector.connect(host='localhost', user='phpmyadmin', password='ba67dfd4uk8aa', database='suporteaquicob')
    if con.is_connected():
        db_info = con.get_server_info()
        cursor = con.cursor(buffered=True)
        cursor.execute("select database();")
        linha = cursor.fetchone()
    if con.is_connected():
        countPropagado = datetime.datetime.now()
        sql4 = ("SELECT csla.id, ssla.nome, csla.ultima_reprovacao FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_tela_sla tsla ON tsla.id = csla.tela WHERE csla.aprovacao_tester IS NULL AND aprovado_reprovado = 'R' AND csla.propagado = 'N' AND ultima_reprovacao IS NOT NULL ORDER BY csla.ultima_reprovacao DESC LIMIT 1;")
        cursor.execute(sql4)
        for (count3) in cursor:
            countPropagado = count3[2]   
        global countPropagadoGlobal
        countPropagadoGlobal = countPropagado

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
            db_info = con.get_server_info()
            cursor = con.cursor(buffered=True)
            cursor.execute("select database();")
            linha = cursor.fetchone()
        if con.is_connected():
            sql4 = ("SELECT csla.id, ssla.nome, csla.ultima_reprovacao FROM tb_chamados_sla csla LEFT JOIN tb_solicitante_sla ssla ON ssla.id = csla.responsavel JOIN tb_tela_sla tsla ON tsla.id = csla.tela WHERE csla.aprovacao_tester IS NULL AND aprovado_reprovado = 'R' AND csla.propagado = 'N' AND ultima_reprovacao IS NOT NULL ORDER BY csla.ultima_reprovacao DESC LIMIT 1;")
            cursor.execute(sql4)
            count = []
            for (count) in cursor:
                countPropagado = count[2]
            global countPropagadoGlobal

            cursor.close()
            con.close()
            
            if(count[2] > countPropagadoGlobal):
                print('reprovado')
                embedVar3 = discord.Embed(title="Teste Reprovado!", color=0xff0000)
                embedVar3.set_thumbnail(url="https://cdn.discordapp.com/attachments/895720491199901828/923618934815621170/Sem_titulo.png")
                embedVar3.add_field(name="ID", value=count[0], inline=True)
                embedVar3.add_field(name="Responsavel", value=count[1], inline=True)
                embedVar3.add_field(name="Data reprovação", value=count[2], inline=True)
                embedVar3.add_field(name="Link", value='http://sla.aquicob.com.br/suporte-aquicob/resources/views/controle-sla/minhas_tarefas.php', inline=True)
                channel3 = discord.utils.get(client.get_all_channels(), id=921394657794064434)
                await channel3.send(embed=embedVar3)
                countPropagadoGlobal = countPropagado
        time.sleep(60)

client.run('OTIzMTk5MzUxNjE3MTIyMzY0.YcMiZQ.3BgzbzHK40Ed-qPf1mk6JLG9lMQ')