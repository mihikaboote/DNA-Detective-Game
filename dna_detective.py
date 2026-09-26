import random

# ============================================================
#                  DNA DETECTIVE
#              BIOINFORMATICS GAME
# ============================================================

# -------------------- GAME VARIABLES ------------------------

player_name =""

score = 0
game_running = True

# Reference DNA sequence
reference_dna = "ATGCGTACGTTAGCTAGCTAACG"

# Fictional biological samples
samples = {
    "Sample A": "ATGCGTACGTTAGCTAGCTAACG",
    "Sample B": "ATGCGTACGCTAGCTAGCTAACG",
    "Sample C": "ATGCGTTCGTTAGCTAGCTAACG",
    "Sample D": "ATGCGTACGTTAGCTTGCTAACG"
}

# Possible DNA patterns
patterns = ["ATG", "GCG", "TAA", "GCT", "CGT"]

# ============================================================
#                    BASIC FUNCTIONS
# ============================================================

def display_title():
    print("\n" + "=" * 60)
    print("                      🧬 DNA DETECTIVE")
    print("                      BIOINFORMATICS GAME")
    print("=" * 60)

def display_menu():
    print("\n" + "-" * 60)
    print("                         MAIN MENU")
    print("-" * 60)

    print("1. Analyze DNA")
    print("2. Calculate GC Content")
    print("3. Search DNA Pattern")
    print("4. Detect Mutations")
    print("5. Investigate Samples")
    print("6. Random DNA Challenge")
    print("7. View Score")
    print("8. Exit")

# ============================================================
#                 DNA VALIDATION
# ============================================================

def validate_dna(sequence):

    sequence = sequence.upper()

    for base in sequence:

        if base not in "ATGC":
            return False

    return True


# ============================================================
#                 COUNT NUCLEOTIDES
# ============================================================

def count_nucleotides(sequence):

    a = 0
    t = 0
    g = 0
    c = 0

    for base in sequence:

        if base == "A":
            a += 1

        elif base == "T":
            t += 1

        elif base == "G":
            g += 1

        elif base == "C":
            c += 1

    return a, t, g, c


# ============================================================
#                 ANALYZE DNA
# ============================================================

def analyze_dna():

    global score

    print("\n" + "=" * 60)
    print("                    DNA ANALYSIS")
    print("=" * 60)

    sequence = input("Enter a DNA sequence: ").upper()

    if validate_dna(sequence) == False:

        print("\nInvalid DNA sequence!")
        print("Only A, T, G and C are allowed.")
        return

    a, t, g, c = count_nucleotides(sequence)

    print("\nDNA Sequence:", sequence)
    print("Length:", len(sequence))

    print("\nNucleotide Count:")
    print("Adenine  (A):", a)
    print("Thymine  (T):", t)
    print("Guanine  (G):", g)
    print("Cytosine (C):", c)

    score += 5

    print("\n+5 points for completing DNA analysis!")


# ============================================================
#                 GC CONTENT
# ============================================================

def calculate_gc_content():

    global score

    print("\n" + "=" * 60)
    print("                    GC CONTENT")
    print("=" * 60)

    sequence = input("Enter a DNA sequence: ").upper()

    if validate_dna(sequence) == False:

        print("\nInvalid DNA sequence!")
        return

    g = sequence.count("G")
    c = sequence.count("C")

    gc = g + c

    percentage = (gc / len(sequence)) * 100

    print("\nGuanine:", g)
    print("Cytosine:", c)
    print("GC bases:", gc)

    print("GC Content:", round(percentage, 2), "%")

    score += 5

    print("\n+5 points!")


# ============================================================
#                 SEARCH DNA PATTERN
# ============================================================

def search_pattern():

    global score

    print("\n" + "=" * 60)
    print("                  DNA PATTERN SEARCH")
    print("=" * 60)

    sequence = input("Enter DNA sequence: ").upper()
    pattern = input("Enter pattern to search: ").upper()

    if validate_dna(sequence) == False:
        print("\nInvalid DNA sequence!")
        return

    if validate_dna(pattern) == False:
        print("\nInvalid DNA pattern!")
        return

    positions = []

    # Linear search through the DNA sequence

    for i in range(len(sequence) - len(pattern) + 1):

        if sequence[i:i + len(pattern)] == pattern:

            positions.append(i)

    if len(positions) > 0:

        print("\nPattern found!")

        print("Pattern:", pattern)

        print("Positions:", positions)

        score += 10

        print("+10 points!")

    else:

        print("\nPattern was not found.")


# ============================================================
#                 MUTATION DETECTION
# ============================================================

