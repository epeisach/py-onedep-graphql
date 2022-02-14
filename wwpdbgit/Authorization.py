# Retrieves authorization for a query

class Authorization(object):
      def __init__(self):
      	    self.__auth=None

      def readFile(self, fpath):	
            with open(fpath, "r") as fin:
                  self.__auth = fin.readline().strip()

      def getBearer(self):
            ret = "Bearer " + self.__auth
            return ret


if __name__ == "__main__":
      a = Authorization()
      a.readFile(".auth")
      
