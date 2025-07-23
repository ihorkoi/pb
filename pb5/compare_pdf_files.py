import hashlib
from difflib import SequenceMatcher


def get_file_hash(filepath):

    h = hashlib.sha224()

    with open(filepath) as file:
        while True:
            batch = file.read(1024)
            if not batch:
                break
        h.update(batch)

    return h.hexdigest()


file1, file2 = get_file_hash(''), get_file_hash('')

if file1 != file2:
    print('These files are not identical')
else:
    print('These files are identical')
