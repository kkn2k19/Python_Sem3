#Write a program in python that will accept 3 angles of the triangle and check that triangle is possible, 
#if possible then check that is it "Acute angled triangle"(All angle are < 90), 
#"Right angled triangle"(any one angle 90) or 
#"Obtuse angled triangle"(one of the angle > 90).
#Also print a "Triangle is not possible" if sum of all angles are not 180 degree.

angle1 = float (input ("Enter the 1st angle : "))
angle2 = float (input ("Enter the 2nd angle : "))
angle3 = float (input ("Enter the 3rd angle : "))
if angle1 + angle2 + angle3 == 180:
  if angle1 < 90 and angle2 < 90 and angle3 < 90:
    print("Acute angled triangle.")
  elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("Right angled triangle.")
  else:
    print("Obtuse angled triangle.")
else :
  print("Triangle is not possible.")
