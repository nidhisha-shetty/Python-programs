import redis
r = redis.Redis(host='localhost', port=6379,db=0) #connecting to redis server
r.set('France', 'Paris') #setting redis key('France') and value('Paris')
r.set('India', 'Delhi')
india_capital = r.get('India') #getting value of a redis key
print(india_capital) 
