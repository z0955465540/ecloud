import flask
import pymysql
from flask import jsonify,render_template,request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["get"])
def home():
    return render_template('index.html')

# ========================== GET DATA ====================================

def db_init():
    db = pymysql.connect(host='localhost',user='porter',passwd='pn1234567890',db='ecloud')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db,cursor

@app.route("/first/<UsageAccountId>", methods=["get"])
def first(UsageAccountId) :
    db, cursor = db_init()
    sql = """
        SELECT DISTINCT product_ProductName ,  CONVERT(sum(lineItem_UnblendedCost),CHAR) FROM 
        ecloud.test where lineItem_UsageAccountId = '{}' group by product_ProductName; 
        """.format(UsageAccountId)
    cursor.execute(sql)
    count_data = cursor.fetchall()
    db.close()

    result = {}
    for i in range(len(count_data)):
        dict_key = count_data[i]["product_ProductName"]
        dict_key = "{%s}"%dict_key
        dict_val = count_data[i]['CONVERT(sum(lineItem_UnblendedCost),CHAR)']
        result[dict_key] = dict_val
    return jsonify(result)

@app.route("/second/<UsageAccountId>", methods=["get"])
def second (UsageAccountId) :
    db, cursor = db_init()
    sql = """
        SELECT product_ProductName as ProductName, 
        DATE_FORMAT(lineItem_UsageStartDate,'%Y-%m-%d') as StartDate,
        CONVERT(SUM(lineItem_UsageAmount),CHAR) as UsageAmount
        FROM ecloud.test where lineItem_UsageAccountId = '{}' 
        GROUP BY lineItem_UsageStartDate , product_ProductName 
        ORDER BY product_ProductName , lineItem_UsageStartDate; 
        """.format(UsageAccountId)
    cursor.execute(sql)
    count_data = cursor.fetchall()
    db.close()

    dict_1 = {}
    dict_3 = {}

    # 2-1 建一個Product的dict+list方便append
    for i in range(len(count_data)):
        ProductName = count_data[i]['ProductName']
        dict_1[ProductName]= []

    # 2-2 把同樣的Product值放進list
    for i in range(len(count_data)):
        ProductName = count_data[i]['ProductName']
        StartDate = count_data[i]["StartDate"]
        UsageAmount = count_data[i]['UsageAmount']
        dict_2 = {}
        dict_2[StartDate] = UsageAmount
        if dict_1[ProductName] == dict_1.get(ProductName):
            dict_1[ProductName].append(dict_2)

    # 2-3 轉成提交格式
    for k1,v1 in dict_1.items():
        dict_4 = {}
        key = "{%s}"%k1
        for i in range(len(v1)):
            for k2,v2 in v1[i].items():
                dict_4[k2] = v2  
        dict_3[key]=dict_4
  
    return jsonify(dict_3)    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)