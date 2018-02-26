##jn1402
##Jaehurn Nam

import sys, os
import copy
from collections import deque
from operator import itemgetter
from functools import reduce


def main():
    random_numb = read_random_numbs()
    input_filename = ''
    verbose = False

    if (len(random_numb) == 0):
        print('Random number not read.')
        quit()

    if (len(sys.argv) >= 4):
        print("too many arguments!")
        quit()

    if (len(sys.argv) == 3):
        if (sys.argv[1] != '--verbose'):
            print("Incorrect Usage!")

        else:
            verbose = True
            input_file = sys.argv[2]
    if (len(sys.argv) == 2):
            input_file = sys.argv[1]

    read_start(input_file, verbose, random_numb)





def read_random_numbs():
    numbs = []
    file_name = 'random-numbers.txt'
    
    with open(file_name) as f:
        for num in f:
            strip = num.rstrip()
            if '\n' not in strip:
                numbs.append(strip)
        return numbs
        

def randomOS(U, random_numb):
    return 1 + (int(random_numb.pop(0)) % U)


def array_partition(arr, upbound):
    return [arr[x:x+upbound] for x in range(0, len(arr), upbound)]

def read_start(input_file, verbose_flag, random_numb):
    with open(input_file) as ff:
        process_objs = create_process_objs(ff)
        simulation(process_objs, verbose_flag, random_numb, input_file)


def create_process_objs(file_data):
    total_processes = 0

    for line in file_data:
        counter = 0;
        process_obj = {}
        process_delin = []

        newline = line.split(' ')

        for num in newline:

            if (counter == 0):
                counter+=1
                total_processes = num
                continue

            if (num == '\n' or num == ''):
                continue

            if (num.isalpha()):
                break

            process_delin.append(num)

        cleaned_processes = list(filter(lambda x: x is not ' ', process_delin))


        if (len(cleaned_processes) % 4 is not 0):
            print('Bad input, not divisible by 4')
            quit()

        partitioned_data = array_partition(cleaned_processes, 4)
        break


    process_objs = []

    for proc in partitioned_data:
        process_obj = {}
        process_obj['A'] = int(proc[0])
        process_obj['B'] = int(proc[1])
        process_obj['C'] = int(proc[2])
        process_obj['IO'] = int(proc[3])
        process_obj['state'] = 'unstarted'
        process_obj['remainCPUB'] = 0
        process_obj['remainingIOB'] = 0
        process_objs.append(process_obj)

    return process_objs


def print_board(row, column, ll):

    b = len(l)

    for i in ll:
        print('+-'*(b)+'+')
        row = '|'
        for j in i:
            row += j+'|'
        print(row)
    print('+-'*(b)+'+')

    print()

    

def user(ll,a,row):
    user = int(input(''))

    new = ll[a-1]

    c=1

    if ll[0][user-1] == ' ':
        while True:
            if new[user-1] == ' ':
                new[user-1]='X'
                break
            else:
                new = ll[a-c]
            c+=1
    elif ll[0][user-1] != ' ':
        j = row-1
        while j>=1:
            j = int(j)
            ll[j][user-1]=ll[j-1][user-1]
            j -= 1
        ll[0][user-1]='X'
            

    print('')
    print('Renewing ...')
    print('')
 
    
#
def computer(ll,column,a):

    print('Computer is randomly making a choice.')
    comp = random.randint(1,column)
    new = ll[a-1]

    d=1

    if ll[0][comp-1] == ' ':
        while True:
            if new[comp-1] == ' ':
                new[comp-1]='O'
                break
            else:
                new = ll[a-d]
            d+=1
    elif ll[0][comp-1] != ' ':
        j = row-1
        while j>=1:
            j = int(j)
            ll[j][comp-1]=ll[j-1][comp-1]
            j -= 1
        ll[0][comp-1]='O'

    print('')
    print('Renewing ...')
    print('')


