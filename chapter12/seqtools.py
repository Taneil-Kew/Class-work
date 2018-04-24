
def remove_at(pos, seq):
    return seq[:pos] + seq[pos+1:]


def insert_at(pos, seq, char):
    return seq[:pos] + char +seq[pos:]