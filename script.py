import noshmishmosh
import numpy as np

#A/B Testing at Nosh Mish Mosh
all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
total_visitor_count = len(all_visitors)
print total_visitor_count #500
paying_visitor_count = len(paying_visitors)
print paying_visitor_count #93

baseline_percent = 93*100.0 / 500
print baseline_percent #18.6

#Minimum Detectable Effect
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print average_payment #26.54
new_customers_needed = np.ceil(1240 / average_payment)
print new_customers_needed #47
percentage_point_increase = new_customers_needed * 100.0 / total_visitor_count
print percentage_point_increase #9.4
minimum_detectable_effect = 100 * percentage_point_increase / baseline_percent
print minimum_detectable_effect #50.53

#Calculating sample size for Nosh Mish Mosh's artisanal rebranding using online A/B Test Calculator, with 90% statistical significance.
ab_sample_size = 290