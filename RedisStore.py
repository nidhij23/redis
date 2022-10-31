import Strings
class RedisStore:
    
    def __init__(self):
        self.__storage_map={}
        self.__temp_storage_map=self.__storage_map
        self.__start_transaction=False

    def pick_storage(self):
        if self.__start_transaction:
            return self.__temp_storage_map
        else:
           return self.__storage_map

    def set_key(self,key,value):
        storage=self.pick_storage()
        storage[key]=value
        return None,True
    
    def get_key(self, key):
        storage=self.pick_storage()
        if key in storage:
            result=storage[key]
        else:
            result="NULL"
        return result, True

    def unset_key(self,key):
        storage=self.pick_storage()
        if key in storage:
            del storage[key]
        return None,True
    
    def count_keys_with_value(self,value):
        count=0
        storage=self.pick_storage()
        for key in storage.keys():
            if storage[key]==value:
                count+=1
        result=count
        return result,True

    def begin_transaction(self):
        self.__start_transaction=True
        return None, True

    def commit_transaction(self):
        result=None
        if self.__start_transaction is False:
            result= Strings.no_transaction
        else:
            self.__storage_map=self.__temp_storage_map
            return result,True
        

    def rollback_transaction(self):
        result=None
        if self.begin_transaction is False:
            result=Strings.no_transaction
        else:
            self.__temp_storage_map=self.__storage_map
            self.__start_transaction= False
        return result,True

    def kill_store(self):
        return None,False
