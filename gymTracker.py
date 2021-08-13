# Gym tracker
##exerciseByDay = {}
# importing pprint to beautify dictionaries printing
import pprint


## function initialisations 
# updateDictionaries will update all the dictionaires after 7 days
def updateDictionaries(newSets):
    for k in chest_workout:
        chest_workout[k] = newSets
    for k in shoulder_workout:
        shoulder_workout[k] = newSets
    for k in bicep_workout:
        bicep_workout[k] = newSets
    for k in legs_workout:
        legs_workout[k] = newSets
    for k in back_workout:
        back_workout[k] = newSets

def calcBMI():
    BMI = weight / (height/100)**2
    print(f"You BMI is {BMI}")

# creating login portal
# creating a email dictionary
# will see about masking the emails to make it secure later

# TO-DO : masking email
emailDict = {}
uName = input("Enter your Username --> ")
email = input("Enter your email-id --> ")
emailDict[uName]=email
print(emailDict)

# Building some logic around BMI and weight trainings : 
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
bmi = calcBMI()

#if userWeight:
    #pass
    # calculating BMI

#emailCheck = email in emailDict.values()
#if emailCheck == True:

# initializing a counter for weekend to scale up the workout
# planning to implement changes to set volumes as per user choice or workout changes per day
counter = 0
# Days dictioaary to take user input 
dayOfWeek = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday',
}
#print(dayOfWeek)
# Dictionary for part to train on specific day
bodyPart = {'Monday':"chest",
            'Tuesday':"biceps",
            'Wednesday':"shoulders",
            'Thursday':"back",
            'Friday':"triceps",
            'Saturday':"legs",
            'Sunday':"cardio",
}
#print(bodyPart)
# Body part object,exercise model
# Initialising training objects
# Planning to scale these up
# Dictionaries Used so that objects can be updated

chest_workout = {

    'Bench Press': "12*3",
    'Dumble Press': "12*3",
    'Bench Press Incline': "12*3",
    'Dumble Press Incline': "12*3",
    'Bench Press Decline': "12*3",
    'Dumble Fly Incline': "12*3",
}
shoulder_workout = {
    "Dumble shoulder Press --> 12*3",
    "Dumble lateral raise --> 12*3",
    "Barbell Press --> 12*3",
    "Dumble Front Raises --> 12*3",
    "Dumble Shrugs --> 12*3",
}
legs_workout = {

    'Back squat':"12*3",
    'Front squat':"12*3",
    'Romanian deadlift"':"12* 3",
    'Good mornings':"12*3",
    'Walking lunges':"12*3",
    'Reverse lunge':"12*3",
    'Lateral lunge':"12*3",
}
back_workout = {

    'Resistance band pull apart':"12*3",
    'Quadruped dumbbell row':"12*3",
    'Lat pulldown':"12*3",
    'Wide dumbbell row':"12*3",
    'Barbell deadlift':"12*3",
    'Hyperextension':"12*3",
    'Good morning':"12*3",
    'Single-arm dumbbell row':"12*3",

    
}
bicep_workout = {
    'Fat-Grip Hammer Curl':"12*3",
    'Behind-the-Back Cable Curl' :"12*3",
    'Bar Preacher Curl' :"12*3",
    'Reverse Curls' :"12*3",
    'Wide-Grip Curl' :"12*3",
}


# creating a dictionary for the difficulty level 
diffDict = {
    '1':"20*4",
    '2':"15*4"
}
# User input for day.
dayToday = int(input("""What day is it today?
                    1. Monday
                    2. Tuesday
                    3. Wednesday
                    4. Thursday
                    5. Friday
                    6. Saturday
                    7. Sunday
                    """))

#print(dayToday)
if dayToday:
    print("Your Today's plan is --> ")
    selectedDay = dayOfWeek[dayToday]
    print(selectedDay)
    partToTrain = bodyPart.get(selectedDay)
    print(f"part to train : {partToTrain}")

    #building logic to check bodypart fetched to then fetch the workout chart
    if partToTrain == "chest":
        #print("in")
        pprint.pprint(chest_workout)
    if partToTrain == "shoulders":
        pprint.pprint(shoulder_workout)
    if partToTrain == "legs":
        pprint.pprint(legs_workout)
    if partToTrain == "back":
        pprint.pprint(back_workout)
    if partToTrain == "biceps":
        pprint.pprint(bicep_workout)
    
# preparing logic for updating the workout intensity once 7 days have been done
counter +=1
if counter == 7:
    updateDictionaries()

#Creating a feedback system post 14 days of workout
# this feedback system call will only be there after 21 days of workout
weight = float(input("Enter your weight in kg: "))
newbmi = calcBMI()
if newbmi < bmi:
    diffLevel = int(input("""Update your training regime to which difficulty level
            1.Hard
            2.Medium
             """))
    if  diffLevel == '1':
        newSets=diffDict.get(diffLevel)
        updateDictionaries(newSets)
    if diffLevel == '2':
        newSets=diffDict.get(diffLevel)
        updateDictionaries(newSets)








    

    
    



