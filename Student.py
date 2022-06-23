class Student:

    def __init__(self, fname, lname, id, major, minor, year, gpa):
        self.__fname = fname
        self.__lname = lname
        self.__id = id
        self.__major = major
        self.__minor = minor
        self.__year = year
        self.__gpa = gpa
    
    # get methods
    def get_fname(self):
        return self.__fname
    
    def get_lname(self):
        return self.__lname
    
    def get_id(self):
        return self.__id
    
    def get_major(self):
        return self.__major
    
    def get_minor(self):
        return self.__minor
    
    def get_year(self):
        return self.__year
    
    def get_gpa(self):
        return self.__gpa
    
    # set methods
    def set_fname(self, fname):
        self.__fname = fname
    
    def set_lname(self, lname):
        self.__lname = lname
    
    def set_id(self, id):
        self.__id = id
    
    def set_major(self, major):
        self.__major = major
    
    def set_minor(self, minor):
        self.__minor = minor
    
    def set_year(self, year):
        self.__year = year
    
    def set_gpa(self, gpa):
        self.__gpa = gpa
    
    
student = Student("Bob", "Ross", 666, "Art", "Philosphy", "Senior", 4.0)
print(student.get_fname(), 
    student.get_lname(), 
    student.get_id(), 
    student.get_major(), 
    student.get_minor(), 
    student.get_year(), 
    student.get_gpa(), 
    sep="\n")