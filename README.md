~ is the user home directory in a path name 
print(os.path.expanduser('~')) is a way to get your own home directory
windows can use either / or \ since it accepts both 
if you want a path directory in a string you would have to use \\ at the start since \ is a special characters within strings 
os.path.split(pathname) splits full path into two parts, the path and the filename 
you can also put this into a tuple 
glob is used to return files that match a specific name or extension 
 glob.glob('examples/*.xml') for example would return all .xml files in the examples directory
 (Note: * is a wildcard)
 file sizes are sometimes rounded to the nearest 4 
 for example: a 23.4 KB file would round up to 24 KB
 you can use realpath to get the full path name back to the drive
 list comprehensions can handle  ant expression in them 
 list comprehensions can also be used to filter items 
 [f for f in glob.glob('*.py') if os.stat(f).st_size > 6000] 
would return every python file in a list where the size is above 6000 bytes 
for multiple values in range it is presented in the format range(a,b,c) where a equals the sart, b equals how many times and c being the step (gap between one value and the next)
if no values are put in, they default to 0 1 and 0 respectively 
