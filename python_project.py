while True:
    n=int(input('No Of Pieces: '))
    if 360%2==0:
        print('Yes, cake can be cut into {} equal pieces'.format(n))
    else:
        print('No, cake cant be cut into {} equal pieces'.format(n))
    if n<=360:
        print('Yes, cake can be cut into {} piece of any size'.format(n))
    else:
        print('No, cake cant be cut into {} piece of any size'.format(n))
    if n*(n+1/2)<=360:
        print('Yes, cake can be cut into {} pieces such that no two of them are equal'.format(n))
    else:
        print('No, cake cant be cut into {} pieces such that no two of them are equal'.format(n))
    print()
    ans=input('Do you want to continue??(y/n):  ').lower()
    if ans=='y':
        continue
    else:
        break
