import ActionController 
import Strings

def sanitize_command(command):
    tokens=command.strip().split(" ")
    return filter(None,tokens)

def parse_command(command):
    tokens=command.strip().split(" ")
    action=tokens[0].upper()
    parameters=tokens[1:]
    return action, parameters
   

def execute_command(command,store):
    action,parameters=parse_command(command)
    if not ActionController.is_valid_action(action):
        print(Strings.error,action)
        return True
    return ActionController.execute_action(store,action,parameters)