# GetMaxProfitAPI

1. Pass JSON input data i.e. Movies and their Start and End dates. Get JSON output i.e. Optimal Selection of Movies for Maximum Profit.
2. For this API greedy algorithm was used. Sorted the movies by their end dates and picked movies such that end of a selected movie does not clash with the start of another.

## How to Run the API?

0. Ensure Python is installed.
1. Download the code from https://github.com/ritzdevp/MoviesProfitAPI
2. cd into MoviesProfitAPI-master. 
3. In the command line type and enter 
```sh
python app.py
```
The app will be running at http://127.0.0.1:5000/get_max_profit_API
4. Now you can pass the JSON input data in two ways.
 
#### Method 1: Pass the data via command line using curl.
#
```sh
curl -d '{"Bala": {"name": "Bala", "start": "0108", "end": "0128"}, "Rock": {"name": "Rock", "start": "0120", "end": "0130"}}' -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/get_max_profit_API
```
#### Method 2: Pass the data via a JSON POST/GET tool for example Insomnia or Postman. Below is a screenshot of passing JSON data request via Insomnia and getting the response back.
#
### Note:
### In the JSON input, enter start and end dates as a string. For example, if the start date is 30 Jan then declare "start":"0130" (month, then day)


![alt text](https://github.com/ritzdevp/MoviesProfitAPI/blob/master/ssinsomnia.png)




#### Sample Input JSON
```
{
	"Bala": {
		"name": "Bala",
		"start": "0108",
		"end": "0128"
	},
	"Rock": {
		"name": "Rock",
		"start": "0120",
		"end": "0130"
	},
	"PolicyMaker": {
		"name": "PolicyMaker",
		"start": "0129",
		"end": "0216"
	},
	"Brave": {
		"name": "Brave",
		"start": "0202",
		"end": "0214"
	},
	"Drive": {
		"name": "Drive",
		"start": "0210",
		"end": "0218"
	},
	"Race": {
		"name": "Race",
		"start": "0215",
		"end": "0228"
	}
}
```


