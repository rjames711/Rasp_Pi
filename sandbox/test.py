import subprocess
entries = subprocess.check_output(['grep', 'timed', '/home/pi/count_log.txt', ])
print entries
print type(entries)
entries = entries.split('\n')
print entries

