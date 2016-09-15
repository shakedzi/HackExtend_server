#!/usr/bin/python
from FrontEnd import DBhandler
import json
import flask

def createPairs(userFriendsList, relevantAdminFriends, adminID):
    # userFriendsList = map of user and it's friends
    # relevantAdminFriends = the friends the admin invited (facebook id)

    # for each admin friend - find it in userFriendsList
    for adminFriend in relevantAdminFriends:
        friendList = userFriendsList[adminFriend]
        # for each friend's userFriendList, for each friend search its friends in relevantAdminFriends
        for friend in friendList:
            if friend != adminID:
                if friend in relevantAdminFriends:
                #if found, check if not already in DB, if not, insert to DB
                    dbhandler = DBhandler.DBhandler()
                    dbhandler.insertPair(friend,adminFriend)

                else:
                    # else - continue
                    continue
    return

def arrangeTables(listOfUsers, adminID):
    #get all relevant pairs from DB
    #send to algorithm and get result

    returnTablesJson = json.dumps('[{'
                                  'guests: ['
                                  '{name: shula, photo: "http://icons.iconarchive.com/icons/webalys/kameleon.pics/512/Woman-9-icon.png"},'
                                  '{name: shoshana, photo: "http://junglejobs.ru/assets/img/female-avatar.png"},'
                                  '{name: yaacov, photo: "https://cdn1.iconfinder.com/data/icons/user-pictures/100/male3-512.png"},'
                                  '{name: yoni, photo: "https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAXiAAAAJDk5NTVkYTVkLTU5MDYtNGIyYS05N2U1LWFkNzFhNzdjNmM2OA.jpg"},'
                                  '{name: Lili, photo: "https://cdn2.iconfinder.com/data/icons/pretty-office-10/512/Teacher-female-512.png"},'
                                  '{name: moshe, photo: "http://icons.iconarchive.com/icons/designbolts/free-male-avatars/128/Male-Avatar-Hair-icon.png"},'
                                  ']'
                                  '},'
                                  '{'
                                  'guestes: ['
                                  '{name: "roy", photo: "http://static.bigstockphoto.com/images/homepage/2016_popular_photo_categories.jpg"},'
                                  '{name: "israel", photo: "http://static.bigstockphoto.com/images/homepage/2016_popular_photo_categories.jpg"},'
                                  '{name: "adi", photo: "http://static.bigstockphoto.com/images/homepage/2016_popular_photo_categories.jpg"},'
                                  '{name: "yoav", photo: "http://static.bigstockphoto.com/images/homepage/2016_popular_photo_categories.jpg"},'
                                  '{name: "dan", photo: "http://static.bigstockphoto.com/images/homepage/2016_popular_photo_categories.jpg"},'
                                  '{name: "nisim", photo: "http://static.bigstockphoto.com/images/homepage/2016_popular_photo_categories.jpg"}'
                                  ']'
                                  '}]')

    return returnTablesJson


createPairs({2:[1,4,5], 3:[1,4,7], 4:[1,2,3]}, [2,3,4], 1)

