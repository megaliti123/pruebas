import tkinter as tkinter
from tkinter import*
import MySQLdb as mysql
import pyglet
import os
import fnmatch


'''	while   player.playing == True:
		try:
			print '{0:.2f}\r'.format(player.time),
		except KeyboardInterrupt:
			print "ctrl-c"
			sys.exit("song paused")
			break   
'''			
mydb = mysql.connect(host='localhost',user='root',passwd='',db='hell music')
cur = mydb.cursor()
player = pyglet.media.Player()

def registrar_cancion():

	global pantalla2
	pantalla2 = Toplevel(frame4)
	pantalla2.geometry("1920x1080")
	pantalla2.title("registro de cancion")

	


	global titulo_entry 
	global genero_entry
	global creador_entry
	global explicitud_entry
	global duracion_entry
	global fechasalida_entry
	

	

	titulo_entry=tkinter.StringVar()
	creador_entry=IntVar()
	genero_entry=IntVar()
	explicitud_entry=tkinter.StringVar()
	duracion_entry = tkinter.StringVar()
	fechasalida_entry=tkinter.StringVar()

	Label(pantalla2,text="registro de canciones",bg="navy", fg="white", width="300", height="3", font=("Calibri",15)).pack()
	Label(pantalla2,text="").pack()

	Label(pantalla2 ,text="titulo").pack()
	titulo_entry = Entry(pantalla2)
	titulo_entry.pack()
	Label(pantalla2).pack()

	Label(pantalla2,text="creador").pack()
	creador_entry = Entry(pantalla2)
	creador_entry.pack()
	Label(pantalla2).pack()

	Label(pantalla2,text="genero").pack()
	genero_entry = Entry(pantalla2)
	genero_entry.pack()
	Label(pantalla2).pack()

	Label(pantalla2,text="explicitud").pack()
	explicitud_entry = Entry(pantalla2)
	explicitud_entry.pack()
	Label(pantalla2).pack()

	Label(pantalla2,text="duracion").pack()
	duracion_entry = Entry(pantalla2)
	duracion_entry.pack()
	Label(pantalla2).pack()

	Label(pantalla2,text="fecha de salida	ejemplo: anio-mes-dia").pack()
	fechasalida_entry = Entry(pantalla2)
	fechasalida_entry.pack()
	Label(pantalla2).pack()

	Button(pantalla2,text="ingresar cancion",command=insertarcosasXD).pack()

def insertarcosasXD():
	
    sql = "INSERT INTO cancion(titulo,genero,creador,explicito,duracion,fecha_salida)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(titulo_entry.get(),genero_entry.get(),creador_entry.get(),explicitud_entry.get(),duracion_entry.get(),fechasalida_entry.get())
	
   
    cur.execute(sql)

    if cur.rowcount == 0:
        mydb.rollback()
    else:
        mydb.commit()
        print(cur.rowcount,"Fue insetado correctamente")


def borrado_insert():
	global pantalla3
	pantalla3 = Toplevel(frame4)
	pantalla3.geometry("1920x1080")
	pantalla3.title("borrado de cancion")

	Label(pantalla3,text="borrar cancion",bg="navy", fg="white", width="300", height="3", font=("Calibri",15)).pack()
	Label(pantalla3,text="").pack()

	global id_borrar_entry

	id_borrar_entry = IntVar()

	Label(pantalla3,text="ingrese id de cancion a borrar").pack()
	id_borrar_entry = Entry(pantalla3)
	id_borrar_entry.pack()
	Label(pantalla3).pack()

	Button(pantalla3,text="borrar",command=eliminar).pack()





	



def eliminar():
 
    SQL = "DELETE FROM cancion WHERE id_cancion='{0}'".format(id_borrar_entry.get())

    cur.execute(SQL)

    if cur.rowcount == 0:
        mydb.rollback()
    else:
        mydb.commit()
        print(cur.rowcount,"Fue eliminado correctamente")



