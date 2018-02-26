##Jaehurn Nam
##jn1402
##Operating Systems
##Lab 3 Banker Simulation

import sys
import traceback
import copy
from collections import deque


#Class for Acitivity
class Activity:
    def __init__(self, activity_type, delay, resource_number):
        self.activity_type = activity_type
        self.delay = delay
        self.resource_number = resource_number

    def __str__(self):
        return str(vars(self))

    def set_initial_claim(self, claim):
        self.initial_claim = claim

    def get_initial_claim(self):
        return self.initial_claim

    def set_units_requested(self, req):
        self.units_requested = req

    def get_units_requested(self):
        return self.units_requested

    def set_units_released(self, rel):
        self.units_released = rel

    def get_units_released(self):
        return self.units_released

    def set_task_number(self, task_number):
        self.task_number = task_number

    def get_task_number(self):
        return self.task_number

#Class for resources
class Resource:
    def __init__(self, number, units):
        self.number = number
        self.units = units

    def __str__(self):
        return str(vars(self))

#Class for tasks
class Task:
    def __init__(self, number):
        self.number = number
        self.activity_index = 0
        self.has_terminated = False
        self.is_aborted = False
        self.activities = []
        self.completed_activities = []

        self.initial_claim = {}
        self.can_claim = {}

        self.resources_held = {}
        self.taken_time = 0
        self.waited_time = 0
        self.delay_before_terminating = 0


    def __str__(self):
        return str(vars(self))

    def get_activities(self):
        return self.activities

    def add_to_resources_held(self, resource, delay, units):
        try:
            self.resources_held[resource]['units'] += units
        except KeyError:
            self.resources_held[resource] = {}
            self.resources_held[resource]['units'] = units
            self.resources_held[resource]['time_remaining'] = delay
            pass


    def set_initial_claim(self, claim, resource_number):
        self.initial_claim[resource_number] = claim
        self.can_claim[resource_number] = claim

    def terminate(self):
        self.has_terminated = True


#Function to wrap the simulation of both algorithms
def simulation(tasks_and_resources, tasks_and_resources_copy, input_file):
    simulate_optimistic_manager(tasks_and_resources[0], tasks_and_resources[1])
    simulate_bankers(tasks_and_resources_copy[0],tasks_and_resources_copy[1],input_file)


# with open('input-01.txt') as f:
#   for line in f:
#     cleanedline = line.strip()
#     if cleanedline:
# ##      print(cleanedline)
#       if cleanedline.isdigit():
#         print("number")
#       else:
#         print("string")
#       tot.append(cleanedline)
# ##      c = f.read(1)
# ##      if not c:
# ##        print("End of file")
# ##        break
# ##      if c.isdigit():
# ##          print("Read a number character:", c)
# ##      else:
# ##          print("Read a string character:",c)

# fintot = []

# print(tot[1].split())

# for ele in tot:
#   fintot.append(ele.split())

# print("fintot",fintot)

# num_tasks = fintot[0][0]
# type_resc = fintot[0][1]
# num_resc = fintot[0][2]

# taskdict = dict.fromkeys(['task1','task2'])


# print(taskdict)


# counter = 0


# resource = {'type1':4}



# for elen in fintot[1:]:
#   if elen[0] == 'initiate':
#     if elen[1] == 1:
#       taskdict['task1'] = 'started'
#     elif elen[1] == 2:
#       taskdict['task2'] = 'started'
    

#   elif elen[0] == 'request':
    

#   elif elen[0] == 'terminate':

#   else:
#     print("wrong input")
# ##    

# f.close()





#State check for the code
state = False


operation_list = ['initiate','request','release','terminate']

#main function contains the run of tasks_and_resc and simulation of both algorithms
def main():
    args = sys.argv

    if (len(args) == 2):

        input_file = args[1]

        tasks_and_resources = create_tasks_and_resources(input_file)
        tasks_and_resources_copy = copy.deepcopy(tasks_and_resources)

        simulation(tasks_and_resources, tasks_and_resources_copy, input_file)

    else:
        print("Incorrect file format")
        quit()

