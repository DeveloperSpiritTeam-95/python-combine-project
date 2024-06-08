# dictionaries are used to store key value paired
# they are unordered, mutable (changeable) and don't allow duplicate keys 
dict = {
    "kay":"value",
    "name":"prabhakar",
    "age":25,
    "salary":50000.0,
    "gender":'Male',
    "marks":[90,95,89,70,30],
    "tuple":(50,70,50,30),
    "languages":{"lang1":"English","lang2":"Telugu"}
}
print(dict)

dict["name"] = "sudhakar"
print(dict)

print("languages:",dict["languages"])

dict["surename"] = "Kimavath"
print(dict)


# nested dictionary

student = {
    "name":"prabha",
    "subjects":{
        "Telugu":89,
        "physics":90,
        "english":69,
        "chemistry":99,
        "biology":79
    }
} 

print("student: ",student)
print("student chemistry sub marks: ",student["subjects"]["chemistry"])
# student["surename"] = "Kimavath"
print(student.keys())
print(student.values())
print(student.items())
print("Name: ",student.get("name"))
print("Sub: ",student.get("subjects"))

print(list(student))
print(list(student)[1])
print(len(list(student)))

student.update({"city":"hyderabad"})
print(student)
print(student.get("city"))

practiceDir = {
    "table":["peace of furniture","list of facts and figures"],
    "cat":"a small animal"
}

print(practiceDir)
print(list(practiceDir)[0])
print(len(list(practiceDir)))
