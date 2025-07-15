{
  "asset": "Bitcoin",
  "prediction": 70543.20,
  "sentiment": "Positive"
}

import numpy as np

# Assuming you already have y_test and y_pred from your model
# Save the first 50 values for graphing
np.save('y_test.npy', y_test[:50])
np.save('y_pred.npy', y_pred[:50])

import numpy as np

# Replace these with your actual data
y_test = [134.5, 130.2, 128.7, 140.1, 138.3]
y_pred = [132.1, 129.9, 130.4, 138.6, 139.0]

# Save them as .npy files
np.save('y_test.npy', y_test)
np.save('y_pred.npy', y_pred)