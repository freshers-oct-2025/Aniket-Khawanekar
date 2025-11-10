import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [5, 5, 6]])

print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)

arr3 = np.arange(1, 10)
print("op arr3:", arr3)

arr4 = np.ones((3, 3))
print("\nMatrix multiplication:")
print(np.dot(arr3[:3], arr4))  # Using first 3 elements for matching shape

data = np.random.randn(100)
print(f"\nMean: {np.mean(data):.2f}")
print(f"Std: {np.std(data):.2f}")
print(f"Min: {np.min(data):.2f}")
print(f"Max: {np.max(data):.2f}")

arr5 = np.array([[1, 2, 3], [4, 5, 6]])
arr6 = np.array([10, 20, 30])
print("\nBroadcasting result:")
print(arr5 + arr6)