def winner(row,column):

    s=0
    d=0


    
    for y in range(0,column):
        for x in range(0,row-3):            
            if ll[x][y]==ll[x+1][y]==ll[x+2][y]==ll[x+3][y]=='X':
                s=1
            elif ll[x][y]==ll[x+1][y]==ll[x+2][y]==ll[x+3][y]=='O':
                d=1
    
    for x in range(0,row):
        for y in range(0,column-3):
            if ll[x][y]==ll[x][y+1]==ll[x][y+2]==ll[x][y+3]=='X':
                s=1
            elif ll[x][y]==ll[x][y+1]==ll[x][y+2]==ll[x][y+3]=='O':
                d=1
                
    
    if s + d >=2:
        print()
        return True
    elif s + d == 1:
        if s ==1:
            print()
            return True
        elif d==1:
            print()
            return True

    return False





def move(self, board):
    if self.name in board.board[self.location]['occupants']:
        board.board[self.location]['occupants'].remove(self.name)
    die = random.randint(2,12)

    spaces = die
    print('The number of moves you got is: ', spaces)
    for giraffe in range(spaces-1):
        self.location += 1
        self.fuel -= 1
        self.location = int(self.location) % len(board.board)
        
        
        if len(board.board[self.location]['next']) > 2:
            
            zebra = board.board[self.location]['next'].split(';')
            
            
            loclist = []
            for x in zebra:
                x = int(x)
                loclist.append(x)

            orbitq = input()

            
            if orbitq == 'Y':
                self.location = loclist[1]
   
  
            else:
                self.location = loclist[0]
  

        if self.location == 0:
            self.money += 500

    
    board.board[self.location]['occupants'].append(self.name)
       
                   


def pay_rent(self):
    renttopay = board.board[self.location]['rent']
    
    if self.money < renttopay:
        board.board[self.location]['owner'].money += self.money
        self.active = False
    else:
        board.board[self.location]['owner'].money += renttopay
        self.money -= renttopay
        

def buy_fuel(self):
    fcost = board.board[self.location]['fuel'].strip('*')
    print(' ', self.fuel)
    famt = int(self.fuel)

 
    
    if fcost:
        print(' ' + fcost)
        while famt:
                ffu = int(input(''))
                if 0 < ffu:
                    newfuel = int(ffu) * int(fcost)
                    self.money -= int(newfuel)
                    self.fuel += ffu
                    other = board.board[self.location]['owner']
                    other.money += int(newfuel)
                    break
                    
                else:
                    print('')


    else:
        if not fcost:
            print('')

        if famt == 0:
            self.active = False


def buy_property(self):
    prp = board.board[self.location]
    prpurchase = board.board[self.location]['purchase']


    if prpurchase:
        pfu = input('Would you like to buy the property? (Y/N): ')
        if not board.board[self.location]['owner']:
            if pfu == 'Y':
                if self.money >= int(prpurchase):
                    self.money -= int(prpurchase)
                    board.board[self.location]['owner'] = self
                    self.owned.append(self.location)
                else:
                    print()
    else:
        print()

def exponentiate(base, power):
    if power == 0:
        return 1
    else:
        return base * exponentiate(base, power-1)
        
def get_nth(list_of, n):
    if n == 0:
        return helpers.head(list_of)
    else:
        return get_nth(helpers.tail(list_of), n-1)

def reverse(list_of):
    if list_of == [] :
        return []
    else:
        return reverse(helpers.tail(list_of)) + [ helpers.head(list_of) ]


def is_older(date_1, date_2):
    if date_1 == []:
        return False
    elif helpers.head(date_1) > helpers.head(date_2):
        return True
    elif helpers.head(date_1) < helpers.head(date_2):
        return False
    else:
        return is_older(helpers.tail(date_1),helpers.tail(date_2))


def exponentiate2(base, power):
    if power == 0:
        return 1
    else:
        return base * exponentiate(base, power-1)
        
def get_nth2(list_of, n):
    if n == 0:
        return helpers.head(list_of)
    else:
        return get_nth(helpers.tail(list_of), n-1)

def reverse2(list_of):
    if list_of == [] :
        return []
    else:
        return reverse(helpers.tail(list_of)) + [ helpers.head(list_of) ]