def ingresar_cambio():
	global pantalla4
	pantalla4 = Toplevel(frame4)
	pantalla4.geometry("1920x1080")
	pantalla4.title("modificar cancion")
	
	Label(pantalla4,text = "modificar cancion", bg = "navy", fg = "white", width = "300", height = "3", font= ("Calibri",15)).pack()

	global id_cambiar_entry
	global titulo_modificar_entry
	global creador_modificar_entry
	global genero_modificar_entry
	global explicitud_modificar_entry
	global duracion_modificar_entry
	global fechasalida_modificar_entry

	id_cambiar_entry = IntVar()
	titulo_modificar_entry = tkinter.StringVar()
	creador_modificar_entry = IntVar()
	genero_modificar_entry = IntVar()
	explicitud_modificar_entry = tkinter.StringVar()
	duracion_modificar_entry = tkinter.StringVar()
	fechasalida_modificar_entry = tkinter.StringVar()

	Label(pantalla4,text = "ingresar id_cancion").pack()
	id_cambiar_entry = Entry(pantalla4)
	id_cambiar_entry.pack()
	Label(pantalla4).pack()

	Label(pantalla4,text = "ingresar nuevo titulo").pack()
	titulo_modificar_entry = Entry(pantalla4)
	titulo_modificar_entry.pack()
	Label(pantalla4).pack()
	
	Label(pantalla4, text = "ingresar nuevo creador").pack()
	creador_modificar_entry = Entry(pantalla4)
	creador_modificar_entry.pack()
	Label(pantalla4).pack()

	Label(pantalla4, text = "ingresar nuevo genero").pack()
	genero_modificar_entry = Entry(pantalla4)
	genero_modificar_entry.pack()
	Label(pantalla4).pack()

	Label(pantalla4,text = "ingresar explicitud").pack()
	explicitud_modificar_entry = Entry(pantalla4)
	explicitud_modificar_entry.pack()
	Label(pantalla4).pack()

	Label(pantalla4, text = "ingresar duracion").pack()
	duracion_modificar_entry = Entry(pantalla4)
	duracion_modificar_entry.pack()
	Label(pantalla4).pack()

	Label(pantalla4,text="ingresar nueva fecha de salida").pack()
	fechasalida_modificar_entry = Entry(pantalla4)
	fechasalida_modificar_entry.pack()
	Label(pantalla4).pack()

	Button(pantalla4, text = "modificar", command=update).pack()

def update():
    
    sql = f"UPDATE cancion SET titulo={titulo_modificar_entry}, creador={creador_modificar_entry}, genero={genero_modificar_entry}, explicito={explicitud_modificar_entry}, duracion={duracion_modificar_entry}, fecha_salida={id_cambiar_entry} WHERE id_cancion={id_cambiar_entry}"
	
		
	
   
    cur.execute(sql)

    if cur.rowcount == 0:
        mydb.rollback()
    else:
        mydb.commit()
        print(cur.rowcount,"Fue modificada correctamente")


def move():
	flag=0
	if listbox.get(0)=='TRACKS' or b.lower()=='tracks':
		for i in range(playbox.size()):
			if playbox.get(i)==v or v=='TRACKS':
				flag=1
				break
		if flag==0:
			playbox.insert('end',v)
	elif listbox.get(0)=='ALBUMS' or b.lower()=='albums':
		playbox.delete(0,'end')
		query = "SELECT cancion.titulo FROM cancion,albums WHERE cancion.albumid=albums.id AND albums.name='%s'"%(v)
		cur.execute(query)
		res = cur.fetchall()
		for i in res:
			playbox.insert('end',i[0])
	elif b.lower()=='genre':
		playbox.delete(0,'end')
		query = "SELECT cancion.titulo FROM cancion,categoria WHERE cancion.genero=categoria.id_categoria AND categoria.categoria='%s'"%(v)
		cur.execute(query)
		res = cur.fetchall()
		for i in res:
			playbox.insert('end',i[0])
	elif b.lower()=='artists':
		playbox.delete(0,'end')
		query="SELECT cancion.titulo FROM cancion,albums,creador_contenido WHERE creador_contenido.id_creador=albums.id_creador AND albums.id=cancion.albumid and creador_contenido.apodo='%s'"%(v)
		cur.execute(query)
		res=cur.fetchall()
		for i in res:
			playbox.insert('end',i[0])		
			


def playinfo(event):
	global pmusic
	widget=event.widget
	items = widget.curselection()
	pmusic = widget.get(items[0])
	ftracks(pmusic)	

