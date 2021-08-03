import sys, subprocess


print('Welcome to MemeFontify!')
print(' ')
text = input('Please enter text you would like to memeify: ')

# Make memeified string
newString = ''
count = 1
for char in text:
    if count % 2 == 0:
        newString += char.upper()
    else:
        newString += char
    count += 1

print(' ')
print('Text created:')
print(' \n---------------------')
print(newString)

# Copy to clipboard
if sys.platform == 'win32':
    cmd='echo '+newString.strip()+'|clip'
    subprocess.check_call(cmd, shell=True)
else:
    cmd='echo '+newString.strip()+'|pbcopy'
    subprocess.check_call(cmd, shell=True)

print(' ')
print('Text Copied to Clipboard!')
