import mysql.connector

DEBUG = False

myconn = mysql.connector.connect(host="localhost", user="root", passwd="010207", database="db")
cursor = myconn.cursor()


class Student:
    def __init__(self, studentId):
        query = "SELECT student_id, `info.name`, `info.email_addr`, `info.admitted_year`, `info.dept_id`, `last_login`,`last_logout`,`duration`,`password`\
                 FROM Student WHERE student_id=" + str(studentId)

        cursor.execute(query)

        result = cursor.fetchall()[0]
        self.username = result[0]
        self.name = result[1]
        self.email_addr = result[2]
        self.admitted_year = result[3]
        self.dept_id = result[4]
        self.last_login = result[5]
        self.last_logout = result[6]
        self.duration = result[7]
        self.password = result[8]

        if DEBUG:
            print(self.username, self.name, self.email_addr, self.admitted_year, self.dept_id)


class Course:
    # results is displayed as a list of tuples
    def __init__(self, studentId):
        query = "SELECT S.name, S.type, S.zoom_link, TI.weekday, TI.start_time, TI.duration, TI.building_name, TI.room_number, \
                        M.name AS 'Material', M.released_date, M.link, I.name, I.title, I.office, I.office_hour, M.message, C.name, T.this_sem, D.date, D.time, D.event\
                 FROM (SELECT * FROM Take T1 WHERE T1.student_id=" + str(studentId) + ") T, Deadline D,\
                                    Section S , (SELECT * FROM Time NATURAL JOIN Room) TI, Course C, \
                                    (SELECT temp.course_id, temp.section_id, temp.material_id, temp.name, temp.released_date, temp.link, Message.message FROM (SELECT Section.course_id, Section.section_id, Material.material_id, Material.name, Material.released_date, Material.link FROM \
                                     Material RIGHT OUTER JOIN Section ON Material.course_id = Section.course_id AND Material.section_id = Section.section_id) temp LEFT OUTER JOIN Message \
                                     ON Message.course_id = temp.course_id AND Message.section_id = temp.section_id) M,\
                                    (SELECT I2.name, I2.title, I2.office, I2.office_hour, T2.course_id, T2.section_id FROM Teach T2, Instructor I2 WHERE T2.instructor_id=I2.instructor_id) I\
                                    WHERE T.course_id=S.course_id AND T.section_id=S.section_id \
                                    AND T.course_id=TI.course_id AND T.section_id=TI.section_id \
                                    AND T.course_id=M.course_id AND T.section_id=M.section_id \
                                    AND T.course_id=I.course_id AND T.section_id=I.section_id \
                                    AND T.course_id=C.course_id AND T.course_id = D.course_id \
                                    AND T.section_id = D.section_id"
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
        self.message = [result[15] for result in results]
        self.course_long_name = [result[16] for result in results]
        self.this_sem = [result[17] for result in results]
        self.ddldate = [result[18] for result in results]
        self.ddltime = [result[19] for result in results]
        self.ddlevent = [result[20] for result in results]

        if DEBUG:
            print("course_name", self.course_name)
            print("name", self.course_long_name)
            print("type", self.course_type)
            print("zoom", self.zoom_link)
            print("weekday", self.weekday)
            print("instructor", self.instructor)
            print("start_time", self.start_time)
            print("material_name", self.material_name)
            print("message", self.message)


if __name__ == '__main__':
    # Test code purpose
    student = Student(4)
    course = Course(4)
    print(student.username)
