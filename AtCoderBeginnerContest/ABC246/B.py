A, B = map(int, input().split())

double_y = (B**2) / (A**2 + B**2)
double_x = 1 - double_y

print(double_x**0.5, double_y**0.5)
