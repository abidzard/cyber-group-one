def bayes_theorem(p_b, p_g_given_b, p_g_given_not_b):
   # calculate P(not B)
   not_b = 1 - p_b
   # calculate P(G)
   p_g = p_g_given_b * p_b + p_g_given_not_b * not_b
   # calculate P(B|G)
   p_b_given_g = (p_g_given_b * p_b) / p_g
   return p_b_given_g

#P(B)
p_b = 1/4

# P(G|B)
p_g_given_b = 1

# P(G|notB)
p_g_given_not_b = 1/3

# calculate P(B|G)
result = bayes_theorem(p_b, p_g_given_b, p_g_given_not_b)

# print result
print('P(B|G) = %.2f%%' % (result * 100))