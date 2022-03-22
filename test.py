

inp = [1,1,1,1,1,1,1,1,1,1,1,1,9]


def max(l):
    # l.sort()
    if(sum(l)/2<l[len(l)-1]):
        l.remove(l[len(l)-1])
    elif(sum(l)%2==1):
        for i in l: 
            if i %2==1: 
                l.remove(i)
                break
    return int(sum(l)/2)

ans1=[]
ans2=[]


def bb(list,max):
    if(len(list)==0):
        return ans1,ans2
    a=list.copy()
    if(len(ans1)==0 and len(ans2)==0):
        ans1.append(a[len(a)-1])
        a.remove(a[len(a)-1])
    if(sum(ans1)==max and sum(ans2)==max) :
        return ans1,ans2
    elif(sum(ans1)<sum(ans2)):
        ans1.append(a[len(a)-1])
        a.remove(a[len(a)-1])
        return bb(a,max)
    elif(sum(ans1)>sum(ans2)):
        ans2.append(a[len(a)-1])
        a.remove(a[len(a)-1])
        return bb(a,max)
    else:
        if(max==0):
            return ans1,ans2
        else: 
            return bb(a,max-1)

def billboard(list):
    list1, list2 = bb(list, max(list))
    if sum(list1) == sum(list2):
        print(list1, list2)
        return sum(list1)
    return list

print(billboard(inp))
