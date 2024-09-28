dd = '''
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
'''

file = open('hoy.html', 'w')

dd = dd.split('\n')

for ff in dd:
 file.write(ff)

file.close()





