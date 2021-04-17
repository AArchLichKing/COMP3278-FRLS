# COMP3278-FRLS
Course project for COMP3278 DBMS. Targeting on automatic login system by face recogniton. 

To use this project, first clone the repository to your own machine by

`git clone https://github.com/AArchLichKing/COMP3278-FRLS.git`

Then to capture your own image run

`python faceCapture.py`

Later train the model by 

`python train.py`

Finally open the main page by

`python main.py`

If you are new version of main function, run 

`python main.py` and click Register New Student. 

Note that the home page can display information only when you are a student with legal student_id (username) i.e. your information is stored in the database. 

![ER diagram](createDB.png)
