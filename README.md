## API


* **URL**

  http://examecloudture.ddns.net/{question}/{lineitem/usageaccountid}

* **Method:**

	`GET`
  
*  **URL Params**

	**Required:**
 
	`question= first or second`

	`lineitem/usageaccountid= lineitem/usageaccountid`

*  **Success Response:**

  * **Code:** 200 <br />
    **Params = first** <br />
	**Content:** 
    ```JSON
        {
            "{AWS CloudTrail}": "0.0000000000", 
			"{AWS Cost Explorer}": "9.8700000000", 
			"{AWS Key Management Service}": "0.0000270000", 
			"{AWS Premium Support}": "4569.0400000000", 
			"{Amazon DynamoDB}": "0.0000001745", 
			"{Amazon Elastic Compute Cloud}": "8914.1195000000", 
			"{Amazon Simple Storage Service}": "2.6955128726", 
			"{AmazonCloudWatch}": "0.0000102907", 
			"{Savings Plans for AWS Compute usage}": "0.0000000000"
        }
    ```
 
  * **Code:** 200 <br />
    **Params = second** <br />
	**Content:** 
    ```JSON
        {
		    "{AWS CloudTrail}": {
		        "2020-04-01": "105.0000000000",
		        "2020-04-02": "455.0000000000",
		        "2020-04-03": "409.0000000000",
		        "2020-04-04": "90.0000000000",
		        "2020-04-05": "261.0000000000",
			...
		    },
		    "{AWS Cost Explorer}": {
		        "2020-04-01": "35.0000000000",
		        "2020-04-02": "6.0000000000",
		        "2020-04-03": "11.0000000000",
		        "2020-04-04": "11.0000000000",
		        "2020-04-05": "6.0000000000",
			...
		    },
		    "{AWS Key Management Service}": {
		        "2020-04-10": "7.0000000000",
		        "2020-04-27": "2.0000000000"
		    },
		    "{AWS Premium Support}": {
		        "2020-04-01": "102586.7800000000"
		    },
		    ...
		}
    ```
	

*  **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{}`  

## DB

* **schema**

	| Column Name | Datatype |
	| ----------- | -------- |
	| id | int(11) AI PK |
	| bill_PayerAccountId | varchar(45) |
	| lineItem_UnblendedCost | decimal(20,10) |
	| lineItem_UnblendedRate | decimal(20,10) |
	| lineItem_UsageAccountId | varchar(45) |
	| lineItem_UsageAmount | decimal(20,10) |
	| lineItem_UsageStartDate | varchar(45) |
	| lineItem_UsageEndDate | varchar(45) |
	| product_ProductName | varchar(255) |
	
## Framework

*  **Front-End**

  * **HTML、CSS、JavaScript_Jquery** <br />

<br />

*  **Back-End**

  * **Python_Flask、MYSQL** <br />

## Services

*  **AWS-EC2 Ubuntu Server 20.04 LTS (HVM), SSD Volume Type**