def is_older2(date_1, date_2):
    if date_1 == []:
        return False
    elif helpers.head(date_1) > helpers.head(date_2):
        return True
    elif helpers.head(date_1) < helpers.head(date_2):
        return False
    else:
        return is_older(helpers.tail(date_1),helpers.tail(date_2))




def  simulation(process_objs, verbose_flag, random_numb, input_file):

    orig_line = procobjs2str(process_objs)
    process_objs.sort(key=itemgetter('A'), reverse=False)

    
    LCFS = LCFS_sch(process_objs, random_numb, orig_line, verbose_flag)

    print(LCFS)
    print('\n\n\n')



def gen_cycle_output(deep_procs_copy, curr_cycle):
    ret = 'Before cycle\t' + str(curr_cycle) + ': \t';
    for idx, proc in enumerate(deep_procs_copy):
        burst = ''

        if (proc['state'] != 'running'):
            burst = str(proc['remainingIOB'])
        else:
            burst = str(proc['remainCPUB'])

        

        if (idx != len(deep_procs_copy)-1):
            ret += (str(proc['state']) + ' ' + burst + ' ')
        else:
            ret += (str(proc['state']) + ' ' + burst + '.')


    return ret


def all_procs_term(process_objs):
    count = 0
    for process in process_objs:
        if (process['state'] == 'terminated'):
            count+=1

    return count is len(process_objs)

def process_object_to_string(proc):
    ret = '('
    ret += str(proc['A']) + ','
    ret += str(proc['B']) + ','
    ret += str(proc['C']) + ','
    ret += str(proc['IO']) + ')'
    return ret

def procobjs2str(process_objs):
    ret = str(len(process_objs)) + '  '
    for proc in process_objs:
        ret += (str(proc['A'])  + ' ')
        ret += (str(proc['B']) + ' ')
        ret += (str(proc['C']) + ' ')
        ret += (str(proc['IO']) + '  ')

    return ret



