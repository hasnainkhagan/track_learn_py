# Create a small coding program that includes your daily problem in which you can use Python conditions.

temperature = int(input("Enter the current temperature in °C: "))
is_raining = input("Is it raining? (yes/no): ")
has_important_event = input("Do you have an important event? (yes/no): ")

if temperature < 10:
    outfit = "Wear a heavy coat and warm clothes."
elif 10 <= temperature <= 20:
    outfit = "Wear a light jacket or sweater."
else:
    outfit = "Wear comfortable summer clothes."

if is_raining == "yes":
    outfit += " Don't forget an umbrella or a raincoat!"

if has_important_event == "yes":
    outfit += " Also, wear something formal or suitable for the event."

print("\nRecommendation:")
print(outfit)
