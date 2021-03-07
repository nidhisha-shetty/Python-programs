# Ram is conducting an online Quiz competition daily where daily participation for contestants is optional. Ram want to send specific notifications to following group of participants
1. Participants who participated everyday
2. Participants who participated only once
3. Participants who participated on the first day and never participated again.

**Input**:
List of every day participant list
Number of participants daily can be form 0 to 100000
Number of days can be from 0 to 1000

**Output**:
List of participants who participated daily
List of participants who participated only once
List of participants who participated on the first day and never participated again.

## Solution:
def everyday(competition_list):
    participants_everyday=[]
    first_day=competition_list[0]

    for candidate in first_day:
        count=0
        for competition in competition_list:
            if candidate in competition:
                count+=1
        if count==len(competition_list):
            participants_everyday.append(candidate)
    return participants_everyday

def once(competition_list):
    participant_once=[]
    participant_list=[participant for competition in competition_list[:] for participant in competition]
    participant_dictionary={}
    for participant in participant_list:
        if participant in participant_dictionary:
            participant_dictionary[participant]+=1
        else:
            participant_dictionary[participant]=1
    for name, occurence in participant_dictionary.items():
        if occurence==1:
            participant_once.append(name)
    return participant_once

def first_day(competition_list):
    participant_firstday=[]
    first_day_competition=competition_list[0]
    other_days=[participant for competition in competition_list[1:] for participant in competition]
    for participant in first_day_competition:     
        if participant in other_days:
            pass
        else:
            participant_firstday.append(participant)    
    return participant_firstday

competition_list=[
['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole'],
['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam'],
] 

print(everyday(competition_list))
print(once(competition_list))
print(first_day(competition_list))



