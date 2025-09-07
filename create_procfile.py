# create_procfile.py 
with open('Procfile', 'w') as f: 
    f.write('web: gunicorn application: app\n') 
 
