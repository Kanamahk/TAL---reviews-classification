#-*-coding:utf-8-*-
from readFileFonctions import *
from traitements import *

def getWholeReviewFromFile(fileName): 
	file_pointer = open(fileName, "r")
	
	gameName = file_pointer.readline()
	opinion = file_pointer.readline()
	hoursPlayed = file_pointer.readline()
	writtenReviews = file_pointer.readline()
	gamesPossessed = file_pointer.readline()
	review = []
	for line in file_pointer.readlines():
		review.append(line)
	file_pointer.close()
	
	contents = gameName, opinion, hoursPlayed, writtenReviews, gamesPossessed, review
	return contents

def getGameName(review):
	return review[0]
	
def getOpinion(review):
	return review[1]

def getHoursPlayed(review):
	return review[2]

def getWrittenReviews(review):
	return review[3]
	
def getGamesPossessed(review):
	return review[4]
	
def getReview(review):
	return review[5]
	
	
def printWholeReview(review):
	print("name of the game : " + review[0])
	print("opinion : " + review[1])
	print("number of hours played : " + review[2])
	print("number of written reviews : " + review[3])
	print("number of games possessed : " + review[4])
	print("review : ")
	for line in review[5]:
		print('\t' + line)

def print_analyse_review(review):
    auxil = read_word_list_file("auxiliary_pos.txt")
    posi = read_word_list_file("Positives.txt")
    nega = read_word_list_file("Negative.txt")
    reviewvalue = 0
    for sent in segment_into_sents(review):
        sentvalue = 0
        print(sent)
        tokens = tokenise_en(normalise(sent,"en"))
        for tok in tokens:
            if tok == "not":
                sentvalue *= -1
            for aux in auxil:
                if tok == (aux + "n't") or tok == (aux + " not"):
                    sentvalue *=-1
            for pos in posi:
                if tok == pos:
                    sentvalue +=1
            for neg in nega:
                if tok == neg:
                    sentvalue -=1
        reviewvalue+=sentvalue

