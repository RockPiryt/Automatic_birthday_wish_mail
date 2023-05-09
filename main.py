import datetime as dt
import pandas
import smtplib
import random


MY_EMAIL= "pythonermail@gmail.com"
APP_PASSWORD_GMAIL ="guzkxmnkxvcwwzen"#kod do aplikacji z gmail
PLACEHOLDER = f"[NAME]"

##################### CODE ######################
#read csv file with person, who has birthday
data = pandas.read_csv("birth_dates.csv")
print(data)#dataframe


#create a key for searching through dict
#tuple with today month and day - it will be a key which we use to seach in dict from csv
now = dt.datetime.now()
now_month = now.month
now_day = now.day

today_tuple = (now_month, now_day)# key!!!! for value in birth_dict
# print(today_tuple)
##################INFO###########################
for (index, row) in data.iterrows():
    month = row["month"]
    print(month)

#####
#row_0 = data[column[index"]=index]
row_0 = data[data["nr"]==0]#Test     pythonermail@gmail.com  2023      5    9 
# row atribute 
user_1 = row_0["name"]#test
print(user_1)
####################################################################


# #create new dict with tuple as key
#iterrows działa tylko z data in Dateframe nie dict
# # new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birth_dict = {(row["month"],row["day"]): row for (index, row) in data.iterrows()}
#index=0 - row["month"] =5 
#index=1 - row["day"] = 7

#check if today date is in birth_dict
if today_tuple in birth_dict:
    #read info about person (whole row) using key (date tuple)
    birthday_person= birth_dict[today_tuple] #odczyt row za pomocą klucza
    #read atributes from birthday_person(whole row)
    birthday_person_name = birthday_person["name"]
    reciver = birthday_person["email"]
    #choose random letter and personalise letter (change name)
    random_number = random.randint(1,3)
    print(random_number)
    with open(f'letter_templates/letter_{random_number}.txt') as letter_file:
        picked_letter = letter_file.read()
        personalised_letter = picked_letter.replace(PLACEHOLDER, birthday_person_name)

    #send letter
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD_GMAIL)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=reciver, msg=f"Subject: Happy Birthday!\n\n{personalised_letter}" )