def play():
	global d	
	d = 'songs/'
	for i in os.listdir('songs'):
		if fnmatch.fnmatch(i.lower(),(pmusic+'*').lower()):
			d=d+i
			break	

	if not d == 'songs/':
	#	print d
		source = pyglet.media.load(d)
	#	print source
		player.queue(source)
		player.eos_action = player.EOS_LOOP
		player.play()
	#	print player.playing
	else:
		print ("no song")

	
def pause():
	player.pause()

def nex():
	
	print(pmusic,d) 
	player.pause()
	play()
	player.next()
	


def dartists():
	listbox.delete(0,'end')
	query = "SELECT albums.name,albums.releasedate FROM albums,creador_contenido WHERE creador_contenido.id_creador=albums.id_creador AND artists.name='%s'"%(v)
	cur.execute(query)
	res = cur.fetchall()
	listbox.insert('end',"ALBUMS")
	listbox.itemconfig('end', {'bg':'red'}) 	
	for i in res:
		value = i[0]
		listbox.insert('end',value)

def dalbums():
	listbox.delete(0,'end')
	query = "SELECT cancion.titulo FROM cancion,albums WHERE cancion.albumid=albums.id AND albums.name='%s'"%(v)
	cur.execute(query)
	res = cur.fetchall()
	listbox.insert('end',"TRACKS")
	listbox.itemconfig('end', {'bg':'red'}) 	
	for i in res:
		value = i[0]
		listbox.insert('end',value)

def dtracks():
	listbox.delete(0,'end')
	query = "SELECT creador_contenido.apodo,albums.name,albums.releasedate,categoria.categoria FROM creador_contenido,albums,categoria,cancion WHERE creador_contenido.id_creador=albums.id_creador AND albums.id=cancion.albumid AND categoria.id_categoria=cancion.genreid AND cancion.titulo='%s'"%(v)
	cur.execute(query)
	res = cur.fetchall()
	listbox.insert('end',"TRACK DETAILS")
	listbox.itemconfig('end', {'bg':'pink'}) 	
	listbox.insert('end','Track Name : '+v)
	for i in res:
		value = 'Artist : '+i[0]
		listbox.insert('end',value)
		value = 'Album : '+i[1]
		listbox.insert('end',value)
		value = 'Album Releasedate : '+str(i[2])
		listbox.insert('end',value)
		value = 'Genre : '+i[3]
		listbox.insert('end',value)

def ftracks(boom):
	listbox.delete(0,'end')
	query = "SELECT creador_contenido.apodo,albums.name,albums.releasedate,categoria.categoria FROM creador_contenido,albums,categotia,cancion WHERE creador_contenido.id_creador=albums.id_creador AND albums.id=cancion.albumid AND categoria.id_categoria=cancion.genero AND cancion.titulo='%s'"%(boom)
	cur.execute(query)
	res = cur.fetchall()
	listbox.insert('end',"TRACK DETAILS")
	listbox.itemconfig('end', {'bg':'pink'}) 	
	listbox.insert('end','Track Name : '+boom)
	for i in res:
		value = 'Artist : '+i[0]
		listbox.insert('end',value)
		value = 'Album : '+i[1]
		listbox.insert('end',value)
		value = 'Album Releasedate : '+str(i[2])
		listbox.insert('end',value)
		value = 'Genre : '+i[3]
		listbox.insert('end',value)


def dgenre():
	listbox.delete(0,'end')
	query = "SELECT cancion.titulo FROM cancion,categoria WHERE cancion.id_categoria = categoria.id_categoria AND categoria.categoria='%s'"%(v)
	cur.execute(query)
	res = cur.fetchall()
	listbox.insert('end',"TRACKS")
	listbox.itemconfig('end', {'bg':'red'}) 	
	for i in res:
		value = i[0]
		listbox.insert('end',value)


def details():
	table = b.lower()
	global ca
	global cc
	global cg
	if table=='artists':
		cc=0
		cg=0
		if ca==1:
			dartists()
		elif ca==2:
			dalbums()
		elif ca==3:
			dtracks()
	elif table=='albums':
		ca=0
		cg=0
		if cc==1:
			dalbums()
		if cc==2:
			dtracks()
			cc=0
	elif table=='cancion':
		cc=0
		ca=0
		cg=0
		dtracks()
	elif table=='genre':
		cc=0
		ca=0
		if cg==1:
			dgenre()	
		if cg==2:
			dtracks()
			cg=0
