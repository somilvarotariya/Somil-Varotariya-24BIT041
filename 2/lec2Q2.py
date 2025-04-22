def ls3():

  a= int(input("enter first number:"))
  b= int(input("enter second number:"))
  c= int(input("enter third number:"))
  lrg=a
  if b>lrg:
      lrg=b
  if c>lrg:
      lrg=c

  sml=a
  if b>sml:
      sml=b
  if c>sml:
      sml=c

  if lrg==sml:
      print("all values are same")
  else:
      print(lrg,"largest",sml,"smallest")

ls3()
