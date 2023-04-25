# Pricing Model Using Gradient Boosting Regressor
Python script that recommended next-period prices that maximize total firm profits = total sales x (price - per-unit cost).

This project involves creating a Python script that will output recommended prices for the next period, with the goal of maximizing total firm profits. The algorithm takes into account accurate predictions of market conditions and per-unit costs in the next period, as well as detailed information about past and present market conditions, own and competitor prices, own per-unit costs, own sales, and market share performance. It is possible to use new inputs or combinations of inputs to improve the algorithm.

The algorithm is designed and trained using data from 55 markets, with information for each period and market including the price of the firm being optimized for, their per-unit costs, total units sold, sales share, competitor prices, and a variable summarizing market conditions. The raw data also includes a period and market identifier. For more detailed information on the variables in the raw data, please refer to the provided description.

Description of variables in data:

• “Mkt_id” - identifier for the market

• “Output_date” - identifier for the period (day)

• “Output_own_price” - own price set in the period (day)

• “Output_own_cost” - own per-unit cost of goods sold for the period

• “Output_comp_price” - average of competitor prices in the period

• “Output_X” - a variable summarizing market conditions in the period (on a scale between 0 and 100)

• “Output_own_sales” - own sales in the period

• “Output_own_share” - own sales share in the period

• “Output_own_profits” - own total profits in the period


Output data example:

mkt_id	output_date	output_own_price	output_own_cost	output_comp_price	output_own_profits	output_X	output_own_share	output_own_sales
44	01jan2019	7.05	5.9	7.11	15.065	42.8	.5152673	13.1
44	02jan2019	7.05	6.05	7.11	24.31	36.14	.5570819	24.31
44	03jan2019	7.05	5.98	7.28	30.78391	34.34	.5799217	28.77
44	04jan2019	7.05	5.98	7.28	20.1695	36.32	.5427674	18.85
44	05jan2019	6.79	6.07	6.68	1.2312	44.06	.4947566	1.71<img width="742" alt="image" src="https://user-images.githubusercontent.com/109412337/234283197-6ec37d59-027a-4aa4-947c-cb79761ac72d.png">
