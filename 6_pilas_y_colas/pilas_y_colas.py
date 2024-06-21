# Pilas(stacks) y colas
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

 # pop
stack_item = stack[len(stack) -1]
del stack[len(stack) -1]
print(stack_item)

# Con la funcion pop
print(stack.pop())
print(stack)

# Cola/Queue
queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

#dequeue
print(queue.pop(0))
print(queue)



