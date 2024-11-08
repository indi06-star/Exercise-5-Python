# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits=["apple", "avocado" ,"orange"]

# TODO: Add a fruit to the end of the list
fruits.append("grape")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"cherry")
# TODO: Remove a fruit from the list
fruits.remove("avocado")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations
# TODO: Create a list of numbers from 1 to 5
numbers=[ 1 , 2 , 3 , 4 ,5]

# TODO: Create a new list with each number squared
numbers_squared=[]
for number in numbers:
    numbers_squared.append(number*number)
print(numbers_squared)

# TODO: Find the sum and average of the original numbers
sum_numbers=sum(numbers)
average_numbers=sum_numbers/len(numbers)

# TODO: Print the results
print(sum_numbers)
print(average_numbers)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries
# TODO: Create a dictionary of countries and their capitals
country_cap= {
    "South Africa" : "Cape Town",
    "Canada" : "Ottawa",
    "Cameroon" :"Yaounde",
    "Germany" : "Berlin",
    "Japan" :"Tokyo" ,

}

    

# TODO: Add a new country-capital pair
country_cap.update({"France" :"Paris" })
    

# TODO: Update the capital of an existing country
country_cap.update({"South Africa" :"Pretoria"}) 

# TODO: Remove a country-capital pair
country_cap.pop("Germany")

# TODO: Print the modified dictionary
print(country_cap)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations
# TODO: Create a dictionary of fruit colors
fruit_colours = {

    "Strawberry" : "red",
    "Orange" : "orange",
   "Banana" : "yellow",
    "Apple" : "green",
}
# TODO: Print all the fruits (keys)
for key in fruit_colours:
    print(key)

# TODO: Print all the colors (values)

for values in fruit_colours:
    print(fruit_colours[values])

# TODO: Print each fruit and its color
for key,value in fruit_colours.items():
    print(key,value)

# TODO: Check if a fruit is in the dictionary and print its color

for key in fruit_colours: 
    if key == "Strawberry":
     print(fruit_colours[key])