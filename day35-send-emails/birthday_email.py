import smtplib
import pandas as pd
import datetime as dt

current = dt.datetime.now()
data = pd.read_csv("birthdays.csv")
data_rows = data[(data["month"] == current.month) & (data["day"] == current.day)]

PLACEHOLDER = "[name]"
with open("letter.txt") as letter:
    template = letter.read()

my_email = "mina.rashidi.86@gmail.com"
my_password = "<REPLACE YOUR PASSWORD>"

for index, row in data_rows.iterrows():
    name = row["name"]
    to_email = row["email"]
    msg_body = template.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Happy Birthday {name} \n\n{msg_body}")

# Or another solution is using Tuple: this does not work with multiple people with the same birth dates
# current_tuple = (current.month, current.day)
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#
# if current_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[current_tuple]
#     PLACEHOLDER = "[name]"
#     with open("letter.txt") as letter:
#         template = letter.read()
#         msg_body = template.replace("[NAME]", birthday_person["name"])
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject: Happy Birthday {birthday_person["name"]} \n\n{msg_body}")
