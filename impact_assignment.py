import math
def subs(all_subs,counter,n,arr,cur_ab_count,allowed):
    if n==counter:
        all_subs.append(''.join(arr.copy()))
        return
    arr.append("A")
    if cur_ab_count+1<allowed: # To keep the consec absent day limit in check and to optimize the code
        subs(all_subs,counter+1,n,arr,cur_ab_count+1,allowed)
    arr.pop()
    arr.append("P")
    subs(all_subs,counter+1,n,arr,0,allowed)
    arr.pop()

if __name__=="__main__":
    n=int(input())
    # days_off=int(input()) for a generic solution
    days_off=4
    all_subsets=[]
    # all_possible_ways=int(math.pow(2,n))
    subs(all_subsets,0,n,[],0,days_off)
    print("All possible cases: ",len(all_subsets))
    ans=0
    for i in all_subsets:
        if i[-1]=="A":
            ans+=1
    print("Missing days: ",ans)
    print(ans,"/",len(all_subsets))
    # print(all_subsets)