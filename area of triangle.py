choice_check = input("enter the type of triangle. (equilateral/isosceles/right triangle): ")

if choice_check == "equilateral":
    lenght_of_side = int(input("enter the lenght of the side of triangle: "))
    area_equilateral = 0.433 * lenght_of_side * lenght_of_side
    print("area of equilateral triangle is: ", area_equilateral)

elif choice_check == "isosceles":
    height_of_triangle = int(input("height of the traingle: "))
    base_of_the_triangle = int(input("enter base of triangle: "))
    area_isosceles = 0.5 * height_of_triangle * base_of_the_triangle
    print("area of isosceles triangle is: ", area_isosceles)

else:
    height_of_right_triangle = int(input("height of right triangle: "))
    base_of_right_triangle = int(input("lenght of base of triangle:"))
    area_right_triangle = 0.5 * height_of_right_triangle * base_of_right_triangle
    print("area of right triangle: ", area_right_triangle)