def LCFS_sch(process_objs, random_numb_global_copy, orig_line, verbose_flag):
    
    random_numb = copy.deepcopy(random_numb_global_copy)
    
    proc_data = []

    run_data = {}
    run_data['CPU_util'] = 0
    run_data['IO_util'] = 0

    for idx, proc in enumerate(process_objs):
        proc_data.append({})
        proc_data[-1]['finish_time'] = 0
        proc_data[-1]['wait_time'] = 0
        proc_data[-1]['IO_time'] = 0
        proc_data[-1]['A'] = proc['A']

    
    output = 'The original input was: ' + orig_line + '\n'
    output += 'The sorted input is: ' + procobjs2str(process_objs) + '\n'

    if (verbose_flag == True):
        output += 'The following is the detailed printout!\n\n'

    deep_proc_copy = copy.deepcopy(process_objs)
    output_all_cycles = []
    readystk = []
    curr_proc = None


    
    curr_cycle = 0
    while(not all_procs_term(deep_proc_copy)):
        
        cycle_output = gen_cycle_output(deep_proc_copy, curr_cycle) + '\n'

        
        for idx, process in enumerate(deep_proc_copy):

            if (process['A'] == curr_cycle and process not in readystk and process['state'] == 'unstarted'):
        
                if (curr_proc == None):
                    if (len(readystk)!= 0):
                        process['state'] = 'ready'
                        readystk.append(process)
                        continue

                    else:
                        process['state'] = 'running'
                        CPU_burst = randomOS(process['B'], random_numb)

                        if (CPU_burst > process['C']):
                            process['C'] = CPU_burst

                        process['reaminCPUB'] = CPU_burst
                        curr_proc = process
                        continue

                else:
                    process['state'] = 'ready'
                    readystk.append(process)
                    continue




            if (process['state'] == 'running'):
                process['reaminCPUB'] -= 1
                process['C'] -= 1
                run_data['CPU_util'] += 1
                process['modified'] = True

                if (process['C'] == 0):
                    process['state'] = 'terminated'
                    proc_data[idx]['finish_time'] = curr_cycle
                    continue

                if (process['reaminCPUB'] == 0):
             
                    set_to_blocked = True

                    if (set_to_blocked == False):
                        process['state'] = 'ready'
                        readystk.append(process)
                        continue

                    else:
                        process['state'] = 'blocked'
                        IO_burst = randomOS(process['IO'], random_numb)
                        process['remainIOB'] = IO_burst
                        continue


            if (process['state'] == 'blocked'):
                process['remainIOB'] -= 1
                run_data['IO_util'] += 1
                proc_data[idx]['IO_time'] += 1
                process['modified'] = True

                if (process['remainIOB'] == 0):
                    

                    set_to_running = True

                    for p in deep_proc_copy:
                        if (p['state'] == 'running' and p['modified']):
                            set_to_running = False;
                            break
                        if (p['state'] == 'running' and not p['modified'] and p['reaminCPUB'] != 1):
                            set_to_running = False;
                            break

                 
            

                    if (set_to_running == False):
                        process['state'] = 'ready'
                        readystk.append(process)
                        continue
                    else:
                        process['state'] = 'running'
                        CPU_burst = randomOS(process['B'], random_numb)

                        if (CPU_burst > process['C']):
                            process['C'] = CPU_burst

                        process['reaminCPUB'] = CPU_burst
                        curr_proc = process
                        continue


            if (process['state'] == 'ready'):
                proc_data[idx]['wait_time'] += 1
               
                next_process_up = readystk[-1]


                if (process != next_process_up):
                    continue

                else:
                    set_to_running = True

                    for p in deep_proc_copy:
                        if (p['state'] == 'running' and p['modified']):
                            set_to_running = False
                            break

                        if (p['state'] == 'running' and not p['modified'] and p['reaminCPUB'] > 1):
                            set_to_running = False
                            break

       


                    if (set_to_running == False):
                        continue
                    else:
                        readystk.pop()

                        process['state'] = 'running'
                        CPU_burst = randomOS(process['B'], random_numb)


                        if (CPU_burst > process['C']):
                            process['C'] = CPU_burst

                        process['reaminCPUB'] = CPU_burst
                        curr_proc = process
                        process['modified'] = True

                        continue


        curr_cycle += 1

        for process in deep_proc_copy:
            process['modified'] = False

        if (verbose_flag):
            output += cycle_output

    run_data['finish_time'] = curr_cycle

    tot_wait = 0
    tot_turn = 0

    for data_obj in proc_data:
        tot_wait += data_obj['wait_time']
        tot_turn += (data_obj['finish_time'] - data_obj['A'])

    run_data['average_wait'] = str(float(tot_wait)/len(proc_data))
    run_data['average_turnaround'] = str(float(tot_turn)/len(proc_data))

    output += '\nThe scheduling algorithm: Last Come First Served\n\n'

    for idx, process in enumerate(process_objs):
        output+= ('Process ' + str(idx) + ':\n')
        output+= ('\t(A,B,C,IO) = ' + process_object_to_string(process) + '\n')
        output+= ('\tFinishing time: ' + str(proc_data[idx]['finish_time']) + '\n')
        output+= ('\tTurnaround time: ' + str(int(proc_data[idx]['finish_time']) - int(process['A'])) + '\n')
        output+= ('\tI/O time: ' + str(proc_data[idx]['IO_time']) + '\n')
        output+= ('\tWaiting time: ' + str(proc_data[idx]['wait_time']) + '\n')
        output+= '\n'

    output+= 'Summary Data:\n'
    output+= '\tFinishing time: ' + str(run_data['finish_time'] - 1) + '\n'
    output+= '\tCPU Utilization: ' + str( float(run_data['CPU_util']) / (run_data['finish_time']-1)) + '\n'
    output+= '\tI/O Utilization: ' + str( float(run_data['IO_util']) / (run_data['finish_time']-1)) + '\n'

    throughput = 100 * float(orig_line[0])/(float(run_data['finish_time'])-1)
    output = output +  '\tThroughput: ' + str(throughput) + ' processes per hundred cycles' + '\n'


    output+= '\tAverage turnaround time: ' + str(run_data['average_turnaround']) + '\n'
    output+= '\tAverage waiting time: ' + str(run_data['average_wait']) + '\n'

 
    return output



main()
