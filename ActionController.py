
from RedisStore import RedisStore as store

actions_mapping = {
    "GET" : store.get_key,
    "SET" :store.set_key,
    "UNSET" :store.unset_key ,
    "NUMEQUALTO": store.count_keys_with_value,
    "BEGIN": store.begin_transaction,
    "COMMIT": store.commit_transaction,
    "ROLLBACK": store.rollback_transaction,
    "END" : store.kill_store
}

def is_valid_action(action):
    if action in actions_mapping:
        return True
    else:
        return False

def execute_action(store,action,parameters):
    result,next_command=actions_mapping[action](store,*parameters)
    if result is not None:
        print(result)
    return next_command

