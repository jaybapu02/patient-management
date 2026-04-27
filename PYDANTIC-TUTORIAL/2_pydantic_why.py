from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of the patient",description="Give the name of the patient in less that 50 chars",examples=["jaychandra,pinky"])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int=Field(gt=0,lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)] #kg
    height:Annotated[float,Field(gt=0,strict=True)] #mtr
    married:Annotated[bool,Field(default=None,description="Is the patient married or unmarried")]
    allergies:Optional[List[str]]=Field(default=None,max_length=5)
    contact_details:Dict[str,str]
    
    @field_validator("email")
    @classmethod
    def email_validater(cls,value):
        valid_domins=["hdfc.com","icici.com"]
        # abc@gamil.com
        domain_name=value.split("@")[-1]
        
        if domain_name not in valid_domins:
            raise ValueError("not a valid domain")
        return value
    
    @field_validator("name")
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age>60 and "emergency" not in model.contact_details:
            raise ValueError("Patient is older than must have emergency contact number.")
        return model
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
        
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("weight",patient.weight)
    print("height",patient.height)
    print("BMI",patient.calculate_bmi)
    print("Inserted")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("updated")
    
patient_info={"name":"jaychandra","email":"abc@hdfc.com","linkedin_url":"https://www.linkedin.com/in/jaychandra-das-739a00243","age":65,"weight":80.2,"height":1.70,"contact_details":{"phone":"9692244008","emergency":"6370119583"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)