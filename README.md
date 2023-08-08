# LibraryManagement

Project Requirements:


1)Install python

2)Install tkinter library

    pip install tk
  
3) Install mysql connector library
   
    pip install mysql-connector-python

   
The following tables are made inside the mysql database named comproj12

1) USERS

        user_ID,user_type,user_name,phone_no,address,email,identification_type,identification_no,password

2) BOOK_DETAILS

        BOOK_CODE,TITLE,CATEGORY,AUTHOR,PUBLICATION,PUBLISH_DATE,EDITION,PRICE,RACK_NO,ARRIVAL_DATE,SUPPLIER_ID

3) MEMBER

        MEMBER_ID,NAME,PHONE_NO,ADDRESS,EMAIL,IDENTIFICATION_TYPE,IDENTIFICATION_NO

4) ISSUE_RETURN

        Membership_ID,Book_ID,Issue_date,Due_date,Return_date,Charges,Fine
