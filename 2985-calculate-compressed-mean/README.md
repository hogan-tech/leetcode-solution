<h2><a href="https://leetcode.com/problems/calculate-compressed-mean/">2985. Calculate Compressed Mean</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Orders</code></p>

<pre>+-------------------+------+
| Column Name       | Type |
+-------------------+------+
| order_id          | int  |
| item_count        | int  |
| order_occurrences | int  |
+-------------------+------+
order_id is column of unique values for this table.
This table contains order_id, item_count, and order_occurrences.
</pre>

<p>Write a solution to calculate the <strong>average</strong> number of items per order, rounded to <code>2</code> <strong>decimal places</strong>.</p>

<p>Return <em>the result table</em><em> in <strong>any</strong> order</em><em>.</em></p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Orders table:
+----------+------------+-------------------+
| order_id | item_count | order_occurrences | 
+----------+------------+-------------------+
| 10       | 1          | 500               | 
| 11       | 2          | 1000              |     
| 12       | 3          | 800               |  
| 13       | 4          | 1000              | 
+----------+------------+-------------------+
<strong>Output</strong>
+-------------------------+
| average_items_per_order | 
+-------------------------+
| 2.70                    |
+-------------------------+
<strong>Explanation</strong>
The calculation is as follows:
 - Total items: (1 * 500) + (2 * 1000) + (3 * 800) + (4 * 1000) = 8900 
 - Total orders: 500 + 1000 + 800 + 1000 = 3300 
 - Therefore, the average items per order is 8900 / 3300 = 2.70</pre>
</div>