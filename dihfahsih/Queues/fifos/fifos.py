from queue import Queue

#customer queue
checkout_queue=Queue()
checkout_queue.put('customer 1')
checkout_queue.put('customer 2')

next_customer=checkout_queue.get()

print(next_customer)

#Task Queue
task_queue=Queue()
task_queue.put("Task 1")
task_queue.put("Task 2")

next_task =task_queue.get()


    