import sys, os
from hanziconv import HanziConv

# Load Anki library
sys.path.append('anki') 
from anki.storage import Collection

cpath = os.path.join(os.getcwd(), 'collection.anki2')

# Load the collection
col = Collection(cpath)

# fields = ['Word', 'Word Alternatives', 'Word Hidden Alternatives', 
#     'Word Typing Corrects', 'Definition', 'Definition Alternatives', 
#     'Definition Hidden Alternatives', 'Definition Typing Corrects', 
#     'Pronunciation', 'Pronunciation Alternatives', 
#     'Pronunciation Hidden Alternatives', 'Pronunciation Typing Corrects', 
#     'Part of Speech', 'Gender', 'Audio', 'Definition -> Word Mem', 'Level', 
#     'Thing']

# print(col.decks.all_names_and_ids())
for deck_metadata in col.decks.all_names_and_ids():
    for tag in col.tags.byDeck(deck_metadata.id):
        for cid in col.find_notes(f'tag:{tag}'): 
            note = col.getNote(cid)
            for i in range(8): # Only update up to Definition Typing Corrects
                if not HanziConv.same(note.fields[i], HanziConv.toTraditional(note.fields[i])):
                    note.fields[i] = note.fields[i] + '( '+ HanziConv.toTraditional(note.fields[i]) + ')'
            col.update_note(note)

# Save changes to collection

col.save()
col.close(downgrade=True)
print('all done!')