def info(event):
	widget=event.widget
	items = widget.curselection()
	global v 
	v = widget.get(items[0])
	b.lower(),v
	if b.lower()=='genre':
		if v=='TRACKS':
			genre()
		elif v=='TRACK DETAILS':
			temp = (listbox.get(1)).split(': ')[1]
			query = "SELECT titulo FROM cancion WHERE categoria=(SELECT categoria FROM cancion WHERE ittulo = '%s')"%(temp)
			listbox.delete(0,'end')
			cur.execute(query)
			res = cur.fetchall()
			listbox.insert('end',"TRACKS")
			listbox.itemconfig('end', {'bg':'red'}) 	
			for i in res:
				value = i[0]
				listbox.insert('end',value)
	elif b.lower()=='albums':
		if v=='TRACKS':
			album()
		elif v=='TRACK DETAILS':
			temp = (listbox.get(1)).split(': ')[1]
			query = "SELECT titulo FROM cancion WHERE albumid=(SELECT albumid FROM cancion WHERE titulo = '%s')"%(temp)
			listbox.delete(0,'end')
			cur.execute(query)
			res = cur.fetchall()
			listbox.insert('end',"TRACKS")
			listbox.itemconfig('end', {'bg':'red'}) 	
			for i in res:
				value = i[0]
				listbox.insert('end',value)
	elif b.lower()=='tracks' and v=='TRACK DETAILS':
		listbox.delete(0,'end')
		cur.execute('SELECT name FROM cancion')
		res=cur.fetchall()
		for i in res:
			value = i[0]
			listbox.insert('end',value)

	elif b.lower()=='artists':
		if v=='ALBUMS':
			artist()
		elif v=='TRACKS':
			temp = listbox.get(1)
			highlight="(SELECT albums.name FROM albums WHERE albums.id=(SELECT albumid FROM cancion WHERE titulo LIKE '%s'))"%(temp)
			cur.execute(highlight)
			hres=cur.fetchall()
			hval=hres[0][0]
			query = "SELECT albums.name FROM albums WHERE albums.id_creador=(SELECT albums.id_creador FROM albums WHERE albums.id= (SELECT albums.id FROM albums WHERE albums.id=(SELECT albumid FROM cancion WHERE titulo LIKE '%s')))"%(temp)
			listbox.delete(0,'end')
			cur.execute(query)
			res = cur.fetchall()
			listbox.insert('end',"ALBUMS")
			listbox.itemconfig('end', {'bg':'red'}) 	
			for i in res:
				value = i[0]
				listbox.insert('end',value)
				if value==hval:
					listbox.selection_set('end')
		elif v=='TRACK DETAILS':
			temp = (listbox.get(1)).split(': ')[1]
			query = "SELECT titulo FROM cancion WHERE albumid=(SELECT albumid FROM cancion WHERE titulo = '%s')"%(temp)
			listbox.delete(0,'end')
			cur.execute(query)
			res = cur.fetchall()
			listbox.insert('end',"TRACKS")
			listbox.itemconfig('end', {'bg':'red'}) 	
			for i in res:
				value = i[0]
				listbox.insert('end',value)


				
				
	global cc,cg,ca
	if ca>3:
		ca=1
	if cc>2:
		cc=1
	if cg>2:
		cg=1
	cc=cc+1
	cg=cg+1
	ca=ca+1
	#print ca,cc,cg,v
	
	
def artist():
	global b  
	global ca
	ca=0
	b = button1.config('text')[-1]
	listbox.delete(0,'end')
	value = entry.get()
	query = "SELECT *FROM creador_contenido WHERE apodo LIKE '"+value+"%'"
	cur.execute(query)
	res= cur.fetchall()
	for i in res:
		value = i[1]
		listbox.insert('end',value)
	entry.delete(0,'end')

