class FunctionAssignment1:
    def SubfieldsinAI ():
        names=["Machine learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for lists in names:
            print(lists)
    def OddEven():
        num=int(input("Enter the number:"))
        if (num%2==0):
            print("The number is Even")
        else:
            print("The number is Odd")
    def MarriageEligibility():
        gender=input("Enter your Gender:")
        age=int(input("Enter your Age:"))
        if((gender=="Male" or gender=="Female") & (age>=21 or age>=18)):
            print("Eligible")
        else:
            print("Not Eligible")
    def triangle():
        height=int(input("Height:"))
        base=int(input("Base:"))
        side1=int(input("Side1:"))
        side2=int(input("Side2:"))
        side3=int(input("Side3:"))
        Area=(height*base)/2
        Perimeter=side1+side2+side3
        print("Area=",Area)
        print("Perimeter=",Perimeter)