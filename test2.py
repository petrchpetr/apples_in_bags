from pprint import pprint



def new_bag(apl,cnt=1):
    return {
            'apl': apl,
            'cnt': cnt
        }.copy()


bags=[]
runs=[]
prev_bag=new_bag(-1,0)
cur_bag=new_bag(-1,0)

def append_last_two(apl):
    global bags,prev_apl
    if len(bags) > 0 and apl == bags[-1]['apl']:
        bags[-1]['cnt'] += 1
    elif len(bags) > 1 and apl == bags[-2]['apl']:
        bags[-2]['cnt'] += 1
    else:
        bags.append(new_bag(apl))
        if len(bags)>2:
            run = {
                'apl1': bags[-2]['apl'],
                'apl2': bags[-3]['apl'],
                'sum': bags[-2]['cnt']+bags[-3]['cnt']
            }
            runs.append(run)
            print('RUNS',runs)
            if prev_apl == bags[-2]['apl']:
                bags.pop(-2)
            else:
                bags.pop(-3)
    prev_apl = apl


def append_two_bags(apl):
    global prev_bag,cur_bag
    if cur_bag['apl'] == apl:
        cur_bag['cnt'] += 1
        return
    if prev_bag['apl'] == apl:
        prev_bag['cnt'] += 1
        tmp = cur_bag
        cur_bag = prev_bag
        prev_bag = tmp
        return

    run = {
        'apl1': prev_bag['apl'],
        'apl2': cur_bag['apl'],
        'sum': prev_bag['cnt'] + cur_bag['cnt']
    }
    runs.append(run)
    print('RUNS',runs)

    prev_bag = cur_bag
    cur_bag = new_bag(apl)




def sort_apls(apls):
    global prev_bag,cur_bag
    if len(apls) < 2:
        raise Exception('not worth counting')
    

    for apl in apls:
        append_two_bags(apl)
        print(apl,prev_bag,cur_bag)



apls = [2, 2, 1, 2,1,2,1,1,2,2, 3, 3, 1, 3, 5,3,4,4,2,5,3,5,2,3,4,5,5]

sort_apls(apls)
print(apls)
pprint(runs)
