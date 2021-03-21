import mysql.connector

DEBUG = False

myconn = mysql.connector.connect(host="localhost", user="root", passwd="1234567", database="FRLS")
cursor = myconn.cursor()

class Student:
    def __init__(self, studentId):
        query = "SELECT student_id, `info.name`, `info.email_addr`, `info.admitted_year`, `info.dept_id`\
                 FROM Student WHERE student_id=" + str(studentId)
        
        cursor.execute(query)
        
        result = cursor.fetchall()[0]
        self.username = result[0]
        self.name = result[1]
        self.email_addr = result[2]
        self.admitted_year = result[3]
        self.dept_id = result[4]
        
        if DEBUG:
            print(self.username, self.name, self.email_addr, self.admitted_year, self.dept_id)
        

class Course:
    #results is displayed as a list of tuples
    def __init__(self, studentId):
        query = "SELECT S.name, S.type, S.zoom_link, TI.weekday, TI.start_time, TI.duration, TI.building_name, TI.room_number, \
                        M.name AS 'Material', M.released_date, M.link, I.name, I.title, I.office, I.office_hour \
                 FROM (SELECT * FROM Take T1 WHERE T1.student_id="+str(studentId)+") T,\
                                    Section S , Time TI, Material M, \
                                    (SELECT I2.name, I2.title, I2.office, I2.office_hour, T2.course_id, T2.section_id FROM Teach T2, Instructor I2 WHERE T2.instructor_id=I2.instructor_id) I\
                                    WHERE T.course_id=S.course_id AND T.section_id=S.section_id \
                                    AND T.course_id=TI.course_id AND T.section_id=TI.section_id \
                                    AND T.course_id=M.course_id AND T.section_id=M.section_id \
                                    AND T.course_id=I.course_id AND T.section_id=I.section_id"
        cursor.execute(query)
        results = cursor.fetchall()
        self.course_name = [result[0] for result in results]
        self.course_type = [result[1] for result in results]
        self.zoom_link = [result[2] for result in results]
        self.weekday = [result[3] for result in results]
        self.start_time = [result[4] for result in results]
        self.duration = [result[5] for result in results]
        self.building_name = [result[6] for result in results]
        self.room_number = [result[7] for result in results]
        self.material_name = [result[8] for result in results]
        self.material_date = [result[9] for result in results]
        self.material_link = [result[10] for result in results]
        self.instructor = [result[12] + result[11] for result in results]
        self.office = [result[13] for result in results]
        self.office_hour = [result[14] for result in results]
        
        if DEBUG:
            print(self.instructor)
            print(self.duration)
            print(self.material_link, self.material_name)



if __name__ == '__main__':
    #Test code purpose
    student = Student(1)
    course = Course(1)