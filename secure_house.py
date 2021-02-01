#!/usr/bin/env python3
import sys


def command_args():
    arg_list = str(sys.argv)
    owner = arg_list[1]
    keys = arg_list[2:]
    print(owner, keys)
    return owner, keys

def get_questions():
    question_list = []
    for line in sys.stdin.readlines():
        question_list.append(line)
    print(question_list)
    return question_list


def ans_queestions(question_list, keys, owner):
    authorized_user_list = []
    for question in question_list:
        key_word = question.split(" ")[0:2]
        key_word = " ".join(question.split(" ")[0:2])
        # insert key
        if key_word == "INSERT KEY":
            user = question.split(" ")[2]
            key = question.split(" ")[3]
            print("KEY %s INSERTED BY %s"%(user, key))
        # turn key
        elif key_word == "TURN KEY":
            user = question.split(" ")[2]
            if key in keys:
                authorized_user_list.append(user)
                print("SUCCESS %s TURNS KEY %s"%(user, key))
            else:
                print("FAILURE %s UNABLE TO TURN KEY %s"%(user, key))
        # enter the house
        elif key_word == "ENTER HOUSE":
            user = question.split(" ")[2]
            if key in keys:
                authorized_user_list.append(user)
                print("ACCESS ALLOWED")
            else:
                print("ACCESS DENIED")
        elif key_word == "WHO'S INSIDE?":
            if authorized_user_list == []:
                print("NOBODY HOME")
            else:
                print(" ".join(authorized_user_list))
        elif key_word == "CHANGE LOCKS":
            user = question.split(" ")[2]
            new_keys = question.split(" ")[3:]
            if user == owner:
                keys = new_keys
                print("OK")
            else:
                print("ACCESS DENIED")
        elif key_word == "LEAVE HOUSE":
            user = question.split(" ")[2]
            if user in authorized_user_list:
                print("OK")
            else:
                print("%s NOT HERE"%(user))
        else:
            print("error")

def main():
    owner, keys = command_args()
    questions = get_questions()
    ans_queestions(questions,keys,owner)







main()