def album():
	global b  
	global cc
	cc=0
	b = button2.config('text')[-1]
	listbox.delete(0,'end')
	value = entry.get()
	query = "SELECT *FROM albums WHERE name LIKE '"+value+"%'"
	cur.execute(query)
	res= cur.fetchall()
	for i in res:
		value = i[2]
		listbox.insert('end',value)
	entry.delete(0,'end')

def track():
	global b  
	b = button3.config('text')[-1]
	listbox.delete(0,'end')
	value = entry.get()
	length = len(value)
	if length<=2:
		query = "SELECT *FROM cancion WHERE titulo LIKE '"+value+"%'"
	elif length>2:
		query="SELECT * FROM cancion  WHERE cancion.titulo REGEXP '[[:<:]]%s[[:>:]]'"%(value)	
	cur.execute(query)
	res= cur.fetchall()
	for i in res:
		value = i[2]
		listbox.insert('end',value)
	entry.delete(0,'end')


def genre():
	global b  
	global cg
	cg=0
	b = button4.config('text')[-1]
	listbox.delete(0,'end')
	value = entry.get()
	query = "SELECT * FROM categoria WHERE categoria LIKE '%"+value+"%'"
	cur.execute(query)
	res= cur.fetchall()
	for i in res:
		value = i[1]
		listbox.insert('end',value)
	entry.delete(0,'end')

root = tkinter.Tk()
BG='light blue'
BUT='grey'
FG='white'

ca=0
cc=0
cg=0
root.title("DBMS Music Player")
root.geometry("1100x350+200+200")
root.config(bg=BG)
frame1 = tkinter.Frame(root,bg=BG)
label = tkinter.Label(frame1,text='Search:',bg=BUT,fg=FG)
entry = tkinter.Entry(frame1)
label.pack(side='left',anchor='w',pady=4,padx=2)
entry.pack(pady=4)
frame1.pack(pady=12)

frame2= tkinter.Frame(root,bg=BG)
button1 = tkinter.Button(frame2,text='Artists',command=artist,bg=BUT,fg=FG)
button1.pack(side='left',padx=2)
button2 = tkinter.Button(frame2,text='Albums',command=album,bg=BUT,fg=FG)
button2.pack(side='left',padx=2)
button3 = tkinter.Button(frame2,text='Tracks',command=track,bg=BUT,fg=FG)
button3.pack(side='left',padx=2)
button4 = tkinter.Button(frame2,text='Genre',command=genre,bg=BUT,fg=FG)
button4.pack(side='left',padx=2)
frame2.pack()

frame3= tkinter.Frame(root,bg=BG,bd=2,relief='sunken')
listbox = tkinter.Listbox(frame3,width=50,height=10)
listbox.pack(pady=12,padx=2,side='left')
listbox.bind("<<ListboxSelect>>",info)

playbox = tkinter.Listbox(frame3,width=50,height=10)
playbox.pack(pady=12,padx=2,side='right')
playbox.bind("<<ListboxSelect>>",playinfo)
button5 = tkinter.Button(frame3,text='Details',command=details,bg=BUT,fg=FG)
button5.pack(padx=2,side='left')
button6 = tkinter.Button(frame3,text='Move',command=move,bg=BUT,fg=FG)
button6.pack(padx=2,side='right')
frame3.pack(pady=2,padx=2)

frame4 = tkinter.Frame(root,bg=BG,bd=2)
playbutton = tkinter.Button(frame4,text='Play',command=play)
playbutton.pack(padx=2,side='left')
pausebutton = tkinter.Button(frame4,text='Pause',command=pause)
pausebutton.pack(padx=2,side='left')
nextbutton = tkinter.Button(frame4,text='Next',command=nex)
nextbutton.pack(padx=2,side='left')

ingresarbutton = tkinter.Button(frame4,text='ingresar_song',command=registrar_cancion)
ingresarbutton.pack(padx=2,side='right')

eliminadobutton = tkinter.Button(frame4,text='borrar_cancion',command=borrado_insert)
eliminadobutton.pack(padx=2,side='right')

modificadodobutton = tkinter.Button(frame4,text='modificar',command=ingresar_cambio)
modificadodobutton.pack(padx=2,side='right')

#progress = ttk.Progressbar(frame3,orient='horizontal',mode='determinate')
#progress.pack()
frame4.pack(pady=2,padx=2,side='bottom')


root.mainloop()
