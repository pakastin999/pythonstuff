import webbrowser





try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found") 

# to search 
query = "nitto site:yksivaihde.net"
query2 = "nitto site:tori.fi"
query3 = "rapha site:https://www.fillaritori.com/forum/14-vaatteet/"
query4 = "rapha site:yksivaihde.net"
query5 = "rapha site:tori.fi"
query6 = "nitto site:fillaritori.com"
query

for j in search(query, num=10, tbs='qdr:m'):
	webbrowser.open_new_tab(j) 
for j in search(query2, num=10, tbs='qdr:m'):
	webbrowser.open_new_tab(j)
for j in search(query3, num=20, tbs='qdr:m'):
	webbrowser.open_new_tab(j) 
for j in search(query4, num=10, tbs='qdr:m'):
	webbrowser.open_new_tab(j) 
for j in search(query5, num=10, tbs='qdr:m'):
	webbrowser.open_new_tab(j)  
for j in search(query6, num=10, tbs='qdr:m'):
	webbrowser.open_new_tab(j) 

print("I'm done")    

