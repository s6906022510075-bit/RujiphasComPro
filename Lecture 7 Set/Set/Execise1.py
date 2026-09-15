survey_results = [
    ["Python", "Javascript", "C++"],
    ["Python", "Javascript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "Javascript"],
    ["Python", "C++", "Java", "JavaScript"],
]

# 1. Identify the languages that were chosen by all participants.
all_languages = set.intersection(*[set(participant) for participant in survey_results])
# 2. Find the languages that were only chosen by a single participant.
language_counts = {}
for participant in survey_results:
    for language in participant:
        language_counts[language] = language_counts.get(language, 0) + 1
single_choice_languages = {language for language, count in language_counts.items() if count == 1}

# 3. Determine the number of unique languages mentioned in the survey.
unique_languages = len(set.union(*[set(participant) for participant in survey_results]))

# 4. List the languages that were chosen by exactly two participants.
exactly_two_choices = {language for language, count in language_counts.items() if count == 2}

# 5. Find participants who have the exact same set of favorite languages.
same_favorite_languages = []
for i, participant1 in enumerate(survey_results):
    for j, participant2 in enumerate(survey_results[i + 1:], i + 1):
        if set(participant1) == set(participant2):
            same_favorite_languages.append((participant1, participant2))

# Output the results
print("Languages chosen by all participants:", all_languages)
print("Languages chosen by only one participant:", single_choice_languages)
print("Number of unique languages mentioned:", unique_languages)
print("Languages chosen by exactly two participants:", exactly_two_choices)
if same_favorite_languages:
    print("Participants with the same favorite languages:")
    for pair in same_favorite_languages:
        print(pair)
            