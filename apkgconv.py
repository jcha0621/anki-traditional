import sys, os

# Load Anki library
sys.path.append('anki') 
from anki.storage import Collection

cpath = os.path.join(os.getcwd(), 'collection.anki2')

# Load the collection
col = Collection(cpath)

# Use the available methods to list the notes
# need to extend to all tags (maybe use col.tags?)
for cid in col.findNotes('tag:A1'): 
    note = col.getNote(cid)
    front = note.fields[0]
    print(front)