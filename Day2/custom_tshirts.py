# Let's start building the cost calculator

# Print the welcome message
print("Welcome to our t-shirt store!")

# Number and colour of small tshirts
s_tshirts = int(input("How many small t-shirts do you need? "))
s_colour = input("What colour do you want for small t-shirts, red, green or blue? ")

# Number and colour of medium tshirts
m_tshirts = int(input("How many medium t-shirts do you need? "))
m_colour = input("What colour do you want for medium t-shirts, red, green or blue? ")

# Number and colour of large tshirts
l_tshirts = int(input("How many large t-shirts do you need? "))
l_colour = input("What colour do you want for large t-shirts, red, green or blue? ")

# Costs of each size
cost_s = 10
cost_m = 12
cost_l = 15

# Cost increase if colour = red
cost_increase_if_red = 2

# Total cost
total_cost = s_tshirts*cost_s + m_tshirts*cost_m + l_tshirts*cost_l

# Final value
if s_colour == 'red':
    total_cost += s_tshirts*cost_increase_if_red

elif m_colour == 'red':
    total_cost += m_tshirts*cost_increase_if_red

elif l_colour == 'red':
    total_cost += l_tshirts*cost_increase_if_red

# Print the final cost of the order
print(f"The final cost of the order is ${total_cost}.")