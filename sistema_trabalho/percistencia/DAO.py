from abc import ABC, abstractclassmethod
import pickle

class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource, 'rb'))


    def salvar(self, key, obj):
        self.__object_cache[key] = obj
        self.__dump()

    def chamar(self, key):
        try:
            return self.__object_cache[key]
        except KeyError:
            return None

    def remover(self, key):
        try:
            del(self.__object_cache[key])
            self.__dump()
        except KeyError:
            return None

    def chamar_todos(self):
        return self.__object_cache.values()