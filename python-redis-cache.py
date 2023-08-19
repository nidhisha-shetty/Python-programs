import redis
r = redis.Redis(host='localhost', port=6379,db=0) #connecting to redis server
r.set('France', 'Paris') #setting redis key('France') and value('Paris')
r.set('India', 'Delhi')
india_capital = r.get('India') #getting value of a redis key
print(india_capital) 

'''
Steps to install redis
1. pip install redis
2. sudo apt-get install redis-server
Start redis
1. on terminal run 'redis-cli' command 
2. run 'keys *' command to get all keys
3. run 'GET <key-name>' command to get the value of key
'''
