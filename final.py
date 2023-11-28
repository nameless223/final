def rectangle():
    leng=input("Enter the length value other than zero ")
    leng=valid(leng,"Length")
    width=int(input("Enter the width value other than zero "))          #func for area of rectangle
    width=valid(width,"Width")
    are=leng*width
    print("The area is:",are)
def triangle():
    base=int(input("Enter the base value other than zero "))
    base=valid(base,"base")
    height=int(input("Enter the height value other than zero "))        #func for calculating area of triangle
    height=valid(height,"height")
    are=0.5*base*height
    print("The area is:",are) 
def circle():
    rad=int(input("Enter the radius of the circle rather than zero "))      #func for calculating radius
    rad=valid(rad,"Radius")
    radi=3.14*rad**2
    print("The radius is:",radi)
    
def valid(check,what):
    V=False
    while V==False:
        try:
            check=float(check)
            if check <=0:
                print(what,"has to be greater than 0. Please reenter:")
                check=input()
                continue
            else:
                V=True
        except ValueError:
            print(what,"cannot be a string. Please reenter:")
            check=input()
    return check
            
def main():
    cont = "Y"
    while cont == "Y":
        shape = input("Enter a shape to calculate area (rectangle, triangle, circle):")
        shape.lower
        

        if shape == "rectangle":            
                rectangle()
            

        elif shape == "triangle":                      
                triangle()
            

        elif shape == "circle":
                circle()        
        

        cont=input("Would you like to run again?(Y or N)")
        cont.upper
main()       



        #rectangle area = L * W
        #triangle area = 1/2 b*w
        #circle area= pie r squared