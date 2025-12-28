marks={
    "Shrey": 98,
    "Rohan": 65,
    "Harshit": 23,
    0: "Harry"
 
}

#print(marks.items())
#print(marks.keys())
marks.update({"Shrey":99})
print(marks)

print(marks.get("Harry2")) #Prints none
print(marks["Harry2"]) #Returns an error