#Function to put the task and resources into an easily readable format to use throughout the lab


def create_tasks_and_resources(input_file):

    tasks = {}
    ret_tasks = []
    resources = []

    try:
        line_counter = 0
        for line in open(input_file):
            cleanedline = line.strip()
            #clean up the line


            if line_counter != 0:
                task_details = cleanedline.split(' ')    
                task_details = list(filter(None, task_details))

            
                if (len(task_details) != 0):
                    a = 'b'

                else:
                    continue

            
                
                task_number = int(task_details[1])
        
                curr_activity = Activity(task_details[0], int(task_details[2]), int(task_details[3]))
                
                # variable_parameter = int(task_details[4])


                #this part checks which action the task is trying to do [initiate, request, release] and do the according operation
                if (task_details[0]== operation_list[0]):

                    curr_activity.set_initial_claim(int(task_details[4]))

                    
                    if int(task_details[1]) in tasks:
                        task = tasks[int(task_details[1])]
                        task.set_initial_claim(int(task_details[4]), int(task_details[3]))
                        task.activities.append(curr_activity)
                    else:
                        task = Task(int(task_details[1]))
                        task.activities.append(curr_activity)
                        task.set_initial_claim(int(task_details[4]), int(task_details[3]))
                        tasks[int(task_details[1])] = task


                elif (task_details[0] == operation_list[1]):
                    curr_activity.set_units_requested(int(task_details[4]))
                    task_to_add_to = tasks[int(task_details[1])]
                    task_to_add_to.activities.append(curr_activity)

                elif (task_details[0] == operation_list[2]):
                    curr_activity.set_units_released(int(task_details[4]))
                    task_to_add_to = tasks[int(task_details[1])]
                    task_to_add_to.activities.append(curr_activity)

                else:
                    task_to_add_to = tasks[int(task_details[1])]
                    task_to_add_to.activities.append(curr_activity)


            else:
                
                conf = cleanedline.split(' ')

            
                num_of_tasks = conf.pop(0)
                num_of_resc = conf.pop(0)

                # create our resource object

                for idx, resource_units in enumerate(conf):
                    task_number = idx + 1
                    units = int(resource_units)
                    r = Resource(task_number, units)
                    resources.append(r)



            line_counter = line_counter + 1
            #increment counter


        for task_number, task in tasks.items():
            ret_tasks.append(task)

        
        return [ret_tasks, resources]

    except IOError:
        print('Could not open file.')

    except Exception as e:
         tb = traceback.format_exc()
         print(tb)

#function to check if task has terminated
def tasks_still_running(tasks):

    for task in tasks:
        if not task.has_terminated:
            return True

    return False

#function to output for optimist
def output_result(tasks):

    tot_taken_time = 0
    tot_waited_time = 0

    for task in tasks:
        
        if (task.is_aborted == False):
            tot_taken_time = tot_taken_time + task.taken_time
            tot_waited_time = tot_waited_time + task.waited_time
            # increment()

            # percent = int(round(float(task.waited_time) / task.taken_time, 2) * 100)

            print('\t' + 'Task ' + str(task.number) + '\t\t' + str(task.taken_time) + '\t' + str(task.waited_time) + '\t' + str(int(round(float(task.waited_time) / task.taken_time, 2) * 100)) + '%')

        else:
            print('\t' + 'Task ' + str(task.number) + '\t\t' + 'aborted')


    if tot_taken_time != 0:
        print('\t' + 'Total ' + '\t\t' + str(tot_taken_time) + '\t' + str(tot_waited_time)  + '\t' + str(int(round(float(tot_waited_time)/tot_taken_time, 2) * 100)) + '%')
        print('\n')
    else:
        print('\t' + 'Total ' + '\t\t' + str(tot_taken_time) + '\t' + str(tot_waited_time)  + '\t' + '0' + '%')
        print('\n')




#function for easy incrementation
# def increment():
#     tot_taken_time
#     tot_waited_time

#     tot_taken_time = tot_taken_time + task.taken_time
#     tot_waited_time = tot_waited_time + task.waited_time