def detect_mutations():

    global score

    print("\n" + "=" * 60)
    print("                  MUTATION DETECTION")
    print("=" * 60)

    print("Reference DNA:")
    print(reference_dna)

    print("\nEnter the sample DNA:")
    sample = input().upper()

    if validate_dna(sample) == False:

        print("\nInvalid DNA sequence!")
        return

    if len(sample) != len(reference_dna):

        print("\nFor this challenge, both sequences")
        print("must have the same length.")

        return

    mutations = []

    for i in range(len(reference_dna)):

        if reference_dna[i] != sample[i]:

            mutations.append(
                (i, reference_dna[i], sample[i])
            )

    if len(mutations) == 0:

        print("\nNo mutations detected!")

        score += 15

        print("+15 points!")

    else:

        print("\nMutations detected:")

        for mutation in mutations:

            position = mutation[0]
            original = mutation[1]
            new = mutation[2]

            print(
                "Position", position,
                ":", original,
                "->",
                new
            )

        print("\nTotal mutations:", len(mutations))

        score += 15

        print("+15 points for detecting mutations!")


# ============================================================
#                 SAMPLE INVESTIGATION
# ============================================================

def investigate_samples():

    global score

    print("\n" + "=" * 60)
    print("                  SAMPLE INVESTIGATION")
    print("=" * 60)

    print("\nReference DNA:")
    print(reference_dna)

    print("\nAvailable samples:")

    sample_names = list(samples.keys())

    for i in range(len(sample_names)):

        print(i + 1, ".", sample_names[i])

    choice = input("\nChoose a sample: ")

    if choice not in ["1", "2", "3", "4"]:

        print("\nInvalid choice!")

        return

    sample_name = sample_names[int(choice) - 1]

    sample = samples[sample_name]

    print("\nYou selected:", sample_name)

    print("Sample DNA:")
    print(sample)

    mutations = []

    for i in range(len(reference_dna)):

        if reference_dna[i] != sample[i]:

            mutations.append(i)

    if len(mutations) == 0:

        print("\nResult: No mutation detected.")

    else:

        print("\nResult:", len(mutations), "mutation(s) detected.")

        print("Mutation positions:", mutations)

    # Random clue

    clues = [
        "The sample contains a nucleotide substitution.",
        "The mutation occurs in the middle region.",
        "The sample differs from the reference sequence.",
        "Further analysis is recommended."
    ]

    print("\nInvestigation clue:")
    print(random.choice(clues))

    score += 10

    print("\n+10 investigation points!")


# ============================================================
#                 RANDOM DNA CHALLENGE
# ============================================================

def random_challenge():

    global score

    print("\n" + "=" * 60)
    print("                  RANDOM DNA CHALLENGE")
    print("=" * 60)

    pattern = random.choice(patterns)

    print("\nFind the pattern:")
    print(pattern)

    sequence = reference_dna

    positions = []

    for i in range(len(sequence) - len(pattern) + 1):

        if sequence[i:i + len(pattern)] == pattern:

            positions.append(i)

    answer = input(
        "\nEnter the position where the pattern first appears: "
    )

    if answer.isdigit():

        answer = int(answer)

        if len(positions) > 0 and answer == positions[0]:

            print("\nCorrect! 🎉")

            score += 20

            print("+20 points!")

        else:

            print("\nIncorrect.")

            if len(positions) > 0:

                print("Correct position:", positions[0])

    else:

        print("\nPlease enter a number.")


# ============================================================
#                     SCORE SYSTEM
# ============================================================

def view_score():

    print("\n" + "=" * 60)
    print("                     SCORE")
    print("=" * 60)

    print("Detective:", player_name)
    print("Score:", score)

    if score >= 80:

        print("Rank: Master Bioinformatics Detective 🏆")

    elif score >= 50:

        print("Rank: Advanced DNA Investigator 🧬")

    elif score >= 20:

        print("Rank: Junior DNA Investigator 🔬")

    else:

        print("Rank: Trainee Detective")


# ============================================================
#                       MAIN GAME
# ============================================================

display_title()

player_name = input("\nEnter your detective name: ")

print("\nWelcome,", player_name + "!")

print("\nYour mission:")

print("Analyze DNA sequences,")
print("detect mutations,")
print("find biological patterns,")
print("and become a Bioinformatics Detective!")

while game_running:

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":

        analyze_dna()

    elif choice == "2":

        calculate_gc_content()

    elif choice == "3":

        search_pattern()

    elif choice == "4":

        detect_mutations()

    elif choice == "5":

        investigate_samples()

    elif choice == "6":

        random_challenge()

    elif choice == "7":

        view_score()

    elif choice == "8":

        print("\n" + "=" * 60)
        print("             THANK YOU FOR PLAYING!")
        print("=" * 60)

        print("Final score:", score)

        if score >= 80:

            print("Excellent work, Master Detective!")

        elif score >= 50:

            print("Great work, Bioinformatics Investigator!")

        elif score >= 20:

            print("Good start, Junior Investigator!")

        else:

            print("Keep investigating!")

        game_running = False

    else:

        print("\nInvalid choice!")
        print("Please choose an option from 1 to 8.")