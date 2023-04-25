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

<img width="742" alt="image" src="https://user-images.githubusercontent.com/109412337/234283197-6ec37d59-027a-4aa4-947c-cb79761ac72d.png">
