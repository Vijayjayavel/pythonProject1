prompt = '\nenter the topping you want to add to your pizza'
prompt += '\n\ttopping name:'
active=True
while active:
    topping =input(prompt)
    if topping == 'quit':
        active=False
    else:
        print(topping + ' added to your pizza')