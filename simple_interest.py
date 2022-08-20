#Write a python script to calculate simple interest

Amount=int(input('Enter Amount : '))
Time=int(input('Enter Duration : '))
Rate=int(input('Enter Rate of Interest : '))

interest=(Amount*Time*Rate)/100
print('Simple Interest : ',interest)