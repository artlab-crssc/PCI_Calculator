#Created by Ben on 11/11/2024, ART Lab, CRSSC


from sqlite3 import connect
import pandas as pd
from Interface import UI

#read excel and create database if not exist
excel='256x36 table.xlsx'
pcitable=pd.read_excel(excel,0)
table256=pd.read_excel(excel,1)
table36=pd.read_excel(excel,2)


def look_up(*args):
    if gui.noz.get()!='any':
        config='='+gui.noz.get()
    else:
        config='>=0.2'
    try:
        #lookup PCI table
        with connect(file) as con:
            pcitable.to_sql('pcitable',con,if_exists='replace',index=False)
            table36.to_sql('table36',con,if_exists='replace',index=False)
            table256.to_sql('table256',con,if_exists='replace',index=False)
            cur=con.cursor()

            '''
            #get all column names
            cur.execute('PRAGMA table_info(table36)')
            columns=cur.fetchall()
            column_names = [column[1] for column in columns]
            print(column_names)
            '''
            #get ratioset no.
            cur.execute(f'SELECT * FROM table36 WHERE Tensile={gui.ratio[0]} AND PrintTime={gui.ratio[1]} AND Elongation={gui.ratio[2]}')
            ratio=cur.fetchone()

            #get nozzle diameter and all possible combinations no.
            cur.execute(f'SELECT * FROM table256 WHERE nozzleDiameter{config}')
            noz=cur.fetchall()
            config_wif_noz=[a[0] for a in noz]
            #config without the set number
            output=[list(a[1:]) for a in noz]

            #only select config with desired combination no.
            cur.execute(f'SELECT * FROM pcitable WHERE Ratioset IN {tuple(config_wif_noz)}')
            rows=cur.fetchall()
            r=[r[ratio[0]] for r in rows]
            #pack config with corresponding PCI
            res=list(zip(output,r))
            #list out the table, sort by descending PCI
            res.sort(key=lambda y:y[1],reverse=True)
            gui.tab.delete(*gui.tab.get_children())
            for i in res:
                #PCI to 5 decimal places
                gui.tab.insert('','end',text='1',values=(*i[0],f'{i[1]:.5f}'))

    except TypeError:
        pass

if __name__=='__main__':
    file='./Database/PCItable.db'
    gui=UI()
    gui.sub.bind('<Button-1>',look_up)
    gui.mainloop()




