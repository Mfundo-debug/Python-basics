import sys
if __name__ == '__main__':
    for idx, arg in enumerate(sys.argv):
       print("Argument #{} is {}".format(idx, arg))
    print ("No. of arguments passed is ", len(sys.argv))