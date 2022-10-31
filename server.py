from RedisStore import RedisStore
import controllers.CommandController as CommandController
import Strings as Strings



def read_from_console(store):
    print(Strings.server_started)
    next=True
    while next:
        command=input(Strings.next_line)
        if command:
            try:
                next=CommandController.execute_command(command,store)
            except Exception as e:
                print(Strings.error,e)

if __name__=="__main__":
    store=RedisStore()
    read_from_console(store)