from scipy.stats import nbinom

p = 0.1  # Probability of getting a star on a single receipt
r = 5  # Number of successes (5 consecutive stars)
total_days = 20  # Maximum days Mark eats at the cafe

# Compute P(X ≤ 20)
prob_win = nbinom.cdf(total_days, r, p)
print(prob_win)