#Function to check if the state is deadlocked
def deadlocked(tasks, task_queue):
    
    if (len(task_queue) < len(tasks)):
        return False
    else:
        return True


#simulation of optimistic manager
# since it is optimistic, we use a simple fifo structure

def simulate_optimistic_manager(tasks, resources):

    task_queue = deque([])

    cycle_counter = 0

    taskq_length = len(task_queue)

    #keep running when not aborted/terminated
    while tasks_still_running(tasks):
        
        for task in task_queue:
            task.waited_time = task.waited_time + 1
            #wait time added

       
        for task in tasks:
            if task.is_aborted or task.has_terminated:
                task.taken_time = task.taken_time + 1
                task.waited_time = task.waited_time + 1
                continue


            current_activity = task.get_activities()[0]

            
            if (current_activity.activity_type == operation_list[0]):
                task.taken_time = task.taken_time + 1
                completed = task.get_activities().pop(0)  
                task.completed_activities.append(completed)

                #Data updated

                continue

            elif (current_activity.activity_type == operation_list[1]):
                task.taken_time = task.taken_time + 1
                resource_idx = current_activity.resource_number - 1
                units = current_activity.units_requested
                #get the number of units requested and remaining
                
                #Checking if task_queue is empty
                if (taskq_length != 0):
                    
                    next_task = task_queue[0]

                    if (task != next_task):
                        task_queue.append(task)
                        continue

                    else:
                        #check if we have enough units remaining to give the requested amount
                        if (units > resources[resource_idx].units):
                            task_queue.append(task)

                        else:
                            task_queue.popleft()
                            resources[resource_idx].units -= units
                            task.add_to_resources_held(resource_idx, current_activity.delay, units)

                            completed = task.get_activities().pop(0)

                            
                            task.completed_activities.append(completed)

                            #now this task is added to the completed activities

                else:
                    
                    if (units > resources[resource_idx].units):
                        task_queue.append(task)

                    else:
                        resources[resource_idx].units -= units
                        task.add_to_resources_held(resource_idx, current_activity.delay, units)
                        completed = task.get_activities().pop(0)
                        task.completed_activities.append(completed)


            elif (current_activity.activity_type == operation_list[2]):
                task.taken_time = task.taken_time + 1
                resource_idx = current_activity.resource_number - 1
                remaining_time = task.resources_held[resource_idx]['time_remaining']


                #update time taken, rescource index, and remaining time
                
                #if there is remaining time
                if (remaining_time != 0):
                    task.resources_held[resource_idx]['time_remaining'] -= 1
                    continue

                #no remaining time
                else:
                    #no delay
                    if (current_activity.delay <= 0):
                        units = current_activity.units_released
                        return_resource = resources[resource_idx]

                        return_resource.units += units

                        task.resources_held[current_activity.resource_number - 1] = {}


                        completed = task.get_activities().pop(0)
                        task.completed_activities.append(completed)
                        continue

                    else:
                        task.resources_held[resource_idx]['time_remaining'] = current_activity.delay
                        task.resources_held[resource_idx]['time_remaining'] -= 1
                        current_activity.delay = 0
                        continue

            elif (current_activity.activity_type == operation_list[3]):

                remaining_time = task.delay_before_terminating

                #there is remaining time
                if (remaining_time != 0):
                    task.taken_time = task.taken_time + 1
                    task.delay_before_terminating -= 1
                    continue

                else:
                    if (current_activity.delay <= 0):
                        task.has_terminated = True
                        completed = task.get_activities().pop(0)
                        #if there is no delay, terminated and completed
                        task.completed_activities.append(completed)
                        continue

                    else:
                        task.taken_time = task.taken_time + 1
                        task.delay_before_terminating = current_activity.delay
                        task.delay_before_terminating -= 1
                        current_activity.delay = 0
                        continue
                        #if there is delay, update by increments and decrements.



            #if deadlocked, keep backtracking until out of the deadlock
            while(deadlocked(tasks, task_queue)):
                
                lowest = sys.maxsize
                for t in tasks:
                    if(t.number < lowest) and not t.is_aborted:
                        lowest = t.number

                task_to_abort = tasks[lowest - 1]
                task_to_abort.is_aborted = True
                task_to_abort.has_terminated = True

                
                for key, value in task_to_abort.resources_held.items():
                    if value:
                        return_resource = resources[key]
                        return_resource.units += value['units']


                task_queue = list(filter(lambda x: x.number is not lowest, task_queue))
                task_queue = deque(task_queue)

        cycle_counter = cycle_counter + 1

    print('                          ' + 'FIFO' + '               ')
    output_result(tasks)

