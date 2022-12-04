import decision_tree
import basic_info
import database

x_train,x_test,y_train,y_test = basic_info.basic_info()

print("tree start")
tree_clf = decision_tree.decision_tree(x_train,x_test,y_train,y_test)

def ask():
    example = input("Hi, share what's in your mind:")
    tree_result = tree_clf.predict([example])[0]
    print("Your mood is "+ tree_result)
    song,artist,url=database.db_random(tree_result)
    print("We recommand you this song: "+song+"---"+artist+"   "+url)
    database.open_web(url)
    again()

def again():
    print("-------------------------")
    open = input("try again?(y/n)")
    if(open=='y'or open=='Y'):
        ask()
    elif(open=='n'or open=='N'):
        print("ok! enjoy your day")
    else:
        again()

ask()