class DataValidator:
    def __init__(self):
        self.errors=[]
    def validate_email(self,email):
        if '@' not in email:
            self.errors.append(f"Invalid email:{email}")
            return False
        return True
    
    def validate_age(self,age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age:{age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

validator = DataValidator()
validator.validate_email("mohamedasif3417gmail.com")
validator.validate_age(80)
print(validator.get_errors())




        