def simulate_bankers(tasks, resources, file_name):
    #implement a fifo manner

    orig_resc = copy.deepcopy(resources)
    
    task_queue = deque([])

    cycle_counter = 0


    #while task is not terminated
    while tasks_still_running(tasks):

        cycle_release = []


        taskq_length = len(task_queue)
        if (taskq_length > 0):
            if (state):
                print('\n')
                print('Checking to see if blocked requests can be satisfied')

            next_task = task_queue[0]

            
            resource_idx = next_task.get_activities()[0].resource_number - 1
            units = next_task.get_activities()[0].units_requested
            #chekcing if grant is available

        
            if (state):
                print('Requesting to unblock task ' + str(next_task.number) + ' ..')

            can_grant = check_if_next_state_is_safe(tasks, resources, next_task, next_task.get_activities()[0].delay, resource_idx, units)

            

            if (can_grant == False):
                if (state):
                    print('Left task ' + str(task.number) + ' blocked. Grant is not safe.')
            else:
                if (state):
                    print('Unblocked task ' + str(next_task.number) + ' and granted resources')

                next_task.taken_time = next_task.taken_time + 1
                task_queue.popleft()

                current_activity = next_task.get_activities()[0]

        
                resources[resource_idx].units -= units
                next_task.can_claim[resource_idx + 1] -= units

                next_task.add_to_resources_held(resource_idx, current_activity.delay, units)

                completed = next_task.get_activities().pop(0)
                next_task.completed_activities.append(completed)

                #update of information


        #update time wiated
        for task in task_queue:
            task.waited_time += 1

        #iterate through our task array
        for task in tasks:
            
            if task.is_aborted or task.has_terminated:
                continue

            current_activity = task.get_activities()[0]

            
            if (current_activity.activity_type == operation_list[0]):

                resource_idx = current_activity.resource_number - 1

                if (task.initial_claim[resource_idx + 1] > orig_resc[resource_idx].units):

                    print('Task ' + str(task.number) + ' aborted because the claim exceeds total amount in system')
                    task.is_aborted = True
                    task.has_terminated = True

                
                    for key, value in task.resources_held.items():
                        if value:
                            return_resource = resources[key]
                            return_resource.units += value['units']

                
                    continue


                task.taken_time = task.taken_time + 1



                #check for state
                if (state):
                    print('Task ' + str(task.number) + ' initiated.')

                completed = task.get_activities().pop(0)
                task.completed_activities.append(completed)

                #completed activities updated
                continue

            elif (current_activity.activity_type == operation_list[1]):

                task.taken_time = task.taken_time + 1

                #check the queue
                if task in task_queue:
                    continue

                
                resource_idx = current_activity.resource_number - 1
                units = current_activity.units_requested
                #get the information about resources

                # print("Task can claim: ")
                # print(task.can_claim)
                # print(task.can_claim[1])

                #checking if task should be aborted
                if (units > task.can_claim[1]):
                    task.is_aborted = True
                    task.has_terminated = True

                    
                    for key, value in task.resources_held.items():
                        if value:
                            return_resource = resources[key]
                            return_resource.units += value['units']

                #check state
                if (state):
                    print('Requesting for task ' + str(task.number) + ' ..')

                

                can_grant = check_if_next_state_is_safe(tasks, resources, task, current_activity.delay, resource_idx, units)
                

                #check grantability
                if (can_grant == False):
                    if (state):
                        print('Request for task ' + str(task.number) + ' blocked.')

                    task.waited_time = task.waited_time + 1
                    task_queue.append(task)

                else:
                    if (state):
                        print('Request for task ' + str(task.number) + ' granted.')

                    
                    resources[resource_idx].units -= units
                    task.can_claim[resource_idx + 1] -= units
                    task.add_to_resources_held(resource_idx, current_activity.delay, units)
                    completed = task.get_activities().pop(0)
                    task.completed_activities.append(completed)

 
            elif (current_activity.activity_type == operation_list[2]):

                resource_idx = current_activity.resource_number - 1
                remaining_time = task.resources_held[resource_idx]['time_remaining']
                

                #check for remaining time
                if (remaining_time != 0):
                    task.resources_held[resource_idx]['time_remaining'] -= 1
                    continue

                else:
                    
                    #check if there is delay
                    if (current_activity.delay <= 0):

                        units = current_activity.units_released
                        return_resource = resources[resource_idx]

                        release_dict = {}
                        release_dict['units'] = units
                        release_dict['resource'] = return_resource
                        release_dict['task'] = task
                        release_dict['current_activity'] = current_activity

                        cycle_release.append(release_dict)
                        continue

                    else:

                        task.resources_held[resource_idx]['time_remaining'] = current_activity.delay
                        task.resources_held[resource_idx]['time_remaining'] -= 1
                        current_activity.delay = 0
                        continue

            elif (current_activity.activity_type == operation_list[3]):

                remaining_time = task.delay_before_terminating

                
                #check if there is remaining time
                if (remaining_time != 0):
                    task.taken_time = task.taken_time + 1
                    task.delay_before_terminating -= 1
                    continue

                else:
                    if (current_activity.delay <= 0):
                        task.has_terminated = True
                        completed = task.get_activities().pop(0)
                        task.completed_activities.append(completed)
                        continue

                    else:
                        task.taken_time = task.taken_time + 1
                        task.delay_before_terminating = current_activity.delay
                        task.delay_before_terminating -= 1
                        current_activity.delay = 0
                        continue

        #iterate through the release array
        for release in cycle_release:
            task = release['task']
            units = release['units']
            return_resource = release['resource']
            current_activity = release['current_activity']
            task.taken_time = task.taken_time + 1

            #check for state
            if (state):
                print('Releasing resources for task ' + str(task.number) + ' ..')
            return_resource.units += units

            task.resources_held[current_activity.resource_number - 1]['units'] = 0
            task.resources_held[current_activity.resource_number - 1]['time_remaining'] = 0

            completed = task.get_activities().pop(0)
            task.completed_activities.append(completed)


        cycle_counter = cycle_counter + 1

    # output_bankers(tasks)

    print('                         ' + "BANKER's" + '    ')
    output_result(tasks)


