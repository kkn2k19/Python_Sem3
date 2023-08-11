#Write a program to input the cost price and the selling price is more than the cost price then 
#calculate and display actual profit and profit per cent otherwise, calculate and display actual loss and loss per cent. 
#If the cost price and the selling price are equal, the program displays the message 'Neither Profit notr Loss'.

cp = float (input("Enter the cost price : "))
sp = float (input("Enter the selling price : "))
if cp > sp:
  loss = cp - sp
  print("Loss : ", loss)
  loss_percent = loss/cp*100
  print("Loss % : ", loss_percent)
elif sp > cp:
  profit = sp - cp
  print("Profit : ", profit)
  profit_percent = profit/cp*100
  print("Profit % : ", profit_percent)
else :
  print("Neither Profit nor Loss.")
