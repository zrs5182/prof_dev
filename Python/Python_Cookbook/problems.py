from notes_utils import *

if __name__ == "__main__":
    # Vars
    chptrs = list()
    chptr_dscrpt = str()
    prblm_dscrpts = dict()

    # Chapter 1 Description
    chptr_dscrpt = "Chapter 1: Data Structures and Algorithms"
    prblm_dscrpts = {
        1 : "Need N-element tuple or sequence to unpack into a collection of variables",
        2 : "",
        3 : "",
        4 : "",
        5 : "",
        6 : "",
        7 : "",
        8 : "",
        9 : "",
        10 : "",
        11 : "",
        12 : "",
        13 : "",
        14 : "",
        15 : "",
        16 : "",
        17 : "",
        18 : "",
        19 : "",
        20 : "",
        }

    # Build Chapter 1 Object
    chptr1 = Chapter(chptr_dscrpt, prblm_dscrpts )

    # Add Chapter 1 to list of chapters
    chptrs.append(chptr1)

    # Create notes
    notes = Notes(chptrs)
    print(notes)