def check_if_next_state_is_safe(tasks, resources, task, delay, resource_idx, units):
    tasks_copy = copy.deepcopy(tasks)
    resources_copy = copy.deepcopy(resources)
    task_copy = copy.deepcopy(task)

    #Check if we have enough resources available


    if (units > resources_copy[resource_idx].units):
        return False

    #Update information as would happen when it was granted
    resources_copy[resource_idx].units -= units
    task_copy.can_claim[resource_idx+1] -= units
    task_copy.add_to_resources_held(resource_idx, delay, units)
    completed = task_copy.get_activities().pop(0)
    task_copy.completed_activities.append(completed)
    tasks_copy[task_copy.number - 1] = task_copy
    tasks_copy = list(filter(lambda x: not x.is_aborted, tasks_copy))
    #Check if all this is possible
    possible = [0] * len(tasks_copy)


    task_length = len(tasks_copy)
    resources_length = len(resources_copy)

    for i in range(task_length):
        for j in range(task_length):
            if (not possible[j]):
                check = 1
                for k in range(resources_length):
                    if (tasks_copy[j].can_claim[k + 1] > resources_copy[k].units):
                        check = 0
                if (check == 1):
                    possible[j] = 1
                    for key, v in tasks_copy[j].resources_held.items():
                        resources_copy[key].units = resources_copy[key].units + v['units']

    if (sum(possible) != len(tasks_copy)):
        return False
    else:
        return True


main()
