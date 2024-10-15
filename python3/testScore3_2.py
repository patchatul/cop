#input testScore, classRank in terminal as string
testScoreString = input("Enter test score: ")
classRankString = input("Enter class rank: ")

#convert string inputs to integer
testScore = int(testScoreString)
classRank = int(classRankString)

#Unit Test 1 testScore 60 & classRank 87 Reject
#Unit Test 2 testScore 87 & classRank 60 Accept
if testScore >= 90:
    if classRank >= 25:
        print("Accept")
    else:
        print("Reject")
else:
    if testScore >= 80:
        if classRank >= 50:
            print("Accept")
        else:
            print("Reject")
    else:
        if testScore >= 70:
            if classRank >= 75:
                print("Accept")
            else:
                print("Reject")
        else:
            print("Reject")

  

