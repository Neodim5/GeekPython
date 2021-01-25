class Operations:
    '''
    Deccription for class
    '''
    class_name: str
    class_attr: int = 100

    @staticmethod
    def lower_string(content: str):
        return content.lower()

    @staticmethod
    def upper_string(content: str):
        return content.upper()

    @classmethod
    def normalize(cls, content):
        cls.lower_string(content)
        cls.upper_string(content)


temp_string = "Hellow"
print(Operations.lower_string(temp_string))
print(Operations.upper_string(temp_string))

print(Operations)
print(Operations.__dict__)
print(Operations.__annotations__)
print(Operations.__doc__)