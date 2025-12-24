# # Orders module (orders)

# Responsibility:

# Handle order creation and validation.

# It should:
# Create new orders
# Check if requested quantity is available
# Decide order status (completed / rejected)
# Trigger stock update only if valid

# 🚫 It should NOT:
# Directly manage product storage
# Change stock without validation