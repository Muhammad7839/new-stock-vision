import matplotlib.pyplot as plt

# Example actual and predicted values
y_test = [134.5, 130.2, 128.7, 140.1, 138.3]
y_pred = [132.1, 129.9, 130.4, 138.6, 139.0]

plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual Prices', marker='o')
plt.plot(y_pred, label='Predicted Prices', marker='x')

plt.title('Actual vs. Predicted Stock Prices (2018)')
plt.xlabel('Sample Index')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.tight_layout()