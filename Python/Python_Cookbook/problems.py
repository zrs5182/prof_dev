class Chapter(object):
    """ Chapter Object for organizing code and problems """
    def __init__(self, description, problem_descriptions):
        self.description = description
        self.problem_descriptions = problem_descriptions

    def __str__(self):
        string = ""

        # Print out Chapter Description
        string = string + "---------- " + self.description + " ----------"+ '\n'

        # Print out Problem Descriptions
        for prob in self.problem_descriptions:
            string = string + "Problem #" + str( prob ) + "\n"
            string = string + "\t" + self.problem_descriptions[prob] + "\n"
        return string

class Notes(object):
    """ Collection of chapters """
    def __init__(self, chapters):
        self.chapters = chapters

    def __str__(self):
        string = ""

        # Output all the chapters
        for chptr in self.chapters:
            string = string + str(chptr) + '\n'

        return string

if __name__ == "__main__":
    # Vars
    chptrs = list()
    chptr_dscrpt = str()
    prblm_dscrpts = dict()

    # Chapter 1 Code
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
