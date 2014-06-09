from notes_utils import *

if __name__ == "__main__":
    # Vars
    chptrs = list()
    chptr_dscrpt = str()
    prblms = list()

    # Chapter 1 Problems
    prblm_nmbr = 1
    prblm_title = "Unpacking a Sequence into Spearate Variables"
    prblm_dscrptn = "You have an N-element tuple or sequence that you would like to unpack into a collection of N variables."
    sltn = "Use the assignment operator with the same number of variables on the left hand side \
            as values in the structure you are tyring to unpack on the right."

    dscssn = "Unpacking works with any object that is iterable. Some iterable types include: \
            strings, files, iterators, and generators. Notes: _ is traditionally used as a throwaway variable."
    code = "data = ['Acme', 50, 91.1, (2012, 12, 21) ]\
            \n _, shares, price, _ = data"
    # Add problem
    prblms.append( Problem(prblm_nmbr, prblm_title, prblm_dscrptn, sltn, dscssn, code) )

    # Chapter 1 Description
    chptr_dscrpt = "Chapter 1: Data Structures and Algorithms"

    # Add Chapter 1 Notes
    chptrs.append( Chapter(chptr_dscrpt, prblms ) )

    # Create notes
    notes = Notes(chptrs)
    print(notes)
