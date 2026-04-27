def insert_patient_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError("Age can't be nagative")
        else:
            print(name)
            print(age)
            print("inserted data into database")
    else:
        raise TypeError("Incorrect Data type")

def update_patient_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError("Age can't be negative")
        else:
            print(name)
            print(age)
            print("updated")
    else:
        raise TypeError("Incorrect Data type")
    
insert_patient_data("jaychandra",-56)