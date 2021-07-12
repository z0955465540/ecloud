from resources import load_data,store

datapath = "C:\\Users\\Porter\\hw-backend-api-enhancement-master\\data\\output.csv"
user = 'porter'
passwd = 'pn1234567890'
host = '13.115.186.148'
port = '3306'
schema = 'ecloud'
table = 'test'

store.create_database(host=host,user=user,passwd=passwd,schema=schema)
store.create_table(host=host,user=user,passwd=passwd,schema=schema,table=table)
df = load_data.load_data(datapath)
store.data_to_mysql(user=user,passwd=passwd,host=host,port=port,schema=schema,df=df,table=table)