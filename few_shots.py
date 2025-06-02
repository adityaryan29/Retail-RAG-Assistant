few_shots = [
    {
        'Question': "How many t-shirts do we have left for Nike in extra small size and white color?",
        'SQLQuery': "SELECT * FROM t_shirts WHERE brand = 'Nike' and size='XS' and color='white'",
        'SQLResult': "Result of the SQL query",
        'Answer': "78"
    },
    {
        'Question': "What is the price of inventory for all small size t-shirts?",
        'SQLQuery': "SELECT SUM(price*stock_quantity) FROM `t_shirts` WHERE `size` = 'S'",
        'SQLResult': "Result of the SQL query",
        'Answer': "25644"
    },
    {
        'Question': "If we have to sell all Levi's t-shirts today. How much revenue our store will generate?",
        'SQLQuery': "SELECT SUM(price*stock_quantity) FROM `t_shirts` WHERE `brand` = 'Levi'",
        'SQLResult': "Result of the SQL query",
        'Answer': "20186"
    },
    {
        'Question': "How many white color Levi's t-shirts do we have available?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi' and color='white'",
        'SQLResult': "Result of the SQL query",
        'Answer': "283"
    }
]