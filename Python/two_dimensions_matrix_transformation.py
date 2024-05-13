import numpy as np
import matplotlib.pyplot as plt
from math import radians

def translate(points, dx, dy):
    translated_points = points + [dx, dy]
    return translated_points

def rotate(points, angle, center):
    translated_points = points - center
    rotation_matrix = np.array([[np.cos(angle), np.sin(angle)],
                                [-np.sin(angle), np.cos(angle)]])
    rotated_points = np.dot(translated_points, rotation_matrix)
    return rotated_points + center

def scale(points, sx, sy):
    scaled_points = points * [sx, sy]
    return scaled_points

def shear(points, shx, shy):
    shear_matrix = np.array([[1, shy],
                              [shx, 1]])
    return np.dot(points, shear_matrix)

def input_points(num_points):
    points = []
    for i in range(num_points):
        x = float(input(f"Enter x-coordinate of point {i+1}: "))
        y = float(input(f"Enter y-coordinate of point {i+1}: "))
        points.append([x, y])
    points.append(points[0])
    return np.array(points)

def main():
    num_points = int(input("Enter the number of points to transform: "))
    original_points = input_points(num_points)
    transformed_points = original_points
    rotation_center = None
    
    while True:
        print("\nWhich action do you want to perform?")
        print("1. Continue with transformations")
        print("2. Display current result")
        print("3. Exit")
        
        action = input("Enter your choice (1/2/3): ")
        
        if action == '3':
            print("Exiting the program...")
            break
        
        if action == '1':
            while True:
                print("\nWhich transformation do you want to perform?")
                print("1. Translation")
                print("2. Rotation")
                print("3. Scaling")
                print("4. Shear")
                print("5. Back to previous menu")
                
                choice = input("Enter your choice (1/2/3/4/5): ")
                
                if choice == '5':
                    break
                
                if choice not in ['1', '2', '3', '4']:
                    print("Invalid choice. Please enter a valid option.")
                    continue

                if choice == '1':
                    dx = float(input("Enter the translation along the x-axis (dx): "))
                    dy = float(input("Enter the translation along the y-axis (dy): "))
                    transformed_points = translate(transformed_points, dx, dy)
                    transformation_name = "Translation"
                elif choice == '2':
                    angle = float(input("Enter the rotation angle (in degrees): "))
                    center_x = float(input("Enter the x-coordinate of the center of rotation: "))
                    center_y = float(input("Enter the y-coordinate of the center of rotation: "))
                    rotation_center = np.array([center_x, center_y])
                    transformed_points = rotate(transformed_points, radians(angle), rotation_center)
                    transformation_name = "Rotation"
                elif choice == '3':
                    sx = float(input("Enter the scaling factor along the x-axis: "))
                    sy = float(input("Enter the scaling factor along the y-axis: "))
                    transformed_points = scale(transformed_points, sx, sy)
                    transformation_name = "Scaling"
                elif choice == '4':
                    shx = float(input("Enter the shear factor along the x-axis: "))
                    shy = float(input("Enter the shear factor along the y-axis: "))
                    transformed_points = shear(transformed_points, shx, shy)
                    transformation_name = "Shear"
        
        elif action == '2':
            print('Displaying current result plot...(close the plot window to continue)')
            plt.plot(original_points[:,0], original_points[:,1], label='Original')
            plt.plot(transformed_points[:,0], transformed_points[:,1], label='Transformed')
            if transformation_name == "Rotation" and rotation_center is not None:
                plt.plot(rotation_center[0], rotation_center[1], 'ro', label='Rotation Center')
            plt.title('Current Result')
            plt.legend()
            plt.grid(True)
            plt.axis('equal')
            plt.show()

if __name__ == "__main__":
    main()