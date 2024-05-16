import os
import datetime 
import matplotlib.pyplot as plt

# the all classes and it's methods are under development 
class ReadingStatics(object):
    """on each load of  pdf file this class will be called, 
    and will contain all the information of the particular book read with date"""
    def __init__(self) -> None:
        
        self.file_name = os.path.join(os.path.dirname(__file__),"reading_statics.csv")
        self.read_books = {}
       

    def file_data(self,file_name)    :
        self.open_time = datetime.datetime.now() 
        # print('adding filename', datetime.datetime.strptime(open_time, "%d %b %Y %H:%M:%S.%f"))
        # print(open_time.time())
      
        if file_name not in self.read_books:
            self.read_books[file_name] = {"openTime":self.open_time.time()}
        # else:
        #     self.save_statistics(endTime=open_time)

    def save_statistics(self,file_name):
        """saves the statistics values e.g. date, book name, start time, end time, duration"""
        print("saving stats")
        endTime = datetime.datetime.now()
        if file_name  in self.read_books:
            self.read_books[file_name]["endTime"] = endTime.time()
            duration = self.open_time -  endTime
            self.read_books[file_name]["duration"] = duration
        print(duration)
        self.addDataToJson()

    def addDataToJson(self):
        # if os.path.exists(self.file_name):
            with open(self.file_name,"w") as file:
                json.dump(self.read_books)
    def show_data(self):
        print("book details : ...")
        print(self.read_books)
        for key,val in self.read_books.items():
            print(key , end=" : ")
            for k,v in val.items():
                print(k,v)

    def plot_statistics(self, filename: str):
        "plot the statistics of the saved file reading_statics.csv"""
        # use matplotlib for graphs
        pass




def main():
    stat = ReadingStatics()
    stat.file_data("file1")
    stat.save_statistics("file1")
    # stat = ReadingStatics()
    stat.file_data("file2")
    stat.save_statistics("file2")
    stat.file_data("file3")
    stat.save_statistics("file3")
    stat.show_data()


if __name__=="__main__":
    main()
