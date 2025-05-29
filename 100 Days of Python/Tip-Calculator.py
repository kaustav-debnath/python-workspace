print("Welcome to the Tip Calculator!")
total_bill = input("What was the total bill?\t$")
tip = input("How much % tip would you like to give? 10, 12 or 15?\t")
participants_to_split = input("How many people to split the bill?\t")

total_final_bill = (1 + float(tip)/100) * float(total_bill)
# print(total_final_bill)
each_person_share = round(total_final_bill / int(participants_to_split),2)
print(f"Each Person should pay: ${each_person_